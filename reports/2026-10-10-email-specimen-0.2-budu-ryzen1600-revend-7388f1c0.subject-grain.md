# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, testee=pcrec_a15fb77b_auto-caps-simdna, testee=pcrec_a15fb77b_auto-nocaps-simdna, testee=pcrec_7388f1c0_auto-caps-simdna, testee=pcrec_7388f1c0_auto-nocaps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 2.53% (`pcrec_a15fb77b_auto-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261010T212216Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-caps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261010T212216Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261010T212820Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-nocaps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261010T212820Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_a15fb77b_auto-caps-simdna__budu-ryzen1600__20261010T211611Z` (store/records/email-specimen@0.2/pcrec_a15fb77b_auto-caps-simdna/email-specimen@0.2__pcrec_a15fb77b_auto-caps-simdna__budu-ryzen1600__20261010T211611Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_a15fb77b_auto-nocaps-simdna__budu-ryzen1600__20261010T213423Z` (store/records/email-specimen@0.2/pcrec_a15fb77b_auto-nocaps-simdna/email-specimen@0.2__pcrec_a15fb77b_auto-nocaps-simdna__budu-ryzen1600__20261010T213423Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
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

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 33.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.8 | 32.6 | 32.8 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.4 | 0.2 | 1.074x | 1.074x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.3 | 34.9 | 35.3 | 0.1 | 1.082x | 1.082x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.3 | 63.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.3 | 68.5 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.2 | 76.3 | 3.2 | 1.078x | 1.078x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.5 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.2 | 43.1 | 43.4 | 0.1 | 1.071x | 1.071x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.2 | 43.1 | 43.9 | 0.3 | 1.071x | 1.071x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.8 | 82.6 | 83.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 83.0 | 82.8 | 83.3 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 86.2 | 85.9 | 93.3 | 2.8 | 1.041x | 1.041x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 87.0 | 86.1 | 87.6 | 0.6 | 1.051x | 1.051x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.8 | 21.2 | 0.1 | 1.142x | 1.142x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.9 | 21.0 | 0.0 | 1.144x | 1.144x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.8 | 28.7 | 30.6 | 0.7 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 32.4 | 32.2 | 33.5 | 0.5 | 1.129x | 1.129x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 32.5 | 32.1 | 42.9 | 4.2 | 1.133x | 1.133x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.7 | 43.4 | 43.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.7 | 43.3 | 44.0 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.7 | 46.3 | 46.9 | 0.2 | 1.070x | 1.070x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.8 | 46.5 | 46.9 | 0.1 | 1.071x | 1.071x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 89.6 | 89.5 | 89.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 89.8 | 89.3 | 89.9 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 93.2 | 93.1 | 93.6 | 0.2 | 1.040x | 1.040x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 93.2 | 93.1 | 100.7 | 3.0 | 1.040x | 1.040x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.3 | 61.0 | 61.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.5 | 61.2 | 61.8 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 65.1 | 65.0 | 65.4 | 0.2 | 1.062x | 1.062x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 65.1 | 65.0 | 65.4 | 0.1 | 1.063x | 1.063x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.1 | 124.6 | 125.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.1 | 124.8 | 125.4 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 129.0 | 128.9 | 137.1 | 3.2 | 1.031x | 1.031x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 129.1 | 128.7 | 129.2 | 0.2 | 1.032x | 1.032x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.8 | 20.9 | 0.0 | 1.141x | 1.141x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.8 | 21.0 | 0.1 | 1.141x | 1.141x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.7 | 29.5 | 0.3 | 1.013x | 1.013x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 32.2 | 32.2 | 42.9 | 4.3 | 1.124x | 1.124x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 32.4 | 32.1 | 33.1 | 0.3 | 1.130x | 1.130x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.1 | 31.1 | 31.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.3 | 33.3 | 33.5 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.3 | 33.2 | 33.5 | 0.1 | 1.072x | 1.072x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.1 | 60.1 | 60.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.2 | 59.9 | 60.4 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 64.3 | 64.2 | 64.3 | 0.1 | 1.069x | 1.069x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 64.4 | 64.2 | 70.9 | 2.6 | 1.072x | 1.072x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.8 | 46.7 | 46.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 47.0 | 46.5 | 47.7 | 0.4 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.4 | 0.1 | 1.073x | 1.073x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 50.3 | 50.2 | 50.3 | 0.0 | 1.074x | 1.074x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.4 | 95.2 | 95.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.4 | 95.3 | 96.4 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 100.7 | 100.7 | 101.1 | 0.2 | 1.056x | 1.056x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 100.8 | 100.7 | 108.1 | 2.9 | 1.057x | 1.057x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 36.9 | 37.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.1 | 37.0 | 37.2 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 39.6 | 39.5 | 39.7 | 0.1 | 1.071x | 1.071x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 39.6 | 39.5 | 39.7 | 0.1 | 1.072x | 1.072x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.2 | 73.9 | 74.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.3 | 74.2 | 74.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 78.4 | 78.2 | 78.6 | 0.1 | 1.057x | 1.057x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 78.6 | 78.4 | 85.4 | 2.8 | 1.059x | 1.059x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.1 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.7 | 32.0 | 0.1 | 1.077x | 1.077x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.3 | 56.1 | 56.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.5 | 68.0 | 3.0 | 1.075x | 1.075x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.5 | 60.7 | 0.1 | 1.075x | 1.075x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.9 | 31.9 | 32.2 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.1 | 32.0 | 32.1 | 0.1 | 1.083x | 1.083x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.3 | 56.1 | 56.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.5 | 67.9 | 2.9 | 1.079x | 1.079x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.6 | 61.2 | 0.2 | 1.079x | 1.079x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.4 | 0.2 | 1.010x | 1.010x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.1 | 0.1 | 1.018x | 1.018x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.2 | 11.7 | 12.9 | 0.4 | 1.026x | 1.026x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 37.9 | 37.8 | 38.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.9 | 37.9 | 38.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 38.0 | 37.8 | 48.4 | 4.2 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 38.0 | 37.8 | 38.0 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.7 | 35.6 | 35.8 | 0.1 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.1 | 38.0 | 38.3 | 0.1 | 1.076x | 1.076x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.2 | 38.1 | 38.4 | 0.1 | 1.079x | 1.079x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.5 | 71.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 71.0 | 70.7 | 72.4 | 0.7 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.3 | 81.9 | 2.6 | 1.065x | 1.065x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.0 | 75.5 | 0.2 | 1.066x | 1.066x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.3 | 35.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.6 | 35.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.4 | 38.2 | 0.3 | 1.058x | 1.058x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.7 | 37.4 | 38.2 | 0.3 | 1.060x | 1.060x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.6 | 70.4 | 71.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.7 | 72.2 | 0.6 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.1 | 75.4 | 0.1 | 1.066x | 1.066x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.1 | 82.2 | 2.8 | 1.067x | 1.067x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.2 | 0.1 | 1.080x | 1.080x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 32.0 | 32.1 | 0.0 | 1.082x | 1.082x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.4 | 56.2 | 56.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.5 | 60.8 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.6 | 60.5 | 68.2 | 3.1 | 1.074x | 1.074x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.3 | 36.5 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.3 | 36.5 | 0.0 | 1.073x | 1.073x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 66.9 | 66.8 | 67.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 66.8 | 67.4 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.0 | 72.2 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.0 | 78.8 | 2.7 | 1.078x | 1.078x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 9.4 | 9.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 1.030x | 1.030x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.9 | 9.7 | 10.9 | 0.5 | 1.156x | 1.156x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.3 | 11.8 | 0.5 | 1.156x | 1.156x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.8 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.1 | 29.0 | 29.8 | 0.3 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 28.9 | 29.5 | 0.2 | 1.008x | 1.008x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.1 | 38.8 | 3.8 | 1.011x | 1.011x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.5 | 37.4 | 38.6 | 0.5 | 1.056x | 1.056x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.1 | 37.4 | 38.4 | 0.4 | 1.073x | 1.073x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 72.4 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.8 | 71.0 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.2 | 75.1 | 82.2 | 2.8 | 1.062x | 1.062x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.2 | 75.6 | 0.1 | 1.064x | 1.064x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 33.9 | 33.9 | 34.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.3 | 36.7 | 0.2 | 1.073x | 1.073x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.3 | 36.6 | 0.1 | 1.074x | 1.074x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 66.9 | 66.8 | 67.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 66.9 | 67.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.2 | 72.1 | 72.3 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 72.2 | 72.1 | 78.5 | 2.6 | 1.079x | 1.079x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.1 | 10.0 | 11.3 | 0.5 | 1.028x | 1.028x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.036x | 1.036x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.2 | 10.2 | 11.2 | 0.4 | 1.140x | 1.140x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 30.8 | 30.5 | 40.8 | 4.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.9 | 30.7 | 31.5 | 0.3 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.9 | 30.8 | 31.1 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 31.0 | 30.7 | 31.1 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.5 | 38.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.5 | 38.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.3 | 41.2 | 41.4 | 0.1 | 1.067x | 1.067x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.3 | 41.2 | 41.4 | 0.1 | 1.068x | 1.068x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.7 | 77.6 | 77.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.7 | 77.6 | 78.1 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 81.9 | 81.7 | 81.9 | 0.1 | 1.054x | 1.054x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 82.0 | 81.9 | 89.7 | 3.1 | 1.055x | 1.055x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 32.0 | 32.1 | 0.0 | 1.080x | 1.080x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.1 | 0.1 | 1.080x | 1.080x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.4 | 56.2 | 56.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.5 | 56.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.4 | 60.6 | 0.1 | 1.073x | 1.073x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.5 | 68.8 | 3.3 | 1.075x | 1.075x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.8 | 41.7 | 42.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.1 | 41.8 | 42.3 | 0.2 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.8 | 44.6 | 44.9 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.9 | 44.8 | 45.2 | 0.1 | 1.075x | 1.075x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.1 | 90.0 | 90.3 | 0.1 | 1.061x | 1.061x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 90.2 | 89.7 | 97.0 | 2.8 | 1.062x | 1.062x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.4 | 38.0 | 0.2 | 1.058x | 1.058x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.7 | 37.6 | 38.5 | 0.3 | 1.062x | 1.062x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.5 | 71.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.0 | 75.6 | 0.2 | 1.065x | 1.065x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.4 | 82.2 | 2.7 | 1.066x | 1.066x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.2 | 0.1 | 1.080x | 1.080x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.1 | 31.9 | 32.3 | 0.1 | 1.082x | 1.082x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.1 | 56.6 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.4 | 68.6 | 3.2 | 1.072x | 1.072x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.6 | 60.5 | 60.6 | 0.0 | 1.072x | 1.072x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.5 | 38.2 | 0.2 | 1.059x | 1.059x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.4 | 38.1 | 0.3 | 1.061x | 1.061x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.8 | 71.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.8 | 71.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.2 | 81.8 | 2.6 | 1.064x | 1.064x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.4 | 75.5 | 0.0 | 1.064x | 1.064x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.7 | 42.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.9 | 44.6 | 45.3 | 0.2 | 1.072x | 1.072x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 45.0 | 44.6 | 45.1 | 0.2 | 1.073x | 1.073x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 90.1 | 89.7 | 96.8 | 2.7 | 1.061x | 1.061x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.1 | 89.8 | 90.3 | 0.2 | 1.061x | 1.061x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.1 | 41.8 | 42.2 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.8 | 44.6 | 44.9 | 0.1 | 1.068x | 1.068x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.1 | 0.2 | 1.070x | 1.070x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.7 | 84.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.1 | 84.8 | 85.1 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.1 | 89.9 | 90.3 | 0.2 | 1.062x | 1.062x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 90.2 | 89.9 | 96.5 | 2.6 | 1.062x | 1.062x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.0 | 24.9 | 25.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.0 | 24.9 | 25.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.0 | 25.0 | 25.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 24.9 | 34.0 | 3.6 | 1.008x | 1.008x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.005x | 1.005x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.6 | 58.6 | 3.9 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.7 | 48.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.9 | 48.7 | 48.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.9 | 48.8 | 49.0 | 0.0 | 1.004x | 1.004x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.005x | 1.005x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 25.1 | 25.0 | 36.6 | 4.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.2 | 25.1 | 25.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 25.1 | 25.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.3 | 25.1 | 25.5 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 33.1 | 33.0 | 33.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 33.2 | 33.2 | 43.1 | 4.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.3 | 33.1 | 34.0 | 0.3 | 1.006x | 1.006x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.6 | 33.1 | 34.0 | 0.4 | 1.014x | 1.014x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.1 | 28.9 | 41.3 | 4.9 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.2 | 29.8 | 0.2 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.1 | 29.5 | 0.1 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.1 | 30.4 | 0.5 | 1.009x | 1.009x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.1 | 29.1 | 29.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 29.1 | 29.2 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.2 | 28.8 | 41.6 | 5.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.5 | 29.1 | 29.9 | 0.3 | 1.014x | 1.014x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.3 | 20.1 | 20.6 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.3 | 20.1 | 20.5 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.4 | 21.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.4 | 21.9 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.5 | 21.5 | 21.6 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 21.6 | 21.4 | 33.9 | 5.0 | 1.005x | 1.005x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.0 | 27.7 | 40.6 | 5.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.0 | 27.9 | 28.7 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.1 | 27.8 | 28.4 | 0.2 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.2 | 28.0 | 28.5 | 0.2 | 1.009x | 1.009x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.7 | 12.1 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.012x | 1.012x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 29.2 | 29.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.6 | 29.5 | 29.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.4 | 30.0 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.9 | 29.6 | 41.1 | 4.5 | 1.013x | 1.013x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.9 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.8 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.6 | 23.4 | 23.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 24.0 | 23.8 | 36.4 | 5.0 | 1.018x | 1.018x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.2 | 24.1 | 24.5 | 0.2 | 1.023x | 1.023x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 24.3 | 24.0 | 24.5 | 0.1 | 1.028x | 1.028x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.3 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.7 | 29.4 | 29.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.7 | 41.2 | 4.5 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.5 | 30.3 | 0.3 | 1.008x | 1.008x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.1 | 29.6 | 30.2 | 0.2 | 1.016x | 1.016x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 1.018x | 1.018x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 1.027x | 1.027x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.038x | 1.038x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.3 | 63.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.5 | 63.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.5 | 68.5 | 68.7 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.6 | 68.5 | 76.8 | 3.3 | 1.079x | 1.079x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 7.4 | 7.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 7.4 | 17.7 | 4.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.6 | 7.6 | 8.6 | 0.4 | 1.160x | 1.160x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.6 | 7.4 | 9.6 | 0.8 | 1.160x | 1.160x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 8.8 | 10.0 | 0.4 | 1.032x | 1.032x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 10.6 | 0.8 | 1.064x | 1.064x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.8 | 10.9 | 0.8 | 1.099x | 1.099x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.8 | 21.7 | 22.8 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.0 | 21.7 | 22.2 | 0.2 | 1.011x | 1.011x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.2 | 22.0 | 22.4 | 0.1 | 1.019x | 1.019x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 22.3 | 22.0 | 32.3 | 4.0 | 1.024x | 1.024x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 12.1 | 13.5 | 0.5 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.5 | 0.1 | 1.009x | 1.009x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.4 | 0.0 | 1.009x | 1.009x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 14.8 | 14.1 | 26.8 | 4.9 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 14.9 | 14.2 | 16.0 | 0.7 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.1 | 14.2 | 15.3 | 0.4 | 1.019x | 1.019x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.2 | 14.4 | 15.3 | 0.3 | 1.023x | 1.023x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.6 | 0.3 | 1.009x | 1.009x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 13.1 | 0.5 | 1.018x | 1.018x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.5 | 11.7 | 13.2 | 0.6 | 1.059x | 1.059x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.2 | 75.2 | 75.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.3 | 75.1 | 75.5 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 79.9 | 79.7 | 86.4 | 2.6 | 1.062x | 1.062x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 80.0 | 79.1 | 80.8 | 0.6 | 1.064x | 1.064x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 9.8 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.4 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.3 | 8.9 | 10.9 | 0.8 | 1.051x | 1.051x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 9.8 | 0.5 | 1.065x | 1.065x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.3 | 65.2 | 65.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.5 | 65.2 | 65.6 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.2 | 70.0 | 70.3 | 0.1 | 1.075x | 1.075x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.4 | 70.3 | 76.5 | 2.4 | 1.077x | 1.077x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.1 | 0.1 | 1.009x | 1.009x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.4 | 0.1 | 1.020x | 1.020x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.2 | 0.2 | 1.021x | 1.021x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.7 | 28.5 | 29.6 | 0.4 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.7 | 28.3 | 39.9 | 4.5 | 1.006x | 1.006x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.8 | 28.7 | 29.7 | 0.4 | 1.008x | 1.008x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.9 | 21.8 | 22.0 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 22.0 | 21.7 | 22.1 | 0.1 | 1.012x | 1.012x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.4 | 21.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 21.6 | 21.4 | 34.0 | 5.0 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.7 | 21.5 | 22.0 | 0.2 | 1.008x | 1.008x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.8 | 21.5 | 21.9 | 0.2 | 1.014x | 1.014x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.0 | 23.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.4 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.9 | 22.8 | 23.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.0 | 22.7 | 23.4 | 0.2 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 23.2 | 22.8 | 32.1 | 3.6 | 1.013x | 1.013x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.3 | 22.9 | 23.4 | 0.2 | 1.020x | 1.020x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 15.1 | 15.0 | 15.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 15.1 | 14.9 | 25.1 | 4.0 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.2 | 15.7 | 0.1 | 1.020x | 1.020x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.5 | 15.3 | 15.6 | 0.1 | 1.029x | 1.029x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.7 | 10.5 | 11.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.8 | 10.5 | 10.9 | 0.2 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.8 | 10.8 | 10.9 | 0.1 | 1.010x | 1.010x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.2 | 0.1 | 1.034x | 1.034x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 72.9 | 72.8 | 73.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.2 | 73.0 | 73.7 | 0.3 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.5 | 77.2 | 77.6 | 0.1 | 1.064x | 1.064x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.5 | 85.1 | 3.0 | 1.066x | 1.066x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 1.014x | 1.014x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.7 | 14.7 | 0.0 | 1.015x | 1.015x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 57.9 | 57.8 | 58.8 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 58.1 | 57.8 | 59.0 | 0.4 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 62.9 | 62.8 | 63.2 | 0.1 | 1.085x | 1.085x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 62.9 | 62.7 | 72.0 | 3.7 | 1.085x | 1.085x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.7 | 10.6 | 11.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.5 | 11.3 | 0.3 | 1.018x | 1.018x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.7 | 10.9 | 0.1 | 1.018x | 1.018x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.1 | 10.6 | 11.2 | 0.3 | 1.033x | 1.033x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 72.9 | 72.9 | 73.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.2 | 72.9 | 73.5 | 0.2 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.6 | 77.4 | 77.7 | 0.1 | 1.064x | 1.064x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.5 | 85.0 | 2.9 | 1.066x | 1.066x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.1 | 13.4 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.7 | 22.5 | 22.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.7 | 22.5 | 23.8 | 0.5 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 22.8 | 22.6 | 35.7 | 5.2 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 22.9 | 22.4 | 24.2 | 0.7 | 1.009x | 1.009x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.009x | 1.009x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.012x | 1.012x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.0 | 16.8 | 17.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.1 | 17.0 | 31.3 | 5.7 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.1 | 17.0 | 17.6 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.3 | 17.2 | 17.7 | 0.2 | 1.014x | 1.014x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.010x | 1.010x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.1 | 1.013x | 1.013x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 16.7 | 16.7 | 30.9 | 5.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.8 | 16.7 | 17.2 | 0.2 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.1 | 16.9 | 17.2 | 0.1 | 1.021x | 1.021x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.3 | 17.1 | 17.8 | 0.3 | 1.032x | 1.032x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.1 | 1.011x | 1.011x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.8 | 17.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.0 | 17.0 | 17.1 | 0.0 | 1.007x | 1.007x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.1 | 16.8 | 27.7 | 4.3 | 1.011x | 1.011x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.3 | 17.1 | 17.8 | 0.3 | 1.024x | 1.024x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 1.008x | 1.008x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.1 | 13.4 | 0.1 | 1.009x | 1.009x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.2 | 19.1 | 19.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 19.3 | 19.2 | 19.8 | 0.2 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.3 | 19.2 | 19.6 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 19.3 | 19.0 | 32.8 | 5.4 | 1.007x | 1.007x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,062.0 | 19,061.7 | 20,589.0 | 610.8 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,062.9 | 19,061.6 | 19,068.2 | 2.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,063.8 | 19,063.2 | 19,064.7 | 0.6 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,064.3 | 19,063.3 | 19,066.1 | 1.0 | 1.000x | 1.000x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,459.8 | 7,459.5 | 7,461.5 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,460.4 | 7,460.0 | 7,461.6 | 0.6 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,460.9 | 7,460.4 | 7,461.2 | 0.3 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,463.6 | 7,459.3 | 7,467.0 | 2.7 | 1.001x | 1.001x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,546.3 | 9,545.8 | 9,547.7 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,546.9 | 9,545.9 | 9,794.2 | 98.4 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,548.7 | 9,548.1 | 9,549.2 | 0.4 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,550.6 | 9,548.9 | 9,553.4 | 1.7 | 1.000x | 1.000x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,036.1 | 19,033.9 | 19,037.3 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,036.3 | 19,034.8 | 19,687.2 | 260.5 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,037.5 | 19,036.7 | 19,059.2 | 8.7 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,037.8 | 19,036.6 | 19,039.2 | 0.9 | 1.000x | 1.000x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,736.2 | 3,734.9 | 3,739.4 | 1.8 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,737.1 | 3,735.5 | 3,737.8 | 0.9 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,738.1 | 3,737.1 | 3,739.9 | 1.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,738.1 | 3,738.0 | 3,741.8 | 1.5 | 1.001x | 1.001x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.3 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,783.2 | 4,781.2 | 4,784.0 | 1.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,783.7 | 4,782.4 | 4,784.4 | 0.8 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,784.7 | 4,781.1 | 5,405.9 | 248.9 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,785.2 | 4,783.0 | 4,788.6 | 2.0 | 1.000x | 1.000x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,642.6 | 7,642.2 | 7,647.8 | 2.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,643.4 | 7,643.1 | 7,644.6 | 0.5 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,644.7 | 7,644.3 | 7,716.4 | 28.7 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,645.2 | 7,644.9 | 7,760.0 | 45.9 | 1.000x | 1.000x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.6 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 11.6 | 1.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 8.6 | 9.5 | 0.4 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 8.9 | 11.1 | 0.9 | 1.105x | 1.105x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.9 | 23.8 | 24.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.9 | 23.9 | 24.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 24.3 | 23.8 | 37.3 | 5.3 | 1.018x | 1.018x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.9 | 24.0 | 25.8 | 0.6 | 1.041x | 1.041x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.1 | 34.0 | 34.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.5 | 36.4 | 37.0 | 0.2 | 1.073x | 1.073x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.9 | 36.4 | 37.1 | 0.3 | 1.084x | 1.084x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 66.9 | 66.9 | 67.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 66.9 | 67.7 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.0 | 72.3 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 72.2 | 72.1 | 78.1 | 2.4 | 1.079x | 1.079x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.6 | 32.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.2 | 0.2 | 1.070x | 1.070x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.5 | 35.6 | 0.3 | 1.072x | 1.072x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.1 | 67.9 | 68.2 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.1 | 75.4 | 2.8 | 1.082x | 1.082x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.9 | 16.7 | 17.1 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.5 | 19.5 | 19.6 | 0.1 | 1.163x | 1.163x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.6 | 19.5 | 19.7 | 0.1 | 1.170x | 1.170x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 26.0 | 25.9 | 26.6 | 0.3 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.6 | 28.5 | 29.3 | 0.3 | 1.105x | 1.105x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.8 | 28.7 | 40.2 | 4.6 | 1.110x | 1.110x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.9 | 0.5 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.1 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.7 | 12.1 | 0.2 | 1.014x | 1.014x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.5 | 30.2 | 30.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.5 | 30.4 | 30.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.6 | 30.2 | 31.0 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 30.7 | 30.1 | 41.1 | 4.2 | 1.006x | 1.006x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.2 | 28.1 | 28.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.2 | 28.1 | 28.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 30.6 | 30.4 | 30.6 | 0.1 | 1.087x | 1.087x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 30.6 | 30.2 | 30.8 | 0.2 | 1.088x | 1.088x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.8 | 52.8 | 53.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.8 | 52.8 | 55.1 | 0.9 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 57.5 | 57.4 | 64.5 | 2.8 | 1.089x | 1.089x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 57.7 | 57.6 | 58.0 | 0.2 | 1.092x | 1.092x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.2 | 56.0 | 56.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.4 | 56.2 | 57.1 | 0.3 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 59.7 | 59.5 | 59.8 | 0.1 | 1.062x | 1.062x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 59.9 | 59.6 | 60.0 | 0.2 | 1.066x | 1.066x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.5 | 114.3 | 115.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.6 | 114.5 | 115.0 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 118.4 | 118.2 | 125.9 | 3.0 | 1.035x | 1.035x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 118.5 | 118.2 | 118.8 | 0.2 | 1.035x | 1.035x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.9 | 42.9 | 43.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.1 | 42.9 | 43.4 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.1 | 42.9 | 43.3 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.2 | 43.0 | 43.3 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 94.0 | 93.9 | 94.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.1 | 93.9 | 96.3 | 0.8 | 1.012x | 1.012x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 98.9 | 98.8 | 99.0 | 0.1 | 1.053x | 1.053x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 99.1 | 98.7 | 108.0 | 3.6 | 1.055x | 1.055x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.1 | 23.1 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.2 | 23.1 | 23.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.3 | 23.2 | 23.6 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 23.3 | 23.1 | 35.5 | 4.9 | 1.008x | 1.008x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.0 | 0.3 | 1.007x | 1.007x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.7 | 30.7 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.8 | 30.1 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.0 | 29.6 | 30.9 | 0.4 | 1.007x | 1.007x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 30.2 | 29.7 | 39.0 | 3.6 | 1.012x | 1.012x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.0 | 0.2 | 1.069x | 1.069x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.7 | 35.3 | 0.2 | 1.076x | 1.076x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.2 | 67.8 | 68.8 | 0.3 | 1.078x | 1.078x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.2 | 68.1 | 74.6 | 2.5 | 1.078x | 1.078x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.7 | 34.6 | 35.0 | 0.2 | 1.069x | 1.069x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.1 | 34.8 | 35.6 | 0.3 | 1.078x | 1.078x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.1 | 67.7 | 68.3 | 0.2 | 1.076x | 1.076x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.0 | 74.6 | 2.6 | 1.079x | 1.079x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.4 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.7 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.6 | 35.1 | 0.2 | 1.079x | 1.079x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.1 | 34.6 | 36.0 | 0.5 | 1.084x | 1.084x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.1 | 67.9 | 68.1 | 0.1 | 1.076x | 1.076x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.2 | 67.9 | 74.8 | 2.7 | 1.077x | 1.077x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.8 | 35.1 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.8 | 35.2 | 0.2 | 1.073x | 1.073x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.1 | 67.9 | 68.3 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.1 | 74.7 | 2.6 | 1.082x | 1.082x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.2 | 0.2 | 1.069x | 1.069x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.1 | 35.0 | 35.6 | 0.2 | 1.079x | 1.079x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.7 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.2 | 67.8 | 68.6 | 0.2 | 1.079x | 1.079x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 74.7 | 2.6 | 1.081x | 1.081x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.008x | 1.008x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.1 | 29.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.1 | 39.9 | 4.3 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.2 | 30.3 | 0.4 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 29.4 | 29.7 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.7 | 11.2 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 1.009x | 1.009x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.9 | 9.7 | 10.0 | 0.1 | 1.010x | 1.010x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.1 | 9.3 | 11.5 | 0.7 | 1.034x | 1.034x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3.9 | 3.9 | 5.0 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 3.9 | 3.9 | 10.8 | 2.7 | 1.010x | 1.010x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.067x | 1.067x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.067x | 1.067x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 8.6 | 10.9 | 0.8 | 1.078x | 1.078x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.7 | 8.9 | 10.5 | 0.6 | 1.100x | 1.100x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 8.9 | 10.6 | 0.7 | 1.128x | 1.128x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 8.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.3 | 8.5 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.3 | 8.5 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 19.0 | 4.3 | 1.007x | 1.007x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 9.7 | 11.2 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.032x | 1.032x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.5 | 10.3 | 11.8 | 0.5 | 1.148x | 1.148x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.5 | 10.0 | 11.5 | 0.7 | 1.149x | 1.149x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 18.1 | 4.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.5 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.0 | 8.3 | 0.1 | 1.037x | 1.037x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.4 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.5 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 7.4 | 7.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 7.7 | 7.4 | 17.7 | 4.0 | 1.039x | 1.039x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.9 | 7.5 | 9.2 | 0.6 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.4 | 7.4 | 8.6 | 0.4 | 1.143x | 1.143x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,781,802.0 | 3,781,293.1 | 3,782,227.3 | 298.8 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,782,560.5 | 3,781,230.2 | 3,783,797.9 | 825.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 3,804,411.7 | 3,804,042.9 | 3,805,260.5 | 530.9 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,805,429.9 | 3,803,617.8 | 3,805,951.2 | 985.3 | 1.006x | 1.006x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,679.5 | 17,661.5 | 17,707.6 | 17.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,682.7 | 17,650.3 | 17,706.1 | 20.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,715.1 | 17,690.7 | 17,761.6 | 23.3 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,716.3 | 17,687.5 | 17,719.2 | 12.5 | 1.002x | 1.002x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,649.6 | 17,644.7 | 17,671.8 | 9.9 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,660.3 | 17,645.5 | 17,696.2 | 17.3 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,677.6 | 17,653.7 | 17,727.8 | 25.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,693.1 | 17,685.4 | 17,718.4 | 14.6 | 1.002x | 1.002x |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 3,163,933.4 | 3,154,655.2 | 3,168,482.4 | 4,542.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,164,062.6 | 3,161,552.6 | 3,166,672.5 | 1,898.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,218,842.8 | 3,215,960.0 | 3,221,387.5 | 1,738.3 | 1.017x | 1.017x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,222,237.7 | 3,216,712.5 | 3,225,757.6 | 2,938.2 | 1.018x | 1.018x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,660.4 | 17,651.7 | 17,706.5 | 19.8 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,675.1 | 17,669.9 | 17,711.9 | 15.4 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,691.8 | 17,659.3 | 17,728.1 | 24.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,717.4 | 17,706.4 | 17,742.1 | 12.9 | 1.003x | 1.003x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.8 | 17.7 | 18.7 | 0.4 | 1.002x | 1.002x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 18.1 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 18.3 | 18.1 | 18.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.7 | 0.4 | 1.002x | 1.002x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.5 | 18.0 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.005x | 1.005x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 1.001x | 1.001x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.5 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 22.2 | 1.8 | 1.003x | 1.003x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 21.7 | 1.6 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 22.1 | 1.8 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.3 | 1.002x | 1.002x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.4 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 25.0 | 2.9 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 22.3 | 1.9 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 20.1 | 1.0 | 1.002x | 1.002x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 19.4 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 22.3 | 1.9 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.004x | 1.004x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.2 | 1.003x | 1.003x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.4 | 0.3 | 1.004x | 1.004x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.004x | 1.004x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.8 | 17.6 | 18.2 | 0.2 | 1.005x | 1.005x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.1 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.8 | 17.6 | 17.9 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.9 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 18.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 19.2 | 0.6 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.004x | 1.004x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.9 | 8.9 | 10.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.9 | 8.9 | 9.5 | 0.3 | 1.006x | 1.006x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 9.3 | 9.0 | 11.1 | 0.8 | 1.047x | 1.047x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.6 | 9.0 | 12.0 | 1.1 | 1.084x | 1.084x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 9.1 | 10.0 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.4 | 0.5 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 1.006x | 1.006x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.9 | 17.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.9 | 17.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.9 | 17.2 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.9 | 17.8 | 0.4 | 1.001x | 1.001x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.5 | 17.4 | 17.5 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.5 | 17.5 | 17.5 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.5 | 17.5 | 17.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.1 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.1 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.8 | 17.6 | 18.6 | 0.4 | 1.007x | 1.007x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.8 | 17.7 | 17.9 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.4 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 1.003x | 1.003x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 18.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 18.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.1 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.8 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 18.5 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 1.003x | 1.003x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.4 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.4 | 17.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 1.003x | 1.003x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 18.6 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.5 | 17.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.004x | 1.004x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.9 | 9.9 | 10.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.9 | 10.0 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.5 | 0.3 | 1.012x | 1.012x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.1 | 10.0 | 11.0 | 0.4 | 1.021x | 1.021x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 6.2 | 6.2 | 7.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 6.2 | 6.2 | 6.4 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 6.3 | 6.2 | 6.8 | 0.2 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 6.2 | 7.4 | 0.5 | 1.190x | 1.190x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.0 | 12.7 | 13.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 1.029x | 1.029x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 1.035x | 1.035x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 17.1 | 17.2 | 0.0 | 1.008x | 1.008x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 17.0 | 17.2 | 0.1 | 1.011x | 1.011x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.1 | 17.2 | 0.1 | 1.012x | 1.012x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.9 | 9.8 | 10.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 10.0 | 9.7 | 10.5 | 0.3 | 1.011x | 1.011x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 10.3 | 9.6 | 10.9 | 0.5 | 1.042x | 1.042x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 10.7 | 10.2 | 10.9 | 0.3 | 1.075x | 1.075x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.2 | 8.9 | 9.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 9.7 | 8.9 | 10.1 | 0.4 | 1.052x | 1.052x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 9.8 | 8.9 | 10.7 | 0.6 | 1.063x | 1.063x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 10.0 | 8.9 | 10.9 | 0.8 | 1.088x | 1.088x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 614,572.7 | 614,311.7 | 615,977.0 | 597.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 614,617.3 | 614,557.1 | 614,873.7 | 114.6 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 614,647.8 | 614,444.4 | 615,494.4 | 382.3 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 614,830.1 | 614,531.2 | 615,127.2 | 205.4 | 1.000x | 1.000x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,672.4 | 17,670.6 | 17,703.4 | 13.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,683.2 | 17,670.8 | 17,710.9 | 14.7 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,697.6 | 17,674.8 | 18,718.9 | 412.4 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,742.7 | 17,700.1 | 17,762.8 | 20.8 | 1.004x | 1.004x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,654.4 | 17,653.8 | 17,686.3 | 14.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,693.9 | 17,664.6 | 17,751.8 | 30.6 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,700.8 | 17,684.4 | 17,704.0 | 7.9 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,717.6 | 17,705.7 | 17,764.8 | 21.0 | 1.004x | 1.004x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 31,025.1 | 30,927.2 | 31,044.7 | 41.6 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 31,027.5 | 30,980.6 | 31,104.0 | 42.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 31,213.1 | 31,159.3 | 31,295.4 | 47.7 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 31,269.7 | 31,218.4 | 31,400.1 | 72.8 | 1.008x | 1.008x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,652.0 | 17,641.7 | 17,700.5 | 22.5 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,658.2 | 17,622.1 | 17,710.5 | 33.7 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,671.5 | 17,637.2 | 17,693.5 | 18.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,681.6 | 17,644.8 | 17,705.2 | 20.7 | 1.002x | 1.002x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.6 | 32.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.6 | 32.7 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.9 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.4 | 63.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.4 | 63.4 | 63.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.5 | 63.4 | 63.5 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.4 | 63.6 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.3 | 40.2 | 40.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.3 | 40.2 | 40.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.5 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.5 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 82.7 | 82.5 | 83.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.8 | 82.8 | 83.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.9 | 82.8 | 83.8 | 0.4 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 83.0 | 82.8 | 83.1 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.5 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.3 | 19.0 | 0.3 | 1.005x | 1.005x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.8 | 28.7 | 29.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.8 | 28.7 | 30.4 | 0.6 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 28.7 | 29.5 | 0.3 | 1.014x | 1.014x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 28.8 | 30.4 | 0.6 | 1.025x | 1.025x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.5 | 43.4 | 43.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.6 | 43.4 | 43.7 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.7 | 43.2 | 43.7 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.7 | 43.5 | 43.8 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 89.6 | 89.4 | 90.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 89.7 | 89.6 | 90.1 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 90.1 | 89.8 | 101.9 | 4.7 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 90.1 | 89.6 | 90.5 | 0.3 | 1.005x | 1.005x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 61.3 | 60.9 | 61.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 61.3 | 61.2 | 61.7 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.4 | 61.3 | 61.6 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.4 | 61.3 | 61.7 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 124.8 | 124.6 | 127.5 | 1.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 124.9 | 124.7 | 125.3 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 125.0 | 124.8 | 125.3 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.1 | 124.8 | 125.5 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.5 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.7 | 29.7 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.9 | 28.8 | 29.1 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.9 | 29.9 | 0.4 | 1.005x | 1.005x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.1 | 31.0 | 31.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.1 | 31.0 | 32.3 | 0.5 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.1 | 31.1 | 31.2 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.1 | 31.0 | 31.1 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.0 | 59.7 | 60.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.1 | 59.6 | 60.6 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.2 | 60.0 | 60.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 60.2 | 59.9 | 60.4 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.7 | 46.6 | 46.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.0 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.0 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.9 | 46.7 | 47.3 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.3 | 95.2 | 95.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 95.3 | 95.2 | 95.6 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 95.5 | 95.3 | 95.8 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 96.0 | 95.1 | 96.6 | 0.5 | 1.007x | 1.007x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.9 | 36.9 | 37.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.9 | 36.9 | 37.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 36.9 | 37.0 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 37.0 | 37.0 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 74.3 | 74.2 | 74.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 74.3 | 74.2 | 74.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.5 | 74.3 | 74.6 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.5 | 74.2 | 75.1 | 0.4 | 1.003x | 1.003x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.4 | 56.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.4 | 56.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.1 | 56.6 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.5 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.4 | 11.8 | 12.5 | 0.3 | 1.022x | 1.022x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 11.9 | 12.4 | 0.2 | 1.022x | 1.022x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.9 | 37.8 | 38.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 37.9 | 37.8 | 38.0 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 37.9 | 37.6 | 38.2 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.9 | 37.8 | 38.1 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.7 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.6 | 0.0 | 1.006x | 1.006x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.6 | 70.5 | 70.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.6 | 70.8 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.5 | 70.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.9 | 70.6 | 71.0 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.1 | 35.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 36.0 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.6 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.5 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.7 | 70.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.5 | 71.1 | 0.2 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.4 | 57.4 | 0.4 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.4 | 58.2 | 0.7 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.6 | 56.5 | 57.7 | 0.6 | 1.002x | 1.002x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 33.9 | 33.9 | 34.1 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.5 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.7 | 0.3 | 1.005x | 1.005x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.9 | 68.6 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.8 | 67.4 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 66.9 | 67.4 | 0.2 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.8 | 66.9 | 75.1 | 3.0 | 1.013x | 1.013x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.9 | 11.8 | 0.4 | 1.121x | 1.121x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.9 | 10.9 | 11.3 | 0.2 | 1.122x | 1.122x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.8 | 29.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.0 | 28.9 | 29.6 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.9 | 29.7 | 0.3 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.4 | 29.7 | 0.1 | 1.019x | 1.019x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.2 | 35.8 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.6 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 37.6 | 0.8 | 1.004x | 1.004x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.5 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.6 | 71.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.9 | 70.8 | 71.0 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.9 | 33.9 | 33.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.0 | 33.8 | 34.4 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.0 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.7 | 34.0 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 66.9 | 66.8 | 67.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.8 | 67.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 66.9 | 67.7 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 67.2 | 66.9 | 68.2 | 0.6 | 1.004x | 1.004x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.7 | 0.2 | 1.018x | 1.018x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.2 | 10.0 | 11.2 | 0.5 | 1.105x | 1.105x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.2 | 10.0 | 12.4 | 0.9 | 1.105x | 1.105x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.7 | 30.5 | 31.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.8 | 30.8 | 30.9 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.9 | 30.8 | 31.1 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 30.9 | 30.8 | 31.3 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.6 | 38.4 | 38.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.6 | 38.6 | 38.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.6 | 38.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.6 | 38.7 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.6 | 77.6 | 77.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.6 | 77.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.7 | 77.6 | 77.8 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.6 | 77.7 | 0.0 | 1.000x | 1.000x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.5 | 56.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.5 | 56.5 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.5 | 56.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.7 | 41.7 | 42.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.9 | 41.6 | 42.1 | 0.2 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.8 | 84.6 | 85.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 84.9 | 84.9 | 84.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 84.9 | 84.8 | 85.0 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.0 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.7 | 70.7 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 79.6 | 3.5 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.9 | 70.8 | 72.2 | 0.6 | 1.002x | 1.002x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.5 | 56.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.5 | 56.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.5 | 56.6 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.5 | 64.9 | 3.3 | 1.001x | 1.001x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.6 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.7 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.6 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.6 | 71.0 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.8 | 41.7 | 42.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.8 | 41.6 | 42.1 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.8 | 41.7 | 42.0 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.1 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 84.9 | 84.8 | 85.0 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 84.9 | 84.8 | 85.1 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.7 | 85.2 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.9 | 41.8 | 41.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.9 | 41.7 | 42.0 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 84.9 | 84.8 | 85.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.9 | 84.8 | 85.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 85.0 | 84.8 | 85.9 | 0.4 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.6 | 85.2 | 86.0 | 0.3 | 1.008x | 1.008x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 24.9 | 25.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.3 | 25.0 | 25.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.3 | 24.8 | 25.8 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.3 | 24.9 | 25.5 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.7 | 48.6 | 48.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.6 | 48.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.7 | 48.6 | 49.1 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.6 | 49.3 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.1 | 24.9 | 25.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 25.1 | 25.4 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.2 | 25.1 | 25.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 25.1 | 25.6 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.005x | 1.005x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 33.1 | 33.0 | 33.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.1 | 33.1 | 38.7 | 2.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.2 | 33.0 | 33.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 33.3 | 33.1 | 33.5 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 29.2 | 29.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.2 | 30.0 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.3 | 29.6 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.1 | 29.9 | 0.3 | 1.006x | 1.006x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.1 | 29.0 | 29.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.1 | 29.0 | 29.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.2 | 29.1 | 30.1 | 0.4 | 1.006x | 1.006x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.2 | 30.0 | 0.3 | 1.017x | 1.017x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.1 | 20.1 | 20.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.4 | 21.4 | 21.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 21.5 | 21.4 | 21.6 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.5 | 21.6 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.5 | 21.6 | 0.0 | 1.004x | 1.004x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.0 | 27.8 | 28.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 28.1 | 27.7 | 28.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.2 | 27.9 | 28.5 | 0.2 | 1.007x | 1.007x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.3 | 27.7 | 29.1 | 0.5 | 1.008x | 1.008x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.015x | 1.015x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.2 | 0.1 | 1.023x | 1.023x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.7 | 29.7 | 30.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.8 | 29.3 | 30.3 | 0.4 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.9 | 29.2 | 30.5 | 0.4 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.6 | 30.3 | 0.3 | 1.006x | 1.006x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.5 | 23.2 | 23.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.9 | 23.5 | 24.2 | 0.2 | 1.018x | 1.018x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.0 | 23.6 | 24.1 | 0.2 | 1.024x | 1.024x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 24.4 | 23.8 | 24.7 | 0.3 | 1.038x | 1.038x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 1.006x | 1.006x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.6 | 30.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.6 | 30.2 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.0 | 29.6 | 30.4 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.0 | 29.4 | 30.2 | 0.3 | 1.006x | 1.006x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 10.0 | 11.2 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.1 | 10.0 | 11.2 | 0.6 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 1.021x | 1.021x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 1.023x | 1.023x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.4 | 63.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.5 | 63.5 | 63.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.4 | 64.1 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.7 | 63.3 | 63.8 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.4 | 7.4 | 7.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.6 | 7.4 | 8.6 | 0.5 | 1.033x | 1.033x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.2 | 7.4 | 8.6 | 0.5 | 1.111x | 1.111x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.6 | 7.4 | 9.5 | 0.8 | 1.159x | 1.159x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.9 | 8.9 | 10.9 | 0.7 | 1.124x | 1.124x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.2 | 0.2 | 1.134x | 1.134x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.8 | 21.6 | 22.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 22.0 | 21.8 | 22.3 | 0.2 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.0 | 21.7 | 22.2 | 0.2 | 1.009x | 1.009x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 22.1 | 21.8 | 23.0 | 0.4 | 1.012x | 1.012x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.7 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.5 | 12.2 | 12.7 | 0.2 | 1.008x | 1.008x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.6 | 12.4 | 13.3 | 0.4 | 1.018x | 1.018x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.2 | 13.9 | 15.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.5 | 14.3 | 15.4 | 0.4 | 1.021x | 1.021x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 15.2 | 14.2 | 15.4 | 0.4 | 1.070x | 1.070x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 15.3 | 15.1 | 15.4 | 0.1 | 1.074x | 1.074x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 12.0 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.9 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.1 | 0.1 | 1.014x | 1.014x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 75.2 | 75.2 | 75.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.1 | 75.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.3 | 75.2 | 75.8 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.4 | 75.1 | 75.8 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.0 | 0.5 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 8.9 | 10.0 | 0.5 | 1.041x | 1.041x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 65.4 | 65.4 | 65.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.4 | 65.3 | 65.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 65.5 | 65.2 | 65.8 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.6 | 65.3 | 66.0 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 1.023x | 1.023x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.023x | 1.023x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.5 | 28.4 | 28.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.8 | 28.3 | 29.1 | 0.3 | 1.010x | 1.010x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.0 | 28.6 | 29.7 | 0.4 | 1.015x | 1.015x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 28.8 | 29.6 | 0.3 | 1.026x | 1.026x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.9 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.8 | 21.8 | 21.9 | 0.0 | 1.004x | 1.004x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.6 | 21.6 | 22.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.6 | 21.4 | 22.1 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 21.7 | 21.6 | 22.4 | 0.3 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.8 | 21.6 | 22.0 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.0 | 22.8 | 23.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.0 | 22.9 | 23.4 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.0 | 22.9 | 23.4 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 23.7 | 23.4 | 23.8 | 0.1 | 1.031x | 1.031x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 15.3 | 15.2 | 15.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 15.3 | 15.3 | 15.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.3 | 15.4 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.3 | 15.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.0 | 0.2 | 1.016x | 1.016x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.0 | 10.4 | 11.2 | 0.3 | 1.019x | 1.019x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.0 | 10.7 | 11.1 | 0.2 | 1.021x | 1.021x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.9 | 72.9 | 73.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.0 | 72.7 | 73.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.0 | 72.8 | 73.2 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 73.1 | 72.7 | 73.4 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.7 | 0.1 | 1.010x | 1.010x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.7 | 0.0 | 1.010x | 1.010x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 57.9 | 57.7 | 58.7 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 57.9 | 57.8 | 58.6 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 57.9 | 57.7 | 58.2 | 0.2 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 58.3 | 58.0 | 58.5 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.7 | 10.9 | 0.1 | 1.016x | 1.016x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.7 | 11.2 | 0.2 | 1.018x | 1.018x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.3 | 0.1 | 1.037x | 1.037x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.0 | 72.6 | 73.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.1 | 73.0 | 73.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 73.1 | 72.9 | 73.3 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 73.2 | 73.0 | 73.6 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 22.6 | 22.4 | 23.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.7 | 22.6 | 22.8 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 22.8 | 22.7 | 23.1 | 0.2 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.8 | 22.5 | 23.1 | 0.3 | 1.010x | 1.010x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.010x | 1.010x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.2 | 17.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.3 | 17.1 | 18.0 | 0.4 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.4 | 17.3 | 17.5 | 0.1 | 1.010x | 1.010x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 16.9 | 18.2 | 0.5 | 1.029x | 1.029x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.006x | 1.006x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 16.7 | 17.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.1 | 17.6 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.2 | 16.9 | 17.8 | 0.3 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.3 | 17.0 | 17.3 | 0.1 | 1.009x | 1.009x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.8 | 16.6 | 17.7 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.1 | 17.4 | 0.1 | 1.022x | 1.022x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.2 | 17.8 | 0.2 | 1.027x | 1.027x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.3 | 17.2 | 17.5 | 0.1 | 1.030x | 1.030x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.2 | 19.0 | 19.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.2 | 19.0 | 19.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 19.2 | 19.0 | 19.3 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 19.7 | 19.2 | 20.1 | 0.3 | 1.026x | 1.026x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,061.5 | 19,061.0 | 19,122.3 | 24.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,061.8 | 19,060.2 | 19,064.4 | 1.4 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,063.0 | 19,062.1 | 19,066.6 | 1.5 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,064.1 | 19,062.7 | 19,065.6 | 0.9 | 1.000x | 1.000x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,458.7 | 7,458.5 | 7,459.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,460.1 | 7,459.4 | 7,460.6 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,460.3 | 7,459.2 | 7,463.6 | 1.7 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,460.6 | 7,459.6 | 7,464.1 | 1.6 | 1.000x | 1.000x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,546.7 | 9,546.1 | 9,547.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,547.1 | 9,546.9 | 9,548.8 | 0.7 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,547.7 | 9,547.1 | 9,548.9 | 0.6 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,547.8 | 9,547.0 | 9,549.4 | 0.8 | 1.000x | 1.000x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,034.8 | 19,034.2 | 19,055.2 | 8.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,035.2 | 19,034.9 | 19,037.7 | 1.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,037.4 | 19,036.2 | 19,042.5 | 2.3 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,037.9 | 19,035.3 | 19,039.7 | 1.9 | 1.000x | 1.000x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,736.1 | 3,735.5 | 3,737.7 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,737.2 | 3,736.1 | 3,872.5 | 54.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,737.5 | 3,736.4 | 3,737.9 | 0.5 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,738.1 | 3,736.5 | 3,739.7 | 1.1 | 1.001x | 1.001x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,783.1 | 4,782.6 | 4,789.4 | 2.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,784.6 | 4,783.5 | 4,885.0 | 40.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,785.1 | 4,782.4 | 4,790.0 | 2.5 | 1.000x | 1.000x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,785.2 | 4,783.8 | 4,785.8 | 0.9 | 1.000x | 1.000x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,643.4 | 7,642.7 | 7,645.0 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,643.5 | 7,642.7 | 7,643.9 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,643.5 | 7,643.2 | 7,644.9 | 0.6 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,643.7 | 7,642.8 | 7,645.9 | 1.1 | 1.000x | 1.000x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 9.8 | 0.4 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.9 | 10.9 | 0.8 | 1.101x | 1.101x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 8.9 | 10.7 | 0.7 | 1.114x | 1.114x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.0 | 23.9 | 24.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 24.0 | 24.0 | 24.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.2 | 23.9 | 24.7 | 0.3 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 24.4 | 23.9 | 26.0 | 0.8 | 1.018x | 1.018x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.0 | 33.8 | 34.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.0 | 33.7 | 37.4 | 1.4 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.1 | 33.8 | 34.2 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 66.9 | 66.9 | 67.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 66.9 | 67.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.1 | 66.9 | 68.7 | 0.8 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.3 | 67.0 | 68.1 | 0.4 | 1.005x | 1.005x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.4 | 35.4 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.6 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 73.0 | 3.9 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.7 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.1 | 63.8 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.7 | 16.7 | 17.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.8 | 16.7 | 17.3 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.8 | 16.7 | 17.0 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 25.8 | 25.7 | 26.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.9 | 25.7 | 26.2 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.9 | 25.8 | 27.1 | 0.5 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 26.0 | 25.8 | 26.4 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.9 | 11.7 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 13.8 | 0.7 | 1.012x | 1.012x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.6 | 11.8 | 12.8 | 0.4 | 1.060x | 1.060x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.9 | 11.8 | 13.9 | 0.8 | 1.086x | 1.086x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.3 | 30.2 | 30.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.3 | 29.9 | 42.9 | 5.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 30.3 | 30.3 | 30.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.7 | 30.1 | 30.9 | 0.3 | 1.014x | 1.014x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.1 | 28.1 | 28.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.2 | 28.1 | 28.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 28.3 | 28.1 | 29.0 | 0.3 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 28.3 | 28.2 | 28.4 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.9 | 52.8 | 53.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 52.9 | 52.8 | 55.2 | 0.9 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.9 | 52.8 | 53.1 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 53.0 | 52.7 | 55.6 | 1.1 | 1.002x | 1.002x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.1 | 55.9 | 56.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 56.2 | 56.1 | 56.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 56.2 | 56.1 | 56.5 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.3 | 56.0 | 56.8 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.3 | 114.1 | 114.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.4 | 114.3 | 115.2 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 114.5 | 114.4 | 115.0 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 114.6 | 114.3 | 114.7 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.9 | 42.8 | 43.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.0 | 42.9 | 43.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.0 | 42.9 | 43.2 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.1 | 42.9 | 43.1 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 93.7 | 93.5 | 94.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 93.8 | 93.8 | 94.3 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 94.0 | 93.7 | 94.3 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 94.0 | 93.8 | 94.1 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.2 | 23.1 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 23.3 | 23.2 | 23.5 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.3 | 23.1 | 23.4 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.4 | 23.2 | 23.7 | 0.2 | 1.009x | 1.009x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.009x | 1.009x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.7 | 29.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.8 | 29.6 | 30.2 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.8 | 29.7 | 30.5 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.6 | 30.1 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.8 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.2 | 63.8 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.4 | 63.2 | 63.7 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.3 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.5 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 64.3 | 0.4 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 64.6 | 0.5 | 1.002x | 1.002x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.4 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.5 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 64.2 | 0.4 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.3 | 29.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 29.5 | 29.2 | 29.9 | 0.3 | 1.003x | 1.003x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 29.2 | 30.1 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.2 | 29.9 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.9 | 9.7 | 10.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.7 | 10.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 1.014x | 1.014x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.0 | 11.3 | 0.5 | 1.040x | 1.040x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.000x | 1.000x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.8 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.8 | 9.8 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 9.0 | 10.0 | 0.4 | 1.100x | 1.100x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 8.9 | 10.5 | 0.5 | 1.103x | 1.103x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.3 | 8.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 8.4 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 8.4 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.4 | 8.3 | 8.5 | 0.1 | 1.015x | 1.015x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 10.0 | 11.8 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 10.0 | 11.4 | 0.6 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.019x | 1.019x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.9 | 0.3 | 1.023x | 1.023x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.0 | 10.3 | 0.9 | 1.037x | 1.037x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.6 | 7.4 | 8.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 8.1 | 7.4 | 8.6 | 0.4 | 1.062x | 1.062x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.2 | 7.4 | 8.6 | 0.5 | 1.083x | 1.083x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.6 | 7.4 | 8.6 | 0.5 | 1.126x | 1.126x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 3,781,012.1 | 3,780,506.7 | 3,790,958.3 | 4,032.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,781,298.9 | 3,780,338.5 | 3,782,413.5 | 672.8 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,783,715.4 | 3,782,407.1 | 3,784,469.2 | 678.6 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,785,158.1 | 3,783,675.5 | 3,810,823.3 | 10,482.7 | 1.001x | 1.001x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,668.3 | 17,646.1 | 17,686.7 | 14.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,670.8 | 17,650.6 | 17,712.5 | 20.9 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,681.2 | 17,665.7 | 17,721.4 | 19.0 | 1.001x | 1.001x |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,683.1 | 17,672.8 | 17,709.2 | 13.1 | 1.001x | 1.001x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,672.5 | 17,661.2 | 17,704.6 | 14.9 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,675.2 | 17,668.9 | 17,717.3 | 19.8 | 1.000x | 1.000x |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,675.6 | 17,633.3 | 17,680.7 | 17.5 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,702.3 | 17,681.9 | 17,719.5 | 14.0 | 1.002x | 1.002x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,216,105.3 | 3,212,923.5 | 3,222,290.9 | 3,786.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,220,264.1 | 3,216,150.4 | 3,224,307.0 | 2,783.0 | 1.001x | 1.001x |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,221,972.1 | 3,216,211.5 | 3,227,614.8 | 4,212.0 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 3,230,027.0 | 3,224,378.2 | 3,233,360.6 | 3,079.6 | 1.004x | 1.004x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,668.4 | 17,645.7 | 17,703.0 | 20.7 | 1.000x | 1.000x |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,687.7 | 17,674.1 | 17,756.3 | 31.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,696.1 | 17,643.2 | 17,704.3 | 22.2 | 1.002x | 1.002x |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | yes | `plain` | same program | 17,701.9 | 17,664.7 | 17,705.7 | 15.5 | 1.002x | 1.002x |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**444 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.982x | no verdict: gap 1.76%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 38.0 | `pcrec_7388f1c0_auto-caps-simdna` | 37.9 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.7 | `pcrec_7388f1c0_auto-caps-simdna` | 9.5 | 0.971x | no verdict: gap 2.90%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.2 | `pcrec_7388f1c0_auto-caps-simdna` | 9.8 | 0.965x | no verdict: gap 3.46%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 31.0 | `pcrec_7388f1c0_auto-caps-simdna` | 30.9 | 0.996x | no verdict: gap 0.39%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 30.9 | `pcrec_a15fb77b_auto-caps-simdna` | 30.8 | 0.995x | no verdict: gap 0.48%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.3 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.0 | `pcrec_7388f1c0_auto-caps-simdna` | 25.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 48.9 | `pcrec_7388f1c0_auto-caps-simdna` | 48.7 | 0.996x | no verdict: gap 0.40%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 48.9 | `pcrec_a15fb77b_auto-caps-simdna` | 48.7 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 25.3 | `pcrec_a15fb77b_auto-caps-simdna` | 25.1 | 0.992x | no verdict: gap 0.78%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 33.3 | `pcrec_7388f1c0_auto-caps-simdna` | 33.1 | 0.994x | no verdict: gap 0.60%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 33.6 | `pcrec_a15fb77b_auto-caps-simdna` | 33.2 | 0.987x | no verdict: gap 1.31%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.3 | `pcrec_a15fb77b_auto-caps-simdna` | 29.1 | 0.994x | no verdict: gap 0.61%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.1 | `pcrec_7388f1c0_auto-caps-simdna` | 16.0 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 20.3 | `pcrec_a15fb77b_auto-caps-simdna` | 20.3 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 28.2 | `pcrec_7388f1c0_auto-caps-simdna` | 28.1 | 0.997x | no verdict: gap 0.34%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 28.0 | `pcrec_a15fb77b_auto-caps-simdna` | 28.0 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.0 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.988x | no verdict: gap 1.19%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.6 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 24.2 | `pcrec_a15fb77b_auto-caps-simdna` | 24.0 | 0.995x | no verdict: gap 0.54%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 23.1 | `pcrec_a15fb77b_auto-caps-simdna` | 23.0 | 0.997x | no verdict: gap 0.35%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.9 | `pcrec_a15fb77b_auto-caps-simdna` | 29.8 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.1 | `pcrec_7388f1c0_auto-caps-simdna` | 9.9 | 0.974x | no verdict: gap 2.58%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 26.2 | `pcrec_7388f1c0_auto-caps-simdna` | 26.2 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.6 | `pcrec_7388f1c0_auto-caps-simdna` | 7.4 | 0.862x | no verdict: gap 13.77%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.6 | `pcrec_a15fb77b_auto-caps-simdna` | 7.4 | 0.862x | no verdict: gap 13.76%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 22.2 | `pcrec_7388f1c0_auto-caps-simdna` | 21.8 | 0.981x | no verdict: gap 1.87%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.4 | `pcrec_7388f1c0_auto-caps-simdna` | 12.3 | 0.994x | no verdict: gap 0.61%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 15.2 | `pcrec_7388f1c0_auto-caps-simdna` | 14.9 | 0.979x | no verdict: gap 2.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 15.1 | `pcrec_a15fb77b_auto-caps-simdna` | 14.8 | 0.981x | no verdict: gap 1.89%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.5 | `pcrec_7388f1c0_auto-caps-simdna` | 11.8 | 0.944x | no verdict: gap 5.57%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 12.0 | 0.990x | no verdict: gap 1.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 28.8 | `pcrec_a15fb77b_auto-caps-simdna` | 28.7 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 21.7 | `pcrec_a15fb77b_auto-caps-simdna` | 21.6 | 0.996x | no verdict: gap 0.40%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.2 | `pcrec_7388f1c0_auto-caps-simdna` | 23.2 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 15.5 | `pcrec_7388f1c0_auto-caps-simdna` | 15.1 | 0.972x | no verdict: gap 2.77%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 15.4 | `pcrec_a15fb77b_auto-caps-simdna` | 15.1 | 0.984x | no verdict: gap 1.60%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.1 | `pcrec_7388f1c0_auto-caps-simdna` | 10.8 | 0.977x | no verdict: gap 2.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 10.8 | `pcrec_a15fb77b_auto-caps-simdna` | 10.7 | 0.992x | no verdict: gap 0.82%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 14.7 | `pcrec_a15fb77b_auto-caps-simdna` | 14.7 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.1 | `pcrec_7388f1c0_auto-caps-simdna` | 10.9 | 0.986x | no verdict: gap 1.44%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.3 | `pcrec_a15fb77b_auto-caps-simdna` | 17.1 | 0.988x | no verdict: gap 1.24%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.3 | `pcrec_a15fb77b_auto-caps-simdna` | 16.7 | 0.969x | no verdict: gap 3.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.3 | `pcrec_a15fb77b_auto-caps-simdna` | 17.1 | 0.987x | no verdict: gap 1.27%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19.3 | `pcrec_7388f1c0_auto-caps-simdna` | 19.3 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,463.6 | `pcrec_7388f1c0_auto-caps-simdna` | 7,460.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 19,037.8 | `pcrec_a15fb77b_auto-caps-simdna` | 19,036.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.2 | `pcrec_a15fb77b_auto-caps-simdna` | 16.2 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 4,783.7 | `pcrec_a15fb77b_auto-caps-simdna` | 4,783.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.8 | `pcrec_7388f1c0_auto-caps-simdna` | 9.5 | 0.965x | no verdict: gap 3.51%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 24.9 | `pcrec_a15fb77b_auto-caps-simdna` | 24.3 | 0.978x | no verdict: gap 2.23%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.0 | `pcrec_7388f1c0_auto-caps-simdna` | 11.8 | 0.986x | no verdict: gap 1.37%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.2 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.9 | `pcrec_7388f1c0_auto-caps-simdna` | 29.8 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.2 | `pcrec_a15fb77b_auto-caps-simdna` | 16.2 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.5 | `pcrec_7388f1c0_auto-caps-simdna` | 29.3 | 0.994x | no verdict: gap 0.61%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.3 | `pcrec_a15fb77b_auto-caps-simdna` | 29.3 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.1 | `pcrec_7388f1c0_auto-caps-simdna` | 9.8 | 0.967x | no verdict: gap 3.31%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 9.9 | `pcrec_a15fb77b_auto-caps-simdna` | 9.8 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4.1 | `pcrec_7388f1c0_auto-caps-simdna` | 3.9 | 0.938x | no verdict: gap 6.24%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 4.1 | `pcrec_a15fb77b_auto-caps-simdna` | 3.9 | 0.947x | no verdict: gap 5.28%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.7 | `pcrec_7388f1c0_auto-caps-simdna` | 9.5 | 0.980x | no verdict: gap 1.98%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.3 | `pcrec_7388f1c0_auto-caps-simdna` | 8.3 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.3 | `pcrec_7388f1c0_auto-caps-simdna` | 10.0 | 0.969x | no verdict: gap 3.07%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 11.5 | `pcrec_a15fb77b_auto-caps-simdna` | 11.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.3 | `pcrec_7388f1c0_auto-caps-simdna` | 8.0 | 0.964x | no verdict: gap 3.61%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.0 | `pcrec_a15fb77b_auto-caps-simdna` | 8.0 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.4 | `pcrec_7388f1c0_auto-caps-simdna` | 7.4 | 0.875x | no verdict: gap 12.53%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 7.9 | `pcrec_a15fb77b_auto-caps-simdna` | 7.7 | 0.974x | no verdict: gap 2.60%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,677.6 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.3 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,693.1 | `pcrec_a15fb77b_auto-caps-simdna` | 17,649.6 | 0.998x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,218,842.8 | `pcrec_7388f1c0_auto-caps-simdna` | 3,164,062.6 | 0.983x | no verdict: gap 1.70%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,222,237.7 | `pcrec_a15fb77b_auto-caps-simdna` | 3,163,933.4 | 0.982x | no verdict: gap 1.81%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,717.4 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.4 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,691.8 | `pcrec_a15fb77b_auto-caps-simdna` | 17,675.1 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.8 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 18.3 | `pcrec_7388f1c0_auto-caps-simdna` | 18.2 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 18.2 | `pcrec_a15fb77b_auto-caps-simdna` | 18.2 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.6 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 0.997x | no verdict: gap 0.34%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 9.6 | `pcrec_a15fb77b_auto-caps-simdna` | 9.3 | 0.966x | no verdict: gap 3.42%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.2 | `pcrec_7388f1c0_auto-caps-simdna` | 9.2 | 0.994x | no verdict: gap 0.62%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.9 | `pcrec_a15fb77b_auto-caps-simdna` | 16.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.8 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.995x | no verdict: gap 0.52%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.6 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 6.3 | `pcrec_a15fb77b_auto-caps-simdna` | 6.2 | 0.991x | no verdict: gap 0.94%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.1 | `pcrec_7388f1c0_auto-caps-simdna` | 17.0 | 0.992x | no verdict: gap 0.82%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.9 | `pcrec_a15fb77b_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.0 | `pcrec_7388f1c0_auto-caps-simdna` | 9.7 | 0.967x | no verdict: gap 3.34%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,830.1 | `pcrec_7388f1c0_auto-caps-simdna` | 614,572.7 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 614,647.8 | `pcrec_a15fb77b_auto-caps-simdna` | 614,617.3 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,269.7 | `pcrec_7388f1c0_auto-caps-simdna` | 31,213.1 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 31,027.5 | `pcrec_a15fb77b_auto-caps-simdna` | 31,025.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,681.6 | `pcrec_a15fb77b_auto-caps-simdna` | 17,658.2 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.5 | `pcrec_7388f1c0_auto-caps-simdna` | 63.5 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 82.9 | `pcrec_a15fb77b_auto-caps-simdna` | 82.7 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 18.3 | `pcrec_7388f1c0_auto-caps-simdna` | 18.3 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.2 | `pcrec_7388f1c0_auto-caps-simdna` | 28.8 | 0.986x | no verdict: gap 1.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.5 | `pcrec_a15fb77b_auto-caps-simdna` | 28.8 | 0.976x | no verdict: gap 2.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 43.7 | `pcrec_7388f1c0_auto-caps-simdna` | 43.6 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 43.7 | `pcrec_a15fb77b_auto-caps-simdna` | 43.5 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 90.1 | `pcrec_7388f1c0_auto-caps-simdna` | 89.7 | 0.996x | no verdict: gap 0.45%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 90.1 | `pcrec_a15fb77b_auto-caps-simdna` | 89.6 | 0.995x | no verdict: gap 0.48%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 61.4 | `pcrec_7388f1c0_auto-caps-simdna` | 61.3 | 0.998x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 61.4 | `pcrec_a15fb77b_auto-caps-simdna` | 61.3 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 125.1 | `pcrec_7388f1c0_auto-caps-simdna` | 125.0 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 18.3 | `pcrec_7388f1c0_auto-caps-simdna` | 18.2 | 0.995x | no verdict: gap 0.47%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 18.3 | `pcrec_a15fb77b_auto-caps-simdna` | 18.2 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 28.9 | `pcrec_7388f1c0_auto-caps-simdna` | 28.9 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 31.1 | `pcrec_7388f1c0_auto-caps-simdna` | 31.1 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 31.1 | `pcrec_a15fb77b_auto-caps-simdna` | 31.1 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 46.9 | `pcrec_7388f1c0_auto-caps-simdna` | 46.7 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 46.8 | `pcrec_a15fb77b_auto-caps-simdna` | 46.8 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 96.0 | `pcrec_a15fb77b_auto-caps-simdna` | 95.5 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 37.0 | `pcrec_7388f1c0_auto-caps-simdna` | 36.9 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 37.0 | `pcrec_a15fb77b_auto-caps-simdna` | 36.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 74.5 | `pcrec_7388f1c0_auto-caps-simdna` | 74.3 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 74.5 | `pcrec_a15fb77b_auto-caps-simdna` | 74.3 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 56.5 | `pcrec_a15fb77b_auto-caps-simdna` | 56.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.7 | `pcrec_a15fb77b_auto-caps-simdna` | 29.7 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.5 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 56.5 | `pcrec_a15fb77b_auto-caps-simdna` | 56.5 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 12.1 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 12.4 | `pcrec_a15fb77b_auto-caps-simdna` | 12.4 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 37.9 | `pcrec_7388f1c0_auto-caps-simdna` | 37.9 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.4 | 0.995x | no verdict: gap 0.47%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 35.6 | `pcrec_a15fb77b_auto-caps-simdna` | 35.5 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.5 | `pcrec_7388f1c0_auto-caps-simdna` | 35.5 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 35.5 | `pcrec_a15fb77b_auto-caps-simdna` | 35.5 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.7 | `pcrec_a15fb77b_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 56.6 | `pcrec_a15fb77b_auto-caps-simdna` | 56.5 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 33.9 | `pcrec_7388f1c0_auto-caps-simdna` | 33.9 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 34.0 | `pcrec_a15fb77b_auto-caps-simdna` | 34.0 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 67.0 | `pcrec_7388f1c0_auto-caps-simdna` | 67.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 67.8 | `pcrec_a15fb77b_auto-caps-simdna` | 67.0 | 0.988x | no verdict: gap 1.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 10.9 | `pcrec_a15fb77b_auto-caps-simdna` | 10.9 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.4 | `pcrec_7388f1c0_auto-caps-simdna` | 29.0 | 0.984x | no verdict: gap 1.55%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.0 | `pcrec_a15fb77b_auto-caps-simdna` | 28.9 | 0.995x | no verdict: gap 0.50%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.5 | `pcrec_7388f1c0_auto-caps-simdna` | 35.4 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 35.6 | `pcrec_a15fb77b_auto-caps-simdna` | 35.5 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 34.0 | `pcrec_7388f1c0_auto-caps-simdna` | 33.9 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 34.0 | `pcrec_a15fb77b_auto-caps-simdna` | 34.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 67.1 | `pcrec_7388f1c0_auto-caps-simdna` | 67.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.3 | `pcrec_7388f1c0_auto-caps-simdna` | 10.2 | 0.983x | no verdict: gap 1.74%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 11.2 | `pcrec_a15fb77b_auto-caps-simdna` | 11.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 38.7 | `pcrec_7388f1c0_auto-caps-simdna` | 38.6 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 38.7 | `pcrec_a15fb77b_auto-caps-simdna` | 38.6 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.7 | `pcrec_a15fb77b_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.5 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 41.9 | `pcrec_7388f1c0_auto-caps-simdna` | 41.7 | 0.995x | no verdict: gap 0.48%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 41.9 | `pcrec_a15fb77b_auto-caps-simdna` | 41.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 84.9 | `pcrec_a15fb77b_auto-caps-simdna` | 84.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 70.8 | `pcrec_7388f1c0_auto-caps-simdna` | 70.7 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.7 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.7 | `pcrec_a15fb77b_auto-caps-simdna` | 29.6 | 0.997x | no verdict: gap 0.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.5 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 56.6 | `pcrec_a15fb77b_auto-caps-simdna` | 56.5 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.5 | `pcrec_7388f1c0_auto-caps-simdna` | 35.4 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 70.8 | `pcrec_7388f1c0_auto-caps-simdna` | 70.8 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 70.8 | `pcrec_a15fb77b_auto-caps-simdna` | 70.8 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 41.9 | `pcrec_7388f1c0_auto-caps-simdna` | 41.8 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 85.0 | `pcrec_a15fb77b_auto-caps-simdna` | 84.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 41.9 | `pcrec_7388f1c0_auto-caps-simdna` | 41.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 41.9 | `pcrec_a15fb77b_auto-caps-simdna` | 41.9 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 85.6 | `pcrec_7388f1c0_auto-caps-simdna` | 85.0 | 0.993x | no verdict: gap 0.70%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 84.9 | `pcrec_a15fb77b_auto-caps-simdna` | 84.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.3 | `pcrec_7388f1c0_auto-caps-simdna` | 25.3 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 25.3 | `pcrec_a15fb77b_auto-caps-simdna` | 25.2 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.2 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 33.1 | `pcrec_a15fb77b_auto-caps-simdna` | 33.1 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.1 | `pcrec_a15fb77b_auto-caps-simdna` | 16.1 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.6 | `pcrec_a15fb77b_auto-caps-simdna` | 29.1 | 0.983x | no verdict: gap 1.65%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 20.2 | `pcrec_7388f1c0_auto-caps-simdna` | 20.2 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 20.2 | `pcrec_a15fb77b_auto-caps-simdna` | 20.1 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.5 | `pcrec_7388f1c0_auto-caps-simdna` | 21.4 | 0.996x | no verdict: gap 0.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 21.5 | `pcrec_a15fb77b_auto-caps-simdna` | 21.5 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 23.1 | `pcrec_a15fb77b_auto-caps-simdna` | 23.0 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 28.3 | `pcrec_a15fb77b_auto-caps-simdna` | 28.1 | 0.994x | no verdict: gap 0.65%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 12.0 | 0.992x | no verdict: gap 0.80%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.9 | `pcrec_7388f1c0_auto-caps-simdna` | 29.7 | 0.994x | no verdict: gap 0.62%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 24.0 | `pcrec_7388f1c0_auto-caps-simdna` | 23.9 | 0.994x | no verdict: gap 0.60%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.1 | `pcrec_7388f1c0_auto-caps-simdna` | 23.0 | 0.994x | no verdict: gap 0.55%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 30.0 | `pcrec_a15fb77b_auto-caps-simdna` | 29.8 | 0.994x | no verdict: gap 0.62%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.3 | `pcrec_7388f1c0_auto-caps-simdna` | 10.2 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.6 | `pcrec_7388f1c0_auto-caps-simdna` | 63.5 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 26.2 | `pcrec_7388f1c0_auto-caps-simdna` | 26.1 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 26.1 | `pcrec_a15fb77b_auto-caps-simdna` | 26.1 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.6 | `pcrec_a15fb77b_auto-caps-simdna` | 8.2 | 0.959x | no verdict: gap 4.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 22.0 | `pcrec_7388f1c0_auto-caps-simdna` | 22.0 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.9 | `pcrec_7388f1c0_auto-caps-simdna` | 11.8 | 0.988x | no verdict: gap 1.17%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 11.8 | `pcrec_a15fb77b_auto-caps-simdna` | 11.8 | 0.994x | no verdict: gap 0.59%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 75.3 | `pcrec_7388f1c0_auto-caps-simdna` | 75.3 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 75.4 | `pcrec_a15fb77b_auto-caps-simdna` | 75.2 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.2 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.962x | no verdict: gap 3.78%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 65.6 | `pcrec_7388f1c0_auto-caps-simdna` | 65.5 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 65.4 | `pcrec_a15fb77b_auto-caps-simdna` | 65.4 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 11.8 | `pcrec_a15fb77b_auto-caps-simdna` | 11.8 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.3 | `pcrec_7388f1c0_auto-caps-simdna` | 28.8 | 0.984x | no verdict: gap 1.56%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.7 | `pcrec_7388f1c0_auto-caps-simdna` | 21.7 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.8 | `pcrec_7388f1c0_auto-caps-simdna` | 21.6 | 0.994x | no verdict: gap 0.57%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.2 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 23.2 | `pcrec_a15fb77b_auto-caps-simdna` | 23.1 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.2 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 15.4 | `pcrec_7388f1c0_auto-caps-simdna` | 15.3 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 15.4 | `pcrec_a15fb77b_auto-caps-simdna` | 15.3 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.0 | `pcrec_7388f1c0_auto-caps-simdna` | 11.0 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 73.0 | `pcrec_7388f1c0_auto-caps-simdna` | 72.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 58.3 | `pcrec_7388f1c0_auto-caps-simdna` | 57.9 | 0.993x | no verdict: gap 0.67%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.1 | `pcrec_7388f1c0_auto-caps-simdna` | 10.9 | 0.981x | no verdict: gap 1.87%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.2 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.43%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 22.8 | `pcrec_7388f1c0_auto-caps-simdna` | 22.6 | 0.990x | no verdict: gap 0.96%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.3 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.77%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.4 | `pcrec_7388f1c0_auto-caps-simdna` | 17.3 | 0.993x | no verdict: gap 0.70%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17.7 | `pcrec_a15fb77b_auto-caps-simdna` | 17.2 | 0.972x | no verdict: gap 2.85%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.3 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.75%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.2 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.3 | `pcrec_7388f1c0_auto-caps-simdna` | 17.2 | 0.992x | no verdict: gap 0.76%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 19,063.0 | `pcrec_a15fb77b_auto-caps-simdna` | 19,061.8 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 7,460.6 | `pcrec_a15fb77b_auto-caps-simdna` | 7,460.3 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9,547.7 | `pcrec_7388f1c0_auto-caps-simdna` | 9,546.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 19,037.4 | `pcrec_a15fb77b_auto-caps-simdna` | 19,035.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,738.1 | `pcrec_7388f1c0_auto-caps-simdna` | 3,736.1 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.2 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4,785.1 | `pcrec_7388f1c0_auto-caps-simdna` | 4,784.6 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 4,785.2 | `pcrec_a15fb77b_auto-caps-simdna` | 4,783.1 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,643.7 | `pcrec_7388f1c0_auto-caps-simdna` | 7,643.4 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 7,643.5 | `pcrec_a15fb77b_auto-caps-simdna` | 7,643.5 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 24.2 | `pcrec_a15fb77b_auto-caps-simdna` | 24.0 | 0.993x | no verdict: gap 0.66%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 34.0 | `pcrec_7388f1c0_auto-caps-simdna` | 34.0 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 34.1 | `pcrec_a15fb77b_auto-caps-simdna` | 34.0 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 67.3 | `pcrec_a15fb77b_auto-caps-simdna` | 66.9 | 0.995x | no verdict: gap 0.52%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 32.6 | `pcrec_a15fb77b_auto-caps-simdna` | 32.5 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.3 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.8 | `pcrec_7388f1c0_auto-caps-simdna` | 16.7 | 0.996x | no verdict: gap 0.43%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.8 | `pcrec_a15fb77b_auto-caps-simdna` | 16.8 | 0.996x | no verdict: gap 0.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 26.0 | `pcrec_7388f1c0_auto-caps-simdna` | 25.9 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 25.9 | `pcrec_a15fb77b_auto-caps-simdna` | 25.8 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.3 | `pcrec_7388f1c0_auto-caps-simdna` | 56.2 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 43.1 | `pcrec_7388f1c0_auto-caps-simdna` | 43.0 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.3 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.80%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.4 | `pcrec_7388f1c0_auto-caps-simdna` | 23.2 | 0.991x | no verdict: gap 0.93%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 23.3 | `pcrec_a15fb77b_auto-caps-simdna` | 23.3 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 13.2 | `pcrec_a15fb77b_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.35%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.8 | `pcrec_7388f1c0_auto-caps-simdna` | 29.8 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.5 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.4 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 63.2 | `pcrec_a15fb77b_auto-caps-simdna` | 63.2 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 32.5 | `pcrec_a15fb77b_auto-caps-simdna` | 32.5 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 63.3 | `pcrec_a15fb77b_auto-caps-simdna` | 63.2 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.6 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 32.5 | `pcrec_a15fb77b_auto-caps-simdna` | 32.5 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 63.3 | `pcrec_a15fb77b_auto-caps-simdna` | 63.2 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 63.3 | `pcrec_a15fb77b_auto-caps-simdna` | 63.2 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.5 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 32.5 | `pcrec_a15fb77b_auto-caps-simdna` | 32.5 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 63.2 | `pcrec_a15fb77b_auto-caps-simdna` | 63.2 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 16.1 | `pcrec_a15fb77b_auto-caps-simdna` | 16.1 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.6 | `pcrec_7388f1c0_auto-caps-simdna` | 29.4 | 0.994x | no verdict: gap 0.62%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 29.5 | `pcrec_a15fb77b_auto-caps-simdna` | 29.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4.1 | `pcrec_7388f1c0_auto-caps-simdna` | 4.1 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 4.1 | `pcrec_a15fb77b_auto-caps-simdna` | 4.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.8 | `pcrec_7388f1c0_auto-caps-simdna` | 9.7 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.4 | `pcrec_a15fb77b_auto-caps-simdna` | 8.3 | 0.988x | no verdict: gap 1.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.3 | `pcrec_7388f1c0_auto-caps-simdna` | 10.2 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.0 | `pcrec_7388f1c0_auto-caps-simdna` | 8.0 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.3 | `pcrec_a15fb77b_auto-caps-simdna` | 8.0 | 0.966x | no verdict: gap 3.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19.2 | `pcrec_7388f1c0_auto-caps-simdna` | 19.1 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 19.1 | `pcrec_a15fb77b_auto-caps-simdna` | 19.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 8.2 | `pcrec_a15fb77b_auto-caps-simdna` | 8.1 | 0.980x | no verdict: gap 1.95%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,785,158.1 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,298.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,783,715.4 | `pcrec_a15fb77b_auto-caps-simdna` | 3,781,012.1 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,683.1 | `pcrec_a15fb77b_auto-caps-simdna` | 17,681.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,220,264.1 | `pcrec_7388f1c0_auto-caps-simdna` | 3,216,105.3 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,696.1 | `pcrec_7388f1c0_auto-caps-simdna` | 17,668.4 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |

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
- `pcrec_a15fb77b_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 192,593,532.0 | 183,489,073.0 | 204,394,658.0 | 7,016,613.6 | 5 | 49,472 | 85,071 | 16,377 | 0.036 | compiled=5 | 9,532,702.0 | 181,987,885.0 | 102,100.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 182,787,890.0 | 166,014,228.0 | 189,889,510.0 | 8,638,702.5 | 5 | 37,040 | 42,326 | 16,649 | 0.047 (max is trial 1) | compiled=5 | 9,712,263.0 | 166,823,544.0 | 199,680.0 |
| `factored` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 180,450,705.0 | 179,800,632.0 | 188,754,653.0 | 3,615,905.0 | 5 | 49,472 | 84,868 | 16,170 | 0.020 | compiled=5 | 9,441,531.0 | 170,746,923.0 | 177,002.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 169,047,345.0 | 168,843,344.0 | 182,548,950.0 | 5,696,967.6 | 5 | 37,040 | 42,143 | 16,462 | 0.034 | compiled=5 | 9,502,823.0 | 159,449,401.0 | 106,481.0 |
| `factored` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 192,388,932.0 | 182,509,297.0 | 200,442,183.0 | 6,907,514.1 | 5 | 49,472 | 85,071 | 16,377 | 0.036 | compiled=5 | 9,328,851.0 | 182,646,655.0 | 187,451.0 |
| `factored` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 207,644,984.0 | 195,182,265.0 | 214,034,860.0 | 6,928,437.9 | 5 | 53,712 | 97,282 | 18,293 | 0.033 | compiled=5 | 11,712,935.0 | 191,551,714.0 | 189,911.0 |
| `factored` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 178,873,944.0 | 174,826,913.0 | 195,096,565.0 | 7,744,816.7 | 5 | 49,472 | 84,868 | 16,170 | 0.043 | compiled=5 | 9,459,712.0 | 169,327,823.0 | 97,770.0 |
| `factored` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 197,167,296.0 | 181,501,079.0 | 198,483,283.0 | 6,432,053.1 | 5 | 53,712 | 97,079 | 18,086 | 0.033 | compiled=5 | 11,491,653.0 | 179,352,667.0 | 95,560.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 160,470,489.0 | 159,945,835.0 | 169,664,277.0 | 4,537,888.2 | 5 | 28,912 | 20,571 | 15,574 | 0.028 | compiled=5 | 2,199,062.0 | 158,055,065.0 | 102,460.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 161,299,053.0 | 151,975,422.0 | 172,459,064.0 | 7,199,025.6 | 5 | 28,808 | 19,474 | 15,916 | 0.045 | compiled=5 | 2,090,122.0 | 159,030,470.0 | 99,211.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,150,810.0 | 163,340,653.0 | 177,970,752.0 | 5,321,879.2 | 5 | 28,912 | 20,571 | 15,574 | 0.032 | compiled=5 | 2,175,522.0 | 163,778,776.0 | 201,121.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,244,018.0 | 156,787,437.0 | 173,726,131.0 | 6,265,876.9 | 5 | 28,808 | 19,474 | 15,916 | 0.038 | compiled=5 | 1,914,900.0 | 163,949,396.0 | 99,631.0 |
| `floor` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 163,220,121.0 | 158,983,618.0 | 169,472,102.0 | 4,072,027.2 | 5 | 28,912 | 20,571 | 15,574 | 0.025 | compiled=5 | 2,156,290.0 | 158,601,784.0 | 111,821.0 |
| `floor` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 183,307,509.0 | 174,340,722.0 | 184,584,496.0 | 3,749,259.9 | 5 | 29,056 | 23,535 | 18,212 | 0.020 | compiled=5 | 2,256,773.0 | 180,949,908.0 | 102,771.0 |
| `floor` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 165,827,825.0 | 152,482,252.0 | 173,141,094.0 | 7,197,610.1 | 5 | 28,912 | 20,571 | 15,574 | 0.043 | compiled=5 | 2,187,632.0 | 163,598,593.0 | 186,921.0 |
| `floor` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 184,796,616.0 | 169,787,225.0 | 190,060,758.0 | 7,748,107.9 | 5 | 29,056 | 23,535 | 18,212 | 0.042 | compiled=5 | 2,271,294.0 | 181,839,772.0 | 104,691.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 169,077,386.0 | 166,480,440.0 | 176,582,287.0 | 4,385,119.2 | 5 | 49,440 | 84,644 | 16,117 | 0.026 | compiled=5 | 8,935,539.0 | 160,059,615.0 | 109,510.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 175,055,258.0 | 170,624,474.0 | 185,141,853.0 | 4,809,764.9 | 5 | 32,904 | 41,919 | 16,409 | 0.027 | compiled=5 | 9,040,949.0 | 165,906,589.0 | 107,721.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 186,100,259.0 | 173,570,820.0 | 191,970,331.0 | 7,062,007.0 | 5 | 49,440 | 84,644 | 16,117 | 0.038 (max is trial 1) | compiled=5 | 10,900,751.0 | 169,805,449.0 | 186,381.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 167,064,416.0 | 166,488,471.0 | 179,924,296.0 | 5,352,034.0 | 5 | 32,904 | 41,919 | 16,409 | 0.032 (max is trial 1) | compiled=5 | 8,693,699.0 | 158,271,746.0 | 193,001.0 |
| `orig` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 180,449,624.0 | 177,287,525.0 | 190,509,198.0 | 4,849,704.8 | 5 | 49,440 | 84,644 | 16,117 | 0.027 | compiled=5 | 8,773,917.0 | 171,207,253.0 | 194,941.0 |
| `orig` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 200,726,985.0 | 196,475,203.0 | 209,402,494.0 | 4,224,669.2 | 5 | 53,672 | 96,855 | 18,033 | 0.021 | compiled=5 | 10,745,219.0 | 187,832,585.0 | 110,771.0 |
| `orig` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 187,850,015.0 | 177,651,958.0 | 189,324,242.0 | 5,336,298.0 | 5 | 49,440 | 84,644 | 16,117 | 0.028 | compiled=5 | 8,931,928.0 | 178,765,315.0 | 101,621.0 |
| `orig` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 200,242,521.0 | 191,740,147.0 | 203,547,712.0 | 5,172,302.7 | 5 | 53,672 | 96,855 | 18,033 | 0.026 | compiled=5 | 10,803,499.0 | 181,284,258.0 | 203,682.0 |

