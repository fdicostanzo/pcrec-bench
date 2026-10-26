# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=email-specimen, version=0.2, machine=ryzen7700x, since=2026-10-25T19:30:00Z, until=2026-10-26T08:00:00Z, testee=pcrec_6b2dbd3e_auto-caps-simdna, testee=pcrec_9ae59f5d4_auto-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 6.04% (`pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `short-subject-search`)
    - `email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261026T054355Z` (store/records/email-specimen@0.2/pcrec_6b2dbd3e_auto-caps-simdna/email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261026T054355Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 11.29%
    - `email-specimen@0.2__pcrec_9ae59f5d4_auto-caps-simdna__ryzen7700x__20261026T053647Z` (store/records/email-specimen@0.2/pcrec_9ae59f5d4_auto-caps-simdna/email-specimen@0.2__pcrec_9ae59f5d4_auto-caps-simdna__ryzen7700x__20261026T053647Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 11.85%
- sub-bench version(s): email-specimen@0.2
- machine(s): ryzen7700x
- schema version(s): 1.10
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.10-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance; under v1.10-group a `substitution` row's one-iteration trials are timed and judged (X32 versioned, [B144])
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

_Computed at SET grain only (the D119 bar is a set-grain statement, as R8's `Δ vs previous version` is); this subject-grain render carries no band -- render the same query at `--grain set`._

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.4 | 18.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.9 | 18.8 | 20.3 | 0.6 | 1.024x | 1.024x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.9 | 34.8 | 35.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 35.0 | 34.9 | 35.1 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.0 | 24.0 | 24.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.8 | 24.3 | 26.8 | 0.9 | 1.033x | 1.033x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 45.8 | 45.7 | 46.8 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 46.1 | 45.8 | 46.3 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.6 | 9.4 | 9.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.5 | 10.5 | 0.3 | 1.016x | 1.016x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.0 | 0.1 | 1.007x | 1.007x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.1 | 26.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.6 | 26.4 | 29.9 | 1.3 | 1.010x | 1.010x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 50.8 | 50.7 | 54.9 | 1.6 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 51.0 | 50.7 | 51.4 | 0.3 | 1.005x | 1.005x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 36.8 | 37.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.0 | 38.0 | 0.3 | 1.003x | 1.003x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 72.5 | 72.4 | 73.7 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 72.6 | 72.5 | 73.6 | 0.4 | 1.002x | 1.002x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.5 | 9.4 | 9.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.0 | 0.2 | 1.034x | 1.034x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.7 | 15.1 | 0.2 | 1.012x | 1.012x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 17.3 | 17.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.6 | 17.5 | 18.7 | 0.4 | 1.016x | 1.016x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 35.0 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 33.0 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 28.0 | 28.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.7 | 28.5 | 30.3 | 0.7 | 1.015x | 1.015x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 54.9 | 54.6 | 55.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 55.0 | 54.8 | 55.9 | 0.4 | 1.002x | 1.002x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.4 | 22.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.9 | 23.0 | 0.4 | 1.043x | 1.043x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 41.1 | 41.0 | 41.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 41.2 | 41.0 | 41.7 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.2 | 16.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.6 | 16.4 | 17.5 | 0.4 | 1.014x | 1.014x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 31.0 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.5 | 17.5 | 0.4 | 1.028x | 1.028x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.5 | 30.3 | 31.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.8 | 30.4 | 31.3 | 0.3 | 1.010x | 1.010x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.3 | 6.0 | 6.8 | 0.2 | 1.035x | 1.035x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 22.0 | 21.9 | 22.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 22.0 | 21.9 | 22.4 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.4 | 20.6 | 0.1 | 1.031x | 1.031x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.3 | 39.2 | 39.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.7 | 39.3 | 40.3 | 0.4 | 1.011x | 1.011x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.8 | 19.8 | 20.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.1 | 21.3 | 0.4 | 1.023x | 1.023x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 39.2 | 39.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.8 | 39.2 | 40.3 | 0.4 | 1.015x | 1.015x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15.3 | 15.3 | 15.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15.7 | 15.4 | 16.1 | 0.2 | 1.023x | 1.023x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.8 | 30.3 | 30.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 31.0 | 30.3 | 31.8 | 0.5 | 1.006x | 1.006x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 19.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.4 | 0.2 | 1.022x | 1.022x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.9 | 36.7 | 37.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 37.3 | 37.0 | 37.9 | 0.4 | 1.009x | 1.009x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.8 | 4.8 | 4.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 4.9 | 5.1 | 0.1 | 1.044x | 1.044x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 16.6 | 16.4 | 16.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 16.7 | 16.5 | 16.8 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.4 | 21.1 | 0.2 | 1.031x | 1.031x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.3 | 39.2 | 39.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.8 | 39.3 | 40.3 | 0.4 | 1.013x | 1.013x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.8 | 19.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.2 | 19.5 | 0.1 | 1.027x | 1.027x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.8 | 36.7 | 37.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 37.3 | 36.7 | 38.1 | 0.5 | 1.014x | 1.014x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.1 | 5.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.2 | 5.3 | 0.0 | 1.018x | 1.018x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.4 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.8 | 22.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.7 | 22.5 | 23.3 | 0.3 | 1.025x | 1.025x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 43.3 | 43.2 | 43.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 43.8 | 43.1 | 44.2 | 0.4 | 1.011x | 1.011x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 17.4 | 0.4 | 1.017x | 1.017x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 31.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.6 | 30.5 | 30.9 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.9 | 24.7 | 25.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.4 | 25.2 | 26.3 | 0.4 | 1.021x | 1.021x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 47.7 | 47.7 | 48.5 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 48.0 | 47.7 | 48.7 | 0.4 | 1.006x | 1.006x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.4 | 20.2 | 20.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.4 | 21.8 | 0.5 | 1.014x | 1.014x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 39.2 | 39.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.9 | 39.1 | 40.0 | 0.4 | 1.017x | 1.017x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.2 | 17.3 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.1 | 16.4 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 30.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 30.9 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.2 | 20.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.4 | 21.7 | 0.5 | 1.013x | 1.013x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.3 | 39.2 | 39.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.9 | 39.2 | 40.1 | 0.4 | 1.014x | 1.014x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.9 | 24.7 | 25.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.4 | 25.0 | 26.2 | 0.4 | 1.021x | 1.021x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 48.1 | 47.7 | 48.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 48.2 | 47.7 | 48.6 | 0.3 | 1.002x | 1.002x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.9 | 24.6 | 25.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.0 | 26.6 | 0.6 | 1.023x | 1.023x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 47.7 | 47.7 | 48.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 48.5 | 47.8 | 49.2 | 0.5 | 1.015x | 1.015x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.6 | 6.6 | 7.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.3 | 0.2 | 1.066x | 1.066x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.3 | 12.0 | 12.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.4 | 11.9 | 12.5 | 0.2 | 1.007x | 1.007x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.0 | 7.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.6 | 7.5 | 0.3 | 1.025x | 1.025x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 28.9 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 6.5 | 7.5 | 0.4 | 1.053x | 1.053x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.6 | 12.4 | 13.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 13.0 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.9 | 7.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.6 | 7.5 | 0.3 | 1.038x | 1.038x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 18.5 | 18.3 | 18.6 | 0.1 | 1.007x | 1.007x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.0 | 8.8 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.0 | 15.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.4 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.5 | 8.1 | 8.7 | 0.2 | 1.021x | 1.021x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.2 | 15.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.3 | 15.1 | 15.6 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.6 | 0.1 | 1.016x | 1.016x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.3 | 11.1 | 11.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.5 | 11.2 | 11.8 | 0.2 | 1.016x | 1.016x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.7 | 0.1 | 1.011x | 1.011x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.6 | 14.9 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.6 | 5.9 | 6.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.8 | 6.0 | 6.9 | 0.4 | 1.036x | 1.036x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.6 | 15.6 | 15.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.6 | 16.1 | 0.2 | 1.015x | 1.015x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 7.8 | 8.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 7.3 | 8.1 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.6 | 11.4 | 12.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.8 | 11.6 | 12.0 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.2 | 12.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.1 | 1.028x | 1.028x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.7 | 15.4 | 16.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.9 | 16.1 | 0.1 | 1.015x | 1.015x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.2 | 5.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.2 | 5.8 | 0.2 | 1.102x | 1.102x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.1 | 35.5 | 36.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 36.2 | 35.6 | 37.0 | 0.5 | 1.003x | 1.003x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.3 | 14.3 | 15.2 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.7 | 0.1 | 1.014x | 1.014x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.7 | 3.3 | 3.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.3 | 3.8 | 0.2 | 1.023x | 1.023x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.2 | 4.1 | 4.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.054x | 1.054x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 10.5 | 10.3 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 10.5 | 10.2 | 10.7 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.4 | 5.9 | 6.7 | 0.3 | 1.047x | 1.047x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.5 | 6.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.4 | 6.8 | 0.2 | 1.006x | 1.006x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.0 | 7.0 | 0.4 | 1.129x | 1.129x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 42.1 | 42.0 | 42.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 42.3 | 42.0 | 42.6 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.2 | 4.2 | 4.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.053x | 1.053x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 36.5 | 36.2 | 36.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.6 | 36.0 | 38.1 | 0.8 | 1.004x | 1.004x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.0 | 7.0 | 0.4 | 1.126x | 1.126x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.9 | 14.8 | 15.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.0 | 14.9 | 15.2 | 0.1 | 1.009x | 1.009x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.8 | 0.2 | 1.024x | 1.024x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.8 | 0.2 | 1.014x | 1.014x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.5 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.5 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.6 | 7.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.0 | 0.0 | 1.013x | 1.013x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.9 | 6.7 | 7.0 | 0.1 | 1.020x | 1.020x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.5 | 6.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 6.3 | 0.3 | 1.036x | 1.036x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 41.3 | 41.1 | 41.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 41.5 | 41.2 | 41.8 | 0.2 | 1.006x | 1.006x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.8 | 7.7 | 8.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.9 | 7.3 | 8.1 | 0.3 | 1.015x | 1.015x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 33.1 | 32.9 | 33.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 33.2 | 32.9 | 33.6 | 0.2 | 1.003x | 1.003x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.5 | 5.5 | 6.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 5.6 | 6.4 | 0.3 | 1.099x | 1.099x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 41.2 | 40.9 | 41.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 41.4 | 41.1 | 41.7 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.6 | 7.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.4 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 10.8 | 10.7 | 11.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 10.8 | 10.7 | 11.1 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.6 | 7.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 6.9 | 7.5 | 0.2 | 1.056x | 1.056x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.0 | 8.0 | 8.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 7.9 | 8.1 | 0.1 | 1.007x | 1.007x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.0 | 7.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 6.7 | 7.5 | 0.3 | 1.052x | 1.052x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.0 | 8.0 | 8.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 7.9 | 8.2 | 0.1 | 1.011x | 1.011x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.6 | 6.6 | 7.6 | 0.4 | 1.074x | 1.074x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.0 | 7.9 | 8.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 7.9 | 8.2 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.0 | 7.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 6.9 | 7.5 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 9.4 | 9.3 | 9.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 9.5 | 9.3 | 9.5 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,360.9 | 11,349.4 | 11,376.4 | 10.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,403.4 | 11,366.3 | 11,457.0 | 35.5 | 1.004x | 1.004x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,459.6 | 4,448.8 | 4,467.9 | 6.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,476.6 | 4,448.7 | 4,513.5 | 25.8 | 1.004x | 1.004x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5,685.6 | 5,682.6 | 5,687.4 | 1.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5,733.1 | 5,707.5 | 5,747.9 | 15.6 | 1.008x | 1.008x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,379.9 | 11,334.1 | 11,412.5 | 26.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,394.7 | 11,384.4 | 11,425.9 | 15.3 | 1.001x | 1.001x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,251.5 | 2,234.6 | 2,254.6 | 8.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,255.2 | 2,246.1 | 2,264.8 | 6.7 | 1.002x | 1.002x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.5 | 8.3 | 8.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.5 | 8.1 | 8.8 | 0.2 | 1.009x | 1.009x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,876.4 | 2,851.2 | 2,882.5 | 13.9 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,884.8 | 2,880.2 | 2,893.5 | 4.4 | 1.003x | 1.003x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,560.9 | 4,550.8 | 4,602.8 | 19.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,616.0 | 4,581.8 | 4,618.6 | 13.9 | 1.012x | 1.012x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.3 | 4.3 | 4.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.5 | 4.5 | 0.0 | 1.053x | 1.053x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.7 | 11.6 | 12.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.7 | 11.6 | 12.1 | 0.2 | 1.001x | 1.001x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.1 | 18.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.5 | 18.7 | 0.1 | 1.019x | 1.019x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 37.5 | 37.1 | 38.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 37.6 | 37.0 | 37.8 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 17.7 | 18.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.3 | 19.5 | 0.5 | 1.006x | 1.006x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.7 | 35.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 35.2 | 34.6 | 35.5 | 0.3 | 1.011x | 1.011x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.6 | 8.5 | 9.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.8 | 8.6 | 9.0 | 0.1 | 1.018x | 1.018x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.4 | 12.3 | 12.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.5 | 12.3 | 12.6 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 1.007x | 1.007x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.9 | 16.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 16.1 | 15.8 | 16.3 | 0.1 | 1.015x | 1.015x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.9 | 14.8 | 16.2 | 0.6 | 1.018x | 1.018x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.5 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.5 | 33.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.8 | 33.3 | 0.2 | 1.003x | 1.003x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 66.1 | 66.0 | 66.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 66.5 | 66.2 | 67.8 | 0.6 | 1.005x | 1.005x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.9 | 24.5 | 25.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 25.0 | 25.2 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 54.3 | 54.3 | 56.9 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 54.6 | 54.2 | 54.8 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.6 | 6.5 | 6.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.9 | 6.9 | 0.0 | 1.051x | 1.051x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.7 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.8 | 6.6 | 7.6 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.0 | 0.0 | 1.023x | 1.023x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 16.1 | 16.0 | 16.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 16.1 | 16.0 | 16.8 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 17.8 | 18.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.3 | 19.6 | 0.4 | 1.022x | 1.022x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.5 | 35.0 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 17.8 | 19.8 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.3 | 19.5 | 0.5 | 1.005x | 1.005x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.6 | 35.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.6 | 35.5 | 0.3 | 1.001x | 1.001x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.0 | 18.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.3 | 19.6 | 0.5 | 1.006x | 1.006x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 36.3 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.9 | 34.7 | 35.1 | 0.1 | 1.009x | 1.009x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 17.8 | 18.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.3 | 19.6 | 0.5 | 1.008x | 1.008x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.9 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.0 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.0 | 18.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.3 | 19.6 | 0.5 | 1.006x | 1.006x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.9 | 0.5 | 1.001x | 1.001x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.3 | 8.3 | 8.4 | 0.1 | 1.032x | 1.032x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.1 | 15.1 | 15.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.1 | 15.0 | 15.3 | 0.1 | 1.000x | 1.000x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.2 | 4.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.6 | 4.4 | 4.9 | 0.1 | 1.044x | 1.044x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2.3 | 2.3 | 2.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2.3 | 2.3 | 2.5 | 0.1 | 1.009x | 1.009x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.2 | 4.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.6 | 4.4 | 4.7 | 0.1 | 1.047x | 1.047x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.6 | 3.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.7 | 4.0 | 0.1 | 1.014x | 1.014x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.2 | 5.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.2 | 5.8 | 0.2 | 1.104x | 1.104x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.7 | 3.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.8 | 3.8 | 0.0 | 1.005x | 1.005x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.5 | 10.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.1 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.6 | 3.4 | 3.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.6 | 3.3 | 3.6 | 0.1 | 1.001x | 1.001x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2,224,791.6 | 2,222,146.5 | 2,249,144.8 | 10,025.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,232,208.0 | 2,229,398.1 | 2,235,273.3 | 1,963.8 | 1.003x | 1.003x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,458.3 | 7,363.5 | 7,485.3 | 51.6 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,495.7 | 7,448.7 | 7,640.1 | 66.6 | 1.005x | 1.005x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,485.3 | 7,422.0 | 7,566.6 | 53.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,490.0 | 7,486.9 | 7,622.2 | 61.7 | 1.001x | 1.001x |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 1,943,996.8 | 1,942,165.1 | 1,975,463.3 | 12,783.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,950,171.3 | 1,944,890.6 | 1,954,050.0 | 3,206.6 | 1.003x | 1.003x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,475.9 | 7,401.3 | 7,613.6 | 75.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,562.9 | 7,532.4 | 7,634.9 | 37.1 | 1.012x | 1.012x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.4 | 4.5 | 0.0 | 1.008x | 1.008x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.008x | 1.008x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.4 | 4.5 | 0.0 | 1.012x | 1.012x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.8 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.009x | 1.009x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 16.6 | 3.9 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.008x | 1.008x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.7 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 5.0 | 0.3 | 1.006x | 1.006x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.8 | 0.2 | 1.004x | 1.004x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.004x | 1.004x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.006x | 1.006x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.009x | 1.009x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.005x | 1.005x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.005x | 1.005x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.006x | 1.006x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.8 | 4.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4.1 | 3.9 | 4.2 | 0.1 | 1.071x | 1.071x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.6 | 4.6 | 4.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.6 | 4.6 | 4.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.5 | 6.5 | 6.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.6 | 6.5 | 6.6 | 0.0 | 1.006x | 1.006x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.006x | 1.006x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.6 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.6 | 6.6 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 7.0 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.7 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2.9 | 2.7 | 3.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.0 | 3.0 | 3.1 | 0.0 | 1.040x | 1.040x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.4 | 6.3 | 6.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.4 | 6.4 | 6.5 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.5 | 6.5 | 6.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.5 | 6.5 | 6.6 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.5 | 4.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.8 | 4.4 | 4.8 | 0.2 | 1.061x | 1.061x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4.3 | 4.2 | 4.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 4.3 | 4.2 | 4.3 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.8 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.8 | 3.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.8 | 4.0 | 0.1 | 1.002x | 1.002x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 307,194.2 | 306,929.5 | 307,743.0 | 277.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 307,498.0 | 307,194.7 | 310,204.9 | 1,255.5 | 1.001x | 1.001x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,509.9 | 7,460.2 | 7,560.9 | 33.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,566.0 | 7,534.4 | 7,657.8 | 43.2 | 1.007x | 1.007x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,546.3 | 7,512.6 | 7,576.0 | 26.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,599.4 | 7,557.0 | 7,687.1 | 43.8 | 1.007x | 1.007x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11,969.9 | 11,874.5 | 12,036.8 | 62.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12,144.5 | 12,135.7 | 12,347.2 | 80.8 | 1.015x | 1.015x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,437.6 | 7,399.3 | 7,520.4 | 39.8 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,564.5 | 7,486.6 | 7,592.9 | 36.1 | 1.017x | 1.017x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.2 | 17.1 | 17.6 | 0.2 | 1.010x | 1.010x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 35.0 | 34.6 | 35.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.4 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.6 | 22.3 | 23.9 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.8 | 22.3 | 23.5 | 0.5 | 1.009x | 1.009x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.4 | 46.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.5 | 46.3 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.4 | 9.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.4 | 8.7 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.1 | 14.1 | 14.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.3 | 14.0 | 14.4 | 0.2 | 1.013x | 1.013x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.4 | 24.1 | 25.5 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.6 | 24.1 | 25.4 | 0.5 | 1.009x | 1.009x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 50.2 | 50.1 | 51.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 50.3 | 50.1 | 51.0 | 0.4 | 1.001x | 1.001x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.4 | 37.3 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 36.8 | 0.3 | 1.005x | 1.005x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.1 | 73.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.1 | 73.4 | 0.5 | 1.001x | 1.001x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 11.5 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.5 | 8.4 | 8.8 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.1 | 14.1 | 14.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.2 | 14.0 | 14.3 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15.9 | 15.7 | 16.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 15.8 | 18.2 | 0.9 | 1.010x | 1.010x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 32.3 | 32.2 | 32.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 32.7 | 32.1 | 32.9 | 0.3 | 1.014x | 1.014x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.5 | 28.4 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.7 | 27.2 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 54.5 | 54.4 | 55.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 54.8 | 54.6 | 55.5 | 0.3 | 1.004x | 1.004x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 19.9 | 21.5 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.0 | 20.5 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 40.8 | 40.8 | 41.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 41.1 | 40.8 | 41.5 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 15.9 | 0.5 | 1.001x | 1.001x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 30.2 | 30.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 30.6 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.5 | 16.0 | 0.5 | 1.004x | 1.004x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 30.1 | 30.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.7 | 30.2 | 30.7 | 0.3 | 1.017x | 1.017x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.5 | 6.0 | 6.6 | 0.2 | 1.062x | 1.062x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 21.7 | 21.7 | 22.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 21.6 | 23.8 | 0.7 | 1.017x | 1.017x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.0 | 21.5 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.1 | 20.4 | 0.5 | 1.000x | 1.000x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 38.8 | 38.7 | 39.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.3 | 38.8 | 39.5 | 0.3 | 1.014x | 1.014x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.0 | 21.4 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.0 | 20.2 | 0.4 | 1.005x | 1.005x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 38.7 | 38.7 | 39.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.1 | 38.7 | 39.3 | 0.3 | 1.009x | 1.009x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15.0 | 14.7 | 15.9 | 0.4 | 1.020x | 1.020x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 30.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.5 | 30.1 | 30.7 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.1 | 18.0 | 19.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 17.9 | 20.5 | 1.1 | 1.004x | 1.004x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 36.5 | 36.4 | 37.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.9 | 36.3 | 37.3 | 0.4 | 1.012x | 1.012x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 4.8 | 5.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.1 | 4.9 | 5.2 | 0.1 | 1.028x | 1.028x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 16.0 | 16.0 | 16.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 15.9 | 16.4 | 0.2 | 1.017x | 1.017x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 21.5 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.2 | 20.4 | 0.5 | 1.012x | 1.012x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 38.8 | 38.7 | 39.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 38.8 | 39.8 | 0.4 | 1.009x | 1.009x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.8 | 20.4 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 17.9 | 19.1 | 0.4 | 1.013x | 1.013x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.6 | 36.3 | 37.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 36.7 | 36.3 | 36.9 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.2 | 5.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.3 | 5.3 | 5.6 | 0.1 | 1.030x | 1.030x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 17.4 | 17.3 | 17.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.4 | 17.6 | 0.1 | 1.010x | 1.010x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.4 | 21.2 | 21.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.4 | 22.7 | 0.5 | 1.006x | 1.006x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 43.0 | 42.9 | 43.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 43.3 | 42.9 | 43.6 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.6 | 15.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.5 | 15.9 | 0.5 | 1.001x | 1.001x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 30.1 | 30.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.6 | 30.2 | 30.8 | 0.2 | 1.013x | 1.013x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.3 | 24.9 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.8 | 23.4 | 24.9 | 0.6 | 1.004x | 1.004x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 47.5 | 47.4 | 48.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 47.5 | 47.4 | 48.5 | 0.5 | 1.000x | 1.000x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 18.9 | 19.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 18.9 | 20.4 | 0.6 | 1.002x | 1.002x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.0 | 38.5 | 39.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.5 | 38.7 | 39.7 | 0.4 | 1.013x | 1.013x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.5 | 15.8 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.9 | 14.6 | 15.2 | 0.2 | 1.009x | 1.009x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 30.1 | 30.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 31.1 | 0.4 | 1.006x | 1.006x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.0 | 20.5 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.1 | 20.2 | 0.4 | 1.001x | 1.001x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 39.1 | 38.8 | 39.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 38.8 | 39.6 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.3 | 24.8 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.4 | 25.0 | 0.6 | 1.003x | 1.003x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.5 | 48.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 48.3 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.2 | 25.5 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.8 | 23.4 | 24.5 | 0.4 | 1.007x | 1.007x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 48.3 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.6 | 48.2 | 0.3 | 1.000x | 1.000x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.2 | 0.1 | 1.011x | 1.011x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.3 | 12.2 | 12.4 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.5 | 0.2 | 1.000x | 1.000x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 29.2 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 6.9 | 7.7 | 0.3 | 1.012x | 1.012x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.5 | 12.3 | 12.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.6 | 12.3 | 12.6 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.0 | 7.5 | 0.2 | 1.054x | 1.054x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 18.9 | 0.2 | 1.020x | 1.020x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.6 | 8.6 | 8.7 | 0.0 | 1.027x | 1.027x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.3 | 15.1 | 15.4 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.5 | 8.3 | 8.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.6 | 8.3 | 8.6 | 0.1 | 1.011x | 1.011x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.3 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 10.8 | 0.1 | 1.011x | 1.011x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.4 | 11.3 | 11.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.5 | 12.6 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.7 | 14.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.6 | 14.9 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 7.0 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.6 | 6.0 | 6.8 | 0.3 | 1.075x | 1.075x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.6 | 15.4 | 15.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.7 | 15.7 | 15.9 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.9 | 7.8 | 8.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 7.7 | 8.0 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.6 | 11.6 | 11.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.8 | 11.6 | 11.8 | 0.1 | 1.013x | 1.013x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.7 | 16.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.6 | 16.1 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.2 | 5.1 | 5.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.5 | 5.1 | 5.7 | 0.2 | 1.058x | 1.058x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 35.7 | 35.5 | 40.5 | 2.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 36.1 | 35.6 | 36.2 | 0.2 | 1.011x | 1.011x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 15.2 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.5 | 4.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.9 | 4.0 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.2 | 4.2 | 4.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.3 | 4.4 | 0.0 | 1.039x | 1.039x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 10.4 | 10.1 | 10.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 10.6 | 10.2 | 10.8 | 0.2 | 1.017x | 1.017x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.1 | 6.8 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.9 | 6.7 | 7.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.9 | 6.4 | 7.0 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.9 | 0.3 | 1.000x | 1.000x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 41.7 | 41.5 | 42.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 41.8 | 41.6 | 42.2 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.2 | 4.2 | 4.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.4 | 4.4 | 4.5 | 0.0 | 1.043x | 1.043x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 35.8 | 35.6 | 36.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.1 | 35.7 | 36.4 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.1 | 6.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.1 | 7.0 | 0.3 | 1.112x | 1.112x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 14.9 | 14.8 | 15.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 14.9 | 14.8 | 15.1 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 11.3 | 11.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.3 | 11.5 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 1.013x | 1.013x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.2 | 12.5 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 11.9 | 12.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.4 | 12.2 | 12.4 | 0.1 | 1.015x | 1.015x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.9 | 7.4 | 0.2 | 1.037x | 1.037x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.7 | 6.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 6.9 | 6.7 | 7.6 | 0.3 | 1.026x | 1.026x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.5 | 6.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.0 | 5.5 | 6.4 | 0.3 | 1.053x | 1.053x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 40.6 | 40.5 | 41.3 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 40.8 | 40.6 | 41.1 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.8 | 7.8 | 8.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 7.7 | 8.1 | 0.2 | 1.026x | 1.026x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 33.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 32.9 | 32.5 | 33.6 | 0.4 | 1.011x | 1.011x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.5 | 6.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.3 | 5.5 | 6.4 | 0.4 | 1.123x | 1.123x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 40.6 | 40.5 | 41.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 40.8 | 40.6 | 41.1 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 7.0 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 7.0 | 7.5 | 0.2 | 1.044x | 1.044x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 10.8 | 10.7 | 11.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 10.8 | 10.7 | 10.9 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.9 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 7.0 | 7.5 | 0.3 | 1.038x | 1.038x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 8.0 | 8.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.3 | 7.9 | 8.3 | 0.1 | 1.026x | 1.026x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.9 | 7.6 | 0.3 | 1.017x | 1.017x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.0 | 7.9 | 15.2 | 2.9 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 7.0 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.2 | 6.9 | 7.6 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 8.0 | 9.6 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 8.1 | 7.9 | 8.2 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 7.0 | 7.5 | 0.2 | 1.067x | 1.067x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 9.3 | 9.3 | 9.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 9.4 | 9.3 | 9.5 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,363.3 | 11,355.5 | 11,389.5 | 12.7 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,412.4 | 11,375.1 | 11,421.9 | 17.6 | 1.004x | 1.004x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,448.0 | 4,444.9 | 4,451.0 | 2.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,480.4 | 4,452.8 | 4,507.8 | 22.2 | 1.007x | 1.007x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5,681.8 | 5,681.1 | 5,841.0 | 63.8 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5,705.3 | 5,687.4 | 5,742.9 | 21.4 | 1.004x | 1.004x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,360.0 | 11,327.0 | 11,411.2 | 28.9 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11,360.1 | 11,336.1 | 11,393.7 | 21.7 | 1.000x | 1.000x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,223.2 | 2,222.6 | 2,251.7 | 13.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,252.1 | 2,244.2 | 2,273.2 | 13.0 | 1.013x | 1.013x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.2 | 8.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.8 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,867.6 | 2,846.0 | 2,878.6 | 13.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,889.8 | 2,874.2 | 2,901.7 | 8.8 | 1.008x | 1.008x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,579.0 | 4,549.2 | 4,602.6 | 19.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,609.2 | 4,578.5 | 4,623.2 | 16.3 | 1.007x | 1.007x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.5 | 4.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.7 | 4.6 | 4.7 | 0.0 | 1.040x | 1.040x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 11.8 | 11.7 | 11.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.9 | 11.7 | 12.3 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.9 | 18.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.1 | 19.2 | 0.4 | 1.013x | 1.013x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36.8 | 36.5 | 38.1 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 37.0 | 36.6 | 37.4 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.3 | 17.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.7 | 17.6 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 35.1 | 34.6 | 35.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 35.1 | 34.8 | 35.3 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 7.4 | 8.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.5 | 7.4 | 7.7 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 11.9 | 11.8 | 12.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.0 | 11.8 | 20.5 | 3.4 | 1.016x | 1.016x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.1 | 6.6 | 0.2 | 1.010x | 1.010x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.9 | 15.9 | 16.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 16.1 | 15.8 | 16.2 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.0 | 13.8 | 16.2 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.1 | 13.8 | 15.0 | 0.4 | 1.010x | 1.010x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.3 | 28.8 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.3 | 33.9 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 32.3 | 34.4 | 0.8 | 1.022x | 1.022x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.7 | 66.7 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.7 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.4 | 25.0 | 26.5 | 0.5 | 1.003x | 1.003x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 54.1 | 54.0 | 54.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 54.1 | 54.0 | 54.8 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 6.9 | 6.9 | 7.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.0 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 12.3 | 12.1 | 12.5 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 6.9 | 7.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7.0 | 7.0 | 7.7 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 16.2 | 16.0 | 16.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 16.2 | 16.1 | 16.4 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.5 | 18.0 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.9 | 17.5 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.9 | 34.6 | 35.2 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.1 | 17.8 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 16.8 | 17.5 | 0.3 | 1.032x | 1.032x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.6 | 35.1 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.8 | 17.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.1 | 16.8 | 17.3 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.5 | 35.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.9 | 34.7 | 35.2 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.8 | 17.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.1 | 16.9 | 20.2 | 1.3 | 1.011x | 1.011x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.5 | 35.1 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.4 | 17.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.8 | 17.3 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 39.6 | 1.9 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.7 | 35.2 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8.4 | 8.3 | 8.6 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.0 | 15.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.3 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.5 | 4.2 | 4.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.8 | 4.4 | 4.8 | 0.1 | 1.047x | 1.047x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2.5 | 2.4 | 2.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2.7 | 2.6 | 2.7 | 0.0 | 1.077x | 1.077x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.6 | 4.2 | 4.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4.8 | 4.4 | 4.8 | 0.2 | 1.042x | 1.042x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.9 | 3.8 | 4.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 4.0 | 4.0 | 4.1 | 0.1 | 1.027x | 1.027x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.4 | 5.2 | 5.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.3 | 5.8 | 0.2 | 1.070x | 1.070x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.7 | 3.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 4.0 | 3.8 | 4.0 | 0.1 | 1.047x | 1.047x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.8 | 10.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.8 | 10.4 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 3.7 | 3.5 | 4.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 3.8 | 3.5 | 3.8 | 0.1 | 1.037x | 1.037x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2,210,364.7 | 2,207,872.8 | 2,240,532.1 | 13,993.9 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,211,338.7 | 2,208,402.4 | 2,221,275.0 | 5,173.8 | 1.000x | 1.000x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,415.0 | 7,260.8 | 7,599.6 | 125.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,473.8 | 7,352.5 | 7,639.9 | 102.7 | 1.008x | 1.008x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,545.0 | 7,514.8 | 7,700.8 | 71.8 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,587.7 | 7,424.9 | 7,606.5 | 77.2 | 1.006x | 1.006x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 1,944,686.2 | 1,939,366.0 | 1,956,888.9 | 6,754.2 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,957,341.7 | 1,945,047.3 | 1,959,886.7 | 6,013.1 | 1.007x | 1.007x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,535.5 | 7,385.8 | 7,625.8 | 79.6 | 1.000x | 1.000x |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 7,540.1 | 7,440.3 | 7,619.2 | 56.8 | 1.001x | 1.001x |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 78,962,809.0 | 78,096,939.0 | 79,347,985.0 | 440,446.0 | 5 | 49,472 | 85,071 | 16,377 | 0.006 | compiled=5 | 4,396,386.0 | 74,349,905.0 | 53,641.0 |
| `factored` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 73,857,769.0 | 73,315,796.0 | 75,048,904.0 | 611,448.3 | 5 | 37,040 | 42,326 | 16,649 | 0.008 | compiled=5 | 3,908,857.0 | 69,891,393.0 | 46,768.0 |
| `factored` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 93,815,091.0 | 92,591,955.0 | 95,061,610.0 | 970,400.1 | 5 | 53,680 | 85,177 | 16,483 | 0.010 | compiled=5 | 6,641,016.0 | 86,831,970.0 | 46,618.0 |
| `factored` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 88,918,513.0 | 88,366,924.0 | 89,940,850.0 | 554,329.1 | 5 | 41,248 | 42,432 | 16,755 | 0.006 | compiled=5 | 4,685,431.0 | 84,165,996.0 | 42,731.0 |
| `floor` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 66,046,005.0 | 64,789,087.0 | 67,090,202.0 | 783,546.0 | 5 | 28,768 | 17,888 | 14,557 | 0.012 (max is trial 1) | compiled=5 | 1,035,782.0 | 64,887,702.0 | 49,142.0 |
| `floor` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 66,803,783.0 | 66,567,579.0 | 67,731,924.0 | 415,028.2 | 5 | 28,808 | 19,474 | 15,916 | 0.006 (max is trial 1) | compiled=5 | 1,002,380.0 | 65,715,622.0 | 51,788.0 |
| `floor` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 81,178,315.0 | 80,240,948.0 | 81,443,154.0 | 485,707.4 | 5 | 28,880 | 17,994 | 14,663 | 0.006 (max is trial 1) | compiled=5 | 2,050,505.0 | 79,097,313.0 | 45,325.0 |
| `floor` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 80,724,359.0 | 79,947,625.0 | 82,080,927.0 | 776,525.0 | 5 | 28,920 | 19,580 | 16,022 | 0.010 (max is trial 1) | compiled=5 | 1,641,875.0 | 78,986,374.0 | 54,072.0 |
| `orig` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 76,225,301.0 | 75,842,499.0 | 77,158,690.0 | 582,513.7 | 5 | 49,440 | 84,644 | 16,117 | 0.008 | compiled=5 | 4,140,684.0 | 72,035,915.0 | 49,113.0 |
| `orig` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 72,180,306.0 | 71,225,448.0 | 72,977,800.0 | 561,080.9 | 5 | 32,904 | 41,919 | 16,409 | 0.008 | compiled=5 | 3,728,346.0 | 68,022,100.0 | 52,339.0 |
| `orig` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 91,152,163.0 | 90,111,772.0 | 92,658,973.0 | 1,015,432.5 | 5 | 53,648 | 84,750 | 16,223 | 0.011 (max is trial 1) | compiled=5 | 6,377,941.0 | 84,746,129.0 | 49,894.0 |
| `orig` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 84,887,134.0 | 84,485,639.0 | 86,586,258.0 | 764,067.0 | 5 | 37,112 | 42,025 | 16,515 | 0.009 | compiled=5 | 4,911,166.0 | 79,897,301.0 | 55,995.0 |
    - emit/code bytes across abi 77: pcrec's size definition moves at the boundary -- a flat ~+106 B of counted stamp and initializer lines on a typical artifact (`RX_COMPOUND`, `RX_MEASURES`, `.measures`/`.next`/`.next_n`), and from abi 83 the find-all iterator scaffold (`_next`, the forwarder twins) is EXCLUDED from both counts with no marker in the emitted text. Read a Delta that spans the boundary against that, not as a program change; the DFA retry machine (`RX_ITER_RETRY=retry`) is NOT scaffold and counts (b142prep: +3-4 KB on narrow DFAs).

