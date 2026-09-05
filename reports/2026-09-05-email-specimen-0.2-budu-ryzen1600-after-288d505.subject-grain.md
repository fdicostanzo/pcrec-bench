# pcrec-bench report

reporter: v13 (2026-09-03)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-09-02T02:40:00Z, until=2026-09-05T04:10:00Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_288d505_auto-caps-simdna, testee=pcrec_1989c62_auto-caps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 8.2% (`pcrec_1989c62_auto-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (../../store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (../../store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z` (../../store/records/email-specimen@0.2/pcrec_1989c62_auto-caps-simdna/email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_288d505_auto-caps-simdna__budu-ryzen1600__20260905T040524Z` (../../store/records/email-specimen@0.2/pcrec_288d505_auto-caps-simdna/email-specimen@0.2__pcrec_288d505_auto-caps-simdna__budu-ryzen1600__20260905T040524Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.5
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 4 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.1 | 0.3 | 0.040x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.6 | 35.4 | 0.3 | 0.040x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 863.9 | 857.9 | 884.2 | 9.0 | 0.991x | 24.913x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.6 | 865.8 | 882.8 | 6.0 | 1.000x | 25.136x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 62.6 | 0.1 | 0.072x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.5 | 63.2 | 0.3 | 0.073x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.1 | 153.9 | 154.6 | 0.3 | 0.178x | 2.466x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 863.8 | 854.6 | 872.1 | 6.6 | 1.000x | 13.816x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.0 | 42.9 | 44.3 | 0.5 | 0.035x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 42.9 | 45.5 | 1.1 | 0.036x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,217.2 | 1,214.6 | 1,229.8 | 5.5 | 0.997x | 28.276x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,220.7 | 1,210.7 | 1,258.3 | 17.5 | 1.000x | 28.357x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 80.2 | 80.8 | 0.2 | 0.066x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 79.9 | 80.6 | 0.2 | 0.066x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.4 | 175.0 | 176.0 | 0.3 | 0.144x | 2.182x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,219.9 | 1,219.7 | 1,231.7 | 5.8 | 1.000x | 15.181x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.3 | 20.6 | 0.1 | 0.027x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.4 | 22.1 | 0.6 | 0.028x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 747.6 | 744.6 | 764.3 | 7.0 | 1.000x | 36.374x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 752.1 | 743.8 | 753.1 | 3.9 | 1.006x | 36.592x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 28.3 | 28.2 | 28.9 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.2 | 28.8 | 0.2 | 0.038x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.3 | 121.4 | 124.5 | 1.2 | 0.164x | 4.350x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 752.1 | 747.7 | 765.2 | 5.9 | 1.000x | 26.541x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.2 | 46.5 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.3 | 47.8 | 0.5 | 0.035x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,327.5 | 1,316.0 | 1,336.1 | 6.9 | 1.000x | 28.661x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,335.8 | 1,327.9 | 1,342.2 | 5.0 | 1.006x | 28.840x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 87.5 | 87.5 | 88.1 | 0.3 | 0.066x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 87.6 | 86.9 | 88.3 | 0.5 | 0.066x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 184.4 | 183.4 | 185.1 | 0.6 | 0.140x | 2.107x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,318.5 | 1,309.2 | 1,328.7 | 6.7 | 1.000x | 15.062x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.1 | 64.9 | 66.1 | 0.4 | 0.074x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.4 | 65.1 | 66.9 | 0.7 | 0.074x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.9 | 867.2 | 884.9 | 6.8 | 0.997x | 13.466x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 879.8 | 865.0 | 881.1 | 6.1 | 1.000x | 13.512x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 123.7 | 123.3 | 123.7 | 0.2 | 0.141x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 123.9 | 123.5 | 124.0 | 0.2 | 0.141x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.2 | 166.1 | 169.0 | 1.0 | 0.191x | 1.352x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 877.0 | 872.0 | 886.0 | 5.8 | 1.000x | 7.090x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.5 | 20.7 | 0.1 | 0.027x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.5 | 20.7 | 0.0 | 0.027x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.0 | 731.8 | 758.4 | 8.9 | 1.000x | 36.519x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 750.8 | 741.8 | 754.9 | 4.6 | 1.001x | 36.560x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 28.3 | 28.2 | 29.1 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.2 | 28.7 | 0.2 | 0.038x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.5 | 122.5 | 124.5 | 0.8 | 0.164x | 4.364x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 753.3 | 745.7 | 754.4 | 3.5 | 1.000x | 26.605x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.9 | 33.1 | 0.1 | 0.025x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 32.9 | 33.2 | 0.1 | 0.025x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,342.6 | 1,332.9 | 1,348.7 | 5.3 | 1.000x | 40.665x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,351.8 | 1,348.6 | 1,360.8 | 4.9 | 1.007x | 40.945x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 59.1 | 59.0 | 59.2 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 59.2 | 59.2 | 59.3 | 0.0 | 0.044x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.1 | 163.7 | 171.5 | 2.9 | 0.122x | 2.776x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,341.0 | 1,339.3 | 1,349.0 | 3.4 | 1.000x | 22.683x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.5 | 0.2 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.2 | 50.7 | 0.2 | 0.052x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 970.7 | 964.5 | 972.0 | 2.8 | 0.998x | 19.328x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.6 | 967.5 | 977.1 | 3.3 | 1.000x | 19.367x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 94.2 | 94.0 | 95.0 | 0.4 | 0.097x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 94.4 | 94.1 | 95.1 | 0.3 | 0.097x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.7 | 171.3 | 180.9 | 3.3 | 0.179x | 1.844x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.5 | 959.3 | 979.6 | 6.7 | 1.000x | 10.324x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.3 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.3 | 39.1 | 39.7 | 0.2 | 0.046x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.2 | 854.5 | 872.4 | 6.0 | 0.996x | 21.874x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.5 | 848.8 | 881.0 | 10.3 | 1.000x | 21.960x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.3 | 73.5 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.3 | 73.6 | 0.1 | 0.085x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 157.8 | 157.7 | 158.0 | 0.1 | 0.184x | 2.149x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.4 | 853.9 | 863.0 | 3.3 | 1.000x | 11.705x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.0 | 0.2 | 0.037x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 855.1 | 854.3 | 868.6 | 5.6 | 0.995x | 27.088x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.7 | 847.1 | 873.7 | 9.9 | 1.000x | 27.233x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.7 | 55.6 | 55.8 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 56.0 | 0.1 | 0.065x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.4 | 147.3 | 147.9 | 0.2 | 0.172x | 2.647x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 858.2 | 849.6 | 864.9 | 5.6 | 1.000x | 15.411x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.3 | 32.4 | 0.4 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 31.9 | 0.1 | 0.045x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 710.7 | 703.7 | 715.5 | 4.1 | 0.999x | 22.513x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.7 | 701.7 | 717.9 | 6.0 | 1.000x | 22.546x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.5 | 55.9 | 0.1 | 0.079x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.2 | 56.0 | 0.3 | 0.079x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.3 | 118.4 | 119.7 | 0.5 | 0.168x | 2.139x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 709.6 | 708.2 | 713.2 | 1.7 | 1.000x | 12.723x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.1 | 0.0 | 0.020x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.7 | 0.1 | 0.020x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.6 | 609.0 | 614.2 | 2.0 | 0.988x | 50.585x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.0 | 609.9 | 625.0 | 5.0 | 1.000x | 51.193x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.3 | 34.9 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.4 | 34.8 | 0.1 | 0.007x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.2 | 433.4 | 440.1 | 2.6 | 0.093x | 12.628x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,706.6 | 4,685.1 | 4,746.1 | 22.6 | 1.000x | 135.947x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 37.5 | 38.1 | 0.2 | 0.034x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.0 | 37.4 | 38.2 | 0.3 | 0.035x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,090.9 | 1,084.9 | 1,120.3 | 12.7 | 0.996x | 28.916x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,095.8 | 1,088.7 | 1,099.9 | 4.0 | 1.000x | 29.045x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.1 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.8 | 69.4 | 0.2 | 0.063x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.6 | 170.0 | 174.3 | 1.6 | 0.155x | 2.476x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,100.5 | 1,085.6 | 1,108.0 | 8.6 | 1.000x | 15.974x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.3 | 37.9 | 0.2 | 0.034x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.0 | 0.3 | 0.034x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,087.4 | 1,080.2 | 1,100.2 | 7.0 | 1.000x | 29.103x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,097.3 | 1,084.6 | 1,106.9 | 7.7 | 1.009x | 29.368x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.1 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.2 | 0.1 | 0.063x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.2 | 169.9 | 174.2 | 1.6 | 0.155x | 2.471x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,101.9 | 1,093.7 | 1,110.4 | 5.5 | 1.000x | 15.992x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.8 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.6 | 31.9 | 0.1 | 0.037x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 868.0 | 857.9 | 875.6 | 7.3 | 1.000x | 27.425x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.3 | 853.2 | 881.5 | 10.6 | 1.000x | 27.435x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.3 | 56.0 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.6 | 56.0 | 0.1 | 0.064x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.2 | 154.0 | 156.5 | 0.9 | 0.177x | 2.775x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.3 | 861.9 | 881.8 | 7.5 | 1.000x | 15.682x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.8 | 35.8 | 35.9 | 0.0 | 0.034x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.8 | 35.7 | 36.0 | 0.1 | 0.034x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,050.5 | 1,045.1 | 1,057.8 | 4.3 | 1.000x | 29.361x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,059.9 | 1,047.0 | 1,065.3 | 6.7 | 1.009x | 29.624x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.9 | 66.5 | 0.2 | 0.062x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.2 | 0.2 | 0.063x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.6 | 172.9 | 174.0 | 0.4 | 0.164x | 2.636x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.6 | 1,047.9 | 1,069.8 | 8.8 | 1.000x | 16.026x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.2 | 0.2 | 0.031x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.5 | 12.0 | 0.2 | 0.033x | 1.074x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 358.0 | 354.6 | 363.5 | 3.0 | 1.000x | 32.774x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 362.1 | 357.4 | 363.6 | 2.1 | 1.012x | 33.153x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.6 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.6 | 0.2 | 0.011x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 260.9 | 257.9 | 275.4 | 6.5 | 0.109x | 9.982x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,384.8 | 2,372.2 | 2,393.7 | 7.9 | 1.000x | 91.232x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.1 | 0.3 | 0.034x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 37.2 | 38.2 | 0.4 | 0.034x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.6 | 1,084.3 | 1,097.7 | 5.6 | 1.000x | 29.226x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,104.8 | 1,084.9 | 1,118.4 | 11.0 | 1.010x | 29.525x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.2 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.9 | 69.1 | 0.1 | 0.063x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.4 | 170.3 | 174.3 | 1.6 | 0.156x | 2.474x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.4 | 1,083.1 | 1,119.1 | 12.3 | 1.000x | 15.844x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.8 | 35.7 | 36.2 | 0.2 | 0.034x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 36.4 | 0.2 | 0.034x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.9 | 1,049.8 | 1,059.0 | 3.7 | 1.000x | 29.513x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,065.4 | 1,049.8 | 1,067.3 | 6.5 | 1.007x | 29.720x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.8 | 66.2 | 0.2 | 0.062x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.1 | 0.1 | 0.062x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.1 | 172.4 | 173.9 | 0.5 | 0.163x | 2.630x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,061.8 | 1,054.2 | 1,063.1 | 3.2 | 1.000x | 16.130x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 10.9 | 11.6 | 0.2 | 0.029x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.2 | 0.1 | 0.031x | 1.074x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 386.2 | 381.4 | 392.7 | 4.3 | 1.000x | 34.276x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 388.8 | 386.9 | 390.6 | 1.5 | 1.007x | 34.508x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.9 | 27.8 | 28.3 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.9 | 28.0 | 0.0 | 0.011x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 264.0 | 260.1 | 271.3 | 3.8 | 0.104x | 9.477x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,543.0 | 2,529.9 | 2,546.0 | 6.0 | 1.000x | 91.298x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.1 | 40.9 | 41.2 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.1 | 41.1 | 41.2 | 0.0 | 0.037x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,111.3 | 1,102.1 | 1,116.1 | 5.1 | 1.000x | 27.070x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,114.8 | 1,104.3 | 1,119.3 | 5.9 | 1.003x | 27.156x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 76.8 | 76.7 | 76.9 | 0.1 | 0.069x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 76.8 | 76.7 | 77.0 | 0.1 | 0.069x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.9 | 174.7 | 177.5 | 1.1 | 0.157x | 2.292x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,117.3 | 1,112.7 | 1,128.4 | 6.4 | 1.000x | 14.558x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.7 | 32.0 | 0.1 | 0.028x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,134.5 | 1,163.8 | 9.8 | 1.000x | 36.128x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,138.1 | 1,158.8 | 7.7 | 1.000x | 36.129x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 54.9 | 55.8 | 0.3 | 0.048x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.6 | 55.8 | 0.1 | 0.049x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.6 | 109.4 | 112.5 | 1.3 | 0.095x | 1.975x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,146.2 | 1,159.2 | 4.9 | 1.000x | 20.694x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 44.8 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.7 | 45.3 | 0.2 | 0.065x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.9 | 682.6 | 690.0 | 2.4 | 1.000x | 15.325x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 686.0 | 675.7 | 692.9 | 5.5 | 1.002x | 15.349x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 83.5 | 83.1 | 83.9 | 0.3 | 0.123x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 83.9 | 83.5 | 84.1 | 0.2 | 0.124x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 98.1 | 98.5 | 0.1 | 0.145x | 1.177x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.1 | 674.1 | 687.8 | 5.6 | 1.000x | 8.107x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.9 | 0.2 | 0.033x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.6 | 0.1 | 0.033x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,129.8 | 1,119.5 | 1,131.9 | 4.6 | 1.000x | 30.304x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,130.3 | 1,121.2 | 1,145.5 | 9.8 | 1.000x | 30.317x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.9 | 68.9 | 0.0 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.1 | 0.2 | 0.061x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.2 | 106.5 | 108.1 | 0.6 | 0.095x | 1.555x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.1 | 1,126.6 | 1,134.3 | 2.7 | 1.000x | 16.390x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.7 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.4 | 0.3 | 0.028x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,137.8 | 1,154.1 | 5.3 | 0.999x | 36.266x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,149.7 | 1,143.9 | 1,171.8 | 10.6 | 1.000x | 36.305x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.7 | 55.9 | 0.0 | 0.049x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 55.9 | 0.1 | 0.049x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.8 | 108.4 | 114.2 | 2.2 | 0.095x | 1.951x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.7 | 1,141.7 | 1,157.2 | 5.1 | 1.000x | 20.593x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.2 | 37.2 | 38.7 | 0.6 | 0.033x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.3 | 0.4 | 0.033x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,136.6 | 1,132.6 | 1,146.8 | 5.1 | 1.000x | 30.537x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,136.9 | 1,131.5 | 1,154.4 | 8.2 | 1.000x | 30.547x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.8 | 69.2 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.7 | 0.3 | 0.061x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.6 | 106.4 | 106.9 | 0.2 | 0.094x | 1.549x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.4 | 1,133.5 | 1,147.7 | 5.3 | 1.000x | 16.478x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.6 | 44.7 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.5 | 44.8 | 0.1 | 0.065x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.4 | 675.6 | 684.3 | 3.6 | 0.994x | 15.241x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.8 | 678.3 | 688.0 | 3.3 | 1.000x | 15.339x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 83.8 | 83.4 | 84.2 | 0.2 | 0.123x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 83.8 | 83.6 | 84.1 | 0.2 | 0.123x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.4 | 98.2 | 100.9 | 1.0 | 0.145x | 1.175x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.5 | 678.9 | 684.4 | 2.1 | 1.000x | 8.113x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.4 | 44.9 | 0.2 | 0.041x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 44.7 | 0.0 | 0.041x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.9 | 1,067.5 | 1,083.2 | 5.1 | 0.996x | 24.099x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.9 | 1,060.7 | 1,091.5 | 11.7 | 1.000x | 24.191x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 83.8 | 83.6 | 84.3 | 0.2 | 0.078x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 83.9 | 83.1 | 84.1 | 0.3 | 0.078x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.3 | 104.1 | 104.4 | 0.1 | 0.097x | 1.245x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.2 | 1,072.2 | 1,083.9 | 3.9 | 1.000x | 12.871x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 775.2 | 784.0 | 2.8 | 0.991x | 59.010x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 786.1 | 779.8 | 788.9 | 3.2 | 1.000x | 59.541x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 22.5 | 22.2 | 22.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 22.6 | 22.1 | 23.2 | 0.4 | 0.008x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.1 | 213.5 | 236.8 | 8.2 | 0.082x | 9.740x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.2 | 2,664.8 | 2,724.5 | 21.9 | 1.000x | 118.808x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.5 | 771.4 | 783.5 | 4.1 | 0.987x | 59.078x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.5 | 778.9 | 809.5 | 10.9 | 1.000x | 59.832x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 45.7 | 45.6 | 46.0 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 45.8 | 45.5 | 45.8 | 0.1 | 0.017x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 235.0 | 229.5 | 236.2 | 2.4 | 0.088x | 5.141x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.5 | 2,654.4 | 2,701.7 | 16.5 | 1.000x | 58.261x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.3 | 774.4 | 792.8 | 7.0 | 1.000x | 59.046x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.9 | 773.4 | 781.0 | 2.7 | 1.002x | 59.167x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.3 | 22.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 22.7 | 0.2 | 0.008x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 214.4 | 220.1 | 2.1 | 0.082x | 9.809x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.6 | 2,657.4 | 2,687.5 | 10.9 | 1.000x | 119.562x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.017x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.6 | 771.1 | 782.9 | 4.1 | 0.996x | 59.011x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.7 | 777.5 | 789.0 | 3.8 | 1.000x | 59.251x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.1 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 29.9 | 29.5 | 30.0 | 0.2 | 0.011x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.8 | 229.1 | 235.8 | 2.5 | 0.088x | 7.866x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.5 | 2,648.2 | 2,674.4 | 8.9 | 1.000x | 89.756x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.017x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 921.5 | 918.9 | 931.7 | 5.0 | 0.995x | 57.185x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 925.8 | 919.6 | 931.8 | 4.1 | 1.000x | 57.451x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.2 | 26.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 26.5 | 0.2 | 0.008x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.9 | 316.3 | 324.4 | 3.0 | 0.098x | 12.302x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,270.2 | 3,237.5 | 3,336.2 | 32.9 | 1.000x | 124.962x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.018x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 874.2 | 871.2 | 880.7 | 3.3 | 1.000x | 54.275x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 875.4 | 869.8 | 880.2 | 3.5 | 1.001x | 54.353x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.2 | 0.1 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.009x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 322.4 | 315.7 | 336.2 | 7.0 | 0.106x | 12.361x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,032.6 | 3,026.0 | 3,039.4 | 5.6 | 1.000x | 116.283x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.4 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.1 | 0.016x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,254.6 | 1,246.1 | 1,280.1 | 12.6 | 1.000x | 62.058x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,254.9 | 1,244.7 | 1,268.0 | 7.8 | 1.000x | 62.073x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.1 | 19.3 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.1 | 19.3 | 0.1 | 0.004x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.1 | 381.6 | 392.8 | 4.2 | 0.084x | 20.235x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,621.5 | 4,601.2 | 4,628.4 | 11.8 | 1.000x | 241.608x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.0 | 0.0 | 0.014x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.1 | 0.015x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,581.8 | 1,579.2 | 1,643.6 | 24.4 | 0.995x | 68.678x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,589.1 | 1,573.4 | 1,592.3 | 6.7 | 1.000x | 68.995x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 25.2 | 25.2 | 25.3 | 0.0 | 0.004x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.5 | 0.1 | 0.004x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 477.9 | 474.7 | 501.6 | 11.0 | 0.081x | 18.948x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,867.4 | 5,866.0 | 5,911.6 | 19.5 | 1.000x | 232.647x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.4 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 13.0 | 0.2 | 0.020x | 1.042x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.9 | 626.0 | 639.5 | 5.5 | 1.000x | 51.896x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.8 | 630.9 | 643.0 | 4.2 | 1.008x | 52.294x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.9 | 27.1 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 27.0 | 27.1 | 0.1 | 0.013x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 194.0 | 187.9 | 195.1 | 2.6 | 0.093x | 7.197x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,077.7 | 2,061.7 | 2,099.7 | 12.7 | 1.000x | 77.094x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.8 | 0.1 | 0.017x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 846.0 | 839.5 | 847.9 | 3.4 | 0.997x | 57.789x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 848.6 | 843.5 | 854.9 | 4.0 | 1.000x | 57.964x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.8 | 21.0 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.9 | 20.8 | 21.0 | 0.1 | 0.007x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 282.8 | 279.5 | 306.2 | 10.0 | 0.097x | 13.563x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,914.4 | 2,902.0 | 2,937.3 | 12.3 | 1.000x | 139.786x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.023x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,006.6 | 994.3 | 1,029.1 | 11.3 | 1.000x | 43.594x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,009.0 | 1,002.1 | 1,021.5 | 6.3 | 1.002x | 43.699x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.5 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 27.3 | 0.1 | 0.008x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.0 | 561.9 | 576.0 | 4.8 | 0.158x | 21.090x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,594.7 | 3,549.9 | 3,615.4 | 25.2 | 1.000x | 133.230x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 11.3 | 11.5 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 0.032x | 1.065x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 376.5 | 374.4 | 379.8 | 1.8 | 0.999x | 33.259x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 377.0 | 375.5 | 381.6 | 2.1 | 1.000x | 33.304x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 62.5 | 0.1 | 0.040x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.2 | 62.5 | 0.1 | 0.040x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 209.5 | 208.6 | 211.7 | 1.0 | 0.135x | 3.361x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,547.8 | 1,538.0 | 1,562.7 | 9.8 | 1.000x | 24.836x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.0 | 0.788x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.2 | 0.0 | 0.790x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 33.7 | 0.4 | 1.000x | 1.269x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.0 | 33.3 | 35.0 | 0.5 | 1.029x | 1.306x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 23.9 | 0.1 | 0.697x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 24.1 | 0.2 | 0.698x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 33.9 | 35.1 | 0.4 | 1.000x | 1.435x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 44.4 | 0.0 | 1.301x | 1.867x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.1 | 0.1 | 0.062x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 10.6 | 0.1 | 0.065x | 1.044x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.2 | 161.1 | 164.0 | 0.9 | 1.000x | 16.155x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.9 | 161.6 | 167.7 | 2.1 | 1.004x | 16.220x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.5 | 18.7 | 0.1 | 0.105x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.5 | 19.8 | 0.6 | 0.106x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.6 | 54.7 | 0.0 | 0.309x | 2.945x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 177.1 | 177.0 | 179.9 | 1.3 | 1.000x | 9.544x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.3 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.022x | 1.047x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 608.9 | 607.3 | 617.2 | 3.8 | 1.000x | 47.718x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 611.9 | 604.7 | 614.7 | 3.5 | 1.005x | 47.954x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 10.8 | 10.6 | 11.0 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 11.4 | 11.1 | 12.3 | 0.4 | 0.018x | 1.059x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.5 | 85.0 | 0.5 | 0.135x | 7.815x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 624.7 | 620.6 | 627.7 | 2.5 | 1.000x | 57.980x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.7 | 0.1 | 0.022x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.2 | 571.8 | 582.2 | 3.7 | 1.000x | 47.713x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 575.5 | 574.1 | 594.4 | 7.7 | 1.000x | 47.730x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.5 | 74.5 | 0.4 | 0.026x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 73.9 | 73.7 | 74.0 | 0.1 | 0.026x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 292.5 | 290.5 | 293.0 | 1.0 | 0.105x | 3.971x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,793.1 | 2,776.7 | 2,800.6 | 8.7 | 1.000x | 37.913x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.7 | 0.1 | 0.065x | 1.068x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 161.1 | 159.1 | 166.5 | 2.5 | 1.000x | 16.415x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.5 | 161.7 | 166.1 | 1.6 | 1.009x | 16.557x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 64.2 | 64.1 | 64.7 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 64.4 | 64.1 | 64.5 | 0.1 | 0.063x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.3 | 157.8 | 160.1 | 0.9 | 0.156x | 2.465x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.3 | 1,007.7 | 1,027.6 | 6.8 | 1.000x | 15.789x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.1 | 0.0 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.6 | 0.1 | 0.022x | 1.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.8 | 571.6 | 580.1 | 3.3 | 0.993x | 47.523x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.0 | 569.8 | 577.4 | 2.9 | 1.000x | 47.877x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.5 | 25.8 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 25.8 | 0.1 | 0.013x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 199.6 | 187.5 | 200.0 | 4.9 | 0.100x | 7.814x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,989.4 | 1,956.6 | 1,997.6 | 14.6 | 1.000x | 77.870x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.0 | 0.022x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 22.0 | 0.1 | 0.022x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.5 | 990.6 | 1,013.8 | 8.5 | 0.994x | 45.944x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,004.2 | 989.0 | 1,018.7 | 10.9 | 1.000x | 46.207x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.8 | 20.1 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.9 | 20.1 | 0.1 | 0.006x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 533.5 | 528.2 | 537.1 | 2.9 | 0.151x | 26.794x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,525.7 | 3,516.8 | 3,538.9 | 7.1 | 1.000x | 177.087x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.0 | 0.014x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.014x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,614.4 | 1,603.2 | 1,635.6 | 10.7 | 0.998x | 69.917x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,617.7 | 1,603.4 | 1,628.1 | 9.7 | 1.000x | 70.058x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 20.4 | 20.2 | 20.8 | 0.2 | 0.003x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.1 | 0.003x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 466.5 | 464.0 | 471.2 | 2.4 | 0.077x | 22.817x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,063.9 | 6,004.3 | 6,176.9 | 61.1 | 1.000x | 296.577x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.4 | 0.5 | 0.017x | 1.010x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 774.2 | 773.1 | 784.9 | 5.2 | 1.000x | 58.706x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.0 | 775.8 | 792.8 | 6.3 | 1.005x | 58.992x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 12.3 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 13.0 | 0.3 | 0.006x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 183.1 | 181.3 | 186.4 | 1.8 | 0.090x | 15.177x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,027.1 | 2,020.1 | 2,096.4 | 33.4 | 1.000x | 168.048x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.6 | 11.9 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.5 | 0.1 | 0.023x | 1.056x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.8 | 540.1 | 578.0 | 14.5 | 1.000x | 46.618x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 549.6 | 546.1 | 556.3 | 3.6 | 1.014x | 47.288x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.7 | 72.2 | 0.2 | 0.028x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 72.1 | 71.9 | 72.3 | 0.1 | 0.028x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 271.3 | 270.7 | 274.6 | 1.8 | 0.106x | 3.767x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,559.3 | 2,541.1 | 2,580.9 | 13.4 | 1.000x | 35.537x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.019x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 765.4 | 762.2 | 802.1 | 14.8 | 1.000x | 52.462x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 765.8 | 763.2 | 772.6 | 3.6 | 1.000x | 52.487x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 56.7 | 56.6 | 57.0 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 56.7 | 56.5 | 57.1 | 0.2 | 0.016x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 378.3 | 372.4 | 381.5 | 3.4 | 0.107x | 6.672x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,519.7 | 3,513.1 | 3,537.6 | 8.7 | 1.000x | 62.081x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.5 | 11.9 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.5 | 0.1 | 0.023x | 1.070x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.6 | 538.1 | 547.8 | 3.6 | 1.000x | 47.222x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.6 | 545.3 | 552.4 | 2.7 | 1.004x | 47.392x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.8 | 72.1 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 72.1 | 72.0 | 72.3 | 0.1 | 0.028x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.3 | 270.8 | 283.7 | 4.6 | 0.107x | 3.797x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,564.9 | 2,544.1 | 2,577.3 | 10.9 | 1.000x | 35.638x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.1 | 0.017x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.2 | 766.6 | 785.4 | 8.1 | 1.000x | 58.725x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 787.0 | 773.9 | 792.2 | 6.5 | 1.013x | 59.462x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.007x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.3 | 213.4 | 228.1 | 4.9 | 0.082x | 11.120x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.4 | 2,658.3 | 2,692.7 | 12.7 | 1.000x | 135.675x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.017x | 1.012x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.4 | 769.5 | 787.0 | 5.9 | 1.000x | 58.693x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 770.3 | 799.3 | 11.3 | 1.003x | 58.891x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.4 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.3 | 14.6 | 0.1 | 0.005x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.9 | 215.0 | 221.4 | 2.3 | 0.082x | 15.170x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.7 | 2,651.0 | 2,690.4 | 13.7 | 1.000x | 185.437x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.017x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.8 | 763.4 | 784.8 | 7.5 | 1.000x | 58.459x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.1 | 770.5 | 785.3 | 5.5 | 1.013x | 59.240x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.3 | 14.2 | 14.4 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.5 | 0.0 | 0.005x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.5 | 215.3 | 220.7 | 2.0 | 0.082x | 15.237x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,660.0 | 2,652.5 | 2,670.4 | 6.1 | 1.000x | 186.345x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.3 | 13.5 | 0.1 | 0.017x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 772.1 | 770.4 | 781.3 | 4.7 | 1.000x | 58.391x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.5 | 772.8 | 787.2 | 4.7 | 1.008x | 58.871x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.5 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.3 | 14.5 | 0.1 | 0.005x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 214.2 | 211.5 | 220.0 | 3.2 | 0.080x | 14.887x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.4 | 2,641.5 | 2,686.6 | 14.6 | 1.000x | 185.281x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.017x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.8 | 767.3 | 785.3 | 5.9 | 1.000x | 58.711x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.0 | 778.1 | 819.8 | 16.0 | 1.008x | 59.181x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 16.5 | 16.4 | 16.7 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 16.6 | 16.4 | 16.7 | 0.1 | 0.006x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.6 | 209.8 | 221.9 | 4.5 | 0.082x | 13.231x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,674.0 | 2,643.3 | 2,679.8 | 13.6 | 1.000x | 161.881x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,167.1 | 10,130.0 | 10,215.3 | 28.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,206.4 | 10,113.3 | 10,239.2 | 44.8 | 1.004x | 1.004x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,066.3 | 19,062.9 | 19,068.1 | 1.7 | 1.875x | 1.875x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,073.4 | 19,066.6 | 19,182.8 | 44.9 | 1.876x | 1.876x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,461.2 | 7,460.4 | 7,501.7 | 16.1 | 0.041x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,464.1 | 7,461.2 | 7,470.2 | 3.3 | 0.041x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 181,474.8 | 180,540.0 | 186,600.1 | 2,137.3 | 1.000x | 24.322x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 181,728.2 | 180,968.3 | 183,515.5 | 889.0 | 1.001x | 24.356x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,548.8 | 9,548.2 | 9,552.8 | 1.9 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,550.5 | 9,550.2 | 9,552.2 | 0.7 | 0.033x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290,683.7 | 289,035.8 | 293,222.9 | 1,369.0 | 0.999x | 30.442x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 290,975.4 | 289,240.3 | 291,726.3 | 875.3 | 1.000x | 30.473x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,040.1 | 19,038.3 | 19,100.3 | 24.2 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,043.2 | 19,042.4 | 19,047.9 | 2.0 | 0.022x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853,818.0 | 846,089.0 | 884,443.3 | 16,079.4 | 1.000x | 44.843x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856,424.9 | 843,206.8 | 891,748.0 | 17,490.2 | 1.003x | 44.980x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,738.0 | 3,737.3 | 3,739.1 | 0.7 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,738.7 | 3,738.5 | 3,739.9 | 0.5 | 0.052x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,436.0 | 71,551.3 | 73,986.6 | 791.3 | 1.000x | 19.378x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73,033.2 | 71,908.1 | 74,142.9 | 802.6 | 1.008x | 19.538x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.4 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.7 | 0.2 | 0.018x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.5 | 874.3 | 904.1 | 13.2 | 1.000x | 54.275x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 904.1 | 874.6 | 941.5 | 22.2 | 1.029x | 55.857x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,787.0 | 4,785.6 | 4,787.8 | 0.8 | 0.023x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,787.0 | 4,786.1 | 4,795.2 | 3.4 | 0.023x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211,624.0 | 211,459.2 | 213,818.0 | 912.0 | 1.000x | 44.208x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,821.7 | 211,105.6 | 215,922.3 | 1,579.6 | 1.006x | 44.458x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,645.7 | 7,644.7 | 7,698.4 | 21.2 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,645.9 | 7,644.6 | 7,648.3 | 1.3 | 0.052x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 148,371.8 | 148,032.4 | 149,375.9 | 456.4 | 1.000x | 19.406x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,600.9 | 147,906.3 | 150,185.6 | 811.3 | 1.002x | 19.436x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.060x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.7 | 0.1 | 0.065x | 1.073x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.5 | 161.0 | 167.3 | 2.2 | 1.000x | 16.554x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.1 | 162.0 | 168.9 | 2.4 | 1.016x | 16.813x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 21.1 | 21.1 | 21.3 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 21.5 | 21.2 | 21.7 | 0.2 | 0.013x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.8 | 141.4 | 142.5 | 0.4 | 0.088x | 6.712x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,616.9 | 1,602.1 | 1,626.3 | 7.8 | 1.000x | 76.550x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 35.8 | 38.5 | 1.0 | 0.034x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 36.1 | 36.7 | 0.3 | 0.034x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.2 | 1,057.1 | 1,077.7 | 6.5 | 1.000x | 29.579x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,071.4 | 1,055.1 | 1,089.6 | 11.0 | 1.004x | 29.694x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.2 | 66.5 | 0.4 | 0.062x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.3 | 75.4 | 3.8 | 0.062x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.8 | 172.3 | 174.2 | 0.7 | 0.162x | 2.618x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.5 | 1,058.4 | 1,078.4 | 7.8 | 1.000x | 16.178x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.3 | 35.5 | 0.4 | 0.034x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.5 | 35.1 | 0.2 | 0.034x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,003.9 | 997.4 | 1,012.1 | 4.8 | 1.000x | 29.158x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,008.2 | 1,001.2 | 1,021.6 | 6.7 | 1.004x | 29.284x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.0 | 62.3 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.1 | 62.4 | 0.1 | 0.062x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.6 | 157.9 | 160.8 | 1.1 | 0.158x | 2.568x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,010.9 | 1,002.4 | 1,013.2 | 3.8 | 1.000x | 16.265x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.3 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.4 | 0.1 | 0.028x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 681.3 | 690.2 | 3.5 | 1.000x | 35.689x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 687.9 | 678.3 | 702.4 | 8.7 | 1.009x | 36.001x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.4 | 25.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 25.8 | 0.1 | 0.038x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 109.3 | 2.1 | 0.152x | 4.097x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.2 | 681.2 | 690.1 | 2.9 | 1.000x | 26.920x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.4 | 14.1 | 0.7 | 0.020x | 1.065x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.6 | 633.0 | 642.3 | 3.2 | 1.000x | 53.307x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.4 | 630.9 | 663.8 | 12.7 | 1.001x | 53.377x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.2 | 27.0 | 27.4 | 0.1 | 0.012x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 27.3 | 27.2 | 27.6 | 0.1 | 0.012x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.3 | 203.3 | 204.7 | 0.5 | 0.091x | 7.477x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,235.9 | 2,223.6 | 2,246.5 | 7.9 | 1.000x | 82.221x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 30.0 | 30.3 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.2 | 30.5 | 0.1 | 0.036x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853.5 | 845.8 | 870.3 | 9.2 | 1.000x | 28.322x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 865.2 | 846.2 | 884.5 | 13.0 | 1.014x | 28.712x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.9 | 51.9 | 52.0 | 0.0 | 0.061x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 52.0 | 51.9 | 52.2 | 0.1 | 0.061x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.8 | 147.4 | 148.8 | 0.5 | 0.174x | 2.846x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 849.3 | 843.4 | 854.4 | 3.7 | 1.000x | 16.352x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.5 | 60.8 | 0.4 | 0.069x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.7 | 60.0 | 0.1 | 0.069x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.6 | 857.3 | 873.0 | 5.5 | 1.000x | 14.528x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.1 | 864.3 | 890.4 | 9.6 | 1.009x | 14.653x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 112.8 | 112.6 | 113.2 | 0.2 | 0.128x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 113.3 | 112.9 | 113.7 | 0.3 | 0.129x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.7 | 163.8 | 165.8 | 0.8 | 0.187x | 1.460x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.9 | 868.1 | 887.8 | 6.4 | 1.000x | 7.792x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 42.8 | 0.0 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.9 | 42.6 | 43.1 | 0.2 | 0.019x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,218.2 | 2,206.5 | 2,255.4 | 18.6 | 1.000x | 51.880x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,232.4 | 2,215.9 | 2,275.5 | 21.7 | 1.006x | 52.211x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 93.1 | 93.0 | 93.3 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 93.1 | 93.0 | 93.4 | 0.1 | 0.030x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.1 | 404.3 | 409.5 | 1.8 | 0.131x | 4.372x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,113.9 | 3,110.2 | 3,161.3 | 19.7 | 1.000x | 33.438x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.5 | 0.1 | 0.017x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.4 | 771.4 | 828.1 | 22.0 | 0.997x | 59.513x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.1 | 778.9 | 798.9 | 6.6 | 1.000x | 59.718x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.5 | 20.7 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.1 | 0.2 | 0.008x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.4 | 214.6 | 221.5 | 2.5 | 0.082x | 10.724x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,690.5 | 2,676.0 | 2,708.5 | 11.1 | 1.000x | 130.901x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.2 | 770.6 | 814.9 | 16.0 | 0.995x | 59.550x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 789.2 | 782.2 | 798.4 | 5.9 | 1.000x | 59.853x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.2 | 0.2 | 0.010x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.1 | 0.2 | 0.010x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 231.5 | 226.5 | 238.2 | 3.8 | 0.087x | 8.642x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.1 | 2,648.7 | 2,691.8 | 13.7 | 1.000x | 99.641x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.5 | 35.2 | 0.2 | 0.034x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.7 | 1,021.5 | 1,039.9 | 6.7 | 1.000x | 29.905x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,046.2 | 1,036.9 | 1,062.5 | 8.3 | 1.009x | 30.180x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.0 | 62.0 | 63.1 | 0.4 | 0.060x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.1 | 62.7 | 0.2 | 0.060x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.9 | 109.0 | 0.9 | 0.104x | 1.741x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.4 | 1,021.5 | 1,048.5 | 8.7 | 1.000x | 16.704x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 35.7 | 0.6 | 0.033x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.0 | 0.2 | 0.034x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,034.7 | 1,018.8 | 1,040.0 | 7.5 | 1.000x | 29.990x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,049.6 | 1,042.0 | 1,060.1 | 6.3 | 1.014x | 30.422x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 63.1 | 0.4 | 0.060x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 62.8 | 0.4 | 0.061x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.7 | 106.4 | 111.5 | 1.9 | 0.104x | 1.727x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,018.0 | 1,043.8 | 8.3 | 1.000x | 16.533x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.4 | 35.0 | 0.2 | 0.030x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 34.4 | 35.9 | 0.6 | 0.031x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.7 | 1,128.7 | 1,158.3 | 10.1 | 1.000x | 32.839x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,155.2 | 1,138.4 | 1,173.7 | 11.2 | 1.011x | 33.197x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.1 | 62.0 | 62.4 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.0 | 62.6 | 0.2 | 0.055x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.3 | 107.3 | 111.9 | 1.6 | 0.095x | 1.743x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,139.6 | 1,128.3 | 1,142.1 | 4.9 | 1.000x | 18.339x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.4 | 35.9 | 0.6 | 0.032x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.4 | 0.3 | 0.032x | 1.010x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.5 | 1,071.5 | 1,091.5 | 6.7 | 1.000x | 31.296x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,092.1 | 1,084.8 | 1,106.2 | 8.6 | 1.014x | 31.719x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.1 | 62.0 | 62.6 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.4 | 0.1 | 0.058x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.2 | 115.8 | 3.3 | 0.100x | 1.730x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.1 | 1,069.2 | 1,095.0 | 10.1 | 1.000x | 17.316x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.4 | 34.8 | 0.1 | 0.032x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.1 | 1,070.5 | 1,082.2 | 4.3 | 1.000x | 31.058x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,088.9 | 1,085.9 | 1,102.1 | 6.1 | 1.016x | 31.546x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.0 | 62.0 | 62.3 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.1 | 62.0 | 62.5 | 0.2 | 0.057x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 107.0 | 115.6 | 3.3 | 0.099x | 1.734x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,081.8 | 1,073.1 | 1,091.8 | 7.6 | 1.000x | 17.436x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 914.0 | 907.6 | 948.5 | 17.7 | 0.998x | 56.791x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 915.7 | 900.8 | 923.9 | 8.7 | 1.000x | 56.896x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 25.9 | 26.7 | 0.2 | 0.008x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 309.8 | 306.4 | 323.5 | 7.7 | 0.097x | 11.790x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,201.4 | 3,179.1 | 3,208.6 | 10.6 | 1.000x | 121.813x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.4 | 12.1 | 0.7 | 0.361x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 10.7 | 11.7 | 0.4 | 0.367x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 2.773x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 30.8 | 0.2 | 1.002x | 2.779x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 4.8 | 4.7 | 7.1 | 0.9 | 0.157x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.4 | 6.7 | 0.5 | 0.178x | 1.132x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 30.9 | 0.2 | 1.000x | 6.367x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 39.9 | 40.6 | 0.3 | 1.321x | 8.411x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 0.324x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.4 | 0.4 | 0.344x | 1.061x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 3.087x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 3.087x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 7.1 | 0.7 | 0.177x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 6.4 | 6.2 | 6.8 | 0.2 | 0.210x | 1.187x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 30.8 | 0.1 | 1.000x | 5.650x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 39.9 | 40.4 | 0.2 | 1.318x | 7.449x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 11.3 | 12.4 | 0.4 | 0.336x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.7 | 12.1 | 0.1 | 0.353x | 1.050x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.9 | 33.8 | 34.6 | 0.3 | 1.000x | 2.979x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 33.9 | 35.3 | 0.5 | 1.025x | 3.053x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.4 | 37.3 | 0.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.3 | 46.4 | 0.0 | 1.276x | 1.276x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.7 | 73.1 | 0.2 | 2.008x | 2.008x |
| 4 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 73.0 | 72.6 | 73.3 | 0.2 | 2.010x | 2.010x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 0.580x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.2 | 0.1 | 0.581x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 34.7 | 0.8 | 1.000x | 1.725x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 35.2 | 0.3 | 1.043x | 1.799x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 16.4 | 0.1 | 0.479x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 16.5 | 0.1 | 0.480x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 34.0 | 35.1 | 0.4 | 1.000x | 2.089x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.3 | 44.4 | 0.1 | 1.299x | 2.714x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,584,231.2 | 3,579,699.4 | 3,584,990.0 | 1,970.1 | 0.069x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,588,166.2 | 3,584,610.6 | 3,591,881.9 | 2,695.2 | 0.070x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,031,195.0 | 6,979,358.0 | 7,057,785.3 | 28,652.1 | 0.136x | 1.962x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,615,885.8 | 51,304,264.0 | 52,022,538.5 | 284,120.8 | 1.000x | 14.401x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,798.8 | 18,672.9 | 18,972.7 | 113.2 | 1.000x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 1,875,059.9 | 1,874,408.6 | 1,884,241.2 | 3,731.1 | 99.743x | 99.743x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 1,879,469.6 | 1,875,068.2 | 1,887,372.7 | 4,969.2 | 99.978x | 99.978x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,589,931.3 | 17,552,497.7 | 17,676,695.0 | 42,309.9 | 935.693x | 935.693x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,761.9 | 18,621.4 | 18,785.8 | 71.3 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 1,875,293.9 | 1,874,473.9 | 1,890,304.6 | 6,081.8 | 99.952x | 99.952x | 5 | 100% |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 1,875,907.4 | 1,874,708.0 | 1,877,189.2 | 877.2 | 99.985x | 99.985x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,181,424.3 | 3,174,984.3 | 3,210,411.4 | 13,896.2 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,190,860.9 | 3,180,049.5 | 3,204,099.7 | 7,837.1 | 0.007x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42,743,471.0 | 42,677,077.0 | 43,235,138.3 | 205,178.3 | 0.096x | 13.435x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 447,267,822.4 | 446,157,442.5 | 452,012,100.1 | 2,246,381.8 | 1.000x | 140.587x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,846.0 | 18,750.9 | 19,031.6 | 94.9 | 1.000x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,152,336.1 | 3,141,180.9 | 3,166,260.5 | 9,508.5 | 167.268x | 167.268x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,157,983.1 | 3,136,546.8 | 3,162,948.2 | 9,308.8 | 167.568x | 167.568x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,545,364.0 | 22,516,477.0 | 23,129,297.3 | 250,645.8 | 1196.294x | 1196.294x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 0.355x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.3 | 1.000x | 2.854x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.003x | 2.863x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.0 | 19.2 | 0.4 | 0.180x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.435x | 2.434x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 99.7 | 105.6 | 2.1 | 1.000x | 5.593x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 11.3 | 0.5 | 0.347x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.352x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.5 | 0.7 | 0.994x | 2.861x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.7 | 0.4 | 1.000x | 2.879x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 19.2 | 0.5 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.5 | 0.3 | 0.439x | 2.430x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.7 | 101.4 | 1.0 | 1.000x | 5.532x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.348x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.355x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 2.862x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 2.872x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.1 | 0.1 | 0.182x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.6 | 0.4 | 0.440x | 2.431x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 99.1 | 101.4 | 0.8 | 1.000x | 5.523x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.1 | 0.0 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.2 | 1.000x | 2.844x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.007x | 2.864x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.179x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.433x | 2.430x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 96.0 | 101.4 | 2.3 | 1.000x | 5.608x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.355x | 1.012x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 32.2 | 1.4 | 1.000x | 2.852x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 1.003x | 2.859x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.5 | 0.5 | 0.184x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.5 | 18.7 | 0.1 | 0.186x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 44.5 | 45.4 | 0.3 | 0.450x | 2.450x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.9 | 101.6 | 1.2 | 1.000x | 5.438x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.844x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.1 | 29.1 | 0.3 | 1.008x | 2.868x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.7 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.4 | 0.3 | 0.440x | 2.436x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.3 | 101.0 | 1.3 | 1.000x | 5.537x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 2.851x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 2.860x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.7 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.8 | 0.4 | 0.440x | 2.425x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 101.4 | 1.4 | 1.000x | 5.516x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.356x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.0 | 1.000x | 2.855x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.002x | 2.861x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 47.8 | 1.5 | 0.443x | 2.444x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.2 | 1.2 | 1.000x | 5.523x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.021x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 2.860x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 2.861x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 45.5 | 0.7 | 0.440x | 2.432x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 100.2 | 1.0 | 1.000x | 5.526x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 11.3 | 0.4 | 0.359x | 1.023x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 2.847x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 28.8 | 0.2 | 1.007x | 2.866x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.183x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.4 | 0.2 | 0.442x | 2.435x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.6 | 1.0 | 1.000x | 5.514x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.360x | 1.025x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 2.850x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.006x | 2.866x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.437x | 2.424x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 101.2 | 1.2 | 1.000x | 5.551x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 28.8 | 0.1 | 1.000x | 2.852x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.1 | 1.002x | 2.857x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.439x | 2.425x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.7 | 1.0 | 1.000x | 5.521x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.015x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 2.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.5 | 0.7 | 1.007x | 2.874x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.183x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.5 | 0.4 | 0.441x | 2.422x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.0 | 98.1 | 101.0 | 1.1 | 1.000x | 5.488x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 2.847x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.7 | 0.4 | 1.006x | 2.865x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.3 | 0.1 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.440x | 2.430x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 98.0 | 100.9 | 1.1 | 1.000x | 5.522x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.1 | 0.0 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.357x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 2.852x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.009x | 2.876x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.6 | 0.2 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 45.9 | 0.8 | 0.441x | 2.443x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.7 | 101.0 | 1.2 | 1.000x | 5.540x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.0 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 30.3 | 0.7 | 1.000x | 2.856x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 2.864x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.3 | 0.1 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.9 | 0.8 | 0.442x | 2.447x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.3 | 101.4 | 1.1 | 1.000x | 5.533x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.1 | 0.0 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.001x | 2.859x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.5 | 0.2 | 0.181x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 46.0 | 1.0 | 0.441x | 2.442x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.3 | 101.0 | 1.3 | 1.000x | 5.534x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 2.855x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.004x | 2.866x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.4 | 0.6 | 0.441x | 2.432x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 5.517x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.354x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 0.999x | 2.863x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 1.000x | 2.867x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.1 | 0.6 | 0.440x | 2.429x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 5.516x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.015x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 2.856x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.002x | 2.862x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.4 | 0.6 | 0.445x | 2.450x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 101.0 | 1.3 | 1.000x | 5.504x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.354x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 2.845x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.7 | 0.0 | 1.005x | 2.859x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.9 | 0.5 | 0.441x | 2.440x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.3 | 100.6 | 1.1 | 1.000x | 5.539x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 0.355x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.000x | 2.856x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.003x | 2.864x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.8 | 49.5 | 2.2 | 0.445x | 2.453x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.6 | 101.0 | 1.2 | 1.000x | 5.513x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 2.862x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 2.871x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.5 | 0.3 | 0.443x | 2.440x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 99.9 | 0.6 | 1.000x | 5.510x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.0 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 2.847x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 29.7 | 0.5 | 1.005x | 2.862x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.3 | 0.3 | 0.440x | 2.428x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.7 | 99.9 | 0.9 | 1.000x | 5.513x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 28.7 | 0.1 | 1.000x | 2.856x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.0 | 0.5 | 1.003x | 2.865x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.9 | 44.6 | 0.3 | 0.447x | 2.465x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 101.1 | 0.9 | 1.000x | 5.518x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.7 | 0.2 | 0.358x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.845x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.008x | 2.868x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.3 | 0.1 | 0.181x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.3 | 0.3 | 0.441x | 2.437x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.9 | 1.1 | 1.000x | 5.531x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.849x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.0 | 1.005x | 2.864x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.3 | 0.6 | 0.437x | 2.428x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 97.4 | 103.1 | 1.8 | 1.000x | 5.561x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.353x | 1.008x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 31.6 | 1.2 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 1.004x | 2.867x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.4 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 47.4 | 1.5 | 0.443x | 2.428x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 104.3 | 2.4 | 1.000x | 5.485x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.359x | 1.023x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.1 | 1.000x | 2.852x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.8 | 0.1 | 1.004x | 2.864x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.183x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 44.8 | 0.4 | 0.446x | 2.444x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.6 | 97.3 | 104.5 | 2.6 | 1.000x | 5.476x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.354x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.849x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.005x | 2.864x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.182x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.442x | 2.429x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 97.7 | 104.6 | 2.4 | 1.000x | 5.500x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 2.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.006x | 2.869x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.438x | 2.439x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 104.7 | 2.4 | 1.000x | 5.563x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 2.846x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 2.870x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.2 | 0.1 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.6 | 45.1 | 0.6 | 0.445x | 2.454x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.3 | 104.8 | 2.6 | 1.000x | 5.515x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.355x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.1 | 0.2 | 1.000x | 2.844x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.007x | 2.863x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.183x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.4 | 0.3 | 0.444x | 2.432x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.7 | 97.3 | 104.9 | 2.8 | 1.000x | 5.480x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.359x | 1.023x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 2.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.002x | 2.860x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.183x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.3 | 0.450x | 2.463x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.5 | 97.6 | 104.1 | 2.4 | 1.000x | 5.468x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.346x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.349x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 0.990x | 2.862x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 29.4 | 0.3 | 1.000x | 2.890x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 22.1 | 1.6 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.442x | 2.433x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 104.4 | 2.4 | 1.000x | 5.506x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.357x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.4 | 0.3 | 1.000x | 2.860x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 2.861x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.4 | 0.3 | 0.442x | 2.441x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.6 | 102.1 | 1.5 | 1.000x | 5.528x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.355x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 2.873x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.441x | 2.428x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.2 | 99.9 | 1.0 | 1.000x | 5.511x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.348x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.355x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 0.997x | 2.863x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.000x | 2.871x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.6 | 0.4 | 0.441x | 2.434x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 100.7 | 1.2 | 1.000x | 5.519x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.353x | 1.010x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 2.864x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 2.864x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.4 | 0.2 | 0.182x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.444x | 2.432x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 100.7 | 1.2 | 1.000x | 5.482x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 1.000x | 2.845x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.005x | 2.859x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.2 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.6 | 47.9 | 1.6 | 0.441x | 2.453x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.2 | 100.5 | 1.2 | 1.000x | 5.562x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.346x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 11.9 | 0.7 | 0.356x | 1.028x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 0.996x | 2.874x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.1 | 0.2 | 1.000x | 2.887x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.7 | 0.0 | 0.264x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 10.1 | 0.6 | 0.265x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 35.0 | 1.0 | 1.000x | 3.791x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 36.3 | 40.1 | 1.3 | 1.151x | 4.365x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 10.9 | 0.1 | 0.123x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 11.1 | 0.2 | 0.124x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 86.8 | 86.4 | 88.4 | 0.7 | 1.000x | 8.143x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.7 | 86.5 | 90.1 | 1.1 | 1.021x | 8.316x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 17.3 | 17.2 | 17.8 | 0.2 | 0.173x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.9 | 0.2 | 0.174x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 52.2 | 3.2 | 0.443x | 2.555x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.1 | 101.2 | 1.2 | 1.000x | 5.764x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.347x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 0.996x | 2.867x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.2 | 1.000x | 2.879x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.5 | 18.2 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.5 | 18.3 | 0.3 | 0.179x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.1 | 0.8 | 0.449x | 2.522x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 98.0 | 101.8 | 1.5 | 1.000x | 5.621x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.357x | 1.021x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 2.860x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 1.001x | 2.863x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 18.2 | 19.6 | 0.5 | 0.193x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 18.6 | 21.5 | 1.1 | 0.199x | 1.033x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.4 | 0.6 | 0.446x | 2.312x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 101.0 | 1.2 | 1.000x | 5.186x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 2.849x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.1 | 1.006x | 2.867x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.0 | 19.8 | 0.6 | 0.187x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 44.1 | 45.8 | 0.6 | 0.450x | 2.407x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.0 | 101.6 | 1.6 | 1.000x | 5.345x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.347x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 0.996x | 2.867x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.0 | 0.2 | 1.000x | 2.880x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.0 | 19.8 | 0.6 | 0.186x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.1 | 18.9 | 0.4 | 0.189x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.1 | 0.5 | 0.448x | 2.401x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.3 | 101.0 | 1.1 | 1.000x | 5.362x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 2.846x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 2.864x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.0 | 18.9 | 0.3 | 0.188x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.191x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.4 | 0.6 | 0.449x | 2.385x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 100.7 | 1.2 | 1.000x | 5.316x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 28.9 | 0.1 | 1.008x | 2.880x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.1 | 18.6 | 0.2 | 0.187x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.189x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.1 | 1.2 | 0.448x | 2.398x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.5 | 100.8 | 1.2 | 1.000x | 5.354x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.015x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 2.856x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.003x | 2.866x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.190x | 1.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.0 | 0.8 | 0.449x | 2.471x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 101.0 | 1.3 | 1.000x | 5.503x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.015x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 2.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.003x | 2.860x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.190x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.6 | 45.2 | 0.5 | 0.449x | 2.470x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.5 | 101.8 | 1.5 | 1.000x | 5.504x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 2.858x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.002x | 2.865x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.1 | 18.9 | 0.4 | 0.190x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.1 | 1.2 | 0.448x | 2.466x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.6 | 101.7 | 1.4 | 1.000x | 5.503x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 2.846x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.2 | 28.9 | 0.2 | 1.005x | 2.861x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.7 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.043x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.6 | 1.4 | 0.447x | 2.463x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 100.9 | 1.1 | 1.000x | 5.515x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.348x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.996x | 2.863x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.000x | 2.873x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.0 | 19.0 | 0.5 | 0.190x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.3 | 1.3 | 0.448x | 2.476x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 100.4 | 0.8 | 1.000x | 5.521x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.358x | 1.024x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 0.999x | 2.861x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.2 | 1.000x | 2.863x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.4 | 18.0 | 19.0 | 0.4 | 0.186x | 1.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 47.2 | 1.3 | 0.448x | 2.458x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 101.0 | 1.1 | 1.000x | 5.491x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 2.843x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 2.865x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 17.9 | 18.9 | 0.4 | 0.183x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.3 | 0.5 | 0.447x | 2.457x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.8 | 100.6 | 0.9 | 1.000x | 5.501x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.0 | 0.2 | 1.000x | 2.843x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.005x | 2.857x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.4 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.6 | 0.3 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.9 | 0.8 | 0.446x | 2.460x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 101.5 | 1.2 | 1.000x | 5.521x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.999x | 2.851x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.3 | 28.7 | 0.1 | 1.000x | 2.852x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.182x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.182x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 51.8 | 3.0 | 0.451x | 2.481x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 100.1 | 1.1 | 1.000x | 5.502x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.999x | 2.867x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 1.000x | 2.869x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.357x | 1.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 2.857x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.5 | 0.3 | 1.000x | 2.866x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.357x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.1 | 0.2 | 1.000x | 2.854x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.002x | 2.860x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.356x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 2.858x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.001x | 2.860x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.354x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.1 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.005x | 2.870x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 2.859x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.002x | 2.864x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 2.860x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 2.869x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.2 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.357x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 2.860x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 32.0 | 1.3 | 1.003x | 2.867x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 28.8 | 0.3 | 1.002x | 2.862x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.0 | 45.4 | 0.6 | 0.448x | 2.479x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.5 | 100.6 | 1.2 | 1.000x | 5.537x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 1.000x | 2.841x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.9 | 0.5 | 1.005x | 2.855x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.1 | 0.5 | 0.448x | 2.476x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.9 | 100.8 | 1.0 | 1.000x | 5.523x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.359x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.9 | 0.2 | 1.000x | 2.842x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 29.0 | 0.2 | 1.009x | 2.869x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.8 | 47.5 | 1.3 | 0.454x | 2.502x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.4 | 100.5 | 0.9 | 1.000x | 5.514x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.1 | 0.356x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.002x | 2.862x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.180x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.4 | 0.180x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.8 | 45.7 | 0.6 | 0.449x | 2.490x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.9 | 101.2 | 1.2 | 1.000x | 5.547x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.354x | 1.012x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 2.859x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.002x | 2.863x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.181x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.0 | 1.2 | 0.447x | 2.472x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.6 | 101.3 | 1.2 | 1.000x | 5.530x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.018x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.849x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.006x | 2.865x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 19.0 | 0.4 | 0.182x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.6 | 45.0 | 0.5 | 0.450x | 2.489x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.4 | 101.1 | 1.3 | 1.000x | 5.532x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 2.857x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.002x | 2.861x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.8 | 44.6 | 52.4 | 2.8 | 0.460x | 2.544x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.1 | 101.8 | 1.6 | 1.000x | 5.528x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.354x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.996x | 2.859x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 2.869x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.3 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.0 | 19.0 | 0.4 | 0.183x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.4 | 0.6 | 0.450x | 2.485x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.8 | 1.5 | 1.000x | 5.524x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.357x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.998x | 2.856x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 2.861x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 19.2 | 0.5 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.183x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.1 | 45.1 | 0.3 | 0.449x | 2.479x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.2 | 101.2 | 1.2 | 1.000x | 5.520x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.999x | 2.862x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 2.863x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.182x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.7 | 0.2 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 49.5 | 2.1 | 0.449x | 2.471x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 102.6 | 1.6 | 1.000x | 5.508x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.0 | 1.000x | 2.841x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.006x | 2.859x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.9 | 45.6 | 0.6 | 0.447x | 2.471x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.7 | 2.4 | 1.000x | 5.527x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.4 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.358x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.5 | 0.1 | 1.000x | 2.842x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.007x | 2.862x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 19.4 | 0.5 | 0.181x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.7 | 0.7 | 0.450x | 2.487x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.6 | 2.5 | 1.000x | 5.524x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.844x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.5 | 0.3 | 1.006x | 2.862x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 19.2 | 0.5 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 44.8 | 0.4 | 0.449x | 2.480x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 102.5 | 1.8 | 1.000x | 5.520x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.351x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.019x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 2.847x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.009x | 2.872x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 22.2 | 1.6 | 0.181x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.7 | 46.2 | 1.0 | 0.453x | 2.494x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.5 | 100.6 | 1.1 | 1.000x | 5.511x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.349x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 1.015x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 2.862x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.001x | 2.864x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 19.8 | 0.7 | 0.182x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.7 | 0.3 | 0.183x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 46.7 | 1.0 | 0.457x | 2.507x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.5 | 100.6 | 1.2 | 1.000x | 5.487x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.348x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.353x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 0.998x | 2.864x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 2.870x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.181x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.3 | 0.6 | 0.445x | 2.481x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.7 | 100.8 | 1.3 | 1.000x | 5.575x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.6 | 0.2 | 0.360x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.6 | 10.8 | 0.1 | 0.374x | 1.038x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 28.7 | 0.2 | 1.000x | 2.777x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.6 | 0.0 | 1.004x | 2.789x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 5.2 | 5.0 | 5.9 | 0.3 | 0.162x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.6 | 6.8 | 0.5 | 0.182x | 1.125x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.2 | 32.2 | 34.9 | 1.1 | 1.000x | 6.177x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.0 | 37.1 | 39.2 | 0.7 | 1.210x | 7.475x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.127x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 11.4 | 12.5 | 0.4 | 0.127x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.6 | 96.6 | 99.3 | 0.9 | 1.000x | 7.874x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 96.9 | 100.2 | 1.1 | 1.008x | 7.935x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.1 | 0.1 | 0.168x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.8 | 0.4 | 0.168x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.7 | 0.7 | 0.444x | 2.639x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.7 | 101.5 | 1.4 | 1.000x | 5.950x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.3 | 0.1 | 0.352x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.7 | 0.1 | 0.362x | 1.029x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 2.841x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.001x | 2.843x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 10.1 | 9.7 | 11.5 | 0.7 | 0.299x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 10.6 | 10.2 | 10.7 | 0.2 | 0.314x | 1.051x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.8 | 33.7 | 34.9 | 0.5 | 1.000x | 3.343x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.1 | 38.5 | 44.6 | 2.3 | 1.156x | 3.864x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 10.0 | 10.3 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 2.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.3 | 2.2 | 1.005x | 2.868x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 8.7 | 8.6 | 9.1 | 0.2 | 0.268x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 9.9 | 9.0 | 10.1 | 0.4 | 0.304x | 1.137x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 35.0 | 1.0 | 1.000x | 3.736x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.8 | 36.3 | 41.3 | 2.1 | 1.160x | 4.334x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 626,935.4 | 626,672.9 | 627,473.7 | 276.9 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 627,124.2 | 626,566.5 | 627,272.9 | 300.8 | 0.175x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,728,929.7 | 1,671,641.0 | 1,736,029.1 | 27,268.7 | 0.482x | 2.758x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,585,463.7 | 3,561,821.5 | 3,642,459.6 | 36,446.1 | 1.000x | 5.719x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 17,686.0 | 17,673.0 | 17,743.3 | 24.6 | 0.998x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 17,699.5 | 17,694.7 | 17,721.0 | 9.8 | 0.999x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,720.1 | 17,679.0 | 17,806.5 | 42.2 | 1.000x | 1.002x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,676.1 | 39,138.6 | 39,809.0 | 239.0 | 2.239x | 2.243x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 17,628.6 | 17,609.7 | 17,690.1 | 29.2 | 0.993x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 17,696.4 | 17,663.8 | 17,738.6 | 25.0 | 0.997x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,749.3 | 17,679.5 | 17,781.5 | 38.4 | 1.000x | 1.007x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,337.4 | 39,223.7 | 40,015.7 | 287.4 | 2.216x | 2.231x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 30,829.4 | 30,743.9 | 30,873.7 | 45.7 | 0.437x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 30,893.6 | 30,852.1 | 30,938.8 | 28.4 | 0.437x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,317.0 | 68,798.6 | 69,580.9 | 260.6 | 0.982x | 2.248x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,617.0 | 70,422.3 | 70,889.1 | 166.8 | 1.000x | 2.291x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 17,634.2 | 17,625.9 | 17,669.8 | 17.0 | 0.994x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 17,643.5 | 17,623.6 | 17,657.6 | 13.8 | 0.994x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,747.4 | 17,718.3 | 17,791.3 | 24.5 | 1.000x | 1.006x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,612.0 | 39,513.1 | 40,068.9 | 198.9 | 2.232x | 2.246x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.5 | 0.0 | 0.059x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 0.059x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 545.3 | 540.1 | 551.4 | 4.2 | 0.985x | 16.792x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.4 | 545.4 | 558.0 | 4.5 | 1.000x | 17.041x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 58.6 | 0.1 | 0.107x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 58.5 | 59.0 | 0.2 | 0.107x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.3 | 77.2 | 80.5 | 1.3 | 0.141x | 1.321x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.5 | 539.0 | 553.7 | 5.4 | 1.000x | 9.361x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.5 | 0.3 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.8 | 40.2 | 0.2 | 0.052x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 764.0 | 759.3 | 782.6 | 8.8 | 1.000x | 19.170x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 768.1 | 746.8 | 771.8 | 9.3 | 1.005x | 19.274x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 77.7 | 77.5 | 77.7 | 0.1 | 0.101x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 77.8 | 77.7 | 78.1 | 0.2 | 0.101x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.9 | 90.6 | 95.8 | 1.8 | 0.122x | 1.209x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.8 | 761.8 | 780.8 | 6.9 | 1.000x | 9.882x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.3 | 0.0 | 0.038x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 483.8 | 473.4 | 487.4 | 4.8 | 0.997x | 26.524x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 485.4 | 478.3 | 503.1 | 8.8 | 1.000x | 26.616x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.5 | 0.2 | 0.054x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.6 | 64.2 | 68.5 | 1.7 | 0.134x | 2.484x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 481.8 | 472.6 | 490.3 | 6.4 | 1.000x | 18.527x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.4 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.3 | 43.4 | 0.1 | 0.056x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 771.2 | 760.1 | 781.3 | 8.3 | 0.992x | 17.819x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.4 | 767.8 | 785.7 | 6.7 | 1.000x | 17.962x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 86.6 | 86.2 | 87.0 | 0.3 | 0.112x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 87.0 | 86.6 | 87.8 | 0.4 | 0.113x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.6 | 92.8 | 94.2 | 0.5 | 0.121x | 1.080x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.5 | 770.3 | 782.3 | 4.5 | 1.000x | 8.905x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.0 | 60.6 | 61.7 | 0.4 | 0.108x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.9 | 61.7 | 0.3 | 0.108x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 567.1 | 561.7 | 570.8 | 3.1 | 1.000x | 9.297x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.0 | 554.8 | 575.2 | 7.6 | 1.009x | 9.377x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.7 | 91.1 | 94.1 | 1.1 | 0.164x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 119.9 | 120.4 | 0.2 | 0.212x | 1.295x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 120.4 | 120.2 | 120.6 | 0.2 | 0.212x | 1.298x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.7 | 561.3 | 573.1 | 4.3 | 1.000x | 6.112x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.5 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.4 | 0.1 | 0.037x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 481.8 | 471.6 | 494.3 | 7.8 | 0.971x | 26.420x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 496.2 | 473.9 | 530.0 | 18.9 | 1.000x | 27.206x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.1 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 27.5 | 0.6 | 0.055x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.2 | 63.9 | 69.5 | 2.1 | 0.136x | 2.507x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 480.6 | 473.6 | 483.7 | 3.5 | 1.000x | 18.473x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.7 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 30.9 | 0.0 | 0.038x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 771.8 | 800.2 | 10.8 | 0.969x | 25.203x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.9 | 775.8 | 843.0 | 24.7 | 1.000x | 26.010x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.6 | 56.0 | 0.1 | 0.070x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.5 | 55.9 | 0.1 | 0.070x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 84.0 | 91.2 | 3.2 | 0.108x | 1.528x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 792.6 | 778.7 | 794.9 | 5.9 | 1.000x | 14.212x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.7 | 46.4 | 46.7 | 0.1 | 0.074x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.5 | 46.9 | 0.2 | 0.075x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.2 | 603.0 | 623.1 | 7.0 | 0.986x | 13.249x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 627.3 | 613.0 | 635.7 | 9.0 | 1.000x | 13.443x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.8 | 85.6 | 96.3 | 4.1 | 0.147x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 91.8 | 92.2 | 0.1 | 0.148x | 1.003x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 92.0 | 92.2 | 0.1 | 0.148x | 1.003x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 622.3 | 612.9 | 629.0 | 5.5 | 1.000x | 6.781x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 37.8 | 0.5 | 0.067x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.1 | 534.1 | 544.5 | 3.6 | 0.990x | 14.804x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.4 | 542.6 | 556.1 | 4.4 | 1.000x | 14.948x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.6 | 69.7 | 0.1 | 0.128x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.6 | 69.7 | 0.1 | 0.128x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.3 | 78.7 | 87.4 | 3.2 | 0.146x | 1.139x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.7 | 538.4 | 551.3 | 4.8 | 1.000x | 7.814x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.6 | 0.0 | 0.054x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535.2 | 532.1 | 542.0 | 3.4 | 0.982x | 18.079x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 544.9 | 537.2 | 549.6 | 4.4 | 1.000x | 18.407x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.5 | 0.0 | 0.095x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.5 | 0.1 | 0.095x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.4 | 74.6 | 83.2 | 3.2 | 0.139x | 1.465x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.3 | 536.2 | 544.0 | 2.9 | 1.000x | 10.559x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 0.067x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.6 | 433.4 | 443.8 | 3.9 | 0.987x | 14.811x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 443.4 | 439.3 | 445.4 | 2.2 | 1.000x | 15.006x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.7 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.7 | 51.4 | 51.9 | 0.2 | 0.119x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.4 | 67.3 | 75.8 | 2.9 | 0.159x | 1.350x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 435.5 | 431.9 | 444.6 | 5.4 | 1.000x | 8.472x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.5 | 0.3 | 0.036x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 346.0 | 338.3 | 350.5 | 4.0 | 0.987x | 27.251x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.6 | 341.0 | 365.6 | 8.5 | 1.000x | 27.616x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.6 | 34.8 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.7 | 0.1 | 0.020x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.9 | 140.3 | 146.1 | 2.6 | 0.081x | 4.100x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.6 | 1,732.2 | 1,776.7 | 14.9 | 1.000x | 50.443x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 36.0 | 0.3 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 36.6 | 0.5 | 0.052x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.1 | 665.2 | 686.4 | 8.0 | 0.983x | 18.952x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.9 | 670.9 | 694.9 | 7.9 | 1.000x | 19.287x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.4 | 66.0 | 0.2 | 0.097x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 66.0 | 0.1 | 0.097x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.4 | 82.3 | 89.7 | 2.8 | 0.122x | 1.256x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.9 | 664.4 | 691.4 | 9.9 | 1.000x | 10.285x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.6 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.052x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.1 | 663.7 | 683.5 | 8.5 | 0.981x | 18.941x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.2 | 670.4 | 697.5 | 9.0 | 1.000x | 19.315x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 65.7 | 0.1 | 0.097x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.097x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.5 | 81.9 | 87.1 | 1.9 | 0.122x | 1.256x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.5 | 666.1 | 691.6 | 8.5 | 1.000x | 10.305x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.9 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.055x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.2 | 522.8 | 542.2 | 6.7 | 0.992x | 18.174x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.4 | 537.1 | 546.1 | 3.4 | 1.000x | 18.317x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.6 | 0.1 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 51.8 | 0.1 | 0.097x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.0 | 76.7 | 84.8 | 3.1 | 0.144x | 1.496x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 534.4 | 529.4 | 549.7 | 7.2 | 1.000x | 10.372x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 33.8 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.0 | 0.1 | 0.052x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 650.4 | 645.3 | 663.3 | 6.9 | 0.994x | 19.249x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 654.3 | 652.0 | 665.4 | 5.0 | 1.000x | 19.364x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.1 | 63.0 | 0.3 | 0.096x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.0 | 0.096x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.0 | 80.7 | 88.9 | 3.2 | 0.124x | 1.295x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.8 | 640.4 | 671.3 | 10.0 | 1.000x | 10.448x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.5 | 12.9 | 0.5 | 0.062x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.5 | 12.1 | 0.2 | 0.062x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 187.0 | 185.2 | 187.3 | 0.8 | 0.987x | 15.966x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 189.5 | 185.1 | 203.3 | 6.2 | 1.000x | 16.179x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 0.024x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 26.7 | 0.3 | 0.024x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.4 | 108.4 | 115.8 | 3.1 | 0.102x | 4.188x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.7 | 1,063.5 | 1,091.4 | 9.9 | 1.000x | 41.204x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.7 | 0.2 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.052x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.7 | 662.3 | 676.7 | 5.4 | 0.987x | 18.918x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.7 | 669.4 | 685.4 | 5.1 | 1.000x | 19.175x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 65.7 | 0.0 | 0.098x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.5 | 65.9 | 0.1 | 0.098x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.8 | 81.1 | 148.5 | 25.8 | 0.125x | 1.276x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.4 | 662.1 | 689.5 | 9.6 | 1.000x | 10.237x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.8 | 0.4 | 0.052x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 651.7 | 645.3 | 665.8 | 7.3 | 1.000x | 19.277x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.1 | 645.7 | 663.0 | 5.9 | 1.005x | 19.378x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.3 | 62.7 | 0.1 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.6 | 0.0 | 0.096x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.7 | 80.5 | 141.0 | 23.2 | 0.127x | 1.322x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 650.4 | 648.0 | 670.7 | 8.2 | 1.000x | 10.397x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.2 | 0.1 | 0.062x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.0 | 13.0 | 0.5 | 0.062x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 192.5 | 192.0 | 195.2 | 1.3 | 0.983x | 15.915x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 195.8 | 188.5 | 199.8 | 4.1 | 1.000x | 16.186x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.6 | 27.9 | 0.1 | 0.025x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 27.8 | 27.5 | 28.3 | 0.3 | 0.026x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 111.0 | 109.4 | 119.3 | 4.4 | 0.102x | 4.021x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,088.1 | 1,080.5 | 1,101.5 | 7.7 | 1.000x | 39.428x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.6 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.6 | 0.1 | 0.056x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.8 | 675.2 | 692.2 | 5.7 | 0.998x | 17.771x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.3 | 682.5 | 696.6 | 5.3 | 1.000x | 17.809x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.3 | 73.1 | 0.3 | 0.107x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.9 | 73.0 | 0.0 | 0.107x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.3 | 84.9 | 158.3 | 28.5 | 0.127x | 1.184x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 679.3 | 697.0 | 6.5 | 1.000x | 9.361x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.042x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 703.4 | 700.4 | 712.0 | 4.1 | 0.994x | 23.761x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.8 | 703.1 | 739.1 | 13.7 | 1.000x | 23.911x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.6 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 52.5 | 0.4 | 0.073x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 89.9 | 97.0 | 2.8 | 0.128x | 1.751x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 705.9 | 696.9 | 709.2 | 4.9 | 1.000x | 13.717x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.9 | 0.1 | 0.092x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 42.0 | 0.2 | 0.093x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 445.6 | 444.5 | 451.6 | 2.8 | 0.989x | 10.699x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.7 | 449.8 | 465.6 | 6.0 | 1.000x | 10.820x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.4 | 70.0 | 76.4 | 2.3 | 0.158x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 80.2 | 80.1 | 80.6 | 0.2 | 0.178x | 1.122x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 80.0 | 84.4 | 1.7 | 0.178x | 1.124x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.8 | 443.3 | 454.7 | 4.0 | 1.000x | 6.310x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.0 | 0.053x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.053x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.2 | 665.6 | 674.6 | 2.9 | 0.997x | 18.976x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.0 | 670.1 | 688.4 | 7.8 | 1.000x | 19.027x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.9 | 0.1 | 0.099x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.7 | 67.7 | 0.8 | 0.099x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.5 | 82.8 | 90.7 | 3.0 | 0.125x | 1.270x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.2 | 661.9 | 675.6 | 4.7 | 1.000x | 10.141x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.6 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.041x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 707.6 | 701.3 | 713.3 | 4.4 | 0.981x | 23.915x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.4 | 714.7 | 742.4 | 9.8 | 1.000x | 24.381x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.8 | 0.2 | 0.073x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.7 | 0.1 | 0.073x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 89.1 | 96.3 | 2.8 | 0.127x | 1.744x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.0 | 703.5 | 720.2 | 5.7 | 1.000x | 13.758x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.048x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.048x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.6 | 722.5 | 733.9 | 4.3 | 0.974x | 20.481x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 743.6 | 727.3 | 750.5 | 7.9 | 1.000x | 21.018x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 65.8 | 0.2 | 0.090x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.8 | 0.1 | 0.090x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.1 | 83.9 | 100.7 | 6.6 | 0.115x | 1.279x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 730.1 | 725.0 | 734.2 | 2.9 | 1.000x | 11.106x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.4 | 42.9 | 0.5 | 0.092x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.9 | 0.1 | 0.092x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.8 | 442.5 | 453.2 | 3.7 | 0.989x | 10.732x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.7 | 445.1 | 464.8 | 7.0 | 1.000x | 10.849x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 69.9 | 77.1 | 2.7 | 0.159x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 80.2 | 80.1 | 80.4 | 0.1 | 0.179x | 1.125x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 80.2 | 80.0 | 84.6 | 1.8 | 0.179x | 1.126x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 446.9 | 443.5 | 455.2 | 3.9 | 1.000x | 6.275x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.8 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.7 | 42.1 | 0.2 | 0.065x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 628.6 | 623.0 | 637.1 | 4.7 | 0.981x | 15.092x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.5 | 626.2 | 654.9 | 10.7 | 1.000x | 15.379x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 79.9 | 81.8 | 0.7 | 0.127x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 80.1 | 80.4 | 0.1 | 0.127x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.3 | 90.8 | 3.7 | 0.128x | 1.015x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.9 | 625.9 | 639.5 | 4.6 | 1.000x | 7.896x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.5 | 0.5 | 0.044x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.7 | 292.9 | 302.4 | 3.4 | 0.977x | 22.283x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 302.6 | 295.3 | 322.3 | 9.6 | 1.000x | 22.804x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.2 | 22.4 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 22.7 | 22.1 | 22.9 | 0.3 | 0.021x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.0 | 67.5 | 76.8 | 3.3 | 0.064x | 3.108x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.1 | 1,066.8 | 1,085.8 | 7.1 | 1.000x | 48.379x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.5 | 0.5 | 0.044x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.8 | 299.7 | 1.8 | 0.980x | 22.272x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.8 | 296.3 | 316.5 | 7.4 | 1.000x | 22.726x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 45.3 | 45.1 | 45.3 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 45.3 | 45.2 | 45.6 | 0.1 | 0.042x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.9 | 70.2 | 77.6 | 2.6 | 0.067x | 1.588x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.4 | 1,062.8 | 1,089.0 | 9.6 | 1.000x | 23.538x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.7 | 0.6 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.4 | 0.5 | 0.044x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.5 | 294.8 | 299.4 | 1.8 | 0.992x | 22.564x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.9 | 295.8 | 317.0 | 7.5 | 1.000x | 22.751x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.5 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.1 | 0.0 | 0.021x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 76.6 | 3.1 | 0.064x | 3.111x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.9 | 1,057.0 | 1,090.1 | 12.0 | 1.000x | 48.453x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.8 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.4 | 0.4 | 0.045x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.6 | 294.0 | 298.7 | 1.7 | 0.981x | 22.323x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.2 | 297.0 | 314.7 | 6.4 | 1.000x | 22.748x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 29.6 | 29.5 | 30.0 | 0.2 | 0.028x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 29.8 | 29.6 | 30.6 | 0.4 | 0.028x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.2 | 70.4 | 77.9 | 2.5 | 0.068x | 2.438x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.0 | 1,057.5 | 1,080.6 | 8.0 | 1.000x | 35.835x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 17.3 | 0.4 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.045x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.8 | 352.4 | 361.4 | 2.9 | 0.993x | 22.070x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 359.4 | 349.7 | 380.0 | 10.1 | 1.000x | 22.229x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.5 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.3 | 26.7 | 0.1 | 0.020x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.6 | 71.1 | 79.1 | 3.0 | 0.055x | 2.729x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,299.4 | 1,294.6 | 1,301.5 | 2.4 | 1.000x | 49.508x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.2 | 0.1 | 0.050x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 17.5 | 0.6 | 0.051x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 312.6 | 307.9 | 318.2 | 3.9 | 0.984x | 19.502x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.6 | 312.5 | 334.9 | 8.1 | 1.000x | 19.811x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.023x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.6 | 0.3 | 0.023x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.0 | 70.7 | 78.7 | 3.1 | 0.063x | 2.717x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,133.0 | 1,129.5 | 1,140.8 | 3.7 | 1.000x | 43.380x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.1 | 21.4 | 0.5 | 0.034x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.1 | 0.034x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 570.5 | 565.7 | 587.3 | 7.9 | 0.970x | 28.246x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 588.2 | 573.0 | 598.6 | 8.8 | 1.000x | 29.119x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.1 | 0.0 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.4 | 0.2 | 0.009x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.1 | 97.4 | 101.1 | 1.4 | 0.045x | 5.158x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,170.6 | 2,151.6 | 2,185.1 | 10.7 | 1.000x | 114.172x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.1 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 791.9 | 790.9 | 794.5 | 1.3 | 0.992x | 34.385x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 798.4 | 786.8 | 815.9 | 10.2 | 1.000x | 34.669x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 25.2 | 25.1 | 25.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 0.008x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 133.0 | 134.5 | 0.6 | 0.044x | 5.278x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,007.1 | 2,991.5 | 3,018.2 | 9.6 | 1.000x | 119.189x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.9 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 12.9 | 0.1 | 0.061x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.7 | 204.6 | 216.4 | 4.4 | 0.990x | 16.332x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.7 | 206.1 | 221.5 | 6.0 | 1.000x | 16.492x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.2 | 0.2 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.0 | 0.037x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 65.7 | 72.5 | 2.7 | 0.094x | 2.574x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.5 | 721.7 | 738.0 | 6.6 | 1.000x | 27.284x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.7 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 0.042x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 337.5 | 336.0 | 339.8 | 1.4 | 0.975x | 23.233x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 346.1 | 334.1 | 360.6 | 9.4 | 1.000x | 23.825x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.9 | 20.7 | 21.1 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 21.1 | 21.0 | 21.4 | 0.1 | 0.017x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.8 | 66.2 | 76.2 | 3.5 | 0.056x | 3.245x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,215.0 | 1,204.7 | 1,222.0 | 6.7 | 1.000x | 58.178x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.1 | 0.047x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.1 | 0.047x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 485.4 | 484.5 | 502.3 | 6.8 | 0.983x | 21.075x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 494.0 | 486.1 | 495.4 | 3.6 | 1.000x | 21.448x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.0 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.9 | 27.1 | 0.1 | 0.015x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.7 | 90.3 | 98.6 | 2.9 | 0.053x | 3.562x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,813.6 | 1,799.7 | 1,818.1 | 6.8 | 1.000x | 67.463x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.2 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.3 | 0.2 | 0.059x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 204.2 | 198.6 | 211.9 | 4.5 | 1.000x | 17.168x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.0 | 202.1 | 207.7 | 1.8 | 1.004x | 17.240x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.063x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 105.7 | 112.6 | 2.5 | 0.115x | 1.820x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 937.3 | 927.6 | 939.4 | 4.5 | 1.000x | 15.882x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.0 | 0.746x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.750x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.1 | 33.6 | 35.0 | 0.5 | 0.977x | 1.310x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.2 | 38.8 | 2.0 | 1.000x | 1.340x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 24.0 | 0.1 | 0.656x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.8 | 33.1 | 3.7 | 0.657x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.0 | 39.0 | 1.4 | 1.000x | 1.525x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.2 | 47.6 | 4.5 | 1.005x | 1.532x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 0.346x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 10.8 | 0.1 | 0.349x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 29.6 | 0.3 | 0.972x | 2.808x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 28.9 | 30.4 | 0.5 | 1.000x | 2.889x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.7 | 19.0 | 0.1 | 0.508x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.5 | 18.9 | 0.2 | 0.508x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.2 | 36.3 | 40.7 | 1.6 | 1.000x | 1.967x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 37.1 | 47.8 | 4.2 | 1.007x | 1.981x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.4 | 14.5 | 0.5 | 0.064x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 208.5 | 205.9 | 217.9 | 4.2 | 0.994x | 15.697x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 209.7 | 208.1 | 212.7 | 1.7 | 1.000x | 15.787x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 11.5 | 11.4 | 11.6 | 0.0 | 0.053x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.6 | 0.2 | 0.055x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 53.2 | 51.3 | 58.2 | 2.4 | 0.245x | 4.636x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.4 | 214.8 | 218.1 | 1.1 | 1.000x | 18.950x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.4 | 13.0 | 0.2 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.5 | 12.9 | 0.1 | 0.084x | 1.012x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 152.4 | 150.8 | 158.2 | 2.6 | 1.000x | 12.012x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.6 | 148.5 | 155.1 | 2.3 | 1.008x | 12.109x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 71.0 | 70.9 | 71.1 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 70.9 | 71.5 | 0.2 | 0.067x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 100.4 | 98.9 | 107.0 | 3.1 | 0.094x | 1.413x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.4 | 1,060.9 | 1,071.8 | 4.1 | 1.000x | 15.068x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 10.8 | 0.1 | 0.347x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.3 | 10.7 | 0.1 | 0.351x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.5 | 0.1 | 0.978x | 2.817x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 29.2 | 30.8 | 0.5 | 1.000x | 2.881x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.1 | 0.2 | 0.115x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 62.2 | 0.2 | 0.115x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 77.2 | 87.3 | 3.8 | 0.144x | 1.259x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.8 | 538.2 | 546.0 | 3.5 | 1.000x | 8.725x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 13.1 | 0.2 | 0.083x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 12.8 | 0.1 | 0.084x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 151.6 | 150.0 | 157.9 | 2.9 | 1.000x | 11.983x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 152.5 | 147.8 | 155.3 | 2.4 | 1.006x | 12.054x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.6 | 26.1 | 0.2 | 0.052x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.5 | 26.0 | 0.2 | 0.052x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 65.5 | 73.0 | 2.5 | 0.137x | 2.638x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 499.0 | 497.7 | 510.5 | 4.8 | 1.000x | 19.325x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 0.046x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 467.4 | 464.4 | 472.3 | 2.8 | 0.987x | 21.475x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.7 | 468.1 | 486.2 | 7.6 | 1.000x | 21.764x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.5 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.5 | 19.0 | 20.0 | 0.4 | 0.011x | 1.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.5 | 85.0 | 93.1 | 3.1 | 0.049x | 4.497x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.8 | 1,737.9 | 1,758.3 | 7.0 | 1.000x | 91.813x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 0.029x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.7 | 780.8 | 800.2 | 7.6 | 0.989x | 34.023x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 794.5 | 783.2 | 807.3 | 9.0 | 1.000x | 34.406x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.2 | 0.2 | 0.007x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.3 | 116.7 | 119.8 | 1.0 | 0.039x | 5.772x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,034.5 | 3,008.6 | 3,060.5 | 19.5 | 1.000x | 148.044x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.044x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.5 | 290.4 | 299.5 | 3.1 | 0.987x | 22.574x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.4 | 293.1 | 317.7 | 8.7 | 1.000x | 22.869x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 13.1 | 0.4 | 0.015x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 12.8 | 12.4 | 13.0 | 0.2 | 0.016x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.6 | 60.0 | 68.7 | 3.1 | 0.077x | 5.043x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.6 | 801.4 | 812.2 | 3.7 | 1.000x | 65.810x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.086x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.2 | 12.7 | 0.2 | 0.086x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.8 | 142.0 | 145.1 | 1.3 | 1.000x | 11.688x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 143.8 | 142.6 | 148.1 | 2.0 | 1.000x | 11.688x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.7 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.5 | 69.0 | 0.2 | 0.067x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.6 | 97.2 | 105.6 | 3.1 | 0.096x | 1.437x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,019.9 | 1,039.8 | 7.3 | 1.000x | 15.034x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 0.048x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.6 | 0.0 | 0.048x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.0 | 298.6 | 301.4 | 1.1 | 0.990x | 20.571x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 303.1 | 296.8 | 309.7 | 4.4 | 1.000x | 20.786x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 54.0 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 53.9 | 53.7 | 54.2 | 0.2 | 0.033x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 103.9 | 102.5 | 112.1 | 3.5 | 0.064x | 1.932x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,632.5 | 1,617.5 | 1,637.8 | 7.4 | 1.000x | 30.352x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.5 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.085x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.2 | 138.7 | 145.1 | 2.1 | 0.984x | 11.578x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 144.6 | 143.7 | 148.0 | 1.5 | 1.000x | 11.771x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.1 | 0.2 | 0.068x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 68.8 | 0.1 | 0.068x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 106.7 | 3.4 | 0.097x | 1.438x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.0 | 1,006.3 | 1,023.0 | 6.1 | 1.000x | 14.760x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.8 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.3 | 14.7 | 0.5 | 0.045x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.2 | 302.0 | 2.9 | 0.996x | 22.197x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.2 | 293.1 | 316.4 | 8.3 | 1.000x | 22.297x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 19.5 | 19.4 | 19.7 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 19.6 | 19.5 | 19.9 | 0.1 | 0.018x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.8 | 68.2 | 81.1 | 5.0 | 0.064x | 3.525x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,071.8 | 1,066.7 | 1,085.4 | 6.5 | 1.000x | 54.943x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.1 | 0.045x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.9 | 294.2 | 316.3 | 8.3 | 1.000x | 22.182x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.0 | 292.8 | 300.2 | 2.8 | 1.000x | 22.188x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.1 | 14.5 | 0.2 | 0.014x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 14.9 | 0.1 | 0.014x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 67.2 | 74.9 | 2.9 | 0.063x | 4.676x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,056.4 | 1,080.2 | 7.8 | 1.000x | 73.992x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 0.045x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.5 | 291.6 | 302.0 | 3.5 | 0.994x | 22.209x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.3 | 294.9 | 315.0 | 7.5 | 1.000x | 22.338x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.2 | 14.0 | 14.5 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 14.6 | 0.1 | 0.014x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.3 | 67.1 | 75.4 | 3.3 | 0.063x | 4.727x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.4 | 1,057.2 | 1,078.9 | 7.5 | 1.000x | 74.991x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 0.045x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.6 | 292.6 | 297.2 | 1.8 | 0.993x | 22.104x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.6 | 295.2 | 315.8 | 7.8 | 1.000x | 22.255x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 14.2 | 14.1 | 14.4 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.7 | 0.1 | 0.013x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 66.9 | 77.0 | 3.9 | 0.063x | 4.758x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,048.7 | 1,075.0 | 10.3 | 1.000x | 75.287x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.045x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 293.6 | 302.6 | 3.4 | 0.985x | 22.106x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 294.7 | 310.8 | 5.8 | 1.000x | 22.441x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.4 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 16.7 | 16.4 | 16.9 | 0.2 | 0.016x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.4 | 67.2 | 77.1 | 3.8 | 0.063x | 4.135x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.0 | 1,056.1 | 1,075.7 | 6.7 | 1.000x | 65.248x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,807.6 | 9,803.5 | 9,928.5 | 48.1 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,855.2 | 9,806.5 | 12,656.5 | 1,195.4 | 1.000x | 1.005x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,061.9 | 19,059.9 | 19,072.6 | 4.7 | 1.934x | 1.944x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,073.6 | 19,067.2 | 19,077.9 | 3.5 | 1.935x | 1.945x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,458.1 | 7,457.5 | 7,469.5 | 4.5 | 0.103x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,465.1 | 7,460.3 | 7,468.6 | 3.2 | 0.103x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,378.4 | 72,269.0 | 74,027.3 | 754.0 | 0.996x | 9.705x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,689.9 | 72,672.9 | 73,928.7 | 484.2 | 1.000x | 9.746x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,545.8 | 9,545.2 | 9,548.7 | 1.2 | 0.060x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,548.6 | 9,546.6 | 9,554.0 | 2.5 | 0.060x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 158,736.5 | 158,161.5 | 159,418.1 | 434.7 | 1.000x | 16.629x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,127.1 | 157,791.5 | 162,247.5 | 1,654.8 | 1.002x | 16.670x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,415.1 | 9,403.1 | 9,437.9 | 11.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,419.3 | 9,412.3 | 9,426.6 | 4.7 | 1.000x | 1.000x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,037.6 | 19,036.1 | 19,042.8 | 2.8 | 2.021x | 2.022x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,051.1 | 19,044.7 | 19,054.8 | 4.0 | 2.023x | 2.023x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,734.9 | 3,734.2 | 3,735.8 | 0.6 | 0.084x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,736.2 | 3,734.1 | 3,739.7 | 1.8 | 0.084x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,486.7 | 44,477.2 | 45,695.2 | 497.0 | 1.000x | 11.911x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,565.1 | 44,446.3 | 44,670.6 | 90.2 | 1.002x | 11.932x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.050x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.050x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.3 | 320.1 | 328.3 | 2.9 | 0.989x | 19.930x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 325.0 | 317.0 | 333.0 | 5.1 | 1.000x | 20.156x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,785.1 | 4,784.8 | 4,786.0 | 0.5 | 0.043x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,786.9 | 4,785.7 | 4,788.4 | 1.1 | 0.043x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109,919.6 | 108,684.5 | 110,183.5 | 547.2 | 0.997x | 22.971x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,242.2 | 109,781.6 | 110,939.9 | 446.6 | 1.000x | 23.039x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,642.3 | 7,642.0 | 7,643.9 | 0.8 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,648.6 | 7,645.3 | 7,656.5 | 3.8 | 0.080x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94,708.6 | 94,592.0 | 95,802.6 | 542.7 | 0.994x | 12.393x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,310.1 | 94,721.9 | 95,982.9 | 470.3 | 1.000x | 12.471x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.6 | 0.1 | 0.357x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.2 | 0.3 | 0.359x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 29.0 | 29.8 | 0.4 | 0.991x | 2.774x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.7 | 0.2 | 1.000x | 2.800x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.4 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.3 | 21.5 | 0.1 | 0.038x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.0 | 61.4 | 71.4 | 3.8 | 0.110x | 2.916x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.1 | 553.4 | 580.2 | 8.8 | 1.000x | 26.427x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.7 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.1 | 0.1 | 0.052x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.3 | 647.6 | 667.6 | 7.8 | 1.000x | 19.391x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 659.4 | 653.3 | 669.0 | 5.5 | 1.009x | 19.574x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.6 | 0.0 | 0.094x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 62.8 | 0.3 | 0.094x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 79.1 | 88.9 | 3.5 | 0.125x | 1.333x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 664.9 | 659.9 | 667.4 | 2.5 | 1.000x | 10.628x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.051x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.8 | 635.0 | 644.5 | 3.2 | 0.999x | 19.755x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638.2 | 630.8 | 645.8 | 6.5 | 1.000x | 19.766x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.8 | 0.2 | 0.090x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 58.8 | 0.2 | 0.091x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.8 | 79.9 | 88.9 | 4.1 | 0.125x | 1.387x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 644.7 | 635.0 | 647.7 | 5.2 | 1.000x | 11.064x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.0 | 0.040x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.1 | 0.041x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.2 | 410.3 | 424.4 | 4.9 | 1.000x | 24.707x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 418.6 | 412.3 | 422.2 | 3.2 | 1.011x | 24.967x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 23.0 | 23.0 | 23.2 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 23.1 | 23.0 | 23.5 | 0.2 | 0.056x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 59.0 | 56.3 | 67.5 | 3.9 | 0.144x | 2.562x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 410.9 | 406.6 | 415.6 | 3.2 | 1.000x | 17.838x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 14.2 | 0.7 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.0 | 12.5 | 13.5 | 0.4 | 0.062x | 1.012x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 210.6 | 205.8 | 212.6 | 2.4 | 1.000x | 16.407x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212.7 | 206.5 | 223.5 | 6.0 | 1.010x | 16.570x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 27.0 | 27.2 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 27.5 | 27.1 | 27.6 | 0.2 | 0.038x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.5 | 68.3 | 73.8 | 2.0 | 0.096x | 2.572x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.0 | 711.0 | 737.7 | 9.4 | 1.000x | 26.772x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.9 | 27.9 | 28.1 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 28.0 | 28.3 | 0.1 | 0.052x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 540.6 | 533.2 | 545.8 | 4.6 | 0.999x | 19.344x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.0 | 537.4 | 547.8 | 3.8 | 1.000x | 19.358x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 48.5 | 0.1 | 0.089x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.4 | 48.7 | 0.1 | 0.089x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 74.6 | 86.1 | 4.2 | 0.143x | 1.604x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.4 | 538.1 | 543.6 | 2.1 | 1.000x | 11.201x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.5 | 55.8 | 0.1 | 0.100x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.4 | 55.9 | 0.2 | 0.100x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 557.3 | 555.8 | 565.7 | 3.6 | 1.000x | 10.031x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.5 | 550.1 | 568.4 | 7.0 | 1.008x | 10.107x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.4 | 88.4 | 97.4 | 3.1 | 0.162x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 109.7 | 0.0 | 0.196x | 1.212x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 109.9 | 109.5 | 110.1 | 0.2 | 0.197x | 1.215x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 558.0 | 554.1 | 566.5 | 4.2 | 1.000x | 6.170x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.6 | 43.4 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 43.1 | 0.1 | 0.035x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,212.7 | 1,178.7 | 1,220.6 | 17.0 | 1.000x | 28.358x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,224.0 | 1,180.2 | 1,271.5 | 29.8 | 1.009x | 28.621x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 89.4 | 89.1 | 89.5 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 89.6 | 89.2 | 89.6 | 0.2 | 0.052x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.8 | 169.2 | 178.6 | 3.2 | 0.099x | 1.923x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,731.7 | 1,725.9 | 1,740.8 | 5.6 | 1.000x | 19.374x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 14.6 | 0.5 | 0.045x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.9 | 296.5 | 305.7 | 3.5 | 1.000x | 22.302x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 301.0 | 296.9 | 305.1 | 2.9 | 1.014x | 22.607x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 20.4 | 20.3 | 20.5 | 0.0 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.3 | 20.9 | 0.2 | 0.019x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 68.0 | 76.6 | 3.2 | 0.064x | 3.361x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.6 | 1,068.6 | 1,092.8 | 8.3 | 1.000x | 52.807x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.5 | 0.5 | 0.045x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 14.8 | 0.6 | 0.045x | 1.008x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.9 | 295.6 | 302.4 | 2.5 | 1.000x | 22.446x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.1 | 296.0 | 304.2 | 3.4 | 1.014x | 22.761x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.7 | 26.8 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.6 | 27.1 | 0.2 | 0.025x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.2 | 70.7 | 77.7 | 2.5 | 0.068x | 2.743x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.1 | 1,055.2 | 1,080.5 | 9.1 | 1.000x | 40.345x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.6 | 0.1 | 0.051x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 631.8 | 625.6 | 638.4 | 4.4 | 0.993x | 19.553x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.4 | 628.8 | 639.5 | 3.8 | 1.000x | 19.698x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 62.8 | 1.8 | 0.091x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 97.4 | 4.0 | 0.136x | 1.500x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 643.9 | 636.7 | 657.9 | 7.5 | 1.000x | 11.046x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.6 | 624.8 | 641.1 | 5.9 | 0.996x | 19.639x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.2 | 625.6 | 638.0 | 4.4 | 1.000x | 19.718x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.1 | 59.9 | 0.7 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 62.7 | 1.7 | 0.091x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 93.4 | 2.4 | 0.136x | 1.500x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 641.6 | 634.3 | 653.9 | 6.7 | 1.000x | 11.014x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.2 | 32.5 | 0.1 | 0.046x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 696.2 | 690.0 | 707.4 | 6.4 | 0.998x | 21.568x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 697.7 | 690.4 | 704.1 | 4.9 | 1.000x | 21.617x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.2 | 58.1 | 59.2 | 0.4 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 60.8 | 1.0 | 0.084x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.8 | 88.3 | 93.5 | 2.0 | 0.127x | 1.524x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 699.8 | 695.3 | 711.8 | 7.1 | 1.000x | 12.018x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.5 | 0.1 | 0.045x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 721.4 | 714.8 | 732.3 | 5.8 | 0.996x | 22.347x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.1 | 711.0 | 728.9 | 6.6 | 1.000x | 22.428x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.7 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 58.3 | 60.5 | 0.9 | 0.081x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 82.9 | 93.3 | 4.9 | 0.115x | 1.429x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 725.5 | 723.7 | 726.3 | 1.0 | 1.000x | 12.430x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.5 | 0.1 | 0.045x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 723.2 | 715.7 | 729.5 | 5.0 | 0.999x | 22.371x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.0 | 714.6 | 730.6 | 5.8 | 1.000x | 22.395x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.7 | 0.2 | 0.081x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 58.1 | 60.7 | 1.0 | 0.081x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 94.3 | 4.6 | 0.115x | 1.425x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.4 | 721.7 | 726.2 | 1.7 | 1.000x | 12.385x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.046x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.8 | 345.6 | 364.4 | 6.6 | 1.000x | 21.822x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 352.6 | 349.8 | 358.5 | 3.0 | 1.005x | 21.935x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 26.5 | 26.3 | 27.9 | 0.6 | 0.021x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.7 | 70.9 | 79.0 | 3.0 | 0.056x | 2.735x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,280.1 | 1,263.2 | 1,288.8 | 8.8 | 1.000x | 48.829x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.7 | 11.6 | 0.3 | 0.374x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.0 | 10.8 | 11.6 | 0.3 | 0.376x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 29.1 | 0.1 | 0.991x | 2.651x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.3 | 0.0 | 1.000x | 2.676x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 4.8 | 4.4 | 5.2 | 0.3 | 0.158x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.184x | 1.166x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.2 | 31.0 | 0.4 | 1.000x | 6.322x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.5 | 34.9 | 48.5 | 4.8 | 1.230x | 7.778x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.6 | 0.1 | 0.354x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.6 | 11.2 | 0.2 | 0.354x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 28.9 | 29.8 | 0.3 | 0.987x | 2.789x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.0 | 29.6 | 30.2 | 0.2 | 1.000x | 2.827x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 5.3 | 5.0 | 5.7 | 0.2 | 0.172x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 6.5 | 6.5 | 6.5 | 0.0 | 0.209x | 1.220x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 35.1 | 1.6 | 1.000x | 5.828x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.8 | 36.4 | 49.7 | 4.9 | 1.250x | 7.286x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.3 | 0.2 | 0.308x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 13.0 | 0.4 | 0.316x | 1.026x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.3 | 35.2 | 40.6 | 1.9 | 0.939x | 3.045x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 38.6 | 35.7 | 41.6 | 2.4 | 1.000x | 3.242x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.0 | 36.6 | 40.7 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.4 | 37.0 | 50.0 | 5.1 | 1.038x | 1.038x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.4 | 73.5 | 0.0 | 1.986x | 1.986x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 73.5 | 72.9 | 74.0 | 0.4 | 1.988x | 1.988x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.2 | 20.7 | 0.6 | 0.508x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.4 | 0.1 | 0.509x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.1 | 35.2 | 0.4 | 0.915x | 1.803x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.8 | 35.2 | 40.1 | 1.8 | 1.000x | 1.969x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 16.2 | 16.1 | 16.3 | 0.1 | 0.446x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 16.2 | 16.1 | 16.5 | 0.1 | 0.447x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.7 | 40.3 | 1.7 | 1.000x | 2.244x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.1 | 49.7 | 5.2 | 1.006x | 2.258x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,576,575.8 | 3,574,991.7 | 3,589,725.4 | 6,003.4 | 0.125x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,582,953.6 | 3,579,330.7 | 3,589,511.9 | 3,391.8 | 0.125x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,700,507.0 | 3,619,299.0 | 3,704,156.4 | 32,418.7 | 0.129x | 1.035x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,638,016.7 | 28,601,379.1 | 29,677,306.8 | 409,825.4 | 1.000x | 8.007x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,983.0 | 17,950.2 | 18,048.6 | 35.9 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 1,892,471.5 | 1,887,969.1 | 1,895,532.6 | 2,576.6 | 105.236x | 105.236x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 1,893,311.9 | 1,892,911.3 | 1,894,652.5 | 723.5 | 105.283x | 105.283x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,559,712.1 | 2,540,969.5 | 2,565,705.2 | 11,254.9 | 142.340x | 142.340x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,933.2 | 17,893.8 | 18,022.1 | 43.7 | 1.000x | 1.000x |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 1,874,805.3 | 1,873,931.1 | 1,876,886.5 | 1,007.3 | 104.544x | 104.544x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 1,875,730.8 | 1,873,708.4 | 1,878,721.4 | 1,667.7 | 104.596x | 104.596x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,818,428.0 | 2,816,233.6 | 2,822,301.8 | 2,573.3 | 157.163x | 157.163x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,126,954.3 | 3,120,311.9 | 3,134,130.2 | 5,310.4 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,137,862.7 | 3,136,574.5 | 3,142,649.2 | 2,109.9 | 0.033x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,966,791.7 | 5,961,199.2 | 6,000,178.1 | 14,414.3 | 0.064x | 1.908x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 93,901,018.6 | 93,759,164.2 | 99,292,858.2 | 2,164,943.1 | 1.000x | 30.030x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,971.3 | 17,957.5 | 17,984.6 | 10.9 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,093,057.1 | 3,084,898.9 | 3,098,371.3 | 5,107.4 | 172.111x | 172.111x |
| 3 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,101,972.4 | 3,087,678.2 | 3,106,436.5 | 7,655.0 | 172.607x | 172.607x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,159,050.0 | 3,155,013.8 | 3,180,387.1 | 9,183.7 | 175.783x | 175.783x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_1989c62_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 164,915,127.0 | 156,981,861.0 | 182,641,919.0 | 8,625,738.7 | 5 | 43,344 | 82,314 | 13,620 | 0.052 | compiled=5 | 21,246,982.0 | 147,074,564.0 | 190,671.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 173,581,817.0 | 166,130,205.0 | 183,948,586.0 | 6,720,513.4 | 5 | 47,584 | 94,525 | 15,536 | 0.039 | compiled=5 | 12,067,839.0 | 161,425,557.0 | 109,531.0 |
| `factored` | `plain` | `pcrec_288d505_auto-caps-simdna` | 158,778,616.0 | 158,398,844.0 | 179,484,234.0 | 8,701,313.4 | 5 | 47,728 | 82,424 | 13,730 | 0.055 (max is trial 1) | compiled=5 | 9,906,122.0 | 148,792,303.0 | 112,661.0 |
| `factored` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 178,193,008.0 | 171,097,333.0 | 180,329,800.0 | 3,444,464.3 | 5 | 47,872 | 94,635 | 15,646 | 0.019 | compiled=5 | 12,137,206.0 | 165,947,621.0 | 103,491.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 138,937,769.0 | 130,915,322.0 | 149,545,609.0 | 6,514,661.1 | 5 | 22,832 | 17,965 | 12,968 | 0.047 | compiled=5 | 1,809,261.0 | 137,082,487.0 | 189,661.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 149,982,771.0 | 145,127,543.0 | 155,552,133.0 | 3,491,085.5 | 5 | 22,968 | 20,308 | 14,985 | 0.023 | compiled=5 | 1,692,279.0 | 148,114,051.0 | 96,651.0 |
| `floor` | `plain` | `pcrec_288d505_auto-caps-simdna` | 140,190,810.0 | 135,797,732.0 | 147,058,772.0 | 4,141,120.9 | 5 | 27,216 | 18,075 | 13,078 | 0.030 | compiled=5 | 1,658,620.0 | 138,230,527.0 | 105,440.0 |
| `floor` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 155,838,228.0 | 143,964,803.0 | 157,904,771.0 | 5,742,878.0 | 5 | 27,352 | 20,418 | 15,095 | 0.037 | compiled=5 | 1,693,591.0 | 154,040,776.0 | 107,020.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 156,626,339.0 | 152,463,315.0 | 162,571,233.0 | 3,827,137.0 | 5 | 43,304 | 81,907 | 13,380 | 0.024 | compiled=5 | 9,352,623.0 | 147,153,485.0 | 107,731.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 169,897,296.0 | 158,601,931.0 | 180,453,986.0 | 7,594,084.9 | 5 | 47,544 | 94,118 | 15,296 | 0.045 (max is trial 1) | compiled=5 | 11,432,616.0 | 150,413,164.0 | 196,642.0 |
| `orig` | `plain` | `pcrec_288d505_auto-caps-simdna` | 155,010,061.0 | 143,823,141.0 | 173,840,701.0 | 9,875,501.6 | 5 | 47,688 | 82,017 | 13,490 | 0.064 | compiled=5 | 9,649,731.0 | 145,232,460.0 | 111,091.0 |
| `orig` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 178,467,200.0 | 164,943,363.0 | 181,739,570.0 | 7,158,180.3 | 5 | 47,832 | 94,228 | 15,406 | 0.040 (max is trial 1) | compiled=5 | 11,517,913.0 | 158,921,187.0 | 105,001.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 70,150.0 | 64,051.0 | 167,201.0 | 39,050.5 | 5 | 951 | 0.557 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,351.0 | 5,120.0 | 51,820.0 | 18,281.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 59,880.0 | 54,300.0 | 175,181.0 | 46,340.9 | 5 | 1,609 | 0.774 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,450.0 | 13,070.0 | 50,681.0 | 14,528.5 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,470.0 | 6,041.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 33,290.0 | 30,010.0 | 102,420.0 | 27,822.1 | 5 | 1,609 | 0.836 (max is trial 1) | compiled=5 |

