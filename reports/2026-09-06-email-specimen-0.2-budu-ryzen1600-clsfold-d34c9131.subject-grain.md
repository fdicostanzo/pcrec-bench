# pcrec-bench report

reporter: v15 (2026-09-05)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-09-06T19:00:00Z, until=2026-09-06T19:15:00Z, testee=pcrec_d34c9131_auto-caps-simdna, testee=pcrec_d34c9131_auto-caps-simdna_noclsfold
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 2.0% (`pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `match-compliance`)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna_noclsfold__budu-ryzen1600__20260906T190801Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna_noclsfold/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna_noclsfold__budu-ryzen1600__20260906T190801Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.5
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.6 | 62.3 | 62.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.9 | 62.4 | 63.4 | 0.3 | 1.005x | 1.005x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.0 | 44.4 | 0.5 | 1.017x | 1.017x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 80.1 | 79.9 | 80.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 79.9 | 80.5 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.3 | 20.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 20.7 | 20.5 | 20.7 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 28.3 | 28.1 | 31.9 | 1.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.9 | 0.6 | 1.011x | 1.011x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.2 | 46.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 46.5 | 46.2 | 47.1 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 87.7 | 87.2 | 102.3 | 5.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 87.7 | 87.5 | 89.5 | 0.7 | 1.001x | 1.001x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 64.9 | 64.8 | 67.2 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 65.6 | 65.3 | 65.9 | 0.2 | 1.011x | 1.011x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 123.5 | 123.3 | 123.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 123.8 | 123.4 | 128.6 | 2.0 | 1.002x | 1.002x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.5 | 20.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 20.8 | 20.4 | 21.4 | 0.3 | 1.010x | 1.010x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.2 | 28.2 | 28.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 28.3 | 28.1 | 28.6 | 0.2 | 1.003x | 1.003x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.8 | 33.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 33.2 | 32.8 | 34.3 | 0.5 | 1.007x | 1.007x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.9 | 58.8 | 59.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 59.1 | 59.0 | 59.5 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 50.3 | 50.1 | 51.3 | 0.4 | 1.002x | 1.002x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 94.4 | 94.3 | 95.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 94.5 | 94.2 | 95.8 | 0.6 | 1.001x | 1.001x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.2 | 39.2 | 40.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.7 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.5 | 73.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 73.8 | 73.6 | 74.0 | 0.1 | 1.000x | 1.000x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.8 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 56.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.7 | 55.5 | 55.8 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 54.9 | 56.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.8 | 55.4 | 55.9 | 0.2 | 1.003x | 1.003x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 13.4 | 0.6 | 1.005x | 1.005x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 35.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 34.8 | 34.7 | 35.3 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 37.6 | 37.2 | 37.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.5 | 37.8 | 0.1 | 1.000x | 1.000x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.2 | 68.9 | 69.4 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.8 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 37.5 | 37.2 | 37.9 | 0.3 | 1.002x | 1.002x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.9 | 69.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.3 | 68.9 | 70.0 | 0.4 | 1.005x | 1.005x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.5 | 31.8 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.3 | 55.2 | 55.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.6 | 55.4 | 55.8 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.8 | 35.8 | 36.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 36.0 | 35.9 | 36.0 | 0.0 | 1.004x | 1.004x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 66.1 | 66.0 | 66.3 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 10.9 | 13.1 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.3 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.2 | 26.1 | 26.4 | 0.1 | 1.000x | 1.000x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 37.3 | 37.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 37.7 | 37.4 | 37.9 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.8 | 69.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.4 | 69.3 | 69.7 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.7 | 36.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.9 | 35.8 | 37.2 | 0.5 | 1.001x | 1.001x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.9 | 66.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 66.0 | 65.1 | 66.3 | 0.4 | 1.002x | 1.002x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.4 | 11.2 | 12.6 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.4 | 12.8 | 0.5 | 1.016x | 1.016x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.9 | 27.8 | 28.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.8 | 28.1 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.1 | 41.0 | 41.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 41.2 | 41.0 | 41.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 76.8 | 76.7 | 77.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 76.9 | 76.8 | 77.2 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.3 | 56.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.7 | 55.6 | 58.2 | 1.0 | 1.005x | 1.005x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.9 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.2 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.6 | 83.2 | 84.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 83.8 | 83.3 | 90.7 | 2.8 | 1.003x | 1.003x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.3 | 37.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 37.6 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.8 | 69.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.3 | 68.8 | 80.3 | 4.4 | 1.004x | 1.004x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.5 | 31.8 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.2 | 55.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.5 | 55.4 | 70.4 | 6.0 | 1.001x | 1.001x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 37.3 | 37.1 | 37.7 | 0.2 | 1.001x | 1.001x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.8 | 69.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.1 | 68.8 | 69.5 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 44.8 | 44.7 | 44.8 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.4 | 83.3 | 84.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 83.8 | 83.5 | 84.0 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.5 | 44.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 44.6 | 44.6 | 44.8 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.5 | 83.3 | 84.8 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 83.7 | 83.4 | 84.1 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.0 | 22.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 22.6 | 22.1 | 22.6 | 0.2 | 1.010x | 1.010x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 45.6 | 45.5 | 45.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 45.7 | 45.6 | 45.8 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.7 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 22.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 22.5 | 22.2 | 22.8 | 0.2 | 1.006x | 1.006x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.7 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 30.0 | 29.6 | 30.2 | 0.2 | 1.013x | 1.013x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.3 | 26.1 | 26.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.7 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.1 | 25.9 | 26.6 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 1.001x | 1.001x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 19.2 | 19.1 | 19.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.3 | 19.1 | 19.5 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 25.5 | 25.2 | 27.2 | 0.7 | 1.008x | 1.008x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 13.0 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 12.5 | 0.2 | 1.001x | 1.001x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.0 | 27.0 | 27.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.2 | 0.1 | 1.000x | 1.000x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.7 | 20.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.9 | 20.8 | 21.2 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.0 | 27.0 | 27.1 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.4 | 11.2 | 11.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.6 | 0.0 | 1.005x | 1.005x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.4 | 62.3 | 62.7 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 1.002x | 1.002x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.7 | 23.7 | 23.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 23.8 | 23.7 | 23.9 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.1 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.6 | 19.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.7 | 18.6 | 18.9 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.0 | 13.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.0 | 13.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 11.5 | 11.5 | 12.4 | 0.3 | 1.001x | 1.001x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.7 | 0.2 | 1.010x | 1.010x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.3 | 73.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 73.9 | 73.8 | 74.0 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.7 | 10.3 | 0.2 | 1.015x | 1.015x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 64.1 | 64.1 | 64.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 64.4 | 64.2 | 64.6 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.2 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 25.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 25.7 | 25.2 | 25.8 | 0.2 | 1.007x | 1.007x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 22.0 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.0 | 19.9 | 20.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.0 | 19.9 | 20.1 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.5 | 20.5 | 20.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 20.8 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 12.1 | 12.1 | 12.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 12.5 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.6 | 11.5 | 11.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 11.9 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.8 | 72.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 72.1 | 71.7 | 72.4 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 56.8 | 56.7 | 57.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 56.9 | 56.7 | 57.1 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.7 | 11.5 | 11.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.5 | 12.0 | 0.2 | 1.008x | 1.008x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.9 | 72.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 72.2 | 72.0 | 72.3 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.2 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.9 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.8 | 20.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 19.9 | 19.8 | 20.0 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.4 | 14.3 | 14.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.9 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.4 | 14.3 | 14.8 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.5 | 14.3 | 14.7 | 0.2 | 1.011x | 1.011x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 16.5 | 16.4 | 16.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.6 | 16.4 | 17.1 | 0.3 | 1.007x | 1.007x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,081.1 | 19,078.9 | 19,086.9 | 2.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19,085.6 | 19,080.5 | 19,098.8 | 6.5 | 1.000x | 1.000x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,466.4 | 7,465.9 | 7,468.5 | 1.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 7,467.8 | 7,467.0 | 7,487.7 | 7.9 | 1.000x | 1.000x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,556.6 | 9,555.2 | 9,578.7 | 8.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 9,557.2 | 9,554.4 | 9,560.7 | 2.1 | 1.000x | 1.000x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,058.2 | 19,052.9 | 19,058.7 | 2.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19,067.1 | 19,050.1 | 19,151.1 | 38.4 | 1.000x | 1.000x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 3,741.6 | 3,739.5 | 3,751.7 | 4.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,741.8 | 3,739.7 | 3,742.8 | 1.1 | 1.000x | 1.000x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 17.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.8 | 0.2 | 1.003x | 1.003x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 4,789.6 | 4,788.2 | 4,791.2 | 1.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,791.6 | 4,788.6 | 4,807.4 | 6.8 | 1.000x | 1.000x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,651.0 | 7,649.2 | 7,651.8 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 7,653.8 | 7,651.7 | 7,664.5 | 4.7 | 1.000x | 1.000x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.2 | 0.2 | 1.012x | 1.012x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 21.4 | 21.1 | 21.7 | 0.2 | 1.007x | 1.007x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.3 | 36.0 | 36.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 36.3 | 36.3 | 36.7 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.1 | 66.2 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 66.1 | 65.9 | 66.3 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.3 | 34.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.6 | 34.6 | 35.0 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 63.0 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.7 | 62.1 | 63.0 | 0.3 | 1.000x | 1.000x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.2 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.4 | 26.6 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 25.5 | 25.4 | 26.4 | 0.4 | 1.003x | 1.003x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 12.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.4 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.1 | 27.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.4 | 27.2 | 27.5 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 30.3 | 30.1 | 30.5 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.9 | 51.8 | 52.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 52.3 | 52.0 | 52.3 | 0.2 | 1.007x | 1.007x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.7 | 61.3 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 60.0 | 59.8 | 60.2 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 112.9 | 112.8 | 113.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 113.4 | 113.3 | 113.6 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.5 | 43.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 43.9 | 0.4 | 1.002x | 1.002x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 93.0 | 92.9 | 93.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 93.5 | 93.0 | 97.7 | 1.8 | 1.005x | 1.005x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.6 | 20.5 | 20.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.1 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.1 | 27.0 | 27.4 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.1 | 35.8 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 36.0 | 0.5 | 1.003x | 1.003x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.7 | 62.5 | 62.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 62.9 | 0.4 | 1.000x | 1.000x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 34.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.4 | 0.4 | 1.004x | 1.004x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 63.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.4 | 62.2 | 69.0 | 2.7 | 1.001x | 1.001x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.6 | 34.4 | 34.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 34.4 | 36.3 | 0.8 | 1.042x | 1.042x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 63.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.6 | 62.3 | 63.1 | 0.3 | 1.005x | 1.005x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 35.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.5 | 0.4 | 1.007x | 1.007x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.1 | 62.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.7 | 62.3 | 66.4 | 1.6 | 1.008x | 1.008x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.2 | 35.3 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 34.6 | 34.3 | 35.5 | 0.4 | 1.001x | 1.001x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.0 | 62.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.6 | 62.2 | 66.1 | 1.5 | 1.002x | 1.002x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.002x | 1.002x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.3 | 26.1 | 26.8 | 0.2 | 1.001x | 1.001x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 10.6 | 12.2 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.8 | 10.7 | 12.7 | 0.7 | 1.026x | 1.026x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 5.5 | 5.3 | 5.5 | 0.1 | 1.025x | 1.025x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.2 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 6.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 6.0 | 5.9 | 6.1 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.4 | 11.2 | 11.6 | 0.1 | 1.012x | 1.012x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 72.7 | 72.5 | 73.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.2 | 72.6 | 73.2 | 0.2 | 1.006x | 1.006x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.2 | 0.0 | 1.000x | 1.000x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 16.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 16.4 | 16.4 | 16.7 | 0.1 | 1.003x | 1.003x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,586,692.1 | 3,581,227.7 | 3,590,651.5 | 3,558.7 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,588,392.8 | 3,584,447.7 | 3,596,392.1 | 4,187.6 | 1.000x | 1.000x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 1,875,111.5 | 1,874,451.5 | 1,896,341.1 | 8,570.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,875,347.2 | 1,874,675.9 | 1,878,002.9 | 1,336.5 | 1.000x | 1.000x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,875,174.1 | 1,874,561.6 | 1,889,879.8 | 5,897.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 1,875,762.8 | 1,873,659.1 | 1,894,626.6 | 7,904.3 | 1.000x | 1.000x |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,192,965.9 | 3,172,183.3 | 3,218,576.7 | 15,379.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,201,787.2 | 3,197,527.9 | 3,222,342.4 | 8,911.6 | 1.003x | 1.003x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,152,957.6 | 3,125,188.6 | 3,209,869.2 | 29,061.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,154,581.3 | 3,146,050.0 | 3,188,941.6 | 15,503.2 | 1.001x | 1.001x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 17.9 | 20.3 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.4 | 18.3 | 18.7 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 1.001x | 1.001x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.3 | 0.2 | 1.000x | 1.000x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.008x | 1.008x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.4 | 0.2 | 1.001x | 1.001x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.0 | 1.012x | 1.012x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.010x | 1.010x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.009x | 1.009x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.3 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.009x | 1.009x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.0 | 1.008x | 1.008x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.009x | 1.009x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.0 | 0.0 | 1.005x | 1.005x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 20.6 | 1.1 | 1.002x | 1.002x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 18.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.1 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.5 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 20.2 | 0.9 | 1.001x | 1.001x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 34.3 | 6.6 | 1.003x | 1.003x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 22.1 | 1.7 | 1.000x | 1.000x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 21.5 | 1.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 19.8 | 0.7 | 1.009x | 1.009x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.012x | 1.012x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.2 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.4 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.8 | 19.6 | 0.7 | 1.007x | 1.007x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.0 | 1.004x | 1.004x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.4 | 0.2 | 1.000x | 1.000x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.011x | 1.011x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.8 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.004x | 1.004x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.012x | 1.012x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 9.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 8.7 | 8.6 | 8.7 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 11.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.8 | 0.1 | 1.013x | 1.013x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.3 | 17.2 | 21.3 | 1.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.3 | 17.3 | 17.3 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.012x | 1.012x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.5 | 17.5 | 17.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.6 | 17.5 | 17.6 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 19.3 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.9 | 18.6 | 0.3 | 1.037x | 1.037x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.011x | 1.011x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.8 | 18.6 | 0.3 | 1.035x | 1.035x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.8 | 18.7 | 0.3 | 1.033x | 1.033x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.8 | 18.8 | 0.4 | 1.035x | 1.035x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.011x | 1.011x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.8 | 18.9 | 0.4 | 1.034x | 1.034x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.013x | 1.013x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.5 | 17.9 | 19.6 | 0.6 | 1.033x | 1.033x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.8 | 18.6 | 0.3 | 1.006x | 1.006x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.003x | 1.003x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 1.007x | 1.007x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.6 | 0.2 | 1.008x | 1.008x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.014x | 1.014x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.7 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.6 | 0.3 | 1.005x | 1.005x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.012x | 1.012x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.8 | 19.1 | 0.5 | 1.006x | 1.006x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.7 | 0.3 | 1.002x | 1.002x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.014x | 1.014x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.002x | 1.002x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.011x | 1.011x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.012x | 1.012x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.002x | 1.002x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.3 | 10.5 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.002x | 1.002x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.006x | 1.006x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.0 | 17.9 | 18.7 | 0.3 | 1.005x | 1.005x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.011x | 1.011x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.013x | 1.013x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.9 | 0.4 | 1.002x | 1.002x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.9 | 0.4 | 1.001x | 1.001x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.9 | 0.4 | 1.002x | 1.002x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.8 | 18.9 | 0.4 | 1.000x | 1.000x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 1.001x | 1.001x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.009x | 1.009x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17.9 | 17.9 | 18.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.4 | 0.2 | 1.005x | 1.005x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.8 | 0.1 | 1.017x | 1.017x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 5.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 6.0 | 5.9 | 6.7 | 0.3 | 1.016x | 1.016x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 16.9 | 16.9 | 17.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.1 | 17.0 | 17.2 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.8 | 0.2 | 1.007x | 1.007x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 9.8 | 9.4 | 9.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 10.4 | 10.3 | 10.5 | 0.1 | 1.064x | 1.064x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 9.2 | 8.6 | 9.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 9.2 | 8.6 | 9.3 | 0.3 | 1.001x | 1.001x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 627,608.5 | 627,494.9 | 628,420.6 | 393.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 628,059.0 | 627,640.4 | 629,819.7 | 964.3 | 1.001x | 1.001x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,667.6 | 17,660.5 | 17,692.6 | 13.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17,712.9 | 17,703.3 | 17,734.8 | 11.3 | 1.003x | 1.003x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,649.3 | 17,628.2 | 17,659.4 | 11.7 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17,699.6 | 17,686.3 | 17,744.9 | 20.0 | 1.003x | 1.003x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 30,716.9 | 30,589.5 | 31,048.0 | 158.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 30,949.2 | 30,783.9 | 32,747.8 | 745.7 | 1.008x | 1.008x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,671.8 | 17,651.3 | 18,368.4 | 281.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 17,703.9 | 17,670.0 | 17,726.7 | 18.6 | 1.002x | 1.002x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.5 | 32.3 | 32.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.6 | 58.4 | 58.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.7 | 58.4 | 59.4 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.8 | 40.1 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 77.7 | 77.6 | 78.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 77.8 | 77.6 | 78.2 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 26.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.2 | 26.1 | 26.4 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 43.2 | 43.6 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 86.3 | 85.9 | 86.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 86.7 | 86.4 | 86.9 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.0 | 60.9 | 61.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 61.0 | 60.8 | 61.2 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 120.1 | 120.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 120.3 | 119.8 | 120.5 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.0 | 26.0 | 26.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.6 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.7 | 55.5 | 56.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 55.8 | 55.7 | 55.9 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 46.7 | 46.6 | 46.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.0 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 91.9 | 91.8 | 92.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 91.8 | 92.6 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 36.7 | 36.6 | 36.8 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 69.6 | 69.5 | 69.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 69.7 | 69.6 | 70.3 | 0.3 | 1.000x | 1.000x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 30.6 | 0.4 | 1.005x | 1.005x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 51.3 | 51.2 | 51.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 52.8 | 0.6 | 1.002x | 1.002x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.6 | 0.0 | 1.000x | 1.000x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 51.8 | 51.4 | 51.9 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.7 | 13.8 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 34.9 | 34.5 | 35.1 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.4 | 35.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 65.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 65.8 | 65.5 | 66.0 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.4 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 65.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 65.7 | 65.4 | 67.1 | 0.7 | 1.001x | 1.001x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.2 | 52.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 51.6 | 51.4 | 52.0 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.7 | 33.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.5 | 62.5 | 62.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.4 | 63.4 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.7 | 12.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.8 | 11.6 | 11.9 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.2 | 26.1 | 26.4 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.4 | 35.1 | 36.2 | 0.4 | 1.003x | 1.003x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 65.8 | 65.5 | 66.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.4 | 66.4 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.7 | 62.4 | 63.0 | 0.2 | 1.000x | 1.000x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.3 | 0.1 | 1.015x | 1.015x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.6 | 27.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.6 | 27.5 | 27.8 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.7 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.7 | 73.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 73.2 | 72.9 | 73.3 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 51.4 | 51.2 | 52.0 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 42.9 | 0.6 | 1.002x | 1.002x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 79.9 | 80.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 80.5 | 80.3 | 81.2 | 0.3 | 1.000x | 1.000x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.4 | 35.4 | 35.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 65.7 | 65.6 | 65.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.3 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 29.8 | 29.5 | 29.8 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 51.4 | 51.2 | 51.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 52.5 | 0.4 | 1.001x | 1.001x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 36.6 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 65.7 | 65.5 | 65.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.5 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 41.8 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 80.6 | 80.2 | 80.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.8 | 80.3 | 81.5 | 0.4 | 1.003x | 1.003x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 41.5 | 41.4 | 41.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 42.2 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 80.6 | 80.3 | 80.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 81.2 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 22.3 | 22.1 | 22.3 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.7 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 45.4 | 45.3 | 45.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.4 | 45.7 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.2 | 0.4 | 1.001x | 1.001x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 22.3 | 22.1 | 22.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.5 | 22.0 | 22.9 | 0.3 | 1.008x | 1.008x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 29.7 | 29.3 | 30.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 29.5 | 30.3 | 0.3 | 1.008x | 1.008x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.3 | 26.0 | 26.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.4 | 26.9 | 0.2 | 1.013x | 1.013x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.4 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.5 | 26.1 | 26.7 | 0.2 | 1.007x | 1.007x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 21.2 | 0.4 | 1.002x | 1.002x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 19.1 | 19.0 | 19.3 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.9 | 0.3 | 1.000x | 1.000x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 25.4 | 25.1 | 25.8 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 13.0 | 0.2 | 1.016x | 1.016x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 27.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.9 | 26.8 | 27.1 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.8 | 20.6 | 21.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 20.7 | 21.5 | 0.3 | 1.018x | 1.018x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.3 | 0.1 | 1.000x | 1.000x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.7 | 27.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.2 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.9 | 58.9 | 59.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.8 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 27.7 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 23.9 | 23.8 | 24.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.9 | 23.7 | 24.0 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 11.3 | 0.3 | 1.017x | 1.017x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.8 | 19.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 18.9 | 18.5 | 19.6 | 0.4 | 1.000x | 1.000x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.9 | 13.6 | 14.7 | 0.4 | 1.014x | 1.014x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 12.0 | 12.0 | 12.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 13.2 | 0.5 | 1.006x | 1.006x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 13.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.0 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 71.1 | 71.0 | 71.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 71.1 | 71.8 | 0.3 | 1.001x | 1.001x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 10.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.6 | 0.1 | 1.000x | 1.000x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 61.9 | 61.6 | 62.0 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.6 | 12.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 25.9 | 25.6 | 26.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 26.2 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.8 | 22.7 | 0.4 | 1.003x | 1.003x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.8 | 19.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 19.0 | 18.9 | 19.5 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.4 | 20.3 | 20.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.6 | 20.4 | 20.8 | 0.2 | 1.012x | 1.012x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 12.6 | 12.6 | 12.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 12.9 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.3 | 12.3 | 12.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.3 | 12.5 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.5 | 68.4 | 68.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 68.7 | 68.4 | 68.9 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 15.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 53.7 | 53.7 | 54.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 53.8 | 53.7 | 53.8 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 68.7 | 68.5 | 69.0 | 0.2 | 1.000x | 1.000x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.5 | 13.3 | 13.9 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 19.9 | 19.7 | 19.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.1 | 19.7 | 20.1 | 0.2 | 1.010x | 1.010x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.7 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.7 | 14.4 | 14.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.4 | 15.4 | 0.4 | 1.010x | 1.010x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.5 | 14.4 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.3 | 15.8 | 0.5 | 1.005x | 1.005x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.8 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 15.5 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 14.6 | 14.5 | 15.1 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 16.4 | 16.3 | 16.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 17.1 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,079.8 | 19,077.0 | 19,143.2 | 25.7 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19,093.8 | 19,077.3 | 19,198.4 | 44.0 | 1.001x | 1.001x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,464.5 | 7,464.1 | 7,483.6 | 7.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 7,466.1 | 7,464.9 | 7,468.2 | 1.1 | 1.000x | 1.000x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 9,553.7 | 9,553.5 | 9,557.7 | 1.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,554.9 | 9,554.3 | 9,574.7 | 7.9 | 1.000x | 1.000x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,055.3 | 19,053.8 | 19,057.1 | 1.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19,056.4 | 19,055.7 | 19,061.4 | 2.3 | 1.000x | 1.000x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,737.9 | 3,737.4 | 3,740.2 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 3,739.8 | 3,739.4 | 3,740.7 | 0.5 | 1.000x | 1.000x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.4 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,788.9 | 4,788.0 | 4,790.6 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 4,790.6 | 4,789.5 | 4,791.6 | 0.7 | 1.000x | 1.000x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,650.2 | 7,648.0 | 7,651.8 | 1.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 7,650.5 | 7,648.2 | 7,655.4 | 2.5 | 1.000x | 1.000x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.7 | 0.1 | 1.009x | 1.009x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 21.3 | 21.2 | 21.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.4 | 21.1 | 22.4 | 0.4 | 1.004x | 1.004x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.0 | 0.1 | 1.000x | 1.000x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.4 | 63.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 62.9 | 62.4 | 63.0 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.7 | 0.5 | 1.001x | 1.001x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.2 | 58.2 | 60.3 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.3 | 58.2 | 58.7 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 17.0 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 23.2 | 23.0 | 23.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 25.6 | 0.9 | 1.003x | 1.003x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.9 | 12.5 | 14.7 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.9 | 12.7 | 14.5 | 0.7 | 1.001x | 1.001x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 28.6 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 27.3 | 26.9 | 27.5 | 0.2 | 1.006x | 1.006x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.2 | 48.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 48.4 | 48.2 | 48.8 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 55.7 | 55.6 | 55.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.8 | 55.4 | 57.3 | 0.7 | 1.002x | 1.002x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.5 | 110.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 109.7 | 109.6 | 109.9 | 0.1 | 1.000x | 1.000x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.7 | 43.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 44.2 | 0.6 | 1.001x | 1.001x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 89.3 | 89.1 | 89.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 88.9 | 90.3 | 0.5 | 1.005x | 1.005x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 14.4 | 0.4 | 1.008x | 1.008x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.4 | 21.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 20.7 | 20.4 | 21.0 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.7 | 26.6 | 27.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.7 | 0.4 | 1.003x | 1.003x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.2 | 33.6 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.3 | 0.4 | 1.001x | 1.001x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.5 | 58.4 | 58.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 59.5 | 58.4 | 59.9 | 0.7 | 1.017x | 1.017x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.1 | 60.4 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.5 | 58.4 | 58.8 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.5 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 60.3 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.4 | 58.3 | 58.8 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.4 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.5 | 58.3 | 58.9 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.0 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 58.5 | 58.3 | 58.9 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 17.3 | 0.5 | 1.004x | 1.004x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 26.3 | 26.2 | 26.5 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.7 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 5.1 | 5.0 | 5.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.7 | 5.2 | 6.2 | 0.3 | 1.112x | 1.112x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.7 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 11.6 | 0.5 | 1.008x | 1.008x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 5.6 | 5.6 | 6.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 7.1 | 0.5 | 1.070x | 1.070x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.9 | 13.2 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.3 | 0.2 | 1.021x | 1.021x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.0 | 73.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 73.8 | 73.6 | 74.1 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.2 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 18.4 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 16.5 | 16.2 | 16.5 | 0.1 | 1.013x | 1.013x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,578,393.8 | 3,576,939.1 | 3,579,998.5 | 1,246.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,584,760.9 | 3,580,701.5 | 3,596,936.9 | 5,833.6 | 1.002x | 1.002x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,885,944.5 | 1,884,012.8 | 1,890,252.9 | 2,131.6 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 1,888,684.0 | 1,887,487.5 | 1,904,417.0 | 6,294.6 | 1.001x | 1.001x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,874,971.6 | 1,874,566.2 | 1,890,593.4 | 6,177.8 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 1,875,623.9 | 1,874,978.6 | 1,879,030.4 | 1,473.4 | 1.000x | 1.000x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,142,869.4 | 3,124,428.1 | 3,160,206.5 | 11,464.4 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,154,491.2 | 3,123,908.6 | 3,189,887.4 | 23,889.3 | 1.004x | 1.004x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,095,320.2 | 3,087,598.5 | 3,100,842.1 | 4,652.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,097,970.9 | 3,075,324.2 | 3,108,149.7 | 11,472.9 | 1.001x | 1.001x |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 164,584,146.0 | 163,200,287.0 | 172,326,812.0 | 3,438,404.2 | 5 | 48,128 | 82,455 | 13,761 | 0.021 | compiled=5 | 9,866,191.0 | 154,496,783.0 | 194,071.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 183,590,851.0 | 175,932,235.0 | 194,146,927.0 | 6,021,076.8 | 5 | 48,264 | 94,666 | 15,677 | 0.033 | compiled=5 | 12,225,066.0 | 171,279,445.0 | 198,781.0 |
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 170,074,877.0 | 165,574,461.0 | 174,532,136.0 | 2,846,142.2 | 5 | 48,128 | 82,455 | 13,761 | 0.017 | compiled=5 | 9,801,310.0 | 160,084,886.0 | 187,742.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 182,524,996.0 | 175,200,711.0 | 198,241,271.0 | 8,554,213.3 | 5 | 48,264 | 94,666 | 15,677 | 0.047 | compiled=5 | 22,588,480.0 | 170,146,669.0 | 206,802.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 146,925,846.0 | 134,069,456.0 | 156,562,775.0 | 7,227,152.4 | 5 | 27,608 | 18,106 | 13,109 | 0.049 | compiled=5 | 1,805,321.0 | 144,978,534.0 | 192,931.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 158,953,769.0 | 153,090,875.0 | 161,812,987.0 | 3,417,763.5 | 5 | 27,752 | 20,449 | 15,126 | 0.022 | compiled=5 | 1,819,561.0 | 155,299,577.0 | 213,442.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 148,633,036.0 | 147,345,037.0 | 151,042,141.0 | 1,583,378.4 | 5 | 27,608 | 18,106 | 13,109 | 0.011 | compiled=5 | 1,795,791.0 | 145,452,277.0 | 114,060.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 161,162,234.0 | 145,941,900.0 | 166,267,634.0 | 8,444,775.9 | 5 | 27,752 | 20,449 | 15,126 | 0.052 | compiled=5 | 1,712,380.0 | 157,287,510.0 | 188,592.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 166,883,659.0 | 162,455,282.0 | 173,020,587.0 | 4,309,592.0 | 5 | 48,088 | 82,048 | 13,521 | 0.026 | compiled=5 | 9,496,359.0 | 154,801,744.0 | 195,231.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 178,790,732.0 | 164,688,805.0 | 180,042,050.0 | 5,996,848.9 | 5 | 48,224 | 94,259 | 15,437 | 0.034 (max is trial 1) | compiled=5 | 11,568,361.0 | 159,379,703.0 | 108,781.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 165,923,203.0 | 156,281,823.0 | 183,938,554.0 | 9,847,499.8 | 5 | 48,088 | 82,048 | 13,521 | 0.059 | compiled=5 | 9,461,649.0 | 156,327,034.0 | 192,201.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 180,745,944.0 | 172,905,155.0 | 187,029,724.0 | 6,048,317.3 | 5 | 48,224 | 94,259 | 15,437 | 0.033 | compiled=5 | 11,567,211.0 | 163,322,697.0 | 108,100.0 |

