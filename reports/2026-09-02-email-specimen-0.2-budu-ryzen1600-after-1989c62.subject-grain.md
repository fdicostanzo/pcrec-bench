# pcrec-bench report

reporter: v12 (2026-09-02)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-09-03T00:00:00Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_1989c62_auto-caps-simdna, testee=pcrec_1989c62_auto-nocaps-simdna, testee=pcrec_1989c62_vm-caps-simdna, testee=pcrec_1989c62_vm-in-caps-simdna, testee=pcrec_96e44c2_auto-caps-simdna, testee=pcrec_96e44c2_auto-nocaps-simdna, testee=pcrec_96e44c2_vm-caps-simdna, testee=pcrec_96e44c2_vm-in-caps-simdna
- record source: store/index.tsv (17 record(s) matching this query)
- records included: 10
- worst other-core busy: 8.2% (`pcrec_1989c62_auto-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-caps-simdna/email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-nocaps-simdna/email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-in-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-caps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-nocaps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-in-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z.jsonl) — agreement: n/a (v1.3)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3, 1.4
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 4 record(s); v1.4 X13 (pre-flight + trial agreement) on 6 record(s) — MIXED: every ranking row's status cell carries the record's schema version (`measured@1.3` / `measured@1.4`)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.4 | 32.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.6 | 0.1 | 0.037x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.1 | 0.3 | 0.040x | 1.069x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.040x | 1.072x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 147.2 | 146.5 | 149.6 | 1.2 | 0.169x | 4.537x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.2 | 147.3 | 148.6 | 0.5 | 0.170x | 4.566x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 150.7 | 150.3 | 152.6 | 0.9 | 0.173x | 4.645x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 152.6 | 151.6 | 153.3 | 0.7 | 0.175x | 4.703x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 863.9 | 857.9 | 884.2 | 9.0 | 0.991x | 26.623x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 871.6 | 865.8 | 882.8 | 6.0 | 1.000x | 26.862x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.7 | 58.5 | 58.9 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 59.0 | 58.5 | 59.3 | 0.3 | 0.068x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.8 | 62.2 | 64.5 | 0.8 | 0.073x | 1.069x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.8 | 62.5 | 63.2 | 0.3 | 0.073x | 1.069x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 148.2 | 147.9 | 148.5 | 0.2 | 0.172x | 2.524x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 148.2 | 147.6 | 148.6 | 0.4 | 0.172x | 2.525x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 148.4 | 147.8 | 151.5 | 1.3 | 0.172x | 2.528x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 151.9 | 151.5 | 152.3 | 0.3 | 0.176x | 2.588x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 154.1 | 153.9 | 154.6 | 0.3 | 0.178x | 2.626x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 863.8 | 854.6 | 872.1 | 6.6 | 1.000x | 14.714x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.1 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 40.0 | 40.0 | 40.4 | 0.1 | 0.033x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.0 | 42.8 | 43.8 | 0.4 | 0.035x | 1.076x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.0 | 42.9 | 44.3 | 0.5 | 0.035x | 1.079x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 198.7 | 197.4 | 199.3 | 0.7 | 0.163x | 4.978x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 199.3 | 198.7 | 199.4 | 0.3 | 0.163x | 4.994x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 199.6 | 199.3 | 229.9 | 11.8 | 0.163x | 5.000x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 200.3 | 199.2 | 202.4 | 1.1 | 0.164x | 5.020x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,217.2 | 1,214.6 | 1,229.8 | 5.5 | 0.997x | 30.498x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,220.7 | 1,210.7 | 1,258.3 | 17.5 | 1.000x | 30.585x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 77.6 | 77.5 | 78.1 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 77.8 | 77.7 | 82.5 | 1.9 | 0.064x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 80.4 | 80.2 | 80.8 | 0.2 | 0.066x | 1.035x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 80.7 | 80.0 | 81.1 | 0.4 | 0.066x | 1.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 175.4 | 175.0 | 176.0 | 0.3 | 0.144x | 2.259x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 201.1 | 200.1 | 202.1 | 0.7 | 0.165x | 2.591x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 205.0 | 204.8 | 206.3 | 0.6 | 0.168x | 2.641x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 207.1 | 206.6 | 209.4 | 1.0 | 0.170x | 2.668x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 211.9 | 211.8 | 214.7 | 1.1 | 0.174x | 2.730x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,219.9 | 1,219.7 | 1,231.7 | 5.8 | 1.000x | 15.716x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.024x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 0.024x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.6 | 20.4 | 22.1 | 0.6 | 0.028x | 1.130x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.6 | 20.6 | 20.9 | 0.1 | 0.028x | 1.131x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 104.3 | 104.3 | 104.5 | 0.1 | 0.140x | 5.717x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 104.8 | 104.5 | 105.7 | 0.5 | 0.140x | 5.745x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 105.0 | 104.8 | 105.5 | 0.2 | 0.140x | 5.753x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 105.4 | 105.1 | 117.1 | 4.6 | 0.141x | 5.775x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 747.6 | 744.6 | 764.3 | 7.0 | 1.000x | 40.977x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 752.1 | 743.8 | 753.1 | 3.9 | 1.006x | 41.223x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.0 | 26.0 | 26.0 | 0.0 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.035x | 1.016x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.2 | 28.8 | 0.2 | 0.038x | 1.098x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 0.038x | 1.102x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 101.9 | 101.8 | 102.2 | 0.1 | 0.135x | 3.919x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 105.4 | 105.4 | 105.6 | 0.1 | 0.140x | 4.055x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 105.5 | 105.5 | 106.3 | 0.3 | 0.140x | 4.059x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 106.9 | 105.2 | 107.7 | 1.0 | 0.142x | 4.110x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 123.3 | 121.4 | 124.5 | 1.2 | 0.164x | 4.741x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 752.1 | 747.7 | 765.2 | 5.9 | 1.000x | 28.927x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.3 | 43.1 | 44.4 | 0.4 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.4 | 43.3 | 43.4 | 0.0 | 0.033x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.5 | 46.3 | 47.8 | 0.5 | 0.035x | 1.075x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 46.6 | 46.2 | 47.3 | 0.4 | 0.035x | 1.076x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 210.3 | 209.4 | 210.9 | 0.5 | 0.158x | 4.855x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 211.4 | 211.2 | 215.4 | 1.6 | 0.159x | 4.881x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 212.4 | 211.9 | 214.5 | 0.9 | 0.160x | 4.905x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 213.0 | 212.3 | 216.2 | 1.7 | 0.160x | 4.918x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,327.5 | 1,316.0 | 1,336.1 | 6.9 | 1.000x | 30.649x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,335.8 | 1,327.9 | 1,342.2 | 5.0 | 1.006x | 30.842x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 86.5 | 86.4 | 87.1 | 0.3 | 0.066x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 86.6 | 86.1 | 87.0 | 0.4 | 0.066x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 87.5 | 87.5 | 88.1 | 0.3 | 0.066x | 1.012x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 87.6 | 87.0 | 88.6 | 0.5 | 0.066x | 1.013x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 184.4 | 183.4 | 185.1 | 0.6 | 0.140x | 2.133x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 220.5 | 219.6 | 220.9 | 0.5 | 0.167x | 2.549x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 221.4 | 220.9 | 222.5 | 0.5 | 0.168x | 2.559x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 224.4 | 221.4 | 226.0 | 1.5 | 0.170x | 2.595x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 224.8 | 224.7 | 227.2 | 1.0 | 0.170x | 2.599x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,318.5 | 1,309.2 | 1,328.7 | 6.7 | 1.000x | 15.244x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 61.1 | 60.8 | 61.4 | 0.2 | 0.069x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 61.3 | 61.1 | 61.6 | 0.2 | 0.070x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 65.0 | 64.8 | 65.4 | 0.2 | 0.074x | 1.065x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 65.1 | 64.9 | 66.1 | 0.4 | 0.074x | 1.066x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 162.1 | 161.7 | 162.7 | 0.4 | 0.184x | 2.655x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 163.0 | 162.7 | 163.4 | 0.3 | 0.185x | 2.670x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 164.0 | 163.7 | 164.2 | 0.2 | 0.186x | 2.686x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 166.2 | 165.6 | 166.9 | 0.4 | 0.189x | 2.721x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 876.9 | 867.2 | 884.9 | 6.8 | 0.997x | 14.360x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 879.8 | 865.0 | 881.1 | 6.1 | 1.000x | 14.409x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 120.1 | 119.9 | 122.0 | 0.8 | 0.137x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 120.7 | 120.1 | 121.0 | 0.3 | 0.138x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 123.8 | 123.4 | 126.5 | 1.1 | 0.141x | 1.030x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 123.9 | 123.5 | 124.0 | 0.2 | 0.141x | 1.031x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 167.2 | 166.1 | 169.0 | 1.0 | 0.191x | 1.392x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 167.6 | 167.4 | 168.1 | 0.3 | 0.191x | 1.395x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 167.7 | 167.4 | 168.4 | 0.4 | 0.191x | 1.396x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 167.7 | 166.8 | 168.4 | 0.5 | 0.191x | 1.396x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 171.5 | 169.8 | 210.1 | 15.6 | 0.196x | 1.428x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 877.0 | 872.0 | 886.0 | 5.8 | 1.000x | 7.300x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.3 | 18.1 | 18.3 | 0.1 | 0.024x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.5 | 20.5 | 20.7 | 0.1 | 0.027x | 1.128x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.6 | 20.4 | 20.9 | 0.1 | 0.028x | 1.134x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 104.3 | 104.2 | 104.4 | 0.1 | 0.139x | 5.728x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 104.5 | 104.5 | 105.1 | 0.3 | 0.139x | 5.742x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 104.8 | 104.8 | 107.6 | 1.1 | 0.140x | 5.758x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 105.3 | 105.1 | 106.7 | 0.6 | 0.140x | 5.786x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 750.0 | 731.8 | 758.4 | 8.9 | 1.000x | 41.195x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 750.8 | 741.8 | 754.9 | 4.6 | 1.001x | 41.242x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 27.4 | 0.5 | 0.035x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.2 | 28.7 | 0.2 | 0.038x | 1.093x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 28.7 | 28.2 | 28.7 | 0.2 | 0.038x | 1.099x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 102.0 | 101.8 | 102.1 | 0.1 | 0.135x | 3.911x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 105.4 | 105.4 | 106.9 | 0.7 | 0.140x | 4.040x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 105.5 | 105.4 | 108.2 | 1.1 | 0.140x | 4.045x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 106.9 | 104.9 | 109.0 | 1.4 | 0.142x | 4.098x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 123.5 | 122.5 | 124.5 | 0.8 | 0.164x | 4.736x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 753.3 | 745.7 | 754.4 | 3.5 | 1.000x | 28.876x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.9 | 30.9 | 30.9 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.0 | 0.023x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.0 | 32.8 | 33.4 | 0.2 | 0.025x | 1.068x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.1 | 32.9 | 33.2 | 0.1 | 0.025x | 1.072x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 226.3 | 225.8 | 230.4 | 1.7 | 0.169x | 7.320x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 227.5 | 227.2 | 228.9 | 0.6 | 0.169x | 7.360x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 228.5 | 228.0 | 228.6 | 0.2 | 0.170x | 7.391x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 231.4 | 230.9 | 231.4 | 0.3 | 0.172x | 7.486x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,342.6 | 1,332.9 | 1,348.7 | 5.3 | 1.000x | 43.432x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,351.8 | 1,348.6 | 1,360.8 | 4.9 | 1.007x | 43.731x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 55.8 | 55.7 | 56.1 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 55.9 | 55.5 | 56.4 | 0.3 | 0.042x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 59.2 | 59.2 | 59.3 | 0.0 | 0.044x | 1.062x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 59.3 | 59.3 | 60.2 | 0.3 | 0.044x | 1.064x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 164.1 | 163.7 | 171.5 | 2.9 | 0.122x | 2.942x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 225.6 | 225.0 | 228.5 | 1.3 | 0.168x | 4.046x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 228.0 | 227.6 | 228.9 | 0.5 | 0.170x | 4.087x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 229.2 | 227.8 | 230.7 | 1.0 | 0.171x | 4.110x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 229.9 | 228.3 | 232.4 | 1.3 | 0.171x | 4.122x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,341.0 | 1,339.3 | 1,349.0 | 3.4 | 1.000x | 24.042x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 46.8 | 46.5 | 47.2 | 0.2 | 0.048x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.9 | 46.5 | 46.9 | 0.2 | 0.048x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.5 | 0.2 | 0.052x | 1.074x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 50.4 | 50.3 | 50.7 | 0.2 | 0.052x | 1.077x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 167.3 | 167.1 | 167.6 | 0.2 | 0.172x | 3.578x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 167.8 | 166.8 | 176.5 | 3.6 | 0.173x | 3.589x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 168.1 | 167.4 | 168.4 | 0.4 | 0.173x | 3.594x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 169.9 | 169.7 | 175.7 | 2.3 | 0.175x | 3.633x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 970.7 | 964.5 | 972.0 | 2.8 | 0.998x | 20.758x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 972.6 | 967.5 | 977.1 | 3.3 | 1.000x | 20.800x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 92.0 | 91.9 | 92.2 | 0.1 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 92.2 | 91.9 | 93.0 | 0.4 | 0.095x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 94.2 | 94.0 | 95.0 | 0.4 | 0.097x | 1.023x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 94.5 | 94.2 | 95.3 | 0.4 | 0.097x | 1.027x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 172.3 | 171.8 | 173.7 | 0.7 | 0.177x | 1.872x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 173.5 | 172.9 | 177.4 | 1.8 | 0.178x | 1.885x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 173.7 | 171.3 | 180.9 | 3.3 | 0.179x | 1.888x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 173.9 | 173.3 | 175.2 | 0.6 | 0.179x | 1.889x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 177.3 | 176.5 | 178.1 | 0.5 | 0.182x | 1.926x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 972.5 | 959.3 | 979.6 | 6.7 | 1.000x | 10.566x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.6 | 36.6 | 37.8 | 0.5 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.7 | 0.0 | 0.042x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.3 | 0.1 | 0.046x | 1.072x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.5 | 0.1 | 0.046x | 1.073x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 152.7 | 151.9 | 153.2 | 0.4 | 0.177x | 4.169x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 153.6 | 153.3 | 154.4 | 0.4 | 0.178x | 4.193x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 155.6 | 155.5 | 156.4 | 0.3 | 0.180x | 4.248x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 158.2 | 156.9 | 158.5 | 0.7 | 0.183x | 4.319x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 859.2 | 854.5 | 872.4 | 6.0 | 0.996x | 23.455x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 862.5 | 848.8 | 881.0 | 10.3 | 1.000x | 23.547x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 69.6 | 69.6 | 69.7 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 69.8 | 69.7 | 70.6 | 0.4 | 0.081x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 73.4 | 73.3 | 73.6 | 0.1 | 0.085x | 1.055x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 73.6 | 73.4 | 73.6 | 0.1 | 0.086x | 1.057x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 149.5 | 148.8 | 150.9 | 0.8 | 0.174x | 2.148x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 150.1 | 150.0 | 150.7 | 0.2 | 0.175x | 2.157x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 150.5 | 150.2 | 151.4 | 0.4 | 0.175x | 2.162x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 153.5 | 152.5 | 153.8 | 0.6 | 0.179x | 2.205x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 157.8 | 157.7 | 158.0 | 0.1 | 0.184x | 2.266x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 859.4 | 853.9 | 863.0 | 3.3 | 1.000x | 12.344x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.034x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.2 | 0.037x | 1.069x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.0 | 0.2 | 0.037x | 1.072x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 144.1 | 144.0 | 144.6 | 0.2 | 0.168x | 4.876x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.5 | 145.0 | 146.6 | 0.6 | 0.169x | 4.923x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.4 | 147.0 | 157.2 | 4.0 | 0.171x | 4.989x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.5 | 148.8 | 150.2 | 0.5 | 0.174x | 5.059x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 855.1 | 854.3 | 868.6 | 5.6 | 0.995x | 28.942x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 859.7 | 847.1 | 873.7 | 9.9 | 1.000x | 29.097x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.6 | 51.5 | 51.9 | 0.1 | 0.060x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 55.8 | 55.6 | 55.8 | 0.1 | 0.065x | 1.086x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.8 | 55.8 | 56.0 | 0.1 | 0.065x | 1.086x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 146.7 | 146.3 | 146.7 | 0.2 | 0.171x | 2.854x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 146.9 | 146.1 | 148.0 | 0.6 | 0.171x | 2.859x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 147.0 | 146.4 | 147.2 | 0.3 | 0.171x | 2.862x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 147.4 | 147.3 | 147.9 | 0.2 | 0.172x | 2.869x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 150.3 | 149.7 | 151.0 | 0.4 | 0.175x | 2.925x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 858.2 | 849.6 | 864.9 | 5.6 | 1.000x | 16.703x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 30.1 | 0.2 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.9 | 0.1 | 0.042x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.6 | 31.3 | 32.4 | 0.4 | 0.044x | 1.066x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.9 | 0.1 | 0.045x | 1.071x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 106.3 | 106.3 | 106.7 | 0.2 | 0.149x | 3.590x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 106.6 | 104.8 | 106.8 | 0.7 | 0.150x | 3.598x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 107.2 | 105.3 | 107.7 | 0.8 | 0.151x | 3.618x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 107.9 | 107.8 | 108.1 | 0.1 | 0.152x | 3.641x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 710.7 | 703.7 | 715.5 | 4.1 | 0.999x | 23.993x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 711.7 | 701.7 | 717.9 | 6.0 | 1.000x | 24.028x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.6 | 51.4 | 51.8 | 0.2 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.6 | 51.5 | 51.9 | 0.1 | 0.073x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 55.5 | 55.4 | 56.0 | 0.3 | 0.078x | 1.075x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.8 | 55.5 | 55.9 | 0.1 | 0.079x | 1.081x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 102.7 | 102.6 | 102.9 | 0.1 | 0.145x | 1.990x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 102.7 | 102.1 | 102.8 | 0.3 | 0.145x | 1.990x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 103.8 | 103.5 | 104.3 | 0.3 | 0.146x | 2.011x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 106.0 | 105.8 | 106.3 | 0.2 | 0.149x | 2.053x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 119.3 | 118.4 | 119.7 | 0.5 | 0.168x | 2.312x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 709.6 | 708.2 | 713.2 | 1.7 | 1.000x | 13.749x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.7 | 0.3 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.1 | 0.0 | 0.020x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.4 | 0.1 | 0.020x | 1.015x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.020x | 1.051x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 211.3 | 209.6 | 221.9 | 4.5 | 0.341x | 17.495x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 212.9 | 211.4 | 215.1 | 1.6 | 0.343x | 17.624x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 213.4 | 210.8 | 215.7 | 1.6 | 0.344x | 17.671x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 214.3 | 212.2 | 220.9 | 3.1 | 0.346x | 17.738x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 612.6 | 609.0 | 614.2 | 2.0 | 0.988x | 50.715x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 620.0 | 609.9 | 625.0 | 5.0 | 1.000x | 51.325x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 34.6 | 34.5 | 35.6 | 0.5 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 34.6 | 34.3 | 34.9 | 0.2 | 0.007x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 34.7 | 34.6 | 35.1 | 0.2 | 0.007x | 1.004x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 34.9 | 34.7 | 35.2 | 0.2 | 0.007x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 437.2 | 433.4 | 440.1 | 2.6 | 0.093x | 12.639x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 2,010.1 | 1,958.3 | 2,108.6 | 54.0 | 0.427x | 58.110x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 2,018.9 | 1,945.7 | 2,063.5 | 48.1 | 0.429x | 58.363x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,032.4 | 1,989.9 | 2,103.7 | 40.3 | 0.432x | 58.755x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 2,047.2 | 2,008.0 | 2,086.1 | 27.4 | 0.435x | 59.182x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 4,706.6 | 4,685.1 | 4,746.1 | 22.6 | 1.000x | 136.062x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.032x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.7 | 37.5 | 37.9 | 0.1 | 0.034x | 1.067x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.0 | 37.4 | 38.2 | 0.3 | 0.035x | 1.075x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.4 | 196.8 | 200.5 | 1.2 | 0.181x | 5.616x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.4 | 198.2 | 199.0 | 0.3 | 0.181x | 5.617x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 200.6 | 200.4 | 201.3 | 0.3 | 0.183x | 5.678x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 203.3 | 201.6 | 204.2 | 0.9 | 0.186x | 5.756x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,090.9 | 1,084.9 | 1,120.3 | 12.7 | 0.996x | 30.878x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,095.8 | 1,088.7 | 1,099.9 | 4.0 | 1.000x | 31.016x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.4 | 65.3 | 65.7 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.7 | 65.6 | 66.1 | 0.2 | 0.060x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 69.0 | 68.8 | 69.4 | 0.2 | 0.063x | 1.056x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.1 | 68.9 | 69.6 | 0.3 | 0.063x | 1.056x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 170.6 | 170.0 | 174.3 | 1.6 | 0.155x | 2.609x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.6 | 198.0 | 199.2 | 0.4 | 0.180x | 3.037x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 203.3 | 202.4 | 203.8 | 0.5 | 0.185x | 3.109x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 206.8 | 205.9 | 206.9 | 0.5 | 0.188x | 3.162x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 207.0 | 206.1 | 209.0 | 1.0 | 0.188x | 3.166x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,100.5 | 1,085.6 | 1,108.0 | 8.6 | 1.000x | 16.831x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.032x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.0 | 0.3 | 0.034x | 1.058x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.7 | 37.3 | 37.8 | 0.2 | 0.035x | 1.066x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 197.8 | 197.5 | 198.2 | 0.3 | 0.182x | 5.597x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.8 | 197.7 | 200.9 | 1.4 | 0.183x | 5.625x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 200.5 | 200.3 | 201.0 | 0.2 | 0.184x | 5.675x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 203.7 | 202.3 | 207.5 | 1.7 | 0.187x | 5.765x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,087.4 | 1,080.2 | 1,100.2 | 7.0 | 1.000x | 30.773x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,097.3 | 1,084.6 | 1,106.9 | 7.7 | 1.009x | 31.053x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.5 | 66.0 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.8 | 66.2 | 0.2 | 0.060x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.9 | 68.8 | 69.1 | 0.1 | 0.063x | 1.049x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.1 | 68.9 | 69.4 | 0.2 | 0.063x | 1.051x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 170.2 | 169.9 | 174.2 | 1.6 | 0.155x | 2.592x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.6 | 198.4 | 199.9 | 0.6 | 0.180x | 3.024x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 203.1 | 202.5 | 206.3 | 1.3 | 0.184x | 3.092x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 205.9 | 205.5 | 206.7 | 0.4 | 0.187x | 3.135x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 206.1 | 205.3 | 210.4 | 1.8 | 0.187x | 3.137x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,101.9 | 1,093.7 | 1,110.4 | 5.5 | 1.000x | 16.773x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.6 | 31.4 | 0.7 | 0.034x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.2 | 0.2 | 0.037x | 1.072x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.8 | 31.6 | 31.9 | 0.1 | 0.037x | 1.077x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 151.7 | 151.2 | 159.0 | 3.0 | 0.175x | 5.129x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 154.2 | 153.3 | 154.5 | 0.4 | 0.178x | 5.212x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 154.7 | 153.9 | 155.1 | 0.4 | 0.178x | 5.230x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 156.9 | 156.2 | 165.4 | 3.5 | 0.181x | 5.304x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 868.0 | 857.9 | 875.6 | 7.3 | 1.000x | 29.343x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 868.3 | 853.2 | 881.5 | 10.6 | 1.000x | 29.353x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.4 | 51.3 | 51.9 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.6 | 51.4 | 51.7 | 0.1 | 0.059x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.6 | 55.3 | 56.0 | 0.2 | 0.064x | 1.081x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 55.6 | 55.4 | 55.7 | 0.1 | 0.064x | 1.082x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 154.2 | 154.0 | 156.5 | 0.9 | 0.177x | 2.999x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 157.5 | 157.3 | 178.9 | 8.6 | 0.181x | 3.064x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 160.3 | 160.2 | 163.0 | 1.1 | 0.184x | 3.117x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 164.1 | 163.8 | 164.4 | 0.2 | 0.188x | 3.191x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 165.5 | 165.3 | 165.7 | 0.1 | 0.190x | 3.220x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 871.3 | 861.9 | 881.8 | 7.5 | 1.000x | 16.947x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.032x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.8 | 35.7 | 36.0 | 0.1 | 0.034x | 1.062x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.9 | 35.8 | 36.1 | 0.1 | 0.034x | 1.065x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 197.3 | 196.0 | 198.4 | 0.9 | 0.188x | 5.846x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.5 | 198.0 | 200.5 | 0.9 | 0.189x | 5.882x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 199.3 | 199.2 | 200.1 | 0.3 | 0.190x | 5.906x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 202.4 | 202.4 | 202.8 | 0.2 | 0.193x | 5.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,050.5 | 1,045.1 | 1,057.8 | 4.3 | 1.000x | 31.124x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,059.9 | 1,047.0 | 1,065.3 | 6.7 | 1.009x | 31.402x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.6 | 62.6 | 63.2 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.8 | 62.5 | 63.1 | 0.2 | 0.059x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 66.0 | 65.9 | 66.2 | 0.1 | 0.062x | 1.053x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 66.0 | 65.8 | 66.2 | 0.2 | 0.063x | 1.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 173.6 | 172.9 | 174.0 | 0.4 | 0.164x | 2.772x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.2 | 198.0 | 201.2 | 1.2 | 0.188x | 3.165x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 203.0 | 202.5 | 206.7 | 1.6 | 0.192x | 3.241x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 205.3 | 204.3 | 205.7 | 0.5 | 0.194x | 3.277x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 205.6 | 205.0 | 207.1 | 0.7 | 0.195x | 3.282x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,055.6 | 1,047.9 | 1,069.8 | 8.8 | 1.000x | 16.852x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.1 | 0.3 | 0.029x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.2 | 0.2 | 0.031x | 1.042x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.4 | 10.8 | 11.7 | 0.3 | 0.032x | 1.084x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.6 | 11.6 | 11.7 | 0.1 | 0.032x | 1.108x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 104.2 | 103.9 | 104.9 | 0.4 | 0.291x | 9.936x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 104.6 | 102.0 | 104.9 | 1.1 | 0.292x | 9.978x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 106.7 | 105.8 | 106.9 | 0.4 | 0.298x | 10.172x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 107.1 | 106.4 | 108.2 | 0.7 | 0.299x | 10.218x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 358.0 | 354.6 | 363.5 | 3.0 | 1.000x | 34.139x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 362.1 | 357.4 | 363.6 | 2.1 | 1.012x | 34.534x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 26.0 | 26.6 | 0.2 | 0.011x | 1.008x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.4 | 26.2 | 26.7 | 0.2 | 0.011x | 1.011x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 26.1 | 26.5 | 0.1 | 0.011x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 260.9 | 257.9 | 275.4 | 6.5 | 0.109x | 10.011x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,419.8 | 1,392.5 | 1,525.4 | 52.6 | 0.595x | 54.471x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,420.0 | 1,347.6 | 1,552.3 | 80.7 | 0.595x | 54.476x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,472.1 | 1,366.4 | 1,536.5 | 56.1 | 0.617x | 56.475x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,496.7 | 1,389.6 | 1,513.8 | 45.1 | 0.628x | 57.420x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,384.8 | 2,372.2 | 2,393.7 | 7.9 | 1.000x | 91.493x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.4 | 35.3 | 38.4 | 1.2 | 0.032x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.1 | 0.3 | 0.034x | 1.061x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.4 | 37.2 | 37.9 | 0.2 | 0.034x | 1.062x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 197.7 | 197.4 | 199.2 | 0.6 | 0.181x | 5.606x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.1 | 197.3 | 199.9 | 1.0 | 0.181x | 5.616x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 200.5 | 200.3 | 200.9 | 0.2 | 0.183x | 5.686x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 203.2 | 201.9 | 204.0 | 0.7 | 0.186x | 5.762x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,093.6 | 1,084.3 | 1,097.7 | 5.6 | 1.000x | 31.007x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,104.8 | 1,084.9 | 1,118.4 | 11.0 | 1.010x | 31.325x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.5 | 66.0 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.7 | 66.6 | 0.4 | 0.060x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.9 | 68.9 | 69.1 | 0.1 | 0.063x | 1.049x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.063x | 1.049x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 170.4 | 170.3 | 174.3 | 1.6 | 0.156x | 2.593x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.8 | 198.2 | 199.3 | 0.4 | 0.182x | 3.024x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 203.6 | 202.5 | 205.6 | 1.1 | 0.187x | 3.098x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 206.0 | 205.9 | 206.5 | 0.2 | 0.189x | 3.134x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 206.5 | 205.9 | 207.6 | 0.6 | 0.189x | 3.142x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,091.4 | 1,083.1 | 1,119.1 | 12.3 | 1.000x | 16.604x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.8 | 34.5 | 0.3 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.0 | 33.8 | 36.8 | 1.1 | 0.032x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.8 | 35.7 | 36.2 | 0.2 | 0.034x | 1.059x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.9 | 35.7 | 36.1 | 0.1 | 0.034x | 1.062x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 197.2 | 196.4 | 197.9 | 0.5 | 0.186x | 5.829x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.4 | 197.5 | 208.5 | 4.2 | 0.188x | 5.865x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 199.8 | 199.6 | 207.0 | 2.9 | 0.189x | 5.905x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 202.4 | 202.2 | 203.0 | 0.3 | 0.191x | 5.981x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,057.9 | 1,049.8 | 1,059.0 | 3.7 | 1.000x | 31.267x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,065.4 | 1,049.8 | 1,067.3 | 6.5 | 1.007x | 31.487x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.6 | 62.5 | 62.8 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.7 | 62.4 | 62.9 | 0.2 | 0.059x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.8 | 65.8 | 66.2 | 0.2 | 0.062x | 1.051x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 66.4 | 65.9 | 69.6 | 1.4 | 0.063x | 1.061x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 173.1 | 172.4 | 173.9 | 0.5 | 0.163x | 2.764x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.3 | 197.2 | 200.9 | 1.3 | 0.187x | 3.166x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 204.3 | 203.3 | 206.6 | 1.1 | 0.192x | 3.261x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 205.4 | 204.7 | 206.5 | 0.6 | 0.193x | 3.280x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 205.8 | 205.5 | 206.7 | 0.4 | 0.194x | 3.286x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,061.8 | 1,054.2 | 1,063.1 | 3.2 | 1.000x | 16.953x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.9 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.3 | 10.9 | 11.6 | 0.2 | 0.029x | 1.041x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.3 | 10.9 | 11.8 | 0.3 | 0.029x | 1.043x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.0 | 11.5 | 12.1 | 0.2 | 0.031x | 1.106x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 105.5 | 104.2 | 107.4 | 1.0 | 0.273x | 9.751x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 106.4 | 105.4 | 132.7 | 10.7 | 0.275x | 9.831x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 108.3 | 107.5 | 108.8 | 0.4 | 0.280x | 10.009x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 109.4 | 108.2 | 111.0 | 1.0 | 0.283x | 10.114x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 386.2 | 381.4 | 392.7 | 4.3 | 1.000x | 35.691x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 388.8 | 386.9 | 390.6 | 1.5 | 1.007x | 35.932x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 27.7 | 27.4 | 27.7 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 27.9 | 27.6 | 28.0 | 0.1 | 0.011x | 1.008x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 28.0 | 27.9 | 28.2 | 0.1 | 0.011x | 1.010x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 28.0 | 27.9 | 28.0 | 0.0 | 0.011x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 264.0 | 260.1 | 271.3 | 3.8 | 0.104x | 9.532x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,497.7 | 1,477.4 | 1,507.1 | 11.8 | 0.589x | 54.084x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,507.6 | 1,497.6 | 1,522.2 | 9.9 | 0.593x | 54.439x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,524.3 | 1,511.1 | 1,551.7 | 14.3 | 0.599x | 55.043x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,560.7 | 1,516.3 | 1,585.8 | 23.1 | 0.614x | 56.360x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,543.0 | 2,529.9 | 2,546.0 | 6.0 | 1.000x | 91.829x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.3 | 38.2 | 39.4 | 0.4 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 38.5 | 38.3 | 42.3 | 1.5 | 0.035x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.1 | 40.9 | 41.2 | 0.1 | 0.037x | 1.071x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.3 | 40.9 | 41.6 | 0.2 | 0.037x | 1.076x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 220.6 | 219.4 | 222.0 | 0.8 | 0.199x | 5.753x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 222.9 | 220.5 | 226.3 | 1.9 | 0.201x | 5.812x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 223.4 | 223.2 | 233.4 | 4.0 | 0.201x | 5.827x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 227.7 | 226.5 | 230.6 | 1.4 | 0.205x | 5.939x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,111.3 | 1,102.1 | 1,116.1 | 5.1 | 1.000x | 28.982x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,114.8 | 1,104.3 | 1,119.3 | 5.9 | 1.003x | 29.074x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 72.9 | 72.8 | 73.0 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 73.1 | 73.0 | 73.2 | 0.1 | 0.065x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 76.8 | 76.7 | 77.0 | 0.1 | 0.069x | 1.053x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 77.0 | 76.8 | 78.0 | 0.5 | 0.069x | 1.057x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 175.9 | 174.7 | 177.5 | 1.1 | 0.157x | 2.414x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 204.7 | 203.8 | 212.2 | 3.2 | 0.183x | 2.809x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 209.2 | 208.4 | 211.4 | 1.0 | 0.187x | 2.870x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 212.0 | 211.5 | 214.5 | 1.1 | 0.190x | 2.909x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 212.1 | 211.1 | 212.9 | 0.6 | 0.190x | 2.911x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,117.3 | 1,112.7 | 1,128.4 | 6.4 | 1.000x | 15.331x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 32.5 | 1.2 | 0.026x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.026x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.7 | 31.4 | 31.8 | 0.1 | 0.028x | 1.070x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.8 | 31.7 | 32.0 | 0.1 | 0.028x | 1.073x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 165.7 | 164.9 | 178.1 | 5.0 | 0.145x | 5.593x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 165.8 | 164.5 | 166.1 | 0.7 | 0.145x | 5.599x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 168.5 | 166.7 | 173.2 | 2.3 | 0.148x | 5.689x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 170.3 | 167.9 | 208.4 | 15.7 | 0.149x | 5.750x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,142.4 | 1,134.5 | 1,163.8 | 9.8 | 1.000x | 38.566x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,142.4 | 1,138.1 | 1,158.8 | 7.7 | 1.000x | 38.567x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.5 | 51.2 | 51.7 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.7 | 51.6 | 55.4 | 1.5 | 0.045x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.5 | 54.9 | 55.8 | 0.3 | 0.048x | 1.078x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 55.7 | 55.4 | 55.8 | 0.2 | 0.048x | 1.082x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 109.6 | 109.4 | 112.5 | 1.3 | 0.095x | 2.129x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 167.5 | 167.4 | 168.0 | 0.2 | 0.146x | 3.254x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 168.1 | 167.4 | 178.7 | 4.3 | 0.146x | 3.266x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 169.5 | 169.4 | 170.0 | 0.2 | 0.148x | 3.292x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 171.0 | 170.9 | 171.0 | 0.0 | 0.149x | 3.321x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,148.5 | 1,146.2 | 1,159.2 | 4.9 | 1.000x | 22.307x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.8 | 41.4 | 41.8 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.8 | 41.7 | 47.8 | 2.4 | 0.061x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.7 | 44.6 | 44.8 | 0.1 | 0.065x | 1.070x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.3 | 0.2 | 0.065x | 1.073x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 136.6 | 136.6 | 181.6 | 18.0 | 0.199x | 3.272x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 137.5 | 137.0 | 138.4 | 0.5 | 0.201x | 3.293x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 137.5 | 137.3 | 139.8 | 1.0 | 0.201x | 3.293x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 140.3 | 137.6 | 145.6 | 3.4 | 0.205x | 3.359x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 684.9 | 682.6 | 690.0 | 2.4 | 1.000x | 16.401x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 686.0 | 675.7 | 692.9 | 5.5 | 1.002x | 16.426x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.5 | 79.9 | 80.7 | 0.3 | 0.119x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.6 | 80.4 | 81.9 | 0.5 | 0.119x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 83.8 | 83.1 | 84.1 | 0.3 | 0.124x | 1.040x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 83.9 | 83.5 | 84.1 | 0.2 | 0.124x | 1.042x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.3 | 98.1 | 98.5 | 0.1 | 0.145x | 1.221x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 139.7 | 139.6 | 140.0 | 0.2 | 0.206x | 1.734x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 139.8 | 139.7 | 150.8 | 4.4 | 0.207x | 1.736x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 141.2 | 141.0 | 141.6 | 0.2 | 0.208x | 1.753x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 141.3 | 141.2 | 143.6 | 0.9 | 0.209x | 1.754x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 677.1 | 674.1 | 687.8 | 5.6 | 1.000x | 8.408x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.031x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.2 | 37.2 | 37.4 | 0.1 | 0.033x | 1.054x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.9 | 0.2 | 0.033x | 1.055x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 166.8 | 165.1 | 167.0 | 0.8 | 0.148x | 4.723x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 167.1 | 165.7 | 168.3 | 1.0 | 0.148x | 4.732x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 169.1 | 168.9 | 216.1 | 18.6 | 0.150x | 4.788x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 169.8 | 168.2 | 174.4 | 2.1 | 0.150x | 4.808x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,129.8 | 1,119.5 | 1,131.9 | 4.6 | 1.000x | 31.984x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,130.3 | 1,121.2 | 1,145.5 | 9.8 | 1.000x | 31.998x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.2 | 65.9 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 66.0 | 65.8 | 66.5 | 0.3 | 0.058x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.9 | 68.8 | 69.1 | 0.2 | 0.061x | 1.049x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.0 | 68.9 | 69.3 | 0.1 | 0.061x | 1.049x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 107.2 | 106.5 | 108.1 | 0.6 | 0.095x | 1.631x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 168.4 | 168.3 | 168.6 | 0.1 | 0.149x | 2.563x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 168.4 | 168.4 | 169.1 | 0.3 | 0.149x | 2.563x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 170.5 | 170.3 | 172.7 | 1.0 | 0.151x | 2.594x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 171.9 | 171.8 | 172.0 | 0.0 | 0.152x | 2.616x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,129.1 | 1,126.6 | 1,134.3 | 2.7 | 1.000x | 17.184x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.026x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.6 | 31.5 | 0.7 | 0.026x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.0 | 0.1 | 0.028x | 1.072x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.4 | 0.3 | 0.028x | 1.073x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 170.3 | 170.1 | 176.4 | 2.5 | 0.148x | 5.763x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 170.3 | 170.0 | 170.3 | 0.1 | 0.148x | 5.763x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 172.3 | 172.3 | 219.2 | 18.7 | 0.150x | 5.833x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 173.1 | 172.7 | 177.7 | 1.9 | 0.151x | 5.857x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,148.5 | 1,137.8 | 1,154.1 | 5.3 | 0.999x | 38.870x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,149.7 | 1,143.9 | 1,171.8 | 10.6 | 1.000x | 38.912x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.4 | 51.4 | 51.5 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.045x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 55.8 | 55.4 | 56.3 | 0.3 | 0.049x | 1.084x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.8 | 55.8 | 55.9 | 0.1 | 0.049x | 1.084x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 108.8 | 108.4 | 114.2 | 2.2 | 0.095x | 2.115x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 171.4 | 171.2 | 174.4 | 1.2 | 0.149x | 3.331x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 171.4 | 171.2 | 171.7 | 0.2 | 0.149x | 3.332x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 173.5 | 173.3 | 173.7 | 0.2 | 0.151x | 3.372x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 174.9 | 174.7 | 175.1 | 0.2 | 0.152x | 3.399x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,148.7 | 1,141.7 | 1,157.2 | 5.1 | 1.000x | 22.327x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.3 | 38.5 | 1.3 | 0.031x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.1 | 0.031x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 37.2 | 37.2 | 38.7 | 0.6 | 0.033x | 1.055x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.5 | 37.2 | 37.7 | 0.2 | 0.033x | 1.062x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 172.8 | 172.7 | 173.0 | 0.1 | 0.152x | 4.899x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 173.4 | 173.2 | 182.4 | 3.6 | 0.153x | 4.914x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 175.2 | 175.0 | 223.8 | 19.5 | 0.154x | 4.964x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 175.9 | 175.5 | 180.4 | 1.8 | 0.155x | 4.985x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,136.6 | 1,132.6 | 1,146.8 | 5.1 | 1.000x | 32.210x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,136.9 | 1,131.5 | 1,154.4 | 8.2 | 1.000x | 32.220x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.8 | 65.6 | 66.1 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.8 | 66.9 | 0.4 | 0.058x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.9 | 68.8 | 69.7 | 0.3 | 0.061x | 1.047x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.1 | 68.9 | 69.3 | 0.1 | 0.061x | 1.051x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 106.6 | 106.4 | 106.9 | 0.2 | 0.094x | 1.621x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 173.8 | 173.6 | 173.9 | 0.1 | 0.153x | 2.642x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 174.0 | 173.8 | 174.2 | 0.1 | 0.153x | 2.645x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 176.0 | 175.6 | 176.2 | 0.2 | 0.155x | 2.675x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 177.4 | 177.1 | 177.6 | 0.2 | 0.156x | 2.697x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,134.4 | 1,133.5 | 1,147.7 | 5.3 | 1.000x | 17.246x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.8 | 41.4 | 45.8 | 1.7 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.8 | 41.4 | 41.9 | 0.2 | 0.061x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 44.6 | 44.6 | 44.7 | 0.1 | 0.065x | 1.069x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.7 | 44.5 | 44.8 | 0.1 | 0.065x | 1.071x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 136.7 | 136.6 | 181.4 | 17.9 | 0.200x | 3.275x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 137.2 | 137.0 | 139.1 | 0.8 | 0.200x | 3.287x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 137.6 | 137.5 | 138.6 | 0.4 | 0.201x | 3.296x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 137.7 | 137.6 | 144.9 | 2.8 | 0.201x | 3.298x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 680.4 | 675.6 | 684.3 | 3.6 | 0.994x | 16.295x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 684.8 | 678.3 | 688.0 | 3.3 | 1.000x | 16.400x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.6 | 80.3 | 81.1 | 0.3 | 0.119x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.6 | 80.1 | 81.4 | 0.4 | 0.119x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 83.7 | 83.4 | 83.9 | 0.2 | 0.123x | 1.039x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 83.8 | 83.6 | 84.1 | 0.2 | 0.123x | 1.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.4 | 98.2 | 100.9 | 1.0 | 0.145x | 1.222x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 139.6 | 139.6 | 139.8 | 0.1 | 0.206x | 1.734x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 139.8 | 139.1 | 140.2 | 0.4 | 0.206x | 1.736x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 141.1 | 141.1 | 141.4 | 0.1 | 0.208x | 1.752x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 141.4 | 141.3 | 141.4 | 0.0 | 0.208x | 1.755x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 679.5 | 678.9 | 684.4 | 2.1 | 1.000x | 8.435x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.7 | 41.4 | 45.7 | 1.6 | 0.039x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.4 | 42.4 | 0.3 | 0.039x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.6 | 44.4 | 44.9 | 0.2 | 0.041x | 1.069x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 44.8 | 44.6 | 44.9 | 0.1 | 0.042x | 1.075x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 166.7 | 166.2 | 174.7 | 3.2 | 0.155x | 4.000x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 168.4 | 167.9 | 177.5 | 3.7 | 0.156x | 4.042x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 170.4 | 168.2 | 215.2 | 18.0 | 0.158x | 4.088x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 171.0 | 170.9 | 175.6 | 1.9 | 0.159x | 4.103x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,073.9 | 1,067.5 | 1,083.2 | 5.1 | 0.996x | 25.769x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,077.9 | 1,060.7 | 1,091.5 | 11.7 | 1.000x | 25.866x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.4 | 80.2 | 80.7 | 0.1 | 0.075x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.5 | 80.3 | 81.4 | 0.4 | 0.075x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 83.7 | 83.3 | 86.1 | 1.0 | 0.078x | 1.041x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 83.8 | 83.6 | 84.3 | 0.2 | 0.078x | 1.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 104.3 | 104.1 | 104.4 | 0.1 | 0.097x | 1.296x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 169.1 | 168.9 | 169.4 | 0.2 | 0.157x | 2.102x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 169.1 | 168.9 | 172.4 | 1.3 | 0.157x | 2.102x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 171.4 | 171.2 | 171.6 | 0.2 | 0.159x | 2.131x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 172.9 | 172.7 | 211.4 | 15.4 | 0.160x | 2.150x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,078.2 | 1,072.2 | 1,083.9 | 3.9 | 1.000x | 13.403x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.007x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.017x | 1.008x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.009x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 190.9 | 178.7 | 194.5 | 5.5 | 0.243x | 14.461x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194.2 | 184.8 | 195.5 | 3.9 | 0.247x | 14.709x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 194.4 | 191.7 | 196.4 | 1.5 | 0.247x | 14.728x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 196.1 | 191.1 | 199.8 | 3.2 | 0.249x | 14.854x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 779.0 | 775.2 | 784.0 | 2.8 | 0.991x | 59.010x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 786.1 | 779.8 | 788.9 | 3.2 | 1.000x | 59.541x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 22.3 | 22.1 | 22.7 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 22.4 | 22.2 | 22.8 | 0.2 | 0.008x | 1.005x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 22.4 | 22.1 | 22.5 | 0.2 | 0.008x | 1.006x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 22.5 | 22.2 | 22.6 | 0.2 | 0.008x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 219.1 | 213.5 | 236.8 | 8.2 | 0.082x | 9.822x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 897.0 | 818.6 | 927.7 | 36.2 | 0.336x | 40.216x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 942.8 | 907.5 | 1,030.8 | 46.6 | 0.353x | 42.269x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 959.2 | 901.2 | 1,268.1 | 135.6 | 0.359x | 43.006x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 960.5 | 892.1 | 997.0 | 36.3 | 0.359x | 43.063x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,672.2 | 2,664.8 | 2,724.5 | 21.9 | 1.000x | 119.804x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 0.017x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.010x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.017x | 1.017x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 191.9 | 189.6 | 192.7 | 1.1 | 0.243x | 14.529x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 192.9 | 191.4 | 194.4 | 1.3 | 0.244x | 14.600x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 194.1 | 192.5 | 197.9 | 1.8 | 0.246x | 14.693x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194.8 | 190.3 | 197.1 | 2.5 | 0.246x | 14.742x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 780.5 | 771.4 | 783.5 | 4.1 | 0.987x | 59.078x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 790.5 | 778.9 | 809.5 | 10.9 | 1.000x | 59.832x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 45.4 | 45.3 | 45.7 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 45.5 | 45.2 | 45.9 | 0.2 | 0.017x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 45.6 | 45.4 | 45.6 | 0.1 | 0.017x | 1.003x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 45.8 | 45.5 | 45.8 | 0.1 | 0.017x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 235.0 | 229.5 | 236.2 | 2.4 | 0.088x | 5.172x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,663.5 | 2,654.4 | 2,701.7 | 16.5 | 1.000x | 58.620x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 3,229.2 | 3,184.6 | 3,374.6 | 68.3 | 1.212x | 71.069x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 3,232.3 | 3,194.5 | 3,308.4 | 39.5 | 1.214x | 71.136x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 3,261.6 | 3,149.8 | 3,326.2 | 58.2 | 1.225x | 71.781x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 3,274.2 | 3,187.9 | 3,337.5 | 56.5 | 1.229x | 72.059x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.007x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.010x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.3 | 0.8 | 0.017x | 1.014x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 190.2 | 179.0 | 193.1 | 4.9 | 0.244x | 14.427x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 193.1 | 190.0 | 207.8 | 6.4 | 0.248x | 14.652x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194.5 | 184.4 | 206.1 | 7.0 | 0.250x | 14.757x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 195.6 | 192.7 | 201.4 | 2.9 | 0.251x | 14.837x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 778.3 | 774.4 | 792.8 | 7.0 | 1.000x | 59.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 779.9 | 773.4 | 781.0 | 2.7 | 1.002x | 59.167x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 22.1 | 22.1 | 22.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 22.1 | 22.0 | 22.3 | 0.1 | 0.008x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 22.3 | 22.3 | 22.5 | 0.1 | 0.008x | 1.010x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 22.4 | 22.3 | 23.3 | 0.4 | 0.008x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 218.9 | 214.4 | 220.1 | 2.1 | 0.082x | 9.908x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 850.0 | 791.2 | 892.1 | 36.9 | 0.319x | 38.482x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 873.6 | 817.6 | 977.9 | 54.3 | 0.328x | 39.553x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 874.8 | 786.8 | 952.0 | 59.6 | 0.328x | 39.604x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 925.6 | 826.8 | 945.6 | 45.2 | 0.347x | 41.905x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,667.6 | 2,657.4 | 2,687.5 | 10.9 | 1.000x | 120.772x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.3 | 0.0 | 0.017x | 1.010x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.2 | 16.5 | 1.3 | 0.017x | 1.013x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 190.2 | 185.6 | 192.5 | 2.6 | 0.243x | 14.417x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 191.0 | 189.5 | 191.7 | 0.8 | 0.244x | 14.480x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 192.8 | 190.5 | 195.2 | 1.8 | 0.247x | 14.610x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 193.4 | 191.1 | 194.9 | 1.4 | 0.247x | 14.662x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 778.6 | 771.1 | 782.9 | 4.1 | 0.996x | 59.011x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 781.7 | 777.5 | 789.0 | 3.8 | 1.000x | 59.251x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 29.7 | 29.6 | 30.0 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 29.7 | 29.4 | 29.9 | 0.2 | 0.011x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 29.9 | 29.6 | 30.2 | 0.2 | 0.011x | 1.006x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 29.9 | 29.5 | 30.0 | 0.2 | 0.011x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 233.8 | 229.1 | 235.8 | 2.5 | 0.088x | 7.874x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,389.1 | 1,327.0 | 1,476.4 | 51.5 | 0.521x | 46.785x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,439.5 | 1,388.2 | 1,501.6 | 44.2 | 0.540x | 48.484x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,450.7 | 1,351.3 | 1,512.1 | 59.3 | 0.544x | 48.861x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,511.0 | 1,372.2 | 1,617.5 | 78.8 | 0.566x | 50.889x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,667.5 | 2,648.2 | 2,674.4 | 8.9 | 1.000x | 89.841x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 15.9 | 19.3 | 1.3 | 0.017x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 0.017x | 1.003x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 292.0 | 269.2 | 319.3 | 16.4 | 0.315x | 18.124x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 294.4 | 245.1 | 306.0 | 22.4 | 0.318x | 18.271x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 298.4 | 288.0 | 308.9 | 7.5 | 0.322x | 18.516x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 301.3 | 287.4 | 311.4 | 8.8 | 0.325x | 18.698x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 921.5 | 918.9 | 931.7 | 5.0 | 0.995x | 57.185x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 925.8 | 919.6 | 931.8 | 4.1 | 1.000x | 57.451x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.2 | 26.2 | 26.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 26.8 | 0.3 | 0.008x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.2 | 0.008x | 1.004x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.4 | 26.1 | 31.0 | 1.9 | 0.008x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 321.9 | 316.3 | 324.4 | 3.0 | 0.098x | 12.302x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,731.4 | 1,713.5 | 1,778.1 | 21.8 | 0.529x | 66.162x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,736.6 | 1,721.7 | 1,751.0 | 9.7 | 0.531x | 66.360x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,741.8 | 1,734.3 | 1,756.6 | 8.3 | 0.533x | 66.557x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,749.6 | 1,732.5 | 1,775.6 | 14.5 | 0.535x | 66.856x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,270.2 | 3,237.5 | 3,336.2 | 32.9 | 1.000x | 124.962x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.1 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 15.9 | 16.1 | 0.1 | 0.018x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.018x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.005x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 289.9 | 275.7 | 301.7 | 9.5 | 0.332x | 18.065x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 293.3 | 286.9 | 304.0 | 7.0 | 0.335x | 18.272x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 296.8 | 288.8 | 312.9 | 8.1 | 0.340x | 18.494x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 310.0 | 279.9 | 312.9 | 12.2 | 0.355x | 19.314x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 874.2 | 871.2 | 880.7 | 3.3 | 1.000x | 54.467x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 875.4 | 869.8 | 880.2 | 3.5 | 1.001x | 54.545x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.7 | 26.7 | 0.4 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.009x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.1 | 0.009x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 26.0 | 39.0 | 5.1 | 0.009x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 322.4 | 315.7 | 336.2 | 7.0 | 0.106x | 12.358x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,725.6 | 1,721.1 | 1,728.8 | 2.9 | 0.569x | 66.150x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,729.9 | 1,668.7 | 1,747.9 | 28.1 | 0.570x | 66.314x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,732.4 | 1,710.8 | 1,744.8 | 11.1 | 0.571x | 66.411x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,741.2 | 1,721.9 | 1,762.9 | 13.5 | 0.574x | 66.750x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,032.6 | 3,026.0 | 3,039.4 | 5.6 | 1.000x | 116.256x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.4 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.4 | 0.1 | 0.016x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.2 | 20.2 | 23.2 | 1.3 | 0.016x | 1.003x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.1 | 0.016x | 1.007x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 146.3 | 145.2 | 163.6 | 7.0 | 0.117x | 7.252x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.3 | 145.0 | 151.8 | 2.5 | 0.117x | 7.303x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 148.4 | 146.0 | 155.1 | 3.3 | 0.118x | 7.358x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.9 | 148.3 | 150.4 | 0.7 | 0.119x | 7.381x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,254.6 | 1,246.1 | 1,280.1 | 12.6 | 1.000x | 62.198x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,254.9 | 1,244.7 | 1,268.0 | 7.8 | 1.000x | 62.213x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.0 | 19.0 | 19.1 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.1 | 19.1 | 32.7 | 5.5 | 0.004x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.1 | 19.1 | 19.3 | 0.1 | 0.004x | 1.005x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 19.2 | 19.1 | 19.3 | 0.0 | 0.004x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 387.1 | 381.6 | 392.8 | 4.2 | 0.084x | 20.343x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 630.8 | 612.7 | 743.7 | 47.6 | 0.136x | 33.153x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 635.3 | 625.5 | 721.0 | 35.7 | 0.137x | 33.390x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 683.6 | 611.9 | 697.8 | 35.9 | 0.148x | 35.930x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 700.2 | 614.1 | 713.6 | 36.9 | 0.152x | 36.800x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 4,621.5 | 4,601.2 | 4,628.4 | 11.8 | 1.000x | 242.899x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.0 | 0.0 | 0.014x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 25.8 | 1.1 | 0.015x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 24.3 | 0.5 | 0.015x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.5 | 0.2 | 0.015x | 1.003x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 475.2 | 462.3 | 478.4 | 6.0 | 0.299x | 20.632x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 479.9 | 472.2 | 497.1 | 8.9 | 0.302x | 20.836x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 480.3 | 385.1 | 485.9 | 38.5 | 0.302x | 20.854x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 487.8 | 487.2 | 493.3 | 2.2 | 0.307x | 21.181x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,581.8 | 1,579.2 | 1,643.6 | 24.4 | 0.995x | 68.678x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,589.1 | 1,573.4 | 1,592.3 | 6.7 | 1.000x | 68.995x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 25.2 | 25.2 | 25.3 | 0.0 | 0.004x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 25.3 | 25.2 | 25.5 | 0.1 | 0.004x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 25.5 | 25.3 | 25.5 | 0.1 | 0.004x | 1.010x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 25.6 | 25.2 | 37.2 | 4.7 | 0.004x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 477.9 | 474.7 | 501.6 | 11.0 | 0.081x | 18.948x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,762.8 | 1,750.8 | 1,791.5 | 14.0 | 0.300x | 69.897x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,764.7 | 1,763.8 | 1,785.6 | 8.9 | 0.301x | 69.972x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,765.3 | 1,758.2 | 1,768.7 | 3.6 | 0.301x | 69.995x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,766.9 | 1,756.1 | 1,772.1 | 5.4 | 0.301x | 70.059x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 5,867.4 | 5,866.0 | 5,911.6 | 19.5 | 1.000x | 232.647x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.4 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.4 | 0.1 | 0.019x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.3 | 0.1 | 0.019x | 1.007x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.9 | 0.2 | 0.020x | 1.040x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.4 | 144.2 | 145.9 | 0.6 | 0.231x | 11.998x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 147.0 | 144.9 | 151.3 | 2.1 | 0.234x | 12.126x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 149.3 | 148.0 | 151.2 | 1.2 | 0.237x | 12.318x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.6 | 147.4 | 151.0 | 1.2 | 0.238x | 12.347x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 628.9 | 626.0 | 639.5 | 5.5 | 1.000x | 51.896x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 633.8 | 630.9 | 643.0 | 4.2 | 1.008x | 52.294x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.8 | 26.8 | 38.4 | 4.6 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.9 | 26.7 | 27.5 | 0.3 | 0.013x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.9 | 27.1 | 0.1 | 0.013x | 1.006x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 27.0 | 26.9 | 27.1 | 0.1 | 0.013x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 194.0 | 187.9 | 195.1 | 2.6 | 0.093x | 7.238x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,469.0 | 1,423.6 | 1,617.1 | 73.4 | 0.707x | 54.815x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,484.1 | 1,400.1 | 1,597.3 | 65.1 | 0.714x | 55.381x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,489.3 | 1,444.0 | 1,500.3 | 22.1 | 0.717x | 55.576x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,553.6 | 1,432.6 | 1,574.1 | 55.1 | 0.748x | 57.974x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,077.7 | 2,061.7 | 2,099.7 | 12.7 | 1.000x | 77.531x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.017x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 0.017x | 1.001x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.7 | 14.7 | 14.8 | 0.1 | 0.017x | 1.008x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 207.7 | 207.3 | 208.8 | 0.5 | 0.245x | 14.209x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 210.8 | 208.1 | 212.1 | 1.4 | 0.248x | 14.421x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 211.1 | 208.0 | 213.9 | 1.9 | 0.249x | 14.440x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 219.0 | 215.3 | 222.3 | 2.6 | 0.258x | 14.980x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 846.0 | 839.5 | 847.9 | 3.4 | 0.997x | 57.875x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 848.6 | 843.5 | 854.9 | 4.0 | 1.000x | 58.050x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 20.7 | 20.7 | 21.1 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 20.8 | 20.8 | 21.0 | 0.1 | 0.007x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 21.0 | 20.8 | 21.0 | 0.1 | 0.007x | 1.010x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 21.0 | 20.9 | 34.6 | 5.4 | 0.007x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 282.8 | 279.5 | 306.2 | 10.0 | 0.097x | 13.636x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,303.0 | 1,301.4 | 1,322.6 | 7.8 | 0.447x | 62.831x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,319.7 | 1,313.3 | 1,328.3 | 5.2 | 0.453x | 63.639x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,323.9 | 1,299.4 | 1,341.9 | 14.8 | 0.454x | 63.841x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,343.2 | 1,321.7 | 1,351.7 | 10.2 | 0.461x | 64.770x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,914.4 | 2,902.0 | 2,937.3 | 12.3 | 1.000x | 140.536x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.2 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.023x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.023x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.2 | 23.0 | 23.4 | 0.1 | 0.023x | 1.007x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 471.2 | 468.6 | 504.6 | 15.1 | 0.468x | 20.469x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 473.7 | 463.6 | 521.4 | 24.8 | 0.471x | 20.578x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 485.9 | 434.4 | 494.1 | 21.6 | 0.483x | 21.107x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 488.5 | 472.3 | 520.6 | 17.4 | 0.485x | 21.219x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,006.6 | 994.3 | 1,029.1 | 11.3 | 1.000x | 43.727x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,009.0 | 1,002.1 | 1,021.5 | 6.3 | 1.002x | 43.832x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.0 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.8 | 38.4 | 4.6 | 0.007x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 27.0 | 26.8 | 27.5 | 0.2 | 0.008x | 1.006x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 27.0 | 26.9 | 27.2 | 0.1 | 0.008x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 569.0 | 561.9 | 576.0 | 4.8 | 0.158x | 21.212x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 2,837.3 | 2,830.1 | 2,861.3 | 11.3 | 0.789x | 105.771x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,866.9 | 2,846.3 | 2,909.4 | 21.7 | 0.798x | 106.876x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 2,867.8 | 2,862.2 | 2,871.8 | 3.8 | 0.798x | 106.910x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 2,879.1 | 2,874.2 | 2,880.7 | 2.7 | 0.801x | 107.332x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,594.7 | 3,549.9 | 3,615.4 | 25.2 | 1.000x | 134.006x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.0 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.1 | 0.1 | 0.030x | 1.019x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.3 | 11.3 | 11.5 | 0.1 | 0.030x | 1.036x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.0 | 0.1 | 0.032x | 1.098x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 105.0 | 104.1 | 106.2 | 0.8 | 0.278x | 9.606x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 105.9 | 104.5 | 109.7 | 1.8 | 0.281x | 9.689x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 105.9 | 104.9 | 107.2 | 0.8 | 0.281x | 9.690x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 106.3 | 104.6 | 106.3 | 0.7 | 0.282x | 9.727x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 376.5 | 374.4 | 379.8 | 1.8 | 0.999x | 34.454x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 377.0 | 375.5 | 381.6 | 2.1 | 1.000x | 34.501x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 59.3 | 58.9 | 59.4 | 0.2 | 0.038x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 62.2 | 62.4 | 0.1 | 0.040x | 1.055x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.3 | 62.2 | 62.5 | 0.1 | 0.040x | 1.056x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 209.5 | 208.6 | 211.7 | 1.0 | 0.135x | 3.548x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 298.2 | 297.5 | 298.5 | 0.3 | 0.193x | 5.051x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 298.6 | 298.3 | 300.2 | 0.7 | 0.193x | 5.059x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 299.9 | 298.0 | 301.0 | 1.1 | 0.194x | 5.080x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 301.4 | 299.1 | 302.5 | 1.2 | 0.195x | 5.105x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,547.8 | 1,538.0 | 1,562.7 | 9.8 | 1.000x | 26.217x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.0 | 0.788x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 0.789x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 0.789x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.790x | 1.002x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 33.0 | 32.7 | 33.7 | 0.4 | 1.000x | 1.269x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 34.0 | 33.3 | 35.0 | 0.5 | 1.029x | 1.306x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 256.4 | 255.7 | 265.3 | 3.6 | 7.773x | 9.861x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 256.6 | 255.9 | 257.8 | 0.7 | 7.778x | 9.867x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 256.9 | 255.9 | 269.5 | 5.2 | 7.788x | 9.880x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 257.0 | 256.5 | 266.7 | 4.0 | 7.790x | 9.882x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 23.7 | 23.5 | 24.5 | 0.3 | 0.696x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 23.8 | 23.7 | 23.9 | 0.1 | 0.697x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 23.8 | 23.7 | 23.8 | 0.1 | 0.697x | 1.001x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 24.1 | 23.8 | 25.2 | 0.5 | 0.707x | 1.016x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 34.1 | 33.9 | 35.1 | 0.4 | 1.000x | 1.437x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 44.3 | 44.4 | 0.0 | 1.301x | 1.869x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,703.9 | 1,682.7 | 1,725.4 | 14.2 | 49.979x | 71.808x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,788.3 | 1,768.3 | 1,865.0 | 36.7 | 52.455x | 75.367x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,808.4 | 1,730.1 | 1,860.2 | 44.8 | 53.043x | 76.211x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,842.8 | 1,672.6 | 1,856.8 | 68.2 | 54.053x | 77.663x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.6 | 9.5 | 12.3 | 1.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.1 | 0.1 | 0.062x | 1.036x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.1 | 0.1 | 0.062x | 1.042x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.2 | 0.3 | 0.065x | 1.091x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.1 | 47.7 | 48.2 | 0.2 | 0.296x | 4.989x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.1 | 47.8 | 50.2 | 0.9 | 0.297x | 4.992x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 49.4 | 49.1 | 49.6 | 0.1 | 0.304x | 5.124x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 49.5 | 49.3 | 245.4 | 78.0 | 0.305x | 5.135x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 162.2 | 161.1 | 164.0 | 0.9 | 1.000x | 16.835x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 162.9 | 161.6 | 167.7 | 2.1 | 1.004x | 16.904x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 18.6 | 18.6 | 18.9 | 0.1 | 0.105x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 18.7 | 18.5 | 18.8 | 0.1 | 0.106x | 1.006x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.8 | 18.5 | 19.8 | 0.6 | 0.106x | 1.012x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.6 | 19.0 | 0.1 | 0.106x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 54.7 | 54.6 | 54.7 | 0.0 | 0.309x | 2.941x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 177.1 | 177.0 | 179.9 | 1.3 | 1.000x | 9.531x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 940.5 | 925.1 | 1,019.4 | 39.2 | 5.310x | 50.611x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 970.9 | 885.3 | 1,047.9 | 59.3 | 5.482x | 52.248x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 991.6 | 952.8 | 1,013.1 | 20.9 | 5.599x | 53.361x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,054.4 | 1,010.2 | 1,075.3 | 26.1 | 5.953x | 56.740x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.3 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.022x | 1.043x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.7 | 13.6 | 14.1 | 0.2 | 0.022x | 1.070x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.2 | 13.3 | 14.6 | 0.4 | 0.023x | 1.110x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 97.2 | 96.3 | 99.0 | 0.9 | 0.160x | 7.620x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 97.8 | 95.6 | 98.0 | 1.0 | 0.161x | 7.666x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 98.3 | 78.2 | 98.8 | 8.0 | 0.162x | 7.707x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 99.2 | 98.6 | 110.6 | 4.6 | 0.163x | 7.774x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 608.9 | 607.3 | 617.2 | 3.8 | 1.000x | 47.718x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 611.9 | 604.7 | 614.7 | 3.5 | 1.005x | 47.954x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 11.0 | 10.9 | 11.0 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 11.4 | 11.1 | 12.3 | 0.4 | 0.018x | 1.038x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 12.0 | 11.4 | 12.9 | 0.6 | 0.019x | 1.089x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 12.0 | 11.9 | 12.1 | 0.1 | 0.019x | 1.093x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 84.2 | 83.5 | 85.0 | 0.5 | 0.135x | 7.663x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 169.3 | 167.5 | 172.8 | 2.3 | 0.271x | 15.408x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 169.3 | 168.8 | 174.0 | 1.9 | 0.271x | 15.412x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 173.4 | 172.6 | 195.6 | 8.9 | 0.278x | 15.785x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 184.8 | 181.7 | 189.6 | 3.3 | 0.296x | 16.816x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 624.7 | 620.6 | 627.7 | 2.5 | 1.000x | 56.856x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.2 | 0.1 | 0.021x | 1.008x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.4 | 12.2 | 14.8 | 1.0 | 0.022x | 1.029x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.9 | 12.6 | 13.0 | 0.1 | 0.022x | 1.068x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.1 | 144.6 | 147.4 | 1.1 | 0.252x | 12.036x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 146.2 | 144.6 | 153.4 | 3.2 | 0.254x | 12.122x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.5 | 146.7 | 152.7 | 2.3 | 0.256x | 12.232x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 149.0 | 147.8 | 156.0 | 2.9 | 0.259x | 12.359x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 575.2 | 571.8 | 582.2 | 3.7 | 1.000x | 47.713x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 575.5 | 574.1 | 594.4 | 7.7 | 1.000x | 47.730x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 71.1 | 71.0 | 71.1 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 71.3 | 71.2 | 71.7 | 0.2 | 0.026x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 73.8 | 73.6 | 74.0 | 0.1 | 0.026x | 1.039x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 73.9 | 73.7 | 74.0 | 0.1 | 0.026x | 1.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 292.5 | 290.5 | 293.0 | 1.0 | 0.105x | 4.117x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 714.5 | 684.3 | 743.7 | 19.7 | 0.256x | 10.055x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 720.1 | 715.5 | 780.3 | 25.5 | 0.258x | 10.134x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 733.9 | 700.2 | 748.7 | 19.8 | 0.263x | 10.328x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 737.1 | 715.0 | 774.3 | 19.8 | 0.264x | 10.373x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,793.1 | 2,776.7 | 2,800.6 | 8.7 | 1.000x | 39.306x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.5 | 11.1 | 0.6 | 0.060x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.061x | 1.008x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.1 | 0.1 | 0.062x | 1.019x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 0.065x | 1.073x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 47.9 | 47.7 | 49.0 | 0.5 | 0.297x | 4.924x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.1 | 47.9 | 56.9 | 3.6 | 0.298x | 4.940x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 49.6 | 48.9 | 49.8 | 0.3 | 0.308x | 5.098x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 49.6 | 48.8 | 49.9 | 0.4 | 0.308x | 5.099x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 161.1 | 159.1 | 166.5 | 2.5 | 1.000x | 16.552x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 162.5 | 161.7 | 166.1 | 1.6 | 1.009x | 16.694x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 61.8 | 61.7 | 62.7 | 0.4 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 61.9 | 61.7 | 62.2 | 0.2 | 0.061x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 64.3 | 64.2 | 64.8 | 0.2 | 0.063x | 1.040x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 64.4 | 64.1 | 64.5 | 0.1 | 0.063x | 1.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 158.3 | 157.8 | 160.1 | 0.9 | 0.156x | 2.560x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 162.9 | 162.7 | 164.0 | 0.5 | 0.161x | 2.635x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 165.0 | 164.7 | 165.5 | 0.3 | 0.163x | 2.668x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 166.3 | 165.6 | 169.9 | 1.5 | 0.164x | 2.690x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 168.9 | 168.6 | 169.9 | 0.4 | 0.167x | 2.732x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,014.3 | 1,007.7 | 1,027.6 | 6.8 | 1.000x | 16.403x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.1 | 0.0 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.9 | 0.3 | 0.021x | 1.011x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.022x | 1.032x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.8 | 12.5 | 13.0 | 0.1 | 0.022x | 1.059x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.6 | 144.4 | 147.1 | 1.1 | 0.252x | 12.080x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 146.1 | 144.5 | 154.7 | 3.9 | 0.253x | 12.120x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.1 | 148.3 | 153.4 | 1.9 | 0.258x | 12.370x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 149.1 | 148.0 | 154.9 | 2.5 | 0.258x | 12.374x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 572.8 | 571.6 | 580.1 | 3.3 | 0.993x | 47.523x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 577.0 | 569.8 | 577.4 | 2.9 | 1.000x | 47.877x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 25.7 | 25.6 | 30.7 | 2.0 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 25.7 | 25.5 | 25.8 | 0.1 | 0.013x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 25.7 | 25.6 | 25.8 | 0.1 | 0.013x | 1.003x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 25.7 | 25.6 | 26.2 | 0.2 | 0.013x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 199.6 | 187.5 | 200.0 | 4.9 | 0.100x | 7.782x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,423.1 | 1,385.3 | 1,470.6 | 30.9 | 0.715x | 55.476x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,456.5 | 1,310.5 | 1,560.0 | 85.4 | 0.732x | 56.780x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,469.3 | 1,428.3 | 1,496.8 | 24.7 | 0.739x | 57.279x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,503.4 | 1,396.3 | 1,560.3 | 65.5 | 0.756x | 58.609x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,989.4 | 1,956.6 | 1,997.6 | 14.6 | 1.000x | 77.555x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.9 | 0.1 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.0 | 0.022x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.8 | 0.0 | 0.022x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.8 | 21.6 | 21.9 | 0.1 | 0.022x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 364.3 | 361.2 | 372.4 | 4.1 | 0.363x | 16.784x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 375.2 | 341.1 | 404.0 | 20.7 | 0.374x | 17.285x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 389.7 | 362.0 | 396.2 | 15.1 | 0.388x | 17.954x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 394.7 | 371.1 | 433.0 | 20.4 | 0.393x | 18.184x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 998.5 | 990.6 | 1,013.8 | 8.5 | 0.994x | 46.003x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,004.2 | 989.0 | 1,018.7 | 10.9 | 1.000x | 46.267x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.0 | 18.9 | 19.9 | 0.4 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.1 | 18.8 | 19.3 | 0.2 | 0.005x | 1.009x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.9 | 19.9 | 20.1 | 0.1 | 0.006x | 1.051x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.0 | 19.9 | 20.1 | 0.0 | 0.006x | 1.057x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 533.5 | 528.2 | 537.1 | 2.9 | 0.151x | 28.144x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,725.2 | 1,717.7 | 1,822.6 | 39.2 | 0.489x | 91.020x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,725.7 | 1,708.4 | 1,737.7 | 11.1 | 0.489x | 91.046x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,727.2 | 1,699.4 | 1,742.6 | 16.2 | 0.490x | 91.126x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,729.0 | 1,708.7 | 1,741.7 | 12.7 | 0.490x | 91.218x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,525.7 | 3,516.8 | 3,538.9 | 7.1 | 1.000x | 186.011x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.5 | 0.2 | 0.014x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.0 | 0.014x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.7 | 0.2 | 0.014x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.5 | 144.7 | 155.5 | 4.0 | 0.090x | 6.305x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.9 | 144.8 | 147.4 | 1.0 | 0.090x | 6.322x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.9 | 147.2 | 151.1 | 1.4 | 0.092x | 6.453x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.3 | 147.5 | 151.7 | 1.5 | 0.092x | 6.471x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,614.4 | 1,603.2 | 1,635.6 | 10.7 | 0.998x | 69.963x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,617.7 | 1,603.4 | 1,628.1 | 9.7 | 1.000x | 70.105x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 20.4 | 20.4 | 20.6 | 0.1 | 0.003x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 20.4 | 20.2 | 20.8 | 0.2 | 0.003x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 20.5 | 20.5 | 21.4 | 0.4 | 0.003x | 1.005x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.1 | 0.003x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 466.5 | 464.0 | 471.2 | 2.4 | 0.077x | 22.849x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 751.3 | 692.9 | 804.6 | 37.4 | 0.124x | 36.795x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 769.7 | 710.2 | 818.4 | 37.4 | 0.127x | 37.697x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 789.4 | 726.9 | 917.5 | 69.5 | 0.130x | 38.660x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 817.8 | 700.5 | 824.3 | 46.6 | 0.135x | 40.052x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 6,063.9 | 6,004.3 | 6,176.9 | 61.1 | 1.000x | 296.989x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.007x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 105.5 | 105.4 | 106.3 | 0.3 | 0.136x | 8.003x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 106.6 | 104.6 | 112.9 | 2.9 | 0.138x | 8.085x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 108.1 | 105.8 | 111.7 | 2.0 | 0.140x | 8.198x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 108.2 | 106.7 | 110.1 | 1.3 | 0.140x | 8.210x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 774.2 | 773.1 | 784.9 | 5.2 | 1.000x | 58.724x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 778.0 | 775.8 | 792.8 | 6.3 | 1.005x | 59.009x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 12.0 | 12.0 | 12.1 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 12.2 | 12.1 | 13.0 | 0.3 | 0.006x | 1.015x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 12.3 | 12.0 | 12.6 | 0.2 | 0.006x | 1.023x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 12.8 | 12.5 | 13.4 | 0.3 | 0.006x | 1.070x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 183.1 | 181.3 | 186.4 | 1.8 | 0.090x | 15.248x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 302.7 | 301.1 | 321.0 | 7.6 | 0.149x | 25.208x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 327.9 | 309.0 | 345.5 | 12.3 | 0.162x | 27.310x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 332.1 | 312.2 | 362.2 | 17.4 | 0.164x | 27.657x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 339.2 | 306.6 | 382.6 | 29.6 | 0.167x | 28.250x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,027.1 | 2,020.1 | 2,096.4 | 33.4 | 1.000x | 168.827x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.5 | 12.3 | 0.3 | 0.021x | 1.029x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.6 | 11.6 | 11.9 | 0.1 | 0.021x | 1.036x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.023x | 1.100x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 128.5 | 127.5 | 135.2 | 2.8 | 0.237x | 11.452x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 128.9 | 128.0 | 131.7 | 1.4 | 0.238x | 11.486x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 131.3 | 130.1 | 135.5 | 2.0 | 0.242x | 11.698x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 131.7 | 131.5 | 135.1 | 1.4 | 0.243x | 11.740x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 541.8 | 540.1 | 578.0 | 14.5 | 1.000x | 48.287x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 549.6 | 546.1 | 556.3 | 3.6 | 1.014x | 48.981x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 68.6 | 68.2 | 68.8 | 0.2 | 0.027x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 68.8 | 68.7 | 69.7 | 0.4 | 0.027x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 72.0 | 71.7 | 72.2 | 0.2 | 0.028x | 1.049x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 72.2 | 71.9 | 72.7 | 0.3 | 0.028x | 1.052x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 271.3 | 270.7 | 274.6 | 1.8 | 0.106x | 3.953x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 591.5 | 576.3 | 594.4 | 6.4 | 0.231x | 8.617x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 597.8 | 587.1 | 600.2 | 4.7 | 0.234x | 8.709x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 598.2 | 589.4 | 622.2 | 13.1 | 0.234x | 8.714x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 602.4 | 554.4 | 613.6 | 20.7 | 0.235x | 8.776x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,559.3 | 2,541.1 | 2,580.9 | 13.4 | 1.000x | 37.285x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.0 | 0.019x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.019x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 0.019x | 1.007x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 244.1 | 206.6 | 282.6 | 27.5 | 0.319x | 16.760x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 244.9 | 234.0 | 283.6 | 21.6 | 0.320x | 16.815x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 245.4 | 214.9 | 304.6 | 30.8 | 0.321x | 16.855x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 246.1 | 221.9 | 287.3 | 24.3 | 0.321x | 16.903x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 765.4 | 762.2 | 802.1 | 14.8 | 1.000x | 52.563x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 765.8 | 763.2 | 772.6 | 3.6 | 1.000x | 52.588x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 53.8 | 53.7 | 54.0 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 54.0 | 53.9 | 54.4 | 0.2 | 0.015x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 56.7 | 56.5 | 57.1 | 0.2 | 0.016x | 1.055x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 56.8 | 56.8 | 57.0 | 0.1 | 0.016x | 1.057x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 378.3 | 372.4 | 381.5 | 3.4 | 0.107x | 7.033x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,012.3 | 986.4 | 1,034.4 | 16.1 | 0.288x | 18.821x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,019.2 | 996.7 | 1,033.7 | 14.3 | 0.290x | 18.948x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,022.1 | 1,020.0 | 1,041.8 | 9.3 | 0.290x | 19.002x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,027.7 | 1,010.9 | 1,047.2 | 13.8 | 0.292x | 19.108x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,519.7 | 3,513.1 | 3,537.6 | 8.7 | 1.000x | 65.438x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.6 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.6 | 0.0 | 0.021x | 1.026x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.6 | 11.5 | 11.9 | 0.1 | 0.021x | 1.031x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.3 | 0.0 | 0.022x | 1.092x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 128.5 | 128.1 | 133.9 | 2.2 | 0.235x | 11.450x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 128.6 | 127.9 | 129.1 | 0.5 | 0.235x | 11.459x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 130.2 | 129.5 | 133.0 | 1.2 | 0.238x | 11.598x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 132.1 | 129.7 | 134.9 | 1.9 | 0.242x | 11.767x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 546.6 | 538.1 | 547.8 | 3.6 | 1.000x | 48.704x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 548.6 | 545.3 | 552.4 | 2.7 | 1.004x | 48.880x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 68.6 | 68.6 | 69.3 | 0.3 | 0.027x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 69.0 | 68.7 | 69.2 | 0.2 | 0.027x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 72.0 | 71.8 | 72.1 | 0.1 | 0.028x | 1.049x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 72.1 | 72.0 | 72.3 | 0.1 | 0.028x | 1.051x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 273.3 | 270.8 | 283.7 | 4.6 | 0.107x | 3.982x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 577.2 | 554.4 | 594.7 | 17.1 | 0.225x | 8.412x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 585.5 | 564.9 | 589.0 | 8.9 | 0.228x | 8.532x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 593.4 | 590.9 | 619.5 | 10.8 | 0.231x | 8.648x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 595.9 | 570.6 | 599.3 | 10.8 | 0.232x | 8.685x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,564.9 | 2,544.1 | 2,577.3 | 10.9 | 1.000x | 37.378x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.003x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.017x | 1.011x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.5 | 13.3 | 13.8 | 0.2 | 0.017x | 1.016x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.3 | 144.4 | 148.1 | 1.3 | 0.187x | 10.978x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.0 | 146.1 | 151.2 | 1.8 | 0.189x | 11.109x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.0 | 144.7 | 155.0 | 3.7 | 0.189x | 11.110x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.1 | 147.6 | 150.8 | 1.2 | 0.191x | 11.192x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 777.2 | 766.6 | 785.4 | 8.1 | 1.000x | 58.725x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 787.0 | 773.9 | 792.2 | 6.5 | 1.013x | 59.462x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.5 | 19.5 | 19.7 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.007x | 1.012x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.8 | 19.5 | 19.9 | 0.2 | 0.007x | 1.014x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.007x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 220.3 | 213.4 | 228.1 | 4.9 | 0.082x | 11.272x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 662.9 | 600.7 | 705.8 | 41.9 | 0.247x | 33.923x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 691.5 | 628.7 | 744.6 | 42.1 | 0.257x | 35.391x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 711.0 | 640.2 | 728.4 | 31.7 | 0.265x | 36.390x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 721.1 | 616.2 | 749.6 | 48.8 | 0.268x | 36.906x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,687.4 | 2,658.3 | 2,692.7 | 12.7 | 1.000x | 137.534x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.2 | 0.017x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.006x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.6 | 144.0 | 148.5 | 1.5 | 0.188x | 11.009x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.9 | 143.7 | 155.2 | 4.0 | 0.188x | 11.027x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 149.4 | 147.2 | 151.5 | 1.7 | 0.192x | 11.293x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.6 | 147.0 | 154.4 | 2.6 | 0.193x | 11.309x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 776.4 | 769.5 | 787.0 | 5.9 | 1.000x | 58.693x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 779.0 | 770.3 | 799.3 | 11.3 | 1.003x | 58.891x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.1 | 14.1 | 14.5 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.4 | 14.3 | 14.6 | 0.1 | 0.005x | 1.019x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.4 | 14.8 | 0.2 | 0.005x | 1.024x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.6 | 14.3 | 14.6 | 0.1 | 0.005x | 1.029x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 217.9 | 215.0 | 221.4 | 2.3 | 0.082x | 15.405x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 550.4 | 526.8 | 697.4 | 63.5 | 0.207x | 38.913x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 623.0 | 554.0 | 634.8 | 31.0 | 0.234x | 44.046x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 629.4 | 545.2 | 691.9 | 47.9 | 0.236x | 44.500x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 652.7 | 606.4 | 662.0 | 21.6 | 0.245x | 46.145x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,663.7 | 2,651.0 | 2,690.4 | 13.7 | 1.000x | 188.320x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.007x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.009x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 146.0 | 145.0 | 147.6 | 0.9 | 0.189x | 11.059x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 147.1 | 145.4 | 153.2 | 2.8 | 0.191x | 11.142x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 149.0 | 146.6 | 151.4 | 1.8 | 0.193x | 11.285x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.6 | 146.9 | 151.5 | 1.8 | 0.194x | 11.329x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 771.8 | 763.4 | 784.8 | 7.5 | 1.000x | 58.459x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 782.1 | 770.5 | 785.3 | 5.5 | 1.013x | 59.240x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.1 | 14.1 | 14.2 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.3 | 14.2 | 14.4 | 0.0 | 0.005x | 1.013x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.4 | 14.2 | 14.6 | 0.1 | 0.005x | 1.019x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.4 | 14.4 | 14.5 | 0.0 | 0.005x | 1.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 217.5 | 215.3 | 220.7 | 2.0 | 0.082x | 15.372x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 577.5 | 530.0 | 615.2 | 32.3 | 0.217x | 40.813x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 595.9 | 526.1 | 693.9 | 64.7 | 0.224x | 42.116x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 622.3 | 573.2 | 661.5 | 28.1 | 0.234x | 43.982x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 639.9 | 556.0 | 703.0 | 47.8 | 0.241x | 45.224x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,660.0 | 2,652.5 | 2,670.4 | 6.1 | 1.000x | 187.995x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.9 | 0.2 | 0.017x | 1.007x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.009x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.5 | 145.2 | 146.6 | 0.5 | 0.188x | 11.000x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 146.6 | 145.4 | 150.8 | 1.9 | 0.190x | 11.087x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 146.8 | 144.4 | 149.8 | 2.0 | 0.190x | 11.098x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.7 | 148.5 | 149.6 | 0.4 | 0.193x | 11.242x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 772.1 | 770.4 | 781.3 | 4.7 | 1.000x | 58.391x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 778.5 | 772.8 | 787.2 | 4.7 | 1.008x | 58.871x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.1 | 14.1 | 14.2 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.3 | 14.3 | 14.4 | 0.0 | 0.005x | 1.016x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.4 | 14.3 | 14.7 | 0.1 | 0.005x | 1.025x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.3 | 14.5 | 0.1 | 0.005x | 1.025x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 214.2 | 211.5 | 220.0 | 3.2 | 0.080x | 15.194x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 592.0 | 522.6 | 660.8 | 53.3 | 0.222x | 41.981x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 600.3 | 542.2 | 655.0 | 39.5 | 0.225x | 42.571x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 610.6 | 535.8 | 645.3 | 37.5 | 0.229x | 43.302x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 636.6 | 534.8 | 649.0 | 52.0 | 0.239x | 45.149x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,666.4 | 2,641.5 | 2,686.6 | 14.6 | 1.000x | 189.094x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.9 | 0.2 | 0.017x | 1.008x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.009x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.8 | 0.2 | 0.017x | 1.013x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 144.9 | 144.2 | 145.5 | 0.5 | 0.187x | 10.992x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.6 | 143.5 | 155.4 | 4.1 | 0.188x | 11.049x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.4 | 147.2 | 149.2 | 0.8 | 0.192x | 11.257x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 148.6 | 147.2 | 150.5 | 1.2 | 0.192x | 11.278x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 773.8 | 767.3 | 785.3 | 5.9 | 1.000x | 58.711x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 780.0 | 778.1 | 819.8 | 16.0 | 1.008x | 59.181x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 16.3 | 16.1 | 16.3 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 16.3 | 16.2 | 16.8 | 0.3 | 0.006x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 16.4 | 16.4 | 16.5 | 0.0 | 0.006x | 1.011x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 16.5 | 16.4 | 16.7 | 0.1 | 0.006x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 218.6 | 209.8 | 221.9 | 4.5 | 0.082x | 13.443x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 536.8 | 526.6 | 666.3 | 64.0 | 0.201x | 33.018x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 597.3 | 562.5 | 667.6 | 38.8 | 0.223x | 36.738x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 616.7 | 568.2 | 657.7 | 31.4 | 0.231x | 37.929x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 632.9 | 567.5 | 654.3 | 34.2 | 0.237x | 38.926x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,674.0 | 2,643.3 | 2,679.8 | 13.6 | 1.000x | 164.468x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,745.9 | 7,738.4 | 7,790.2 | 19.4 | 0.762x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,749.4 | 7,745.0 | 7,756.2 | 3.7 | 0.762x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,754.2 | 7,748.1 | 7,756.9 | 3.7 | 0.763x | 1.001x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,755.2 | 7,747.4 | 8,225.1 | 186.2 | 0.763x | 1.001x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 10,167.1 | 10,130.0 | 10,215.3 | 28.3 | 1.000x | 1.313x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 10,206.4 | 10,113.3 | 10,239.2 | 44.8 | 1.004x | 1.318x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,070.0 | 19,067.1 | 19,075.8 | 3.3 | 1.876x | 2.462x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,073.4 | 19,066.6 | 19,182.8 | 44.9 | 1.876x | 2.462x |
| 9 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,097.9 | 19,091.5 | 19,103.6 | 4.4 | 1.878x | 2.466x |
| 10 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,106.5 | 19,095.9 | 19,123.9 | 9.2 | 1.879x | 2.467x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,464.1 | 7,461.2 | 7,470.2 | 3.3 | 0.041x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,464.2 | 7,461.4 | 7,620.5 | 62.9 | 0.041x | 1.000x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,469.7 | 7,467.1 | 7,492.0 | 9.4 | 0.041x | 1.001x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,475.4 | 7,472.5 | 7,483.9 | 4.0 | 0.041x | 1.002x | 5 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29,179.8 | 28,990.6 | 29,201.7 | 78.1 | 0.161x | 3.909x | 5 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29,195.9 | 29,068.1 | 29,320.5 | 83.5 | 0.161x | 3.912x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 181,474.8 | 180,540.0 | 186,600.1 | 2,137.3 | 1.000x | 24.313x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 181,728.2 | 180,968.3 | 183,515.5 | 889.0 | 1.001x | 24.347x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9,550.5 | 9,550.2 | 9,552.2 | 0.7 | 0.033x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9,550.5 | 9,549.3 | 9,557.8 | 3.1 | 0.033x | 1.000x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9,561.5 | 9,557.7 | 9,577.0 | 6.7 | 0.033x | 1.001x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9,567.2 | 9,562.1 | 9,570.2 | 3.0 | 0.033x | 1.002x | 5 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72,154.8 | 71,883.0 | 73,275.2 | 601.0 | 0.248x | 7.555x | 5 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 72,293.3 | 71,975.5 | 73,170.3 | 411.2 | 0.248x | 7.570x | 5 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 290,683.7 | 289,035.8 | 293,222.9 | 1,369.0 | 0.999x | 30.436x | 5 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 290,975.4 | 289,240.3 | 291,726.3 | 875.3 | 1.000x | 30.467x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,043.2 | 19,042.4 | 19,047.9 | 2.0 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,047.2 | 19,041.4 | 19,054.1 | 4.3 | 0.022x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,077.7 | 19,065.4 | 19,097.5 | 11.0 | 0.022x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,078.7 | 19,067.8 | 19,085.9 | 6.1 | 0.022x | 1.002x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194,185.2 | 194,072.3 | 204,946.7 | 4,278.6 | 0.227x | 10.197x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 194,217.0 | 194,021.8 | 200,044.0 | 2,357.1 | 0.227x | 10.199x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194,364.9 | 193,853.4 | 220,653.9 | 10,564.8 | 0.228x | 10.207x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 194,376.3 | 194,239.7 | 194,632.2 | 134.1 | 0.228x | 10.207x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 853,818.0 | 846,089.0 | 884,443.3 | 16,079.4 | 1.000x | 44.836x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 856,424.9 | 843,206.8 | 891,748.0 | 17,490.2 | 1.003x | 44.973x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 3,738.0 | 3,737.3 | 3,739.1 | 0.7 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 3,738.1 | 3,735.2 | 3,740.5 | 1.8 | 0.052x | 1.000x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 3,740.8 | 3,738.4 | 3,742.7 | 1.6 | 0.052x | 1.001x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 3,746.5 | 3,745.4 | 3,748.3 | 1.3 | 0.052x | 1.002x | 5 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10,980.5 | 10,949.7 | 11,026.1 | 24.5 | 0.152x | 2.938x | 5 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11,027.1 | 10,975.9 | 11,107.6 | 45.7 | 0.152x | 2.950x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 72,436.0 | 71,551.3 | 73,986.6 | 791.3 | 1.000x | 19.378x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 73,033.2 | 71,908.1 | 74,142.9 | 802.6 | 1.008x | 19.538x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.9 | 0.3 | 0.018x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.7 | 0.2 | 0.018x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.018x | 1.004x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 298.2 | 283.6 | 311.9 | 10.5 | 0.339x | 18.457x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 299.9 | 284.9 | 309.2 | 7.9 | 0.341x | 18.561x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 302.4 | 265.3 | 315.9 | 18.5 | 0.344x | 18.717x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 310.5 | 296.6 | 321.8 | 9.8 | 0.353x | 19.217x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 878.5 | 874.3 | 904.1 | 13.2 | 1.000x | 54.376x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 904.1 | 874.6 | 941.5 | 22.2 | 1.029x | 55.960x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 4,787.0 | 4,785.6 | 4,787.8 | 0.8 | 0.023x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 4,787.8 | 4,784.4 | 4,788.6 | 1.5 | 0.023x | 1.000x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 4,794.5 | 4,792.5 | 4,804.9 | 4.6 | 0.023x | 1.002x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 4,797.0 | 4,793.3 | 4,798.3 | 2.0 | 0.023x | 1.002x | 5 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 99,310.0 | 93,823.6 | 100,357.4 | 2,811.4 | 0.469x | 20.746x | 5 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 99,792.2 | 98,079.8 | 101,283.0 | 1,035.8 | 0.472x | 20.847x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 211,624.0 | 211,459.2 | 213,818.0 | 912.0 | 1.000x | 44.208x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 212,821.7 | 211,105.6 | 215,922.3 | 1,579.6 | 1.006x | 44.458x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,645.4 | 7,643.8 | 7,649.2 | 1.9 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,645.9 | 7,644.6 | 7,648.3 | 1.3 | 0.052x | 1.000x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,660.7 | 7,657.2 | 7,669.9 | 4.7 | 0.052x | 1.002x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,665.8 | 7,652.6 | 7,708.3 | 25.3 | 0.052x | 1.003x | 5 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32,715.8 | 32,654.9 | 32,876.9 | 76.5 | 0.220x | 4.279x | 5 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32,949.2 | 32,703.1 | 33,055.4 | 125.3 | 0.222x | 4.310x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 148,371.8 | 148,032.4 | 149,375.9 | 456.4 | 1.000x | 19.407x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 148,600.9 | 147,906.3 | 150,185.6 | 811.3 | 1.002x | 19.437x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.0 | 0.1 | 0.061x | 1.015x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 0.064x | 1.059x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.4 | 9.5 | 11.6 | 1.0 | 0.070x | 1.163x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.0 | 47.5 | 48.4 | 0.3 | 0.295x | 4.884x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.1 | 47.6 | 57.0 | 3.6 | 0.296x | 4.895x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 49.2 | 48.9 | 49.5 | 0.2 | 0.303x | 5.013x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 49.3 | 48.8 | 49.7 | 0.3 | 0.303x | 5.020x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 162.5 | 161.0 | 167.3 | 2.2 | 1.000x | 16.554x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 165.1 | 162.0 | 168.9 | 2.4 | 1.016x | 16.813x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 21.1 | 21.1 | 21.2 | 0.0 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 21.2 | 21.1 | 21.3 | 0.1 | 0.013x | 1.003x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 21.3 | 21.0 | 21.3 | 0.1 | 0.013x | 1.007x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 21.5 | 21.2 | 21.7 | 0.2 | 0.013x | 1.018x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 141.8 | 141.4 | 142.5 | 0.4 | 0.088x | 6.710x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,172.1 | 1,116.7 | 1,255.1 | 55.8 | 0.725x | 55.475x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,180.1 | 1,170.4 | 1,288.4 | 44.3 | 0.730x | 55.857x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,192.6 | 1,188.2 | 1,251.2 | 25.6 | 0.738x | 56.447x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,195.8 | 1,108.0 | 1,255.6 | 53.4 | 0.740x | 56.601x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,616.9 | 1,602.1 | 1,626.3 | 7.8 | 1.000x | 76.528x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.7 | 33.6 | 34.1 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.6 | 33.8 | 0.1 | 0.032x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.1 | 35.8 | 38.5 | 1.0 | 0.034x | 1.071x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 36.2 | 35.9 | 36.5 | 0.2 | 0.034x | 1.074x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 197.3 | 196.8 | 197.6 | 0.3 | 0.185x | 5.856x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 198.1 | 198.0 | 199.1 | 0.4 | 0.186x | 5.880x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 199.5 | 199.3 | 209.9 | 4.2 | 0.187x | 5.920x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 202.2 | 202.1 | 202.9 | 0.3 | 0.189x | 6.002x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,067.2 | 1,057.1 | 1,077.7 | 6.5 | 1.000x | 31.675x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,071.4 | 1,055.1 | 1,089.6 | 11.0 | 1.004x | 31.799x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.7 | 62.6 | 63.1 | 0.2 | 0.059x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 66.0 | 65.3 | 75.4 | 3.8 | 0.062x | 1.054x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 66.0 | 65.9 | 66.3 | 0.1 | 0.062x | 1.054x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 172.8 | 172.3 | 174.2 | 0.7 | 0.162x | 2.759x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 198.4 | 197.7 | 201.0 | 1.4 | 0.186x | 3.168x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 203.4 | 203.1 | 205.8 | 1.0 | 0.191x | 3.249x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 205.7 | 205.5 | 206.4 | 0.4 | 0.193x | 3.286x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 205.8 | 205.1 | 207.9 | 1.0 | 0.193x | 3.287x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,067.5 | 1,058.4 | 1,078.4 | 7.8 | 1.000x | 17.049x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.3 | 0.0 | 0.032x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.4 | 34.3 | 35.5 | 0.4 | 0.034x | 1.067x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.8 | 34.5 | 36.0 | 0.5 | 0.035x | 1.080x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 171.0 | 170.7 | 173.4 | 1.0 | 0.170x | 5.300x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 172.4 | 171.5 | 173.7 | 0.8 | 0.172x | 5.344x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 175.1 | 174.7 | 179.5 | 1.8 | 0.174x | 5.427x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 176.2 | 175.9 | 177.6 | 0.6 | 0.176x | 5.462x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,003.9 | 997.4 | 1,012.1 | 4.8 | 1.000x | 31.120x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,008.2 | 1,001.2 | 1,021.6 | 6.7 | 1.004x | 31.255x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.5 | 58.5 | 61.2 | 1.1 | 0.058x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.2 | 62.0 | 62.3 | 0.1 | 0.061x | 1.066x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 62.1 | 62.4 | 0.1 | 0.062x | 1.069x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 159.6 | 157.9 | 160.8 | 1.1 | 0.158x | 2.739x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 167.5 | 166.9 | 168.2 | 0.4 | 0.166x | 2.874x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 169.6 | 167.4 | 171.7 | 1.5 | 0.168x | 2.910x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 170.3 | 169.9 | 172.4 | 0.9 | 0.168x | 2.922x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 176.3 | 175.8 | 176.5 | 0.3 | 0.174x | 3.024x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,010.9 | 1,002.4 | 1,013.2 | 3.8 | 1.000x | 17.346x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.7 | 16.7 | 16.8 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.9 | 0.1 | 0.025x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.2 | 0.1 | 0.028x | 1.143x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.4 | 0.1 | 0.028x | 1.144x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 76.4 | 75.6 | 80.3 | 1.7 | 0.112x | 4.564x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 77.1 | 76.8 | 82.1 | 2.0 | 0.113x | 4.606x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 86.5 | 86.5 | 86.7 | 0.1 | 0.127x | 5.169x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 86.9 | 86.8 | 87.6 | 0.3 | 0.127x | 5.191x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 682.0 | 681.3 | 690.2 | 3.5 | 1.000x | 40.740x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 687.9 | 678.3 | 702.4 | 8.7 | 1.009x | 41.096x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 23.2 | 23.0 | 23.4 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 23.3 | 23.2 | 24.0 | 0.3 | 0.034x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 25.7 | 25.5 | 25.8 | 0.1 | 0.038x | 1.109x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 25.8 | 25.4 | 26.0 | 0.2 | 0.038x | 1.114x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 81.9 | 81.7 | 82.2 | 0.2 | 0.120x | 3.531x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 84.2 | 84.2 | 85.6 | 0.5 | 0.123x | 3.631x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 87.8 | 87.8 | 88.3 | 0.2 | 0.128x | 3.786x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 89.7 | 89.6 | 89.8 | 0.1 | 0.131x | 3.868x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 104.1 | 103.7 | 109.3 | 2.1 | 0.152x | 4.489x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 684.2 | 681.2 | 690.1 | 2.9 | 1.000x | 29.500x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 11.8 | 12.5 | 0.3 | 0.019x | 1.028x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.8 | 0.1 | 0.020x | 1.066x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.5 | 12.2 | 13.8 | 0.6 | 0.021x | 1.135x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.6 | 143.8 | 148.3 | 1.5 | 0.229x | 12.189x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.7 | 145.1 | 150.6 | 2.1 | 0.229x | 12.204x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.3 | 146.6 | 151.1 | 1.5 | 0.233x | 12.416x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 149.0 | 146.8 | 149.3 | 0.9 | 0.234x | 12.478x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 636.6 | 633.0 | 642.3 | 3.2 | 1.000x | 53.307x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 637.4 | 630.9 | 663.8 | 12.7 | 1.001x | 53.377x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 27.2 | 27.1 | 27.3 | 0.1 | 0.012x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 27.2 | 27.0 | 27.3 | 0.1 | 0.012x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 27.2 | 27.1 | 27.3 | 0.1 | 0.012x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 27.3 | 27.2 | 27.6 | 0.1 | 0.012x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 203.3 | 203.3 | 204.7 | 0.5 | 0.091x | 7.477x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,386.8 | 1,358.3 | 1,492.8 | 48.5 | 0.620x | 50.995x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,395.9 | 1,291.6 | 1,466.5 | 60.6 | 0.624x | 51.328x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,420.6 | 1,398.9 | 1,460.1 | 23.1 | 0.635x | 52.238x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,448.3 | 1,374.6 | 1,503.5 | 43.6 | 0.648x | 53.255x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,235.9 | 2,223.6 | 2,246.5 | 7.9 | 1.000x | 82.216x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 28.0 | 27.9 | 30.5 | 1.0 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.2 | 0.1 | 0.033x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.4 | 0.1 | 0.035x | 1.079x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.3 | 30.2 | 30.5 | 0.1 | 0.036x | 1.083x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 139.1 | 138.8 | 142.0 | 1.2 | 0.163x | 4.967x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 140.8 | 140.3 | 141.2 | 0.3 | 0.165x | 5.027x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 142.0 | 140.9 | 168.0 | 10.6 | 0.166x | 5.069x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 143.6 | 142.5 | 144.1 | 0.6 | 0.168x | 5.129x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 853.5 | 845.8 | 870.3 | 9.2 | 1.000x | 30.477x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 865.2 | 846.2 | 884.5 | 13.0 | 1.014x | 30.896x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 48.5 | 48.4 | 49.6 | 0.5 | 0.057x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 48.5 | 48.3 | 48.7 | 0.2 | 0.057x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.9 | 51.9 | 52.0 | 0.0 | 0.061x | 1.070x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 52.0 | 51.4 | 52.1 | 0.2 | 0.061x | 1.072x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 144.5 | 144.1 | 145.0 | 0.3 | 0.170x | 2.979x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 145.4 | 145.2 | 145.6 | 0.1 | 0.171x | 2.996x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 145.4 | 144.8 | 147.9 | 1.1 | 0.171x | 2.997x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 147.8 | 147.4 | 148.8 | 0.5 | 0.174x | 3.046x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 148.9 | 148.6 | 149.4 | 0.3 | 0.175x | 3.068x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 849.3 | 843.4 | 854.4 | 3.7 | 1.000x | 17.502x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.6 | 55.2 | 55.8 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.7 | 55.3 | 56.0 | 0.2 | 0.064x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 59.8 | 59.5 | 60.8 | 0.4 | 0.069x | 1.076x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 60.1 | 59.4 | 61.8 | 0.8 | 0.069x | 1.082x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 154.8 | 154.2 | 155.1 | 0.3 | 0.178x | 2.786x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 156.6 | 155.6 | 157.6 | 0.7 | 0.180x | 2.817x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 157.3 | 156.5 | 183.4 | 10.6 | 0.181x | 2.831x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 159.1 | 158.5 | 159.4 | 0.3 | 0.183x | 2.864x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 868.6 | 857.3 | 873.0 | 5.5 | 1.000x | 15.632x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 876.1 | 864.3 | 890.4 | 9.6 | 1.009x | 15.767x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 109.6 | 109.5 | 110.5 | 0.4 | 0.125x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 109.9 | 109.6 | 110.6 | 0.4 | 0.125x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 113.3 | 112.8 | 113.9 | 0.4 | 0.129x | 1.034x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 113.3 | 112.9 | 113.7 | 0.3 | 0.129x | 1.034x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 159.9 | 159.5 | 160.7 | 0.4 | 0.182x | 1.460x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 160.6 | 160.4 | 160.9 | 0.2 | 0.183x | 1.466x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 161.0 | 160.8 | 161.8 | 0.4 | 0.183x | 1.470x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 164.4 | 163.8 | 165.3 | 0.5 | 0.187x | 1.500x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 164.7 | 163.8 | 165.8 | 0.8 | 0.187x | 1.504x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 878.9 | 868.1 | 887.8 | 6.4 | 1.000x | 8.023x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.7 | 42.6 | 43.0 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 42.8 | 42.7 | 44.6 | 0.8 | 0.019x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 42.8 | 42.7 | 42.8 | 0.0 | 0.019x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.9 | 42.6 | 43.1 | 0.2 | 0.019x | 1.003x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 738.2 | 735.9 | 789.7 | 20.7 | 0.333x | 17.276x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 739.7 | 736.5 | 743.8 | 2.4 | 0.333x | 17.312x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 1,054.9 | 1,044.3 | 1,071.9 | 9.8 | 0.476x | 24.689x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 1,055.5 | 1,048.3 | 1,100.5 | 19.3 | 0.476x | 24.704x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,218.2 | 2,206.5 | 2,255.4 | 18.6 | 1.000x | 51.915x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 2,232.4 | 2,215.9 | 2,275.5 | 21.7 | 1.006x | 52.246x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 89.4 | 89.2 | 89.5 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 89.6 | 89.2 | 90.3 | 0.4 | 0.029x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 93.1 | 93.0 | 93.3 | 0.1 | 0.030x | 1.041x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 93.2 | 93.0 | 93.4 | 0.1 | 0.030x | 1.042x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 407.1 | 404.3 | 409.5 | 1.8 | 0.131x | 4.552x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 912.8 | 909.9 | 915.4 | 2.1 | 0.293x | 10.206x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 916.1 | 915.4 | 919.7 | 1.6 | 0.294x | 10.243x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,256.7 | 1,233.2 | 1,267.3 | 11.4 | 0.404x | 14.051x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,257.8 | 1,248.5 | 1,272.0 | 8.3 | 0.404x | 14.063x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,113.9 | 3,110.2 | 3,161.3 | 19.7 | 1.000x | 34.817x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.0 | 0.3 | 0.017x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.011x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 145.4 | 144.5 | 148.5 | 1.4 | 0.185x | 11.019x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 145.6 | 144.3 | 146.2 | 0.7 | 0.185x | 11.034x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 146.7 | 145.4 | 150.1 | 1.7 | 0.186x | 11.113x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 148.2 | 148.1 | 151.0 | 1.2 | 0.188x | 11.226x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 785.4 | 771.4 | 828.1 | 22.0 | 0.997x | 59.513x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 788.1 | 778.9 | 798.9 | 6.6 | 1.000x | 59.718x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.0 | 0.008x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 20.7 | 20.6 | 21.1 | 0.2 | 0.008x | 1.010x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.7 | 20.6 | 20.8 | 0.1 | 0.008x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 220.4 | 214.6 | 221.5 | 2.5 | 0.082x | 10.777x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 750.7 | 725.3 | 854.2 | 49.7 | 0.279x | 36.705x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 770.1 | 724.9 | 871.5 | 59.2 | 0.286x | 37.649x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 833.0 | 780.9 | 917.9 | 53.3 | 0.310x | 40.727x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 837.6 | 731.6 | 890.2 | 66.5 | 0.311x | 40.952x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,690.5 | 2,676.0 | 2,708.5 | 11.1 | 1.000x | 131.540x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.0 | 0.3 | 0.017x | 1.007x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.009x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.010x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 191.3 | 188.5 | 192.5 | 1.5 | 0.242x | 14.508x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 191.8 | 182.5 | 197.4 | 4.9 | 0.243x | 14.548x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 193.7 | 189.5 | 196.0 | 2.2 | 0.245x | 14.690x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 194.6 | 189.5 | 197.0 | 2.8 | 0.247x | 14.761x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 785.2 | 770.6 | 814.9 | 16.0 | 0.995x | 59.550x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 789.2 | 782.2 | 798.4 | 5.9 | 1.000x | 59.853x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.7 | 26.6 | 26.9 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.8 | 26.7 | 27.2 | 0.2 | 0.010x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.8 | 26.6 | 26.9 | 0.1 | 0.010x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.9 | 26.7 | 26.9 | 0.1 | 0.010x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 231.5 | 226.5 | 238.2 | 3.8 | 0.087x | 8.671x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,122.3 | 1,103.9 | 1,178.1 | 30.2 | 0.420x | 42.037x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,167.9 | 1,099.5 | 1,229.4 | 54.1 | 0.438x | 43.745x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,177.7 | 1,117.6 | 1,211.4 | 30.5 | 0.441x | 44.114x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,180.5 | 1,166.8 | 1,292.4 | 51.3 | 0.442x | 44.218x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,669.1 | 2,648.7 | 2,691.8 | 13.7 | 1.000x | 99.975x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.031x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.6 | 34.4 | 34.9 | 0.1 | 0.033x | 1.071x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.8 | 34.5 | 35.2 | 0.2 | 0.034x | 1.077x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 173.4 | 173.3 | 173.5 | 0.1 | 0.167x | 5.371x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 174.8 | 174.1 | 176.7 | 0.9 | 0.169x | 5.413x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 176.5 | 176.5 | 176.5 | 0.0 | 0.170x | 5.466x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 177.2 | 176.8 | 177.5 | 0.2 | 0.171x | 5.488x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,036.7 | 1,021.5 | 1,039.9 | 6.7 | 1.000x | 32.109x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,046.2 | 1,036.9 | 1,062.5 | 8.3 | 1.009x | 32.404x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.4 | 58.2 | 58.8 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.3 | 58.8 | 0.2 | 0.056x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.0 | 62.0 | 63.1 | 0.4 | 0.060x | 1.063x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.4 | 62.2 | 62.6 | 0.1 | 0.060x | 1.069x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 108.0 | 106.9 | 109.0 | 0.9 | 0.104x | 1.850x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 174.0 | 173.9 | 174.8 | 0.3 | 0.168x | 2.981x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 174.1 | 174.1 | 174.3 | 0.1 | 0.168x | 2.983x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 175.8 | 175.7 | 177.3 | 0.7 | 0.170x | 3.011x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 176.3 | 176.0 | 178.7 | 1.0 | 0.170x | 3.020x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,036.4 | 1,021.5 | 1,048.5 | 8.7 | 1.000x | 17.756x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.9 | 0.2 | 0.031x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.5 | 34.4 | 35.7 | 0.6 | 0.033x | 1.069x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.7 | 34.4 | 34.8 | 0.1 | 0.034x | 1.075x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 173.7 | 173.3 | 179.6 | 2.4 | 0.168x | 5.383x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 174.9 | 174.1 | 175.1 | 0.4 | 0.169x | 5.420x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 176.5 | 176.4 | 176.6 | 0.1 | 0.171x | 5.472x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 177.0 | 176.9 | 179.0 | 0.8 | 0.171x | 5.487x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,034.7 | 1,018.8 | 1,040.0 | 7.5 | 1.000x | 32.074x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,049.6 | 1,042.0 | 1,060.1 | 6.3 | 1.014x | 32.536x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.2 | 58.1 | 58.4 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.2 | 58.2 | 58.7 | 0.2 | 0.056x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 62.2 | 63.1 | 0.3 | 0.060x | 1.071x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.7 | 62.0 | 62.8 | 0.4 | 0.061x | 1.077x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 107.7 | 106.4 | 111.5 | 1.9 | 0.104x | 1.850x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 174.0 | 173.6 | 174.2 | 0.2 | 0.169x | 2.989x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 174.2 | 174.1 | 174.4 | 0.1 | 0.169x | 2.992x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 175.7 | 175.6 | 175.8 | 0.1 | 0.170x | 3.017x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 176.3 | 176.2 | 176.7 | 0.2 | 0.171x | 3.028x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,031.5 | 1,018.0 | 1,043.8 | 8.3 | 1.000x | 17.717x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.0 | 0.028x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.2 | 32.5 | 0.1 | 0.028x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.4 | 34.3 | 35.0 | 0.3 | 0.030x | 1.065x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.4 | 34.4 | 35.9 | 0.6 | 0.031x | 1.095x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 166.2 | 164.4 | 166.6 | 0.8 | 0.145x | 5.143x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 166.5 | 165.4 | 166.9 | 0.5 | 0.146x | 5.151x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 168.9 | 168.5 | 170.9 | 0.9 | 0.148x | 5.225x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 169.1 | 169.1 | 169.4 | 0.1 | 0.148x | 5.232x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,142.7 | 1,128.7 | 1,158.3 | 10.1 | 1.000x | 35.354x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,155.2 | 1,138.4 | 1,173.7 | 11.2 | 1.011x | 35.740x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.1 | 58.8 | 0.2 | 0.051x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 62.1 | 62.5 | 0.2 | 0.055x | 1.069x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.3 | 62.0 | 62.6 | 0.2 | 0.055x | 1.069x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 108.3 | 107.3 | 111.9 | 1.6 | 0.095x | 1.859x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 168.4 | 168.2 | 170.2 | 0.7 | 0.148x | 2.889x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 168.4 | 168.2 | 168.7 | 0.2 | 0.148x | 2.890x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 170.1 | 170.0 | 170.2 | 0.1 | 0.149x | 2.919x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 171.5 | 171.5 | 171.7 | 0.1 | 0.151x | 2.943x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,139.6 | 1,128.3 | 1,142.1 | 4.9 | 1.000x | 19.555x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.030x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.4 | 34.4 | 35.9 | 0.6 | 0.032x | 1.067x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.5 | 34.2 | 36.4 | 0.8 | 0.032x | 1.069x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 159.6 | 158.8 | 161.7 | 1.2 | 0.148x | 4.947x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 159.6 | 159.3 | 160.8 | 0.6 | 0.148x | 4.947x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 160.9 | 160.9 | 161.4 | 0.2 | 0.149x | 4.988x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 161.6 | 161.3 | 162.2 | 0.3 | 0.150x | 5.011x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,077.5 | 1,071.5 | 1,091.5 | 6.7 | 1.000x | 33.400x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,092.1 | 1,084.8 | 1,106.2 | 8.6 | 1.014x | 33.852x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.2 | 58.1 | 58.6 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.5 | 58.3 | 61.3 | 1.1 | 0.054x | 1.005x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.1 | 62.0 | 62.6 | 0.2 | 0.058x | 1.067x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.2 | 62.1 | 62.4 | 0.1 | 0.058x | 1.070x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 107.4 | 107.2 | 115.8 | 3.3 | 0.100x | 1.846x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 161.1 | 160.8 | 161.3 | 0.1 | 0.150x | 2.770x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 162.7 | 162.5 | 162.9 | 0.1 | 0.151x | 2.797x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 162.9 | 162.7 | 164.5 | 0.6 | 0.152x | 2.801x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 163.4 | 162.9 | 165.8 | 1.0 | 0.152x | 2.809x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,075.1 | 1,069.2 | 1,095.0 | 10.1 | 1.000x | 18.483x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.0 | 0.3 | 0.030x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x | 1.068x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.5 | 34.3 | 34.8 | 0.2 | 0.032x | 1.068x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 159.0 | 158.8 | 159.3 | 0.2 | 0.148x | 4.920x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 159.7 | 159.3 | 161.7 | 0.9 | 0.149x | 4.939x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 161.0 | 160.9 | 161.5 | 0.2 | 0.150x | 4.979x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 162.1 | 161.1 | 163.1 | 0.7 | 0.151x | 5.014x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,072.1 | 1,070.5 | 1,082.2 | 4.3 | 1.000x | 33.162x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,088.9 | 1,085.9 | 1,102.1 | 6.1 | 1.016x | 33.683x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.4 | 58.2 | 58.5 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.2 | 59.0 | 0.3 | 0.054x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.0 | 62.0 | 62.3 | 0.1 | 0.057x | 1.063x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 62.2 | 62.5 | 0.1 | 0.058x | 1.068x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 107.6 | 107.0 | 115.6 | 3.3 | 0.099x | 1.843x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 161.0 | 160.9 | 161.3 | 0.2 | 0.149x | 2.758x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 162.7 | 162.6 | 163.9 | 0.5 | 0.150x | 2.787x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 163.0 | 162.8 | 163.5 | 0.3 | 0.151x | 2.792x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 163.2 | 163.1 | 163.4 | 0.1 | 0.151x | 2.796x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,081.8 | 1,073.1 | 1,091.8 | 7.6 | 1.000x | 18.535x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.001x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 295.5 | 283.4 | 316.0 | 13.6 | 0.323x | 18.352x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 307.0 | 278.3 | 319.7 | 13.8 | 0.335x | 19.063x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 308.9 | 284.1 | 310.3 | 10.0 | 0.337x | 19.184x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 312.5 | 291.3 | 313.5 | 10.2 | 0.341x | 19.405x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 914.0 | 907.6 | 948.5 | 17.7 | 0.998x | 56.755x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 915.7 | 900.8 | 923.9 | 8.7 | 1.000x | 56.860x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.1 | 26.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.008x | 1.003x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.8 | 26.6 | 0.2 | 0.008x | 1.003x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.5 | 26.2 | 26.6 | 0.1 | 0.008x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 309.8 | 306.4 | 323.5 | 7.7 | 0.097x | 11.825x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 1,721.9 | 1,711.3 | 1,732.4 | 7.3 | 0.538x | 65.716x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 1,726.8 | 1,721.8 | 1,749.0 | 9.8 | 0.539x | 65.903x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,744.6 | 1,713.4 | 1,768.8 | 19.0 | 0.545x | 66.582x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,746.2 | 1,725.1 | 1,751.3 | 9.2 | 0.545x | 66.643x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,201.4 | 3,179.1 | 3,208.6 | 10.6 | 1.000x | 122.180x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.1 | 0.1 | 0.360x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.9 | 10.4 | 12.1 | 0.7 | 0.361x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.0 | 10.8 | 11.6 | 0.3 | 0.363x | 1.010x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 11.0 | 12.5 | 0.6 | 0.365x | 1.014x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 2.778x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 30.4 | 30.3 | 30.8 | 0.2 | 1.002x | 2.784x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 47.1 | 46.5 | 47.6 | 0.4 | 1.553x | 4.314x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 47.1 | 46.8 | 47.3 | 0.2 | 1.554x | 4.318x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.1 | 47.6 | 48.3 | 0.3 | 1.589x | 4.415x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.2 | 47.9 | 49.3 | 0.5 | 1.591x | 4.421x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 4.4 | 4.4 | 5.5 | 0.4 | 0.146x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 4.8 | 4.7 | 5.3 | 0.2 | 0.157x | 1.075x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 5.4 | 5.4 | 6.7 | 0.5 | 0.178x | 1.220x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.184x | 1.262x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.5 | 30.4 | 30.9 | 0.2 | 1.000x | 6.858x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 40.3 | 39.9 | 40.6 | 0.3 | 1.321x | 9.060x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 49.0 | 48.8 | 50.6 | 0.7 | 1.609x | 11.031x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 49.8 | 49.2 | 50.1 | 0.3 | 1.633x | 11.198x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 50.2 | 49.5 | 50.4 | 0.3 | 1.647x | 11.296x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 52.3 | 52.2 | 52.6 | 0.1 | 1.717x | 11.777x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.5 | 9.7 | 0.1 | 0.321x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 0.324x | 1.009x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.330x | 1.029x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.9 | 0.2 | 0.350x | 1.091x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 3.113x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 3.114x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 47.4 | 47.0 | 47.6 | 0.2 | 1.565x | 4.872x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 47.6 | 47.2 | 47.8 | 0.2 | 1.571x | 4.890x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.4 | 48.3 | 48.8 | 0.2 | 1.596x | 4.968x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.6 | 48.4 | 49.5 | 0.4 | 1.602x | 4.989x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 5.3 | 5.0 | 5.4 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 5.4 | 5.3 | 5.7 | 0.1 | 0.179x | 1.025x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 6.4 | 6.2 | 6.8 | 0.2 | 0.210x | 1.203x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 6.5 | 6.5 | 7.7 | 0.5 | 0.214x | 1.225x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.4 | 30.4 | 30.8 | 0.1 | 1.000x | 5.725x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 40.1 | 39.9 | 40.4 | 0.2 | 1.318x | 7.548x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 65.5 | 64.1 | 66.5 | 0.9 | 2.154x | 12.331x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 66.7 | 66.4 | 68.4 | 0.8 | 2.192x | 12.552x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 68.7 | 67.8 | 70.7 | 1.0 | 2.258x | 12.929x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 71.0 | 69.7 | 71.1 | 0.5 | 2.332x | 13.352x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.0 | 0.0 | 0.322x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.1 | 12.7 | 0.6 | 0.331x | 1.025x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.4 | 11.3 | 12.4 | 0.4 | 0.336x | 1.041x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.2 | 0.1 | 0.354x | 1.099x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 33.9 | 33.8 | 34.6 | 0.3 | 1.000x | 3.101x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 34.7 | 33.9 | 35.3 | 0.5 | 1.025x | 3.178x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 110.3 | 109.5 | 113.3 | 1.4 | 3.256x | 10.096x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 111.0 | 108.7 | 115.3 | 2.3 | 3.277x | 10.162x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 111.8 | 110.3 | 113.2 | 1.1 | 3.299x | 10.232x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 112.3 | 111.1 | 113.8 | 1.0 | 3.316x | 10.283x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 36.3 | 35.4 | 37.3 | 0.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 46.4 | 46.3 | 46.4 | 0.0 | 1.276x | 1.276x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 72.7 | 72.4 | 72.8 | 0.2 | 2.001x | 2.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 72.9 | 72.7 | 73.1 | 0.2 | 2.008x | 2.008x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 73.6 | 73.5 | 74.5 | 0.4 | 2.027x | 2.027x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 73.6 | 73.1 | 74.2 | 0.3 | 2.028x | 2.028x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,839.2 | 2,836.3 | 2,900.3 | 24.6 | 78.190x | 78.190x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 2,859.9 | 2,830.6 | 3,036.6 | 75.1 | 78.759x | 78.759x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 2,868.2 | 2,864.7 | 2,934.3 | 26.8 | 78.988x | 78.988x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 2,877.6 | 2,869.2 | 2,914.7 | 18.4 | 79.246x | 79.246x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.2 | 0.1 | 0.579x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 0.580x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 0.580x | 1.001x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 0.583x | 1.006x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 33.0 | 32.7 | 34.7 | 0.8 | 1.000x | 1.726x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 34.4 | 34.3 | 35.2 | 0.3 | 1.043x | 1.800x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 164.0 | 162.5 | 166.7 | 1.6 | 4.969x | 8.577x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 164.2 | 162.2 | 165.6 | 1.2 | 4.976x | 8.588x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 166.3 | 163.4 | 170.3 | 2.3 | 5.037x | 8.694x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 167.7 | 166.1 | 168.0 | 0.7 | 5.081x | 8.770x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 16.1 | 16.1 | 16.5 | 0.2 | 0.473x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 16.2 | 16.1 | 17.0 | 0.3 | 0.474x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 16.3 | 16.2 | 16.4 | 0.1 | 0.478x | 1.011x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 16.3 | 16.3 | 16.4 | 0.1 | 0.479x | 1.013x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 34.1 | 34.0 | 35.1 | 0.4 | 1.000x | 2.116x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.3 | 44.3 | 44.4 | 0.1 | 1.299x | 2.749x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 790.4 | 768.5 | 824.2 | 21.0 | 23.178x | 49.042x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 810.9 | 768.7 | 866.8 | 31.7 | 23.777x | 50.310x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 816.7 | 781.9 | 821.3 | 14.6 | 23.947x | 50.670x |
| 10 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 837.8 | 821.2 | 856.9 | 14.0 | 24.568x | 51.984x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,581,417.1 | 3,579,713.5 | 3,585,395.3 | 2,084.5 | 0.069x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,581,485.2 | 3,575,620.5 | 3,714,875.4 | 53,552.4 | 0.069x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,584,231.2 | 3,579,699.4 | 3,584,990.0 | 1,970.1 | 0.069x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,588,937.2 | 3,586,878.6 | 3,598,651.7 | 4,198.3 | 0.070x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 7,031,195.0 | 6,979,358.0 | 7,057,785.3 | 28,652.1 | 0.136x | 1.963x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 11,068,535.0 | 10,733,163.0 | 13,251,238.0 | 914,437.3 | 0.214x | 3.091x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 11,639,288.0 | 11,107,086.0 | 12,408,393.0 | 461,188.9 | 0.225x | 3.250x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 11,887,350.0 | 11,405,027.0 | 13,862,231.0 | 849,554.5 | 0.230x | 3.319x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12,204,220.0 | 11,456,745.0 | 12,883,584.0 | 460,305.1 | 0.236x | 3.408x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 51,615,885.8 | 51,304,264.0 | 52,022,538.5 | 284,120.8 | 1.000x | 14.412x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 18,798.8 | 18,672.9 | 18,972.7 | 113.2 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 1,877,627.3 | 1,876,565.4 | 1,886,670.4 | 3,759.9 | 99.880x | 99.880x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 1,879,469.6 | 1,875,068.2 | 1,887,372.7 | 4,969.2 | 99.978x | 99.978x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 1,881,379.0 | 1,877,943.1 | 1,890,945.6 | 4,695.8 | 100.080x | 100.080x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 1,891,541.7 | 1,889,089.9 | 1,896,202.9 | 2,429.5 | 100.620x | 100.620x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 17,589,931.3 | 17,552,497.7 | 17,676,695.0 | 42,309.9 | 935.693x | 935.693x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 84,163,304.0 | 83,289,168.0 | 90,624,651.0 | 2,981,935.3 | 4477.052x | 4477.052x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 84,428,288.0 | 83,695,475.0 | 89,394,618.0 | 2,336,118.2 | 4491.148x | 4491.148x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 84,673,810.0 | 83,837,085.0 | 85,471,734.0 | 622,370.8 | 4504.209x | 4504.209x |
| 10 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 84,810,791.0 | 83,147,550.0 | 86,117,238.0 | 963,194.5 | 4511.495x | 4511.495x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 18,761.9 | 18,621.4 | 18,785.8 | 71.3 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 1,875,293.9 | 1,874,473.9 | 1,890,304.6 | 6,081.8 | 99.952x | 99.952x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 1,876,184.2 | 1,875,029.7 | 1,883,934.8 | 3,543.8 | 100.000x | 100.000x | 5 | 100% |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 1,877,090.2 | 1,875,636.1 | 1,891,546.8 | 6,013.5 | 100.048x | 100.048x | 5 | 100% |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 1,878,044.0 | 1,876,100.5 | 1,898,775.9 | 8,532.0 | 100.099x | 100.099x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,137,206.7 | 3,121,378.4 | 3,158,632.2 | 13,287.6 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,149,477.5 | 3,131,450.4 | 3,160,155.8 | 11,463.0 | 0.007x | 1.004x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,190,860.9 | 3,180,049.5 | 3,204,099.7 | 7,837.1 | 0.007x | 1.017x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,198,130.0 | 3,181,344.2 | 3,221,693.9 | 13,692.0 | 0.007x | 1.019x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 42,743,471.0 | 42,677,077.0 | 43,235,138.3 | 205,178.3 | 0.096x | 13.625x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 101,043,491.0 | 99,738,183.0 | 118,828,272.0 | 8,417,120.6 | 0.226x | 32.208x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 105,545,892.0 | 99,130,185.0 | 116,018,334.0 | 6,447,326.9 | 0.236x | 33.643x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 109,997,738.0 | 105,797,194.0 | 116,888,179.0 | 3,862,132.4 | 0.246x | 35.062x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 116,495,339.0 | 106,043,167.0 | 121,751,489.0 | 5,198,372.7 | 0.260x | 37.133x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 447,267,822.4 | 446,157,442.5 | 452,012,100.1 | 2,246,381.8 | 1.000x | 142.569x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 18,846.0 | 18,750.9 | 19,031.6 | 94.9 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,092,666.6 | 3,082,447.1 | 3,098,093.6 | 5,314.4 | 164.102x | 164.102x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,099,418.9 | 3,089,559.4 | 3,113,057.2 | 8,833.6 | 164.460x | 164.460x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,157,983.1 | 3,136,546.8 | 3,162,948.2 | 9,308.8 | 167.568x | 167.568x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,166,592.9 | 3,147,195.3 | 3,177,016.8 | 9,675.8 | 168.025x | 168.025x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 22,545,364.0 | 22,516,477.0 | 23,129,297.3 | 250,645.8 | 1196.294x | 1196.294x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 98,751,873.0 | 97,612,716.0 | 116,217,796.0 | 7,943,807.3 | 5239.938x | 5239.938x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 99,774,883.0 | 97,301,189.0 | 117,139,853.0 | 7,493,961.0 | 5294.221x | 5294.221x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 100,302,832.0 | 98,512,922.0 | 102,903,057.0 | 1,503,431.5 | 5322.235x | 5322.235x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 112,022,042.0 | 98,318,421.0 | 115,256,721.0 | 5,938,688.2 | 5944.075x | 5944.075x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.830x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.3 | 0.2 | 0.341x | 1.948x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.0 | 0.342x | 1.955x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 0.355x | 2.029x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.0 | 0.355x | 2.030x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.3 | 1.000x | 5.712x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.003x | 5.728x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 14.0 | 0.4 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.132x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.9 | 17.8 | 18.5 | 0.2 | 0.178x | 1.378x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 18.0 | 19.2 | 0.4 | 0.180x | 1.395x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 18.2 | 17.7 | 18.6 | 0.3 | 0.180x | 1.399x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.1 | 20.9 | 0.9 | 0.187x | 1.451x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.258x | 2.005x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 26.4 | 0.2 | 0.259x | 2.009x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.435x | 3.377x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 101.0 | 99.7 | 105.6 | 2.1 | 1.000x | 7.762x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.5 | 0.2 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.824x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.335x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.340x | 1.958x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.352x | 2.029x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.0 | 0.356x | 2.051x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 30.5 | 0.7 | 0.994x | 5.727x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.6 | 29.7 | 0.4 | 1.000x | 5.763x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.136x | 1.019x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.177x | 1.327x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 0.177x | 1.328x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.180x | 1.351x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 19.2 | 0.5 | 0.181x | 1.356x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 0.285x | 2.138x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.288x | 2.155x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.8 | 44.5 | 0.3 | 0.439x | 3.291x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.9 | 98.7 | 101.4 | 1.0 | 1.000x | 7.491x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.337x | 1.937x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.341x | 1.960x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.355x | 2.041x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.357x | 2.051x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.726x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 5.745x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.1 | 12.1 | 12.7 | 0.2 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.073x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16.9 | 16.8 | 17.0 | 0.1 | 0.169x | 1.392x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.4 | 18.0 | 0.2 | 0.175x | 1.441x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 0.178x | 1.463x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.178x | 1.463x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.491x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.1 | 0.1 | 0.182x | 1.496x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.6 | 44.6 | 0.4 | 0.440x | 3.618x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 99.1 | 101.4 | 0.8 | 1.000x | 8.221x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.342x | 1.946x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.343x | 1.951x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.2 | 1.000x | 5.689x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.007x | 5.729x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 15.2 | 15.1 | 15.9 | 0.3 | 0.150x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.4 | 15.3 | 15.5 | 0.1 | 0.152x | 1.011x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.175x | 1.165x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.2 | 0.2 | 0.176x | 1.168x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.178x | 1.185x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.179x | 1.191x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.433x | 2.880x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 53.0 | 52.9 | 53.1 | 0.1 | 0.525x | 3.488x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 53.3 | 53.2 | 53.7 | 0.2 | 0.528x | 3.512x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 101.0 | 96.0 | 101.4 | 2.3 | 1.000x | 6.646x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.341x | 1.947x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.342x | 1.952x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.355x | 2.024x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 32.2 | 1.4 | 1.000x | 5.704x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 1.003x | 5.719x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.1 | 0.183x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.6 | 18.5 | 18.7 | 0.1 | 0.186x | 1.017x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.7 | 18.0 | 18.8 | 0.3 | 0.187x | 1.022x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 19.7 | 19.6 | 19.8 | 0.1 | 0.198x | 1.080x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 20.6 | 20.6 | 20.8 | 0.1 | 0.207x | 1.131x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.9 | 44.5 | 45.4 | 0.3 | 0.450x | 2.458x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 80.7 | 80.6 | 81.0 | 0.1 | 0.810x | 4.421x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 80.7 | 80.4 | 81.9 | 0.5 | 0.810x | 4.421x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.6 | 97.9 | 101.6 | 1.2 | 1.000x | 5.457x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.2 | 0.321x | 1.825x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.937x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.341x | 1.941x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 2.040x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.691x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.1 | 29.1 | 0.3 | 1.008x | 5.740x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.2 | 12.1 | 12.2 | 0.1 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.067x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16.8 | 16.8 | 17.1 | 0.1 | 0.169x | 1.384x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 0.175x | 1.433x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.451x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.178x | 1.458x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.481x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.484x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.6 | 44.4 | 0.3 | 0.440x | 3.607x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.8 | 97.3 | 101.0 | 1.3 | 1.000x | 8.199x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.340x | 1.940x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 2.036x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.045x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.699x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.718x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.1 | 12.1 | 12.2 | 0.0 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.073x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.169x | 1.391x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.4 | 17.4 | 0.0 | 0.175x | 1.441x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.462x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.462x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.493x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.496x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.6 | 44.8 | 0.4 | 0.440x | 3.610x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.5 | 101.4 | 1.4 | 1.000x | 8.211x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.279x | 1.592x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.321x | 1.836x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.938x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.340x | 1.944x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.356x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.359x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.0 | 1.000x | 5.711x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.002x | 5.723x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 15.2 | 15.1 | 15.3 | 0.0 | 0.153x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.4 | 15.4 | 15.4 | 0.0 | 0.155x | 1.014x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.165x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.167x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.187x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.1 | 0.1 | 0.182x | 1.190x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.7 | 47.8 | 1.5 | 0.443x | 2.901x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 53.0 | 52.9 | 53.8 | 0.4 | 0.533x | 3.492x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 53.5 | 53.2 | 54.5 | 0.5 | 0.537x | 3.523x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.8 | 101.2 | 1.2 | 1.000x | 6.556x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.337x | 1.931x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.937x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.042x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.050x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 5.719x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.722x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.360x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.389x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 27.2 | 0.6 | 0.260x | 1.995x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 25.9 | 26.5 | 0.2 | 0.266x | 2.035x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.6 | 45.5 | 0.7 | 0.440x | 3.372x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.5 | 100.2 | 1.0 | 1.000x | 7.662x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.825x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.340x | 1.938x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 11.3 | 0.4 | 0.359x | 2.047x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.694x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.3 | 28.8 | 0.2 | 1.007x | 5.732x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.026x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.178x | 1.365x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.392x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.183x | 1.396x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.0 | 0.1 | 0.261x | 1.997x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.9 | 0.3 | 0.263x | 2.010x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.8 | 44.4 | 0.2 | 0.442x | 3.377x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.7 | 100.6 | 1.0 | 1.000x | 7.648x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.937x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.940x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.051x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.360x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.701x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.006x | 5.733x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.133x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.363x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.386x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.387x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.6 | 0.3 | 0.260x | 2.003x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.1 | 0.2 | 0.260x | 2.005x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.437x | 3.362x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.0 | 97.8 | 101.2 | 1.2 | 1.000x | 7.699x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.592x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.831x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.935x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.340x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.029x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.6 | 28.8 | 0.1 | 1.000x | 5.706x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.1 | 1.002x | 5.716x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 14.8 | 14.8 | 15.3 | 0.2 | 0.148x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.1 | 15.1 | 15.1 | 0.0 | 0.151x | 1.020x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.200x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 19.5 | 0.7 | 0.178x | 1.200x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.220x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.222x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.439x | 2.959x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 50.2 | 50.2 | 50.3 | 0.1 | 0.505x | 3.400x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 50.4 | 50.1 | 50.7 | 0.2 | 0.506x | 3.410x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.8 | 100.7 | 1.0 | 1.000x | 6.737x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.339x | 1.932x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.940x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.030x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.0 | 0.356x | 2.033x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.705x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 30.5 | 0.7 | 1.007x | 5.748x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.9 | 13.9 | 14.0 | 0.0 | 0.140x | 1.021x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 0.179x | 1.306x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.179x | 1.307x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.0 | 0.182x | 1.327x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.183x | 1.330x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 31.0 | 31.0 | 31.2 | 0.1 | 0.313x | 2.282x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 31.5 | 31.3 | 32.1 | 0.3 | 0.318x | 2.318x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.6 | 44.5 | 0.4 | 0.441x | 3.216x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.0 | 98.1 | 101.0 | 1.1 | 1.000x | 7.285x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.321x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.926x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.342x | 1.945x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.360x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.694x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.7 | 0.4 | 1.006x | 5.729x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.021x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.301x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.1 | 0.2 | 0.178x | 1.301x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.0 | 0.0 | 0.181x | 1.323x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.329x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 31.0 | 30.9 | 31.4 | 0.2 | 0.312x | 2.280x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 31.5 | 31.2 | 31.6 | 0.2 | 0.317x | 2.316x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.440x | 3.215x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.3 | 98.0 | 100.9 | 1.1 | 1.000x | 7.306x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.942x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 2.033x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.357x | 2.034x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.705x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.009x | 5.754x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.4 | 12.4 | 12.5 | 0.0 | 0.124x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.047x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 0.177x | 1.425x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.177x | 1.425x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.180x | 1.452x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.6 | 0.2 | 0.181x | 1.453x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 19.5 | 19.5 | 20.7 | 0.5 | 0.195x | 1.571x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 19.8 | 19.8 | 21.0 | 0.5 | 0.198x | 1.597x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.6 | 45.9 | 0.8 | 0.441x | 3.549x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.8 | 97.7 | 101.0 | 1.2 | 1.000x | 8.047x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.340x | 1.941x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.942x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 30.3 | 0.7 | 1.000x | 5.709x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.725x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.1 | 0.137x | 1.026x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.329x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.1 | 0.178x | 1.338x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.3 | 0.1 | 0.181x | 1.356x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.363x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 0.287x | 2.149x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.9 | 28.8 | 28.9 | 0.0 | 0.289x | 2.171x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.1 | 43.7 | 45.9 | 0.8 | 0.442x | 3.317x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 98.3 | 101.4 | 1.1 | 1.000x | 7.501x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.6 | 9.6 | 9.8 | 0.1 | 0.336x | 1.921x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.936x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.713x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.001x | 5.718x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.136x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.330x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.179x | 1.345x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.355x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.5 | 0.2 | 0.181x | 1.360x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.5 | 28.4 | 29.1 | 0.3 | 0.286x | 2.145x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.289x | 2.171x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.7 | 46.0 | 1.0 | 0.441x | 3.312x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 97.3 | 101.0 | 1.3 | 1.000x | 7.506x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.320x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.7 | 0.0 | 0.338x | 1.930x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.340x | 1.941x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.027x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.710x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.004x | 5.733x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 14.0 | 13.9 | 14.3 | 0.2 | 0.141x | 1.029x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.304x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 0.178x | 1.306x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.326x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.327x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 30.9 | 30.9 | 31.0 | 0.0 | 0.311x | 2.277x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 31.4 | 31.2 | 31.6 | 0.2 | 0.315x | 2.309x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 45.4 | 0.6 | 0.441x | 3.227x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 7.320x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.1 | 0.277x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.337x | 1.931x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.339x | 1.943x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.354x | 2.030x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.050x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 0.999x | 5.725x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 1.000x | 5.732x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.134x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.8 | 0.1 | 0.137x | 1.025x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.6 | 18.0 | 0.2 | 0.177x | 1.327x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 0.177x | 1.327x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.357x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.358x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.5 | 28.4 | 28.6 | 0.1 | 0.287x | 2.146x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.290x | 2.170x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 45.1 | 0.6 | 0.440x | 3.293x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 7.479x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.204x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.587x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.929x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.930x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.027x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.039x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 5.704x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.002x | 5.715x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 14.0 | 13.9 | 14.7 | 0.3 | 0.142x | 1.034x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.300x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.303x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.182x | 1.327x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.328x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 30.9 | 30.8 | 31.0 | 0.1 | 0.311x | 2.274x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 31.2 | 31.2 | 31.6 | 0.2 | 0.315x | 2.298x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.1 | 43.7 | 45.4 | 0.6 | 0.445x | 3.251x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.3 | 101.0 | 1.3 | 1.000x | 7.302x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.5 | 0.2 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.340x | 1.932x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.341x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.354x | 2.015x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.691x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.7 | 0.0 | 1.005x | 5.718x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 14.2 | 14.2 | 14.3 | 0.0 | 0.142x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.5 | 14.5 | 0.0 | 0.145x | 1.020x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.247x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.247x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.268x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.270x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.7 | 44.9 | 0.5 | 0.441x | 3.095x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 47.2 | 45.3 | 48.3 | 1.2 | 0.474x | 3.330x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 47.4 | 46.6 | 49.1 | 0.9 | 0.476x | 3.343x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.6 | 97.3 | 100.6 | 1.1 | 1.000x | 7.026x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.6 | 0.2 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.830x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.0 | 0.1 | 0.338x | 1.930x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.930x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 0.355x | 2.025x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.358x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.000x | 5.713x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.003x | 5.728x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 20.0 | 0.9 | 0.178x | 1.359x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.361x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.388x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.389x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.4 | 0.2 | 0.261x | 1.997x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.9 | 0.4 | 0.264x | 2.015x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.2 | 43.8 | 49.5 | 2.2 | 0.445x | 3.402x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.6 | 101.0 | 1.2 | 1.000x | 7.645x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.337x | 1.929x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.937x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.026x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.723x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.741x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.178x | 1.359x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.386x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 26.0 | 26.6 | 0.2 | 0.262x | 2.003x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.263x | 2.006x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.6 | 44.5 | 0.3 | 0.443x | 3.381x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 98.0 | 99.9 | 0.6 | 1.000x | 7.636x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.2 | 0.0 | 0.212x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.830x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.937x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.942x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.025x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.358x | 2.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.693x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.0 | 29.7 | 0.5 | 1.005x | 5.722x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.178x | 1.360x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.178x | 1.363x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.385x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.387x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 0.263x | 2.014x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.5 | 25.9 | 26.7 | 0.4 | 0.267x | 2.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.7 | 43.7 | 44.3 | 0.3 | 0.440x | 3.366x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.3 | 97.7 | 99.9 | 0.9 | 1.000x | 7.645x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.0 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.340x | 1.944x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 2.023x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.1 | 0.356x | 2.031x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.3 | 28.7 | 0.1 | 1.000x | 5.712x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 30.0 | 0.5 | 1.003x | 5.732x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.3 | 0.134x | 1.024x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.390x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.7 | 26.4 | 0.2 | 0.263x | 2.012x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.9 | 26.9 | 0.4 | 0.264x | 2.021x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 43.9 | 44.6 | 0.3 | 0.447x | 3.421x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 98.3 | 101.1 | 0.9 | 1.000x | 7.657x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.928x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.2 | 0.2 | 0.342x | 1.945x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.7 | 0.2 | 0.358x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.361x | 2.052x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.689x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.008x | 5.735x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.1 | 13.3 | 0.1 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 20.9 | 1.3 | 0.178x | 1.360x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.360x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.385x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.394x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.8 | 26.6 | 0.3 | 0.262x | 2.006x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.8 | 0.3 | 0.262x | 2.007x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.3 | 0.3 | 0.441x | 3.375x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.8 | 100.9 | 1.1 | 1.000x | 7.661x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.339x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.700x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.0 | 1.005x | 5.729x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.132x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.363x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.177x | 1.367x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.179x | 1.385x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.389x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.6 | 26.4 | 0.3 | 0.260x | 2.008x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.261x | 2.014x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 45.3 | 0.6 | 0.437x | 3.372x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.3 | 97.4 | 103.1 | 1.8 | 1.000x | 7.723x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.323x | 1.843x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.0 | 0.1 | 0.342x | 1.952x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.353x | 2.015x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 31.6 | 1.2 | 1.000x | 5.713x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 1.004x | 5.734x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.024x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.179x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.179x | 1.365x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.386x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.388x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.9 | 26.2 | 0.1 | 0.262x | 1.996x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.8 | 26.5 | 0.3 | 0.264x | 2.011x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.6 | 47.4 | 1.5 | 0.443x | 3.368x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.8 | 97.4 | 104.3 | 2.4 | 1.000x | 7.608x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.928x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.343x | 1.957x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.359x | 2.047x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.1 | 1.000x | 5.705x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 28.8 | 0.1 | 1.004x | 5.729x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.179x | 1.362x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.179x | 1.362x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.183x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.183x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.263x | 1.995x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.8 | 27.3 | 0.6 | 0.266x | 2.019x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.6 | 44.8 | 0.4 | 0.446x | 3.388x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.6 | 97.3 | 104.5 | 2.6 | 1.000x | 7.594x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.338x | 1.926x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.341x | 1.944x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.354x | 2.017x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.698x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.005x | 5.728x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.5 | 0.2 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.021x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.179x | 1.363x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.179x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.182x | 1.386x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.182x | 1.389x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.263x | 2.002x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 26.0 | 26.4 | 0.2 | 0.266x | 2.024x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.442x | 3.366x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.1 | 97.7 | 104.6 | 2.4 | 1.000x | 7.622x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.932x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.340x | 1.938x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.709x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.006x | 5.740x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.1 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 0.176x | 1.358x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.177x | 1.362x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.180x | 1.384x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.390x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.2 | 0.2 | 0.259x | 1.992x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.2 | 0.260x | 2.003x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.438x | 3.375x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.0 | 97.8 | 104.7 | 2.4 | 1.000x | 7.699x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.340x | 1.937x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.344x | 1.956x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.039x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.689x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.737x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.361x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.178x | 1.362x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.386x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.2 | 0.1 | 0.181x | 1.386x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 26.0 | 26.5 | 0.2 | 0.264x | 2.019x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.7 | 26.5 | 0.3 | 0.264x | 2.021x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.2 | 43.6 | 45.1 | 0.6 | 0.445x | 3.402x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.3 | 104.8 | 2.6 | 1.000x | 7.644x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.340x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.344x | 1.956x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.355x | 2.018x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.5 | 29.1 | 0.2 | 1.000x | 5.688x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.007x | 5.727x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 0.179x | 1.358x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.179x | 1.363x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.183x | 1.387x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.183x | 1.394x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.7 | 26.6 | 0.3 | 0.264x | 2.003x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.265x | 2.010x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.6 | 44.4 | 0.3 | 0.444x | 3.372x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.7 | 97.3 | 104.9 | 2.8 | 1.000x | 7.599x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.4 | 0.2 | 0.279x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.6 | 9.6 | 9.8 | 0.1 | 0.337x | 1.923x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 0.341x | 1.946x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.1 | 0.358x | 2.046x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.359x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.712x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.002x | 5.725x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.4 | 0.2 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.180x | 1.364x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.180x | 1.365x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.183x | 1.388x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.183x | 1.389x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.9 | 0.4 | 0.263x | 1.991x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.5 | 0.3 | 0.264x | 1.997x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.3 | 0.450x | 3.414x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.5 | 97.6 | 104.1 | 2.4 | 1.000x | 7.580x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.173x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.334x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.337x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.349x | 2.020x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 2.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 0.990x | 5.725x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 29.0 | 28.5 | 29.4 | 0.3 | 1.000x | 5.781x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.2 | 0.134x | 1.025x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.178x | 1.360x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.178x | 1.361x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.383x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 22.1 | 1.6 | 0.182x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.6 | 26.3 | 0.3 | 0.261x | 1.990x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.8 | 0.4 | 0.261x | 1.995x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.442x | 3.373x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.4 | 104.4 | 2.4 | 1.000x | 7.633x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.940x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.942x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 2.044x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.357x | 2.045x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.4 | 0.3 | 1.000x | 5.722x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.723x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 14.0 | 0.3 | 0.134x | 1.024x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.181x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 0.262x | 2.005x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.9 | 26.7 | 0.3 | 0.264x | 2.025x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.0 | 43.7 | 44.4 | 0.3 | 0.442x | 3.385x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.6 | 97.6 | 102.1 | 1.5 | 1.000x | 7.664x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.339x | 1.934x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.355x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.713x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.745x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.361x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.3 | 0.2 | 0.261x | 1.998x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.8 | 27.4 | 0.7 | 0.262x | 2.005x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.441x | 3.367x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.3 | 97.2 | 99.9 | 1.0 | 1.000x | 7.642x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.277x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.937x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.339x | 1.950x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.355x | 2.037x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 2.049x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 0.997x | 5.731x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.000x | 5.746x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.024x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.179x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.0 | 0.181x | 1.384x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.385x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.6 | 25.9 | 0.1 | 0.261x | 1.991x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 27.1 | 0.5 | 0.262x | 1.997x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.6 | 0.4 | 0.441x | 3.368x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.4 | 100.7 | 1.2 | 1.000x | 7.636x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 12.6 | 1.4 | 0.319x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.939x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.340x | 1.947x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.1 | 0.353x | 2.020x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 5.729x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 5.729x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.2 | 0.135x | 1.024x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.179x | 1.365x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.6 | 0.3 | 0.180x | 1.371x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.183x | 1.394x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.7 | 25.5 | 26.7 | 0.4 | 0.260x | 1.981x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 26.0 | 27.5 | 0.5 | 0.267x | 2.032x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.444x | 3.373x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.8 | 97.4 | 100.7 | 1.2 | 1.000x | 7.605x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.939x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.0 | 0.1 | 0.342x | 1.948x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 2.024x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 2.040x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 1.000x | 5.693x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.005x | 5.722x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.0 | 0.136x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.329x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 0.177x | 1.335x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.2 | 0.1 | 0.180x | 1.353x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.355x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.5 | 28.4 | 28.7 | 0.1 | 0.285x | 2.141x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.287x | 2.160x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.1 | 43.6 | 47.9 | 1.6 | 0.441x | 3.319x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.0 | 97.2 | 100.5 | 1.2 | 1.000x | 7.526x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.173x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.209x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.932x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.336x | 1.941x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.355x | 2.052x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 11.9 | 0.7 | 0.356x | 2.056x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 0.996x | 5.748x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 29.0 | 28.7 | 29.1 | 0.2 | 1.000x | 5.774x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.264x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 8.6 | 8.6 | 8.9 | 0.1 | 0.264x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 8.6 | 8.6 | 10.1 | 0.6 | 0.265x | 1.003x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 9.0 | 8.6 | 9.1 | 0.2 | 0.278x | 1.053x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.4 | 13.3 | 14.0 | 0.3 | 0.413x | 1.566x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.4 | 13.1 | 14.6 | 0.5 | 0.414x | 1.569x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 32.5 | 32.5 | 35.0 | 1.0 | 1.000x | 3.791x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 37.4 | 36.3 | 40.1 | 1.3 | 1.151x | 4.366x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 59.9 | 59.0 | 60.7 | 0.6 | 1.844x | 6.992x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 60.4 | 59.4 | 65.0 | 2.2 | 1.858x | 7.044x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.065x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.070x | 1.079x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.106x | 1.636x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.8 | 11.7 | 0.7 | 0.115x | 1.785x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.1 | 9.8 | 10.3 | 0.1 | 0.116x | 1.796x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.5 | 9.9 | 11.3 | 0.5 | 0.121x | 1.872x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.7 | 10.5 | 10.9 | 0.1 | 0.123x | 1.901x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.8 | 0.1 | 0.123x | 1.910x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 86.8 | 86.4 | 88.4 | 0.7 | 1.000x | 15.478x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 88.7 | 86.5 | 90.1 | 1.1 | 1.021x | 15.807x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 11.0 | 10.9 | 11.5 | 0.2 | 0.110x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.183x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 14.2 | 14.2 | 14.2 | 0.0 | 0.142x | 1.290x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.0 | 0.166x | 1.506x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 17.3 | 17.2 | 17.4 | 0.1 | 0.173x | 1.570x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 17.3 | 17.2 | 17.8 | 0.2 | 0.173x | 1.576x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.3 | 17.3 | 17.4 | 0.0 | 0.174x | 1.577x |
| 8 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.3 | 27.0 | 3.8 | 0.174x | 1.580x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.2 | 43.7 | 52.2 | 3.2 | 0.443x | 4.026x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.8 | 98.1 | 101.2 | 1.2 | 1.000x | 9.082x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.5 | 9.9 | 0.1 | 0.336x | 1.936x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.337x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.040x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.355x | 2.042x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 0.996x | 5.734x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.2 | 1.000x | 5.757x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.1 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.5 | 17.5 | 17.6 | 0.0 | 0.177x | 1.347x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.5 | 20.1 | 1.0 | 0.178x | 1.353x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 17.7 | 17.5 | 18.3 | 0.3 | 0.179x | 1.359x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 17.5 | 18.3 | 0.3 | 0.183x | 1.396x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.7 | 25.7 | 28.2 | 1.0 | 0.269x | 2.051x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.7 | 26.1 | 27.4 | 0.5 | 0.270x | 2.052x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.7 | 46.1 | 0.8 | 0.449x | 3.416x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.1 | 98.0 | 101.8 | 1.5 | 1.000x | 7.613x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.830x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.340x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.357x | 2.043x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.048x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.720x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 1.001x | 5.725x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 14.8 | 14.8 | 15.0 | 0.1 | 0.149x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.1 | 15.1 | 15.1 | 0.0 | 0.151x | 1.015x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.180x | 1.207x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.180x | 1.208x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.267x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.2 | 18.2 | 19.6 | 0.5 | 0.193x | 1.293x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 43.7 | 45.4 | 0.6 | 0.446x | 2.991x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 50.2 | 50.0 | 50.5 | 0.2 | 0.505x | 3.387x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 50.4 | 50.2 | 52.0 | 0.6 | 0.506x | 3.395x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.5 | 101.0 | 1.2 | 1.000x | 6.707x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.824x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.928x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.343x | 1.952x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 2.040x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.697x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.1 | 1.006x | 5.732x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.8 | 0.2 | 0.134x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.331x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 21.5 | 1.5 | 0.178x | 1.333x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.4 | 0.181x | 1.359x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.418x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 0.288x | 2.158x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.8 | 28.2 | 29.0 | 0.3 | 0.289x | 2.164x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.8 | 44.1 | 45.8 | 0.6 | 0.450x | 3.371x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.0 | 101.6 | 1.6 | 1.000x | 7.486x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.335x | 1.929x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.338x | 1.950x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.039x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.356x | 2.049x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 0.996x | 5.737x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.5 | 29.0 | 0.2 | 1.000x | 5.762x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.1 | 0.136x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 0.177x | 1.327x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.177x | 1.331x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 18.0 | 18.9 | 0.3 | 0.182x | 1.368x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.1 | 18.9 | 0.4 | 0.189x | 1.419x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.5 | 28.3 | 29.0 | 0.2 | 0.285x | 2.143x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 0.287x | 2.152x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 43.6 | 45.1 | 0.5 | 0.448x | 3.363x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.8 | 98.3 | 101.0 | 1.1 | 1.000x | 7.510x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.825x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.928x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.0 | 0.1 | 0.341x | 1.940x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.359x | 2.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.693x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.728x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.6 | 0.1 | 0.135x | 1.026x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.179x | 1.361x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.179x | 1.363x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.9 | 0.3 | 0.183x | 1.390x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.191x | 1.452x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.1 | 0.1 | 0.263x | 2.005x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.265x | 2.018x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 43.8 | 45.4 | 0.6 | 0.449x | 3.416x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.9 | 97.6 | 100.7 | 1.2 | 1.000x | 7.614x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.833x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.941x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.340x | 1.943x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.040x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.358x | 2.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.714x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.7 | 28.9 | 0.1 | 1.008x | 5.760x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.6 | 0.1 | 0.134x | 1.024x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.179x | 1.369x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.393x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.189x | 1.453x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.263x | 2.015x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.7 | 26.6 | 0.4 | 0.264x | 2.023x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.6 | 43.6 | 47.1 | 1.2 | 0.448x | 3.434x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.6 | 97.5 | 100.8 | 1.2 | 1.000x | 7.666x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.338x | 1.932x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.340x | 1.942x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.709x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.003x | 5.729x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.026x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.179x | 1.365x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.183x | 1.394x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.190x | 1.452x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.7 | 26.2 | 0.2 | 0.263x | 2.007x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.3 | 0.263x | 2.011x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.7 | 46.0 | 0.8 | 0.449x | 3.430x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.4 | 101.0 | 1.3 | 1.000x | 7.638x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.938x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 2.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.714x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.003x | 5.729x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.5 | 14.5 | 0.0 | 0.146x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 14.8 | 14.8 | 14.8 | 0.0 | 0.149x | 1.020x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.178x | 1.223x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.1 | 0.179x | 1.227x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.182x | 1.248x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.0 | 18.9 | 0.4 | 0.190x | 1.303x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.6 | 45.2 | 0.5 | 0.449x | 3.076x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 47.5 | 47.2 | 47.6 | 0.1 | 0.479x | 3.282x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 47.6 | 47.4 | 47.8 | 0.1 | 0.480x | 3.288x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.5 | 101.8 | 1.5 | 1.000x | 6.853x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.588x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.824x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.936x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.341x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.037x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.710x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.002x | 5.724x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.1 | 0.134x | 1.026x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 0.179x | 1.364x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.181x | 1.386x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.1 | 18.9 | 0.4 | 0.190x | 1.452x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.8 | 0.3 | 0.262x | 2.002x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.3 | 0.1 | 0.262x | 2.003x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.7 | 47.1 | 1.2 | 0.448x | 3.422x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.6 | 101.7 | 1.4 | 1.000x | 7.636x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.338x | 1.926x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.940x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 2.034x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.359x | 2.045x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.695x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.2 | 28.9 | 0.2 | 1.005x | 5.726x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.5 | 14.7 | 0.1 | 0.145x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 14.8 | 14.8 | 14.8 | 0.0 | 0.148x | 1.020x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.224x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.2 | 0.2 | 0.178x | 1.225x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.245x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.303x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.7 | 47.6 | 1.4 | 0.447x | 3.077x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 47.5 | 47.5 | 47.7 | 0.1 | 0.477x | 3.286x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 47.6 | 47.5 | 48.2 | 0.3 | 0.477x | 3.289x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 97.8 | 100.9 | 1.1 | 1.000x | 6.889x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.931x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.339x | 1.948x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.039x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.996x | 5.722x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.000x | 5.743x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.021x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.178x | 1.361x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.178x | 1.362x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.384x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.0 | 19.0 | 0.5 | 0.190x | 1.449x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.8 | 25.5 | 26.1 | 0.2 | 0.259x | 1.983x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.260x | 1.992x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.6 | 43.6 | 47.3 | 1.3 | 0.448x | 3.429x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 98.3 | 100.4 | 0.8 | 1.000x | 7.647x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.592x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.336x | 1.926x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.937x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.035x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.358x | 2.048x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 0.999x | 5.721x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.2 | 1.000x | 5.726x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.179x | 1.363x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.179x | 1.366x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.182x | 1.386x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.4 | 18.0 | 19.0 | 0.4 | 0.186x | 1.419x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.5 | 26.1 | 0.2 | 0.261x | 1.990x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.264x | 2.008x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.3 | 43.7 | 47.2 | 1.3 | 0.448x | 3.410x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.9 | 97.6 | 101.0 | 1.1 | 1.000x | 7.617x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.212x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.588x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.824x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.340x | 1.933x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.340x | 1.933x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.034x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.358x | 2.035x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.683x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.728x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.2 | 0.178x | 1.361x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.179x | 1.364x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.182x | 1.388x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 17.9 | 18.9 | 0.4 | 0.183x | 1.399x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.3 | 0.1 | 0.262x | 2.000x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.4 | 26.5 | 0.3 | 0.263x | 2.006x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.3 | 43.7 | 45.3 | 0.5 | 0.447x | 3.410x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.8 | 100.6 | 0.9 | 1.000x | 7.634x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.940x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.342x | 1.944x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.039x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 2.039x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.5 | 29.0 | 0.2 | 1.000x | 5.688x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.005x | 5.718x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.363x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.4 | 0.181x | 1.389x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.9 | 0.3 | 0.181x | 1.391x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.8 | 25.6 | 26.4 | 0.3 | 0.259x | 1.985x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.7 | 26.2 | 0.2 | 0.261x | 2.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.4 | 43.8 | 45.9 | 0.8 | 0.446x | 3.418x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 97.8 | 101.5 | 1.2 | 1.000x | 7.671x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.825x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.339x | 1.934x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.936x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 2.034x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.358x | 2.045x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.999x | 5.703x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.3 | 28.7 | 0.1 | 1.000x | 5.706x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.179x | 1.365x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.179x | 1.367x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.182x | 1.388x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.6 | 26.2 | 0.2 | 0.262x | 2.004x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.3 | 0.2 | 0.263x | 2.005x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 43.7 | 51.8 | 3.0 | 0.451x | 3.444x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 97.3 | 100.1 | 1.1 | 1.000x | 7.638x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.2 | 0.1 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.318x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.337x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.938x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.040x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.040x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.999x | 5.732x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 1.000x | 5.738x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.209x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.825x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.938x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.339x | 1.943x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 2.047x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.357x | 2.048x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.715x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 29.5 | 0.3 | 1.000x | 5.733x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.933x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.341x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.357x | 2.039x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.4 | 29.1 | 0.2 | 1.000x | 5.712x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.002x | 5.723x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.1 | 0.1 | 0.340x | 1.942x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.341x | 1.947x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.356x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.716x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.001x | 5.720x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.0 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.929x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.941x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.354x | 2.026x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.358x | 2.045x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.1 | 1.000x | 5.715x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.005x | 5.741x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.587x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.939x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.340x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.030x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.710x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.002x | 5.721x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.935x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.936x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 2.034x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.720x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.739x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.829x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.339x | 1.938x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.341x | 1.947x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.357x | 2.038x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.717x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.3 | 32.0 | 1.3 | 1.003x | 5.732x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.828x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.338x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.341x | 1.949x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.718x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.0 | 28.8 | 0.3 | 1.002x | 5.728x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.178x | 1.364x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.178x | 1.364x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.181x | 1.390x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 26.0 | 26.2 | 0.1 | 0.261x | 2.003x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.261x | 2.008x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 44.0 | 45.4 | 0.6 | 0.448x | 3.439x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.8 | 97.5 | 100.6 | 1.2 | 1.000x | 7.680x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.341x | 1.937x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.0 | 0.1 | 0.342x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.037x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.361x | 2.053x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 1.000x | 5.686x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.9 | 0.5 | 1.005x | 5.714x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.4 | 13.3 | 13.6 | 0.1 | 0.135x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.6 | 13.6 | 14.1 | 0.2 | 0.137x | 1.017x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.178x | 1.324x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.5 | 0.3 | 0.178x | 1.324x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.345x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.346x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 28.3 | 28.2 | 28.4 | 0.1 | 0.285x | 2.112x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.288x | 2.134x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.6 | 43.7 | 45.1 | 0.5 | 0.448x | 3.326x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.9 | 100.8 | 1.0 | 1.000x | 7.421x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.280x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.341x | 1.936x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.1 | 0.2 | 0.342x | 1.945x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.359x | 2.038x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.8 | 0.3 | 0.361x | 2.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.5 | 28.9 | 0.2 | 1.000x | 5.683x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.4 | 29.0 | 0.2 | 1.009x | 5.736x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.6 | 18.5 | 0.3 | 0.179x | 1.367x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.387x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 19.0 | 0.4 | 0.182x | 1.389x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.2 | 0.1 | 0.260x | 1.992x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.261x | 1.994x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 45.1 | 43.8 | 47.5 | 1.3 | 0.454x | 3.471x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 98.4 | 100.5 | 0.9 | 1.000x | 7.649x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.320x | 1.827x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.339x | 1.938x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.1 | 0.356x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.710x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.002x | 5.721x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.1 | 12.1 | 12.1 | 0.0 | 0.121x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.073x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16.8 | 16.8 | 17.1 | 0.1 | 0.168x | 1.391x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.4 | 17.8 | 0.2 | 0.175x | 1.442x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.177x | 1.463x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.465x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.4 | 0.180x | 1.489x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.181x | 1.491x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.9 | 43.8 | 45.7 | 0.6 | 0.449x | 3.706x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.9 | 97.9 | 101.2 | 1.2 | 1.000x | 8.255x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.830x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.930x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.354x | 2.023x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.717x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.002x | 5.726x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.178x | 1.364x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.180x | 1.385x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.181x | 1.392x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.5 | 26.1 | 0.2 | 0.260x | 1.993x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.4 | 0.2 | 0.260x | 1.993x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.6 | 43.6 | 47.0 | 1.2 | 0.447x | 3.432x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 97.6 | 101.3 | 1.2 | 1.000x | 7.677x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.589x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.340x | 1.936x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.340x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.035x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.699x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.006x | 5.731x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12.1 | 12.1 | 12.2 | 0.0 | 0.121x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.072x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.169x | 1.391x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 0.175x | 1.438x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.462x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 18.1 | 0.1 | 0.178x | 1.466x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.489x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 19.0 | 0.4 | 0.182x | 1.497x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.9 | 43.6 | 45.0 | 0.5 | 0.450x | 3.703x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 97.4 | 101.1 | 1.3 | 1.000x | 8.232x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.588x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.824x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.934x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.340x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 2.031x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.709x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.002x | 5.718x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 0.178x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.017x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.181x | 1.017x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 18.8 | 18.5 | 19.1 | 0.2 | 0.188x | 1.058x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.199x | 1.118x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 45.8 | 44.6 | 52.4 | 2.8 | 0.460x | 2.585x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 72.5 | 72.4 | 72.5 | 0.1 | 0.728x | 4.091x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 72.7 | 72.6 | 73.4 | 0.3 | 0.730x | 4.100x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.6 | 97.1 | 101.8 | 1.6 | 1.000x | 5.618x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.277x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.825x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.336x | 1.927x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.937x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.354x | 2.033x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.358x | 2.051x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.996x | 5.715x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 5.736x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 15.7 | 15.7 | 15.9 | 0.1 | 0.158x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.9 | 15.9 | 16.0 | 0.0 | 0.160x | 1.017x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.9 | 0.5 | 0.178x | 1.127x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 17.9 | 0.1 | 0.179x | 1.134x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.182x | 1.154x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 18.0 | 19.0 | 0.4 | 0.183x | 1.160x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.8 | 43.7 | 45.4 | 0.6 | 0.450x | 2.854x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 58.5 | 58.4 | 59.0 | 0.2 | 0.588x | 3.730x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.593x | 3.763x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.8 | 101.8 | 1.5 | 1.000x | 6.344x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.826x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.341x | 1.948x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 12.7 | 1.2 | 0.341x | 1.949x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.357x | 2.045x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.054x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.998x | 5.712x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.722x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.5 | 0.2 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.4 | 13.3 | 14.2 | 0.3 | 0.134x | 1.029x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.365x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.6 | 18.4 | 0.3 | 0.179x | 1.367x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 18.8 | 0.3 | 0.182x | 1.390x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.183x | 1.404x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.6 | 26.2 | 0.2 | 0.260x | 1.994x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.1 | 0.262x | 2.003x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 44.1 | 45.1 | 0.3 | 0.449x | 3.438x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 98.2 | 101.2 | 1.2 | 1.000x | 7.655x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.830x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.937x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.338x | 1.937x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.039x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.052x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.999x | 5.725x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 5.729x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.2 | 0.134x | 1.024x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.361x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 21.2 | 1.4 | 0.179x | 1.365x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.182x | 1.386x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.183x | 1.396x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.4 | 0.2 | 0.262x | 2.000x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.8 | 26.4 | 0.2 | 0.264x | 2.015x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.7 | 49.5 | 2.1 | 0.449x | 3.427x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.2 | 98.0 | 102.6 | 1.6 | 1.000x | 7.637x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.826x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.339x | 1.931x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.342x | 1.943x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 2.036x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.0 | 1.000x | 5.690x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.006x | 5.726x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.178x | 1.363x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.178x | 1.365x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.3 | 0.181x | 1.386x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 0.262x | 2.006x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.8 | 26.5 | 0.2 | 0.263x | 2.014x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.5 | 43.9 | 45.6 | 0.6 | 0.447x | 3.424x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.7 | 104.7 | 2.4 | 1.000x | 7.657x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.205x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.588x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.826x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.339x | 1.929x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.935x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.358x | 2.037x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.4 | 28.5 | 0.1 | 1.000x | 5.683x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.007x | 5.723x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.023x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.178x | 1.365x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.9 | 17.7 | 18.6 | 0.3 | 0.179x | 1.375x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.389x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 17.9 | 19.4 | 0.5 | 0.181x | 1.390x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.8 | 26.2 | 0.1 | 0.260x | 1.995x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.7 | 27.4 | 0.6 | 0.262x | 2.004x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.8 | 43.7 | 45.7 | 0.7 | 0.450x | 3.451x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.5 | 97.7 | 104.6 | 2.5 | 1.000x | 7.663x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.339x | 1.929x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.7 | 0.0 | 0.341x | 1.938x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 2.028x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.690x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.5 | 0.3 | 1.006x | 5.726x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.178x | 1.362x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.178x | 1.365x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.7 | 27.1 | 0.4 | 0.265x | 2.026x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 25.6 | 26.5 | 0.3 | 0.265x | 2.027x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 43.7 | 44.8 | 0.4 | 0.449x | 3.440x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.4 | 97.5 | 102.5 | 1.8 | 1.000x | 7.657x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.280x | 1.592x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.321x | 1.825x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.340x | 1.937x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.341x | 1.939x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 2.038x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.694x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.009x | 5.744x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.178x | 1.364x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 0.178x | 1.364x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.390x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.392x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.4 | 0.3 | 0.260x | 1.991x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.8 | 27.3 | 0.5 | 0.264x | 2.020x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.9 | 43.7 | 46.2 | 1.0 | 0.453x | 3.459x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 99.3 | 97.5 | 100.6 | 1.1 | 1.000x | 7.644x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.591x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.939x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.340x | 1.946x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.029x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.724x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.001x | 5.729x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.179x | 1.361x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.179x | 1.364x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 17.9 | 19.8 | 0.7 | 0.182x | 1.385x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.386x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 25.9 | 25.7 | 26.3 | 0.2 | 0.263x | 1.995x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.264x | 2.003x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 45.1 | 43.9 | 46.7 | 1.0 | 0.457x | 3.473x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 98.8 | 97.5 | 100.6 | 1.2 | 1.000x | 7.601x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.590x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.827x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.938x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.339x | 1.944x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.353x | 2.023x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.356x | 2.046x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 0.998x | 5.727x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 5.740x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.132x | 1.023x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.177x | 1.365x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.8 | 17.7 | 21.1 | 1.3 | 0.177x | 1.371x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.180x | 1.394x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.181x | 1.396x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 25.8 | 26.5 | 0.2 | 0.259x | 2.005x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.261x | 2.016x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.7 | 43.6 | 45.3 | 0.6 | 0.445x | 3.441x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.4 | 97.7 | 100.8 | 1.3 | 1.000x | 7.731x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.3 | 5.3 | 5.3 | 0.0 | 0.187x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.8 | 5.8 | 5.8 | 0.0 | 0.203x | 1.083x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.6 | 8.6 | 8.6 | 0.0 | 0.302x | 1.613x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 0.312x | 1.668x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.6 | 10.6 | 10.8 | 0.1 | 0.373x | 1.996x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.6 | 10.6 | 10.8 | 0.1 | 0.374x | 1.997x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.9 | 0.1 | 0.378x | 2.021x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.6 | 10.9 | 0.1 | 0.382x | 2.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.4 | 28.2 | 28.7 | 0.2 | 1.000x | 5.344x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.5 | 28.5 | 28.6 | 0.0 | 1.004x | 5.367x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 5.0 | 5.0 | 5.0 | 0.0 | 0.156x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 5.1 | 5.0 | 5.3 | 0.1 | 0.157x | 1.006x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 5.6 | 5.6 | 6.9 | 0.5 | 0.174x | 1.118x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 5.9 | 5.6 | 6.8 | 0.5 | 0.182x | 1.167x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 6.7 | 6.6 | 6.9 | 0.1 | 0.208x | 1.334x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 7.1 | 7.1 | 7.1 | 0.0 | 0.220x | 1.411x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 9.2 | 9.2 | 9.4 | 0.1 | 0.284x | 1.823x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 10.2 | 10.2 | 10.3 | 0.0 | 0.317x | 2.032x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 32.2 | 32.2 | 34.9 | 1.1 | 1.000x | 6.410x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 39.0 | 37.1 | 39.2 | 0.7 | 1.210x | 7.756x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 8.1 | 8.0 | 8.6 | 0.2 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.0 | 0.5 | 0.091x | 1.090x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.2 | 0.1 | 0.111x | 1.336x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.7 | 0.1 | 0.118x | 1.419x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.4 | 11.4 | 12.5 | 0.4 | 0.127x | 1.526x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.127x | 1.526x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.1 | 0.128x | 1.535x |
| 8 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.6 | 0.1 | 0.129x | 1.545x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 97.6 | 96.6 | 99.3 | 0.9 | 1.000x | 12.013x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.3 | 96.9 | 100.2 | 1.1 | 1.008x | 12.105x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 11.0 | 10.9 | 11.5 | 0.2 | 0.109x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.185x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 14.2 | 14.2 | 14.2 | 0.0 | 0.141x | 1.294x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 16.6 | 16.5 | 16.8 | 0.1 | 0.165x | 1.511x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 16.9 | 16.8 | 17.1 | 0.1 | 0.168x | 1.540x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.1 | 0.169x | 1.549x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.0 | 0.169x | 1.550x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17.1 | 16.9 | 17.2 | 0.1 | 0.170x | 1.557x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44.6 | 43.7 | 45.7 | 0.7 | 0.444x | 4.065x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 100.5 | 97.7 | 101.5 | 1.4 | 1.000x | 9.164x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.6 | 5.0 | 5.6 | 0.2 | 0.195x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.079x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.5 | 0.2 | 0.278x | 1.425x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.635x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.733x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.4 | 0.3 | 0.339x | 1.740x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.826x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.7 | 0.1 | 0.362x | 1.857x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.126x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.001x | 5.130x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 9.3 | 9.2 | 9.9 | 0.3 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 9.6 | 9.4 | 10.2 | 0.3 | 0.284x | 1.035x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 10.6 | 10.5 | 10.6 | 0.1 | 0.314x | 1.145x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 10.6 | 10.2 | 10.7 | 0.2 | 0.314x | 1.145x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 30.4 | 0.7 | 0.853x | 3.106x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 33.8 | 33.7 | 34.9 | 0.5 | 1.000x | 3.641x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 34.4 | 28.9 | 34.8 | 2.2 | 1.018x | 3.706x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 39.1 | 38.5 | 44.6 | 2.3 | 1.156x | 4.208x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 137.4 | 133.4 | 144.1 | 3.5 | 4.066x | 14.804x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 137.8 | 135.7 | 139.7 | 1.5 | 4.077x | 14.843x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5.6 | 5.0 | 5.6 | 0.3 | 0.196x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.079x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.423x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.634x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.729x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.342x | 1.744x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.357x | 1.824x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 1.826x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.105x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.8 | 28.6 | 34.3 | 2.2 | 1.005x | 5.132x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.263x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.264x | 1.003x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 9.2 | 8.6 | 9.4 | 0.3 | 0.281x | 1.069x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 9.9 | 9.0 | 10.1 | 0.4 | 0.304x | 1.157x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 10.8 | 10.8 | 10.9 | 0.0 | 0.332x | 1.261x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 10.9 | 10.9 | 10.9 | 0.0 | 0.335x | 1.275x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 32.6 | 32.5 | 35.0 | 1.0 | 1.000x | 3.804x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 37.8 | 36.3 | 41.3 | 2.1 | 1.160x | 4.413x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 45.2 | 45.2 | 46.3 | 0.4 | 1.387x | 5.278x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 45.8 | 45.5 | 45.9 | 0.2 | 1.405x | 5.346x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 581,707.3 | 576,544.6 | 596,660.3 | 8,174.8 | 0.162x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 627,124.2 | 626,566.5 | 627,272.9 | 300.8 | 0.175x | 1.078x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 627,246.0 | 626,914.5 | 1,062,268.9 | 173,551.6 | 0.175x | 1.078x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 628,684.2 | 627,967.1 | 635,823.3 | 2,884.7 | 0.175x | 1.081x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 628,731.1 | 627,718.5 | 630,599.7 | 1,044.9 | 0.175x | 1.081x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 658,242.3 | 648,348.3 | 710,633.7 | 25,446.9 | 0.184x | 1.132x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,728,929.7 | 1,671,641.0 | 1,736,029.1 | 27,268.7 | 0.482x | 2.972x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,585,463.7 | 3,561,821.5 | 3,642,459.6 | 36,446.1 | 1.000x | 6.164x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 3,923,994.5 | 3,914,908.5 | 3,954,707.3 | 14,707.0 | 1.094x | 6.746x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 4,012,120.3 | 4,009,847.7 | 4,058,000.5 | 22,964.0 | 1.119x | 6.897x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 17,662.8 | 17,643.8 | 17,854.8 | 77.7 | 0.997x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17,669.7 | 17,659.5 | 17,766.6 | 40.8 | 0.997x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 17,686.0 | 17,673.0 | 17,743.3 | 24.6 | 0.998x | 1.001x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,720.1 | 17,679.0 | 17,806.5 | 42.2 | 1.000x | 1.003x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17,732.9 | 17,674.9 | 17,758.6 | 27.6 | 1.001x | 1.004x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 39,676.1 | 39,138.6 | 39,809.0 | 239.0 | 2.239x | 2.246x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 310,113.4 | 310,042.7 | 311,418.4 | 525.4 | 17.501x | 17.557x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 310,324.2 | 310,168.3 | 319,607.6 | 3,718.1 | 17.513x | 17.569x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 3,047,388.0 | 2,800,119.1 | 3,293,198.7 | 190,533.4 | 171.973x | 172.531x |
| 10 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 3,076,750.8 | 2,841,198.8 | 3,247,798.5 | 162,904.6 | 173.630x | 174.193x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 17,621.4 | 17,597.3 | 17,997.0 | 150.9 | 0.993x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 17,628.6 | 17,609.7 | 17,690.1 | 29.2 | 0.993x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17,697.9 | 17,667.5 | 17,855.7 | 73.4 | 0.997x | 1.004x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17,734.3 | 17,719.4 | 17,782.4 | 22.7 | 0.999x | 1.006x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,749.3 | 17,679.5 | 17,781.5 | 38.4 | 1.000x | 1.007x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 39,337.4 | 39,223.7 | 40,015.7 | 287.4 | 2.216x | 2.232x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 310,117.0 | 309,910.7 | 310,479.5 | 183.7 | 17.472x | 17.599x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 310,392.8 | 310,137.1 | 319,688.7 | 3,742.7 | 17.488x | 17.615x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 2,791,699.8 | 2,789,004.5 | 2,829,668.1 | 15,450.1 | 157.285x | 158.427x |
| 10 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,799,563.2 | 2,789,783.7 | 3,071,085.4 | 108,296.7 | 157.728x | 158.873x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 30,829.4 | 30,743.9 | 30,873.7 | 45.7 | 0.437x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 30,896.9 | 30,746.9 | 30,951.7 | 70.7 | 0.438x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 30,939.0 | 30,875.2 | 30,967.6 | 31.3 | 0.438x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 30,981.7 | 30,853.5 | 31,202.3 | 126.7 | 0.439x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 69,317.0 | 68,798.6 | 69,580.9 | 260.6 | 0.982x | 2.248x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 70,617.0 | 70,422.3 | 70,889.1 | 166.8 | 1.000x | 2.291x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 320,961.8 | 320,429.3 | 323,151.1 | 952.5 | 4.545x | 10.411x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 322,506.7 | 322,072.3 | 325,096.1 | 1,112.4 | 4.567x | 10.461x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 3,337,656.4 | 3,274,377.3 | 3,374,722.5 | 43,521.6 | 47.264x | 108.262x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 3,368,779.2 | 3,294,248.8 | 3,384,503.3 | 33,560.1 | 47.705x | 109.272x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 17,634.2 | 17,625.9 | 17,669.8 | 17.0 | 0.994x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 17,645.2 | 17,634.8 | 17,673.2 | 14.3 | 0.994x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 17,695.9 | 17,676.9 | 18,034.9 | 136.4 | 0.997x | 1.003x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 17,734.5 | 17,696.4 | 18,368.6 | 257.2 | 0.999x | 1.006x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,747.4 | 17,718.3 | 17,791.3 | 24.5 | 1.000x | 1.006x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 39,612.0 | 39,513.1 | 40,068.9 | 198.9 | 2.232x | 2.246x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 310,051.9 | 309,924.5 | 310,227.2 | 106.8 | 17.470x | 17.582x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 310,488.9 | 310,268.5 | 310,797.5 | 215.1 | 17.495x | 17.607x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,941,908.1 | 2,900,648.5 | 3,407,472.8 | 190,740.9 | 165.766x | 166.830x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 3,407,572.1 | 2,910,537.8 | 3,410,830.8 | 218,862.0 | 192.004x | 193.237x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 0.059x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.5 | 32.3 | 32.8 | 0.1 | 0.059x | 1.003x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 0.059x | 1.005x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.5 | 44.3 | 44.7 | 0.2 | 0.080x | 1.373x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 44.7 | 44.4 | 45.8 | 0.5 | 0.081x | 1.377x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 47.1 | 46.7 | 47.3 | 0.2 | 0.085x | 1.451x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 47.1 | 47.0 | 49.2 | 0.8 | 0.085x | 1.453x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 545.3 | 540.1 | 551.4 | 4.2 | 0.985x | 16.809x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 553.4 | 545.4 | 558.0 | 4.5 | 1.000x | 17.058x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 53.3 | 53.3 | 53.7 | 0.2 | 0.097x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 54.2 | 53.9 | 64.1 | 4.0 | 0.099x | 1.016x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 55.1 | 54.4 | 55.7 | 0.4 | 0.101x | 1.034x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.5 | 58.4 | 71.4 | 5.1 | 0.107x | 1.097x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.6 | 58.3 | 58.8 | 0.2 | 0.107x | 1.099x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.6 | 58.5 | 59.0 | 0.2 | 0.107x | 1.100x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.8 | 58.4 | 67.4 | 3.5 | 0.107x | 1.102x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 73.4 | 73.0 | 75.5 | 0.9 | 0.134x | 1.377x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 77.3 | 77.2 | 80.5 | 1.3 | 0.141x | 1.450x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 547.5 | 539.0 | 553.7 | 5.4 | 1.000x | 10.271x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 39.9 | 39.7 | 41.4 | 0.6 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 40.0 | 39.7 | 40.1 | 0.1 | 0.052x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 40.0 | 39.8 | 40.2 | 0.2 | 0.052x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 40.1 | 39.8 | 40.4 | 0.2 | 0.053x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 84.9 | 84.4 | 85.4 | 0.3 | 0.111x | 2.124x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 86.2 | 85.0 | 86.2 | 0.5 | 0.113x | 2.157x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 88.7 | 88.1 | 89.9 | 0.7 | 0.116x | 2.221x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 91.4 | 90.3 | 92.0 | 0.6 | 0.120x | 2.289x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 764.0 | 759.3 | 782.6 | 8.8 | 1.000x | 19.123x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 768.1 | 746.8 | 771.8 | 9.3 | 1.005x | 19.226x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 77.8 | 77.6 | 78.0 | 0.1 | 0.101x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 77.8 | 77.7 | 78.1 | 0.2 | 0.101x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 77.9 | 77.8 | 82.4 | 1.8 | 0.101x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 77.9 | 77.7 | 83.5 | 2.2 | 0.102x | 1.002x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 88.8 | 88.7 | 90.0 | 0.5 | 0.116x | 1.142x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 90.4 | 90.2 | 90.6 | 0.1 | 0.118x | 1.163x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 91.2 | 90.7 | 92.6 | 0.7 | 0.119x | 1.173x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 92.8 | 92.5 | 92.9 | 0.1 | 0.121x | 1.193x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 93.9 | 90.6 | 95.8 | 1.8 | 0.122x | 1.208x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 767.8 | 761.8 | 780.8 | 6.9 | 1.000x | 9.873x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.3 | 0.0 | 0.038x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.3 | 0.0 | 0.038x | 1.000x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.4 | 18.2 | 18.9 | 0.3 | 0.038x | 1.007x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.3 | 30.0 | 30.4 | 0.1 | 0.062x | 1.658x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 30.5 | 30.3 | 30.9 | 0.2 | 0.063x | 1.668x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.2 | 33.1 | 33.3 | 0.1 | 0.068x | 1.817x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.3 | 33.1 | 36.3 | 1.3 | 0.069x | 1.821x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 483.8 | 473.4 | 487.4 | 4.8 | 0.997x | 26.494x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 485.4 | 478.3 | 503.1 | 8.8 | 1.000x | 26.585x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 26.0 | 26.1 | 0.0 | 0.054x | 1.003x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 26.0 | 26.2 | 0.1 | 0.054x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 33.6 | 3.0 | 0.054x | 1.009x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 37.9 | 37.5 | 38.4 | 0.3 | 0.079x | 1.459x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 38.0 | 37.9 | 39.2 | 0.5 | 0.079x | 1.462x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 38.7 | 38.5 | 38.7 | 0.1 | 0.080x | 1.486x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 54.7 | 54.6 | 68.5 | 5.6 | 0.113x | 2.102x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 64.6 | 64.2 | 68.5 | 1.7 | 0.134x | 2.484x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 481.8 | 472.6 | 490.3 | 6.4 | 1.000x | 18.527x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.3 | 43.3 | 43.4 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.5 | 0.1 | 0.056x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.4 | 43.3 | 43.5 | 0.1 | 0.056x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.4 | 43.2 | 43.5 | 0.1 | 0.056x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 59.1 | 57.6 | 61.7 | 1.3 | 0.076x | 1.365x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 59.2 | 58.5 | 60.0 | 0.6 | 0.076x | 1.367x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 59.9 | 59.2 | 60.4 | 0.4 | 0.077x | 1.382x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 60.0 | 59.3 | 61.2 | 0.7 | 0.077x | 1.385x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 771.2 | 760.1 | 781.3 | 8.3 | 0.992x | 17.813x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 777.4 | 767.8 | 785.7 | 6.7 | 1.000x | 17.956x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 66.2 | 65.2 | 69.2 | 1.4 | 0.086x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 66.4 | 66.0 | 71.0 | 1.9 | 0.086x | 1.004x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 67.5 | 66.5 | 68.2 | 0.6 | 0.087x | 1.020x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 84.9 | 84.2 | 93.5 | 3.5 | 0.110x | 1.283x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 86.6 | 86.2 | 87.0 | 0.3 | 0.112x | 1.310x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 86.8 | 86.5 | 86.9 | 0.2 | 0.112x | 1.312x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 86.9 | 86.3 | 91.1 | 1.7 | 0.113x | 1.313x |
| 8 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 87.1 | 86.8 | 87.5 | 0.2 | 0.113x | 1.316x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 93.6 | 92.8 | 94.2 | 0.5 | 0.121x | 1.415x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 771.5 | 770.3 | 782.3 | 4.5 | 1.000x | 11.662x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 57.5 | 57.1 | 58.8 | 0.6 | 0.101x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 58.0 | 57.3 | 58.3 | 0.3 | 0.102x | 1.009x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 60.7 | 60.4 | 62.5 | 0.8 | 0.107x | 1.055x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 60.7 | 60.6 | 60.9 | 0.1 | 0.107x | 1.056x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 61.1 | 60.8 | 61.4 | 0.2 | 0.108x | 1.062x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 61.1 | 61.0 | 61.2 | 0.1 | 0.108x | 1.062x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 61.1 | 61.0 | 61.5 | 0.2 | 0.108x | 1.063x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 61.1 | 60.9 | 61.7 | 0.3 | 0.108x | 1.063x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 567.1 | 561.7 | 570.8 | 3.1 | 1.000x | 9.862x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 572.0 | 554.8 | 575.2 | 7.6 | 1.009x | 9.947x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 65.8 | 64.6 | 65.9 | 0.5 | 0.116x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 66.8 | 65.8 | 67.3 | 0.5 | 0.118x | 1.015x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 67.8 | 67.8 | 68.8 | 0.4 | 0.120x | 1.031x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 88.7 | 88.3 | 88.9 | 0.2 | 0.157x | 1.349x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 92.7 | 91.1 | 94.1 | 1.1 | 0.164x | 1.409x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 120.4 | 120.2 | 120.6 | 0.2 | 0.212x | 1.830x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 120.4 | 120.4 | 120.5 | 0.1 | 0.212x | 1.830x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 120.4 | 119.9 | 130.3 | 4.0 | 0.212x | 1.830x |
| 9 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 120.4 | 119.4 | 120.8 | 0.4 | 0.212x | 1.830x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 566.7 | 561.3 | 573.1 | 4.3 | 1.000x | 8.615x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.3 | 0.1 | 0.037x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.4 | 0.1 | 0.037x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 0.037x | 1.005x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 30.3 | 30.3 | 30.5 | 0.1 | 0.061x | 1.665x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.4 | 30.2 | 30.4 | 0.1 | 0.061x | 1.666x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.3 | 33.2 | 33.8 | 0.2 | 0.067x | 1.827x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.4 | 33.3 | 34.6 | 0.5 | 0.067x | 1.833x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 481.8 | 471.6 | 494.3 | 7.8 | 0.971x | 26.441x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 496.2 | 473.9 | 530.0 | 18.9 | 1.000x | 27.228x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 26.0 | 26.1 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 25.9 | 26.7 | 0.3 | 0.054x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.0 | 33.2 | 2.8 | 0.054x | 1.004x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.4 | 26.0 | 27.5 | 0.6 | 0.055x | 1.012x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 38.0 | 37.8 | 39.3 | 0.5 | 0.079x | 1.459x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 38.1 | 37.4 | 38.5 | 0.4 | 0.079x | 1.460x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 38.7 | 38.4 | 38.8 | 0.1 | 0.080x | 1.483x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 54.6 | 54.6 | 55.1 | 0.2 | 0.114x | 2.096x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 65.2 | 63.9 | 69.5 | 2.1 | 0.136x | 2.501x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 480.6 | 473.6 | 483.7 | 3.5 | 1.000x | 18.432x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.7 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 30.9 | 30.8 | 31.1 | 0.1 | 0.038x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.1 | 0.038x | 1.000x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.1 | 30.9 | 31.6 | 0.2 | 0.039x | 1.007x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 95.2 | 95.0 | 96.5 | 0.6 | 0.118x | 3.081x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 96.3 | 94.7 | 98.9 | 1.4 | 0.120x | 3.115x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 96.7 | 96.5 | 98.1 | 0.6 | 0.120x | 3.129x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 96.7 | 95.4 | 98.2 | 1.1 | 0.120x | 3.130x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 779.0 | 771.8 | 800.2 | 10.8 | 0.969x | 25.203x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 803.9 | 775.8 | 843.0 | 24.7 | 1.000x | 26.010x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 55.8 | 55.5 | 55.9 | 0.1 | 0.070x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 55.9 | 55.9 | 56.1 | 0.1 | 0.070x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 56.0 | 55.7 | 62.8 | 2.8 | 0.071x | 1.003x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 56.1 | 55.7 | 59.1 | 1.3 | 0.071x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 85.2 | 84.0 | 91.2 | 3.2 | 0.108x | 1.528x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 129.0 | 127.2 | 130.0 | 0.9 | 0.163x | 2.314x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 132.4 | 132.1 | 133.5 | 0.5 | 0.167x | 2.373x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 138.2 | 135.6 | 144.5 | 3.1 | 0.174x | 2.477x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 139.5 | 134.6 | 142.9 | 2.9 | 0.176x | 2.501x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 792.6 | 778.7 | 794.9 | 5.9 | 1.000x | 14.210x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.7 | 46.4 | 46.7 | 0.1 | 0.074x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.7 | 46.6 | 47.0 | 0.2 | 0.074x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 46.9 | 46.5 | 47.3 | 0.3 | 0.075x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 46.9 | 46.7 | 47.5 | 0.3 | 0.075x | 1.005x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 52.5 | 52.3 | 53.3 | 0.4 | 0.084x | 1.125x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 53.5 | 52.7 | 53.9 | 0.4 | 0.085x | 1.146x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.5 | 55.4 | 56.5 | 0.4 | 0.089x | 1.190x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.7 | 55.6 | 55.9 | 0.1 | 0.089x | 1.194x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 618.2 | 603.0 | 623.1 | 7.0 | 0.986x | 13.249x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 627.3 | 613.0 | 635.7 | 9.0 | 1.000x | 13.443x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 62.0 | 61.0 | 68.2 | 2.6 | 0.100x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 62.4 | 61.8 | 62.7 | 0.3 | 0.100x | 1.008x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 64.3 | 63.9 | 65.1 | 0.4 | 0.103x | 1.037x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 78.0 | 77.5 | 89.6 | 4.7 | 0.125x | 1.258x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 91.8 | 85.6 | 96.3 | 4.1 | 0.147x | 1.481x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 92.0 | 91.8 | 92.3 | 0.2 | 0.148x | 1.484x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 92.0 | 91.8 | 92.2 | 0.1 | 0.148x | 1.485x |
| 8 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 92.3 | 91.9 | 92.5 | 0.2 | 0.148x | 1.489x |
| 9 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 92.5 | 91.8 | 102.3 | 4.0 | 0.149x | 1.493x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 622.3 | 612.9 | 629.0 | 5.5 | 1.000x | 10.044x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 36.7 | 36.6 | 37.1 | 0.2 | 0.067x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.7 | 36.6 | 36.7 | 0.1 | 0.067x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 36.7 | 36.5 | 37.8 | 0.5 | 0.067x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.3 | 45.9 | 46.6 | 0.3 | 0.085x | 1.265x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 46.6 | 46.3 | 46.8 | 0.2 | 0.085x | 1.272x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.7 | 48.6 | 51.0 | 1.1 | 0.089x | 1.330x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.8 | 48.5 | 49.0 | 0.2 | 0.089x | 1.332x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 542.1 | 534.1 | 544.5 | 3.6 | 0.990x | 14.804x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 547.4 | 542.6 | 556.1 | 4.4 | 1.000x | 14.948x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 55.1 | 54.5 | 55.6 | 0.4 | 0.101x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 55.3 | 54.6 | 55.8 | 0.4 | 0.102x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 56.9 | 56.7 | 57.3 | 0.2 | 0.105x | 1.032x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 69.6 | 69.6 | 69.7 | 0.1 | 0.128x | 1.262x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 69.6 | 69.5 | 81.5 | 4.8 | 0.128x | 1.263x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 69.6 | 69.4 | 69.8 | 0.1 | 0.128x | 1.263x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 69.7 | 69.5 | 69.9 | 0.1 | 0.128x | 1.265x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 75.2 | 75.0 | 92.1 | 6.8 | 0.138x | 1.364x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 79.3 | 78.7 | 87.4 | 3.2 | 0.146x | 1.438x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 543.7 | 538.4 | 551.3 | 4.8 | 1.000x | 9.863x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 31.2 | 0.7 | 0.054x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.054x | 1.000x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.8 | 0.1 | 0.054x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.6 | 42.4 | 43.7 | 0.5 | 0.078x | 1.441x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 42.7 | 42.6 | 42.9 | 0.1 | 0.078x | 1.443x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.9 | 44.8 | 45.2 | 0.1 | 0.082x | 1.517x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 45.5 | 45.1 | 47.2 | 0.9 | 0.084x | 1.538x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 535.2 | 532.1 | 542.0 | 3.4 | 0.982x | 18.088x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 544.9 | 537.2 | 549.6 | 4.4 | 1.000x | 18.416x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 50.6 | 50.0 | 54.6 | 1.6 | 0.093x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 50.7 | 50.4 | 50.8 | 0.1 | 0.093x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.4 | 51.2 | 51.5 | 0.1 | 0.095x | 1.016x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 51.5 | 51.4 | 63.5 | 4.8 | 0.095x | 1.017x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.5 | 51.4 | 51.5 | 0.1 | 0.095x | 1.017x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.7 | 51.5 | 52.2 | 0.2 | 0.095x | 1.022x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 52.7 | 52.4 | 53.0 | 0.2 | 0.097x | 1.041x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 71.0 | 70.8 | 75.5 | 1.8 | 0.131x | 1.403x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 75.4 | 74.6 | 83.2 | 3.2 | 0.139x | 1.490x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 543.3 | 536.2 | 544.0 | 2.9 | 1.000x | 10.735x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.7 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.8 | 0.1 | 0.067x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 0.067x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 0.067x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.4 | 30.8 | 32.5 | 0.6 | 0.071x | 1.062x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.9 | 31.4 | 33.2 | 0.6 | 0.072x | 1.081x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.4 | 32.8 | 35.0 | 0.7 | 0.075x | 1.131x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.0 | 33.4 | 34.6 | 0.4 | 0.077x | 1.152x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 437.6 | 433.4 | 443.8 | 3.9 | 0.987x | 14.827x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 443.4 | 439.3 | 445.4 | 2.2 | 1.000x | 15.022x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 36.3 | 35.8 | 36.9 | 0.4 | 0.083x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 36.4 | 36.2 | 36.4 | 0.1 | 0.084x | 1.004x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 37.1 | 36.8 | 37.4 | 0.2 | 0.085x | 1.024x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 37.6 | 36.6 | 37.7 | 0.4 | 0.086x | 1.038x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.4 | 51.3 | 51.6 | 0.1 | 0.118x | 1.417x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 51.5 | 51.2 | 63.6 | 4.9 | 0.118x | 1.421x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.7 | 51.4 | 51.9 | 0.2 | 0.119x | 1.425x |
| 8 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.7 | 51.5 | 51.8 | 0.1 | 0.119x | 1.425x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 69.4 | 67.3 | 75.8 | 2.9 | 0.159x | 1.913x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 435.5 | 431.9 | 444.6 | 5.4 | 1.000x | 12.009x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.4 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.7 | 0.2 | 0.035x | 1.010x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.036x | 1.031x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.8 | 0.1 | 0.036x | 1.032x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 31.3 | 31.0 | 32.2 | 0.5 | 0.089x | 2.543x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 31.3 | 30.9 | 31.5 | 0.2 | 0.089x | 2.544x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.6 | 61.1 | 10.9 | 0.096x | 2.742x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.0 | 33.7 | 36.0 | 0.9 | 0.097x | 2.758x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 346.0 | 338.3 | 350.5 | 4.0 | 0.987x | 28.102x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 350.6 | 341.0 | 365.6 | 8.5 | 1.000x | 28.479x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 34.6 | 34.5 | 34.7 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 34.6 | 34.5 | 41.9 | 2.9 | 0.020x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 34.7 | 34.6 | 34.9 | 0.1 | 0.020x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 34.7 | 34.6 | 34.8 | 0.1 | 0.020x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 141.9 | 140.3 | 146.1 | 2.6 | 0.081x | 4.100x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 319.0 | 314.8 | 323.3 | 3.0 | 0.183x | 9.218x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 319.6 | 316.1 | 320.6 | 1.6 | 0.183x | 9.234x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 322.1 | 320.7 | 328.2 | 2.6 | 0.185x | 9.308x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 324.5 | 324.0 | 341.3 | 6.7 | 0.186x | 9.378x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,745.6 | 1,732.2 | 1,776.7 | 14.9 | 1.000x | 50.442x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.4 | 35.3 | 36.6 | 0.5 | 0.052x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.7 | 0.2 | 0.052x | 1.005x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 62.6 | 60.4 | 65.2 | 1.8 | 0.092x | 1.775x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72.5 | 72.2 | 74.1 | 0.7 | 0.106x | 2.056x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73.1 | 72.8 | 73.4 | 0.2 | 0.107x | 2.073x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73.6 | 73.5 | 73.8 | 0.1 | 0.108x | 2.087x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 670.1 | 665.2 | 686.4 | 8.0 | 0.983x | 19.002x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 681.9 | 670.9 | 694.9 | 7.9 | 1.000x | 19.338x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 64.9 | 64.3 | 66.0 | 0.7 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 65.2 | 64.6 | 65.3 | 0.2 | 0.097x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.6 | 65.4 | 66.0 | 0.2 | 0.097x | 1.010x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.4 | 66.8 | 0.5 | 0.097x | 1.012x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 66.1 | 65.5 | 66.5 | 0.3 | 0.098x | 1.018x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 66.2 | 65.5 | 82.4 | 6.6 | 0.098x | 1.019x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 70.2 | 66.8 | 71.9 | 2.0 | 0.104x | 1.080x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 82.3 | 81.7 | 82.8 | 0.4 | 0.122x | 1.267x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 82.4 | 82.3 | 89.7 | 2.8 | 0.122x | 1.269x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 674.9 | 664.4 | 691.4 | 9.9 | 1.000x | 10.391x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.6 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.052x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.052x | 1.005x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 61.8 | 60.3 | 65.7 | 1.9 | 0.091x | 1.752x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72.6 | 72.5 | 74.8 | 0.9 | 0.107x | 2.060x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73.2 | 73.1 | 73.8 | 0.3 | 0.107x | 2.077x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73.6 | 73.4 | 73.7 | 0.1 | 0.108x | 2.087x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 668.1 | 663.7 | 683.5 | 8.5 | 0.981x | 18.952x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 681.2 | 670.4 | 697.5 | 9.0 | 1.000x | 19.326x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 64.3 | 64.2 | 64.9 | 0.3 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 65.1 | 64.5 | 66.4 | 0.6 | 0.096x | 1.012x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.5 | 65.3 | 65.8 | 0.2 | 0.097x | 1.019x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.097x | 1.022x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.8 | 65.6 | 66.0 | 0.1 | 0.097x | 1.023x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.7 | 82.3 | 6.6 | 0.097x | 1.024x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 67.4 | 67.0 | 70.3 | 1.4 | 0.100x | 1.048x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 82.5 | 81.9 | 87.1 | 1.9 | 0.122x | 1.282x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 82.5 | 81.5 | 83.1 | 0.5 | 0.122x | 1.283x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 676.5 | 666.1 | 691.6 | 8.5 | 1.000x | 10.517x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.9 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.055x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.055x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.6 | 32.3 | 1.1 | 0.055x | 1.004x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 48.0 | 47.8 | 49.8 | 0.7 | 0.089x | 1.624x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 48.6 | 47.7 | 50.8 | 1.1 | 0.090x | 1.644x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 50.3 | 50.1 | 50.4 | 0.1 | 0.093x | 1.701x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 50.4 | 50.2 | 53.8 | 1.6 | 0.093x | 1.704x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 537.2 | 522.8 | 542.2 | 6.7 | 0.992x | 18.174x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 541.4 | 537.1 | 546.1 | 3.4 | 1.000x | 18.317x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 51.6 | 51.5 | 63.3 | 4.7 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.6 | 51.4 | 51.8 | 0.1 | 0.097x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.6 | 51.3 | 51.7 | 0.2 | 0.097x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.6 | 51.4 | 52.0 | 0.2 | 0.097x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 54.6 | 54.1 | 55.1 | 0.4 | 0.102x | 1.059x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 54.8 | 54.8 | 56.0 | 0.5 | 0.103x | 1.063x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 57.5 | 56.8 | 61.4 | 1.9 | 0.108x | 1.116x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 72.7 | 72.4 | 73.3 | 0.3 | 0.136x | 1.409x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 77.0 | 76.7 | 84.8 | 3.1 | 0.144x | 1.494x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 534.4 | 529.4 | 549.7 | 7.2 | 1.000x | 10.363x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.6 | 33.9 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.0 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.8 | 34.0 | 0.1 | 0.052x | 1.002x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.0 | 0.1 | 0.052x | 1.003x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 58.0 | 57.8 | 62.2 | 1.7 | 0.089x | 1.718x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 66.8 | 66.6 | 66.9 | 0.1 | 0.102x | 1.978x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 67.1 | 67.1 | 67.3 | 0.1 | 0.103x | 1.988x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 67.9 | 67.7 | 68.0 | 0.1 | 0.104x | 2.010x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 650.4 | 645.3 | 663.3 | 6.9 | 0.994x | 19.264x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 654.3 | 652.0 | 665.4 | 5.0 | 1.000x | 19.379x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 61.7 | 61.1 | 62.7 | 0.5 | 0.094x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 62.3 | 61.7 | 62.8 | 0.4 | 0.095x | 1.009x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.6 | 62.1 | 63.0 | 0.3 | 0.096x | 1.014x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.6 | 62.3 | 78.7 | 6.5 | 0.096x | 1.014x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.6 | 62.3 | 63.2 | 0.3 | 0.096x | 1.015x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.7 | 62.6 | 63.1 | 0.2 | 0.096x | 1.016x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 64.7 | 64.1 | 65.7 | 0.5 | 0.099x | 1.049x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 80.7 | 80.0 | 80.9 | 0.3 | 0.123x | 1.308x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 81.0 | 80.7 | 88.9 | 3.2 | 0.124x | 1.313x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 653.8 | 640.4 | 671.3 | 10.0 | 1.000x | 10.592x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.5 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.9 | 10.7 | 12.7 | 0.7 | 0.058x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.6 | 11.5 | 11.8 | 0.1 | 0.061x | 1.062x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.8 | 11.5 | 12.1 | 0.2 | 0.062x | 1.083x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.1 | 25.1 | 25.3 | 0.1 | 0.132x | 2.301x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 25.4 | 25.0 | 26.4 | 0.5 | 0.134x | 2.330x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.137x | 2.372x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.9 | 25.8 | 27.8 | 0.8 | 0.137x | 2.376x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 187.0 | 185.2 | 187.3 | 0.8 | 0.987x | 17.140x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 189.5 | 185.1 | 203.3 | 6.2 | 1.000x | 17.369x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 0.024x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.2 | 26.2 | 26.4 | 0.1 | 0.024x | 1.004x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.4 | 26.1 | 26.9 | 0.3 | 0.024x | 1.009x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 26.2 | 33.3 | 2.8 | 0.025x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 109.4 | 108.4 | 115.8 | 3.1 | 0.102x | 4.188x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 227.1 | 225.5 | 233.6 | 2.8 | 0.211x | 8.692x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 228.6 | 226.5 | 342.9 | 45.8 | 0.212x | 8.749x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 232.0 | 228.9 | 235.5 | 2.1 | 0.215x | 8.878x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 233.9 | 232.0 | 245.2 | 4.8 | 0.217x | 8.951x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,076.7 | 1,063.5 | 1,091.4 | 9.9 | 1.000x | 41.204x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.7 | 0.2 | 0.052x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.4 | 0.0 | 0.052x | 1.000x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.052x | 1.001x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 60.5 | 60.4 | 65.4 | 2.0 | 0.089x | 1.713x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72.5 | 72.4 | 73.1 | 0.2 | 0.107x | 2.053x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73.1 | 72.7 | 73.7 | 0.4 | 0.108x | 2.068x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73.7 | 73.6 | 74.0 | 0.1 | 0.109x | 2.086x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 668.7 | 662.3 | 676.7 | 5.4 | 0.987x | 18.923x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 677.7 | 669.4 | 685.4 | 5.1 | 1.000x | 19.180x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 64.9 | 64.4 | 66.9 | 0.9 | 0.096x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 65.4 | 62.9 | 66.4 | 1.2 | 0.097x | 1.008x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.6 | 65.7 | 0.0 | 0.098x | 1.013x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.098x | 1.013x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 65.7 | 65.5 | 82.1 | 6.6 | 0.098x | 1.013x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.6 | 66.4 | 0.3 | 0.098x | 1.017x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 68.0 | 66.7 | 69.6 | 1.2 | 0.101x | 1.049x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 82.2 | 81.8 | 88.7 | 2.7 | 0.122x | 1.267x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 83.8 | 81.1 | 148.5 | 25.8 | 0.125x | 1.293x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 672.4 | 662.1 | 689.5 | 9.6 | 1.000x | 10.368x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.8 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.0 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.9 | 0.0 | 0.052x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.052x | 1.001x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 57.9 | 57.6 | 62.6 | 1.9 | 0.089x | 1.714x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 66.7 | 66.5 | 68.0 | 0.5 | 0.102x | 1.976x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 67.3 | 67.0 | 67.7 | 0.2 | 0.103x | 1.994x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 67.9 | 67.3 | 68.7 | 0.5 | 0.104x | 2.011x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 651.7 | 645.3 | 665.8 | 7.3 | 1.000x | 19.294x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 655.1 | 645.7 | 663.0 | 5.9 | 1.005x | 19.395x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 61.8 | 61.4 | 63.1 | 0.6 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 62.2 | 62.2 | 62.5 | 0.1 | 0.096x | 1.007x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.5 | 62.3 | 62.7 | 0.2 | 0.096x | 1.011x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.5 | 62.3 | 62.8 | 0.2 | 0.096x | 1.011x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.6 | 62.5 | 62.6 | 0.0 | 0.096x | 1.013x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.8 | 62.5 | 78.7 | 6.4 | 0.096x | 1.015x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 64.5 | 64.2 | 68.4 | 1.6 | 0.099x | 1.043x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 80.1 | 79.8 | 87.6 | 3.0 | 0.123x | 1.295x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 82.7 | 80.5 | 141.0 | 23.2 | 0.127x | 1.338x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 650.4 | 648.0 | 670.7 | 8.2 | 1.000x | 10.522x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 11.1 | 11.8 | 0.3 | 0.057x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.8 | 0.3 | 0.057x | 1.007x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.2 | 0.1 | 0.062x | 1.083x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.2 | 0.1 | 0.062x | 1.087x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 25.5 | 25.4 | 26.0 | 0.2 | 0.130x | 2.295x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.7 | 25.7 | 27.2 | 0.6 | 0.132x | 2.314x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.5 | 26.4 | 26.7 | 0.1 | 0.136x | 2.385x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.7 | 26.6 | 28.9 | 0.9 | 0.136x | 2.395x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 192.5 | 192.0 | 195.2 | 1.3 | 0.983x | 17.300x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 195.8 | 188.5 | 199.8 | 4.1 | 1.000x | 17.595x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 27.6 | 27.4 | 39.4 | 4.7 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 27.7 | 27.5 | 27.9 | 0.1 | 0.025x | 1.004x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 27.7 | 27.5 | 27.9 | 0.2 | 0.025x | 1.005x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 27.8 | 27.5 | 28.3 | 0.3 | 0.026x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 111.0 | 109.4 | 119.3 | 4.4 | 0.102x | 4.028x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 237.9 | 237.6 | 521.0 | 113.0 | 0.219x | 8.633x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 239.2 | 236.6 | 243.8 | 2.6 | 0.220x | 8.681x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 241.1 | 237.3 | 244.3 | 2.4 | 0.222x | 8.752x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 244.8 | 241.6 | 254.1 | 4.5 | 0.225x | 8.887x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,088.1 | 1,080.5 | 1,101.5 | 7.7 | 1.000x | 39.493x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 38.3 | 38.3 | 38.5 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.4 | 38.3 | 39.0 | 0.3 | 0.056x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.6 | 0.1 | 0.056x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 38.4 | 38.3 | 39.0 | 0.3 | 0.056x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 63.1 | 63.0 | 63.8 | 0.3 | 0.092x | 1.647x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 63.7 | 63.3 | 63.7 | 0.2 | 0.093x | 1.660x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 65.8 | 65.7 | 66.6 | 0.3 | 0.096x | 1.717x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 66.2 | 65.8 | 68.9 | 1.2 | 0.097x | 1.726x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 681.8 | 675.2 | 692.2 | 5.7 | 0.998x | 17.782x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 683.3 | 682.5 | 696.6 | 5.3 | 1.000x | 17.820x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 70.0 | 69.2 | 70.2 | 0.5 | 0.103x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 70.1 | 69.5 | 70.7 | 0.4 | 0.103x | 1.002x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 72.6 | 71.2 | 76.0 | 2.1 | 0.106x | 1.037x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 72.9 | 72.3 | 73.1 | 0.3 | 0.107x | 1.041x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 72.9 | 72.6 | 72.9 | 0.1 | 0.107x | 1.041x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 73.0 | 72.9 | 84.0 | 4.4 | 0.107x | 1.043x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 73.1 | 73.0 | 73.5 | 0.2 | 0.107x | 1.045x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 86.3 | 84.9 | 158.3 | 28.5 | 0.127x | 1.233x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 87.5 | 86.7 | 88.0 | 0.5 | 0.128x | 1.249x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 682.0 | 679.3 | 697.0 | 6.5 | 1.000x | 9.743x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.042x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 0.042x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.8 | 0.1 | 0.042x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 74.9 | 74.7 | 76.6 | 0.7 | 0.106x | 2.528x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 76.5 | 75.3 | 76.6 | 0.6 | 0.108x | 2.583x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 85.1 | 83.8 | 86.1 | 0.8 | 0.120x | 2.875x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 86.9 | 86.0 | 87.4 | 0.5 | 0.123x | 2.934x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 703.4 | 700.4 | 712.0 | 4.1 | 0.994x | 23.754x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 707.8 | 703.1 | 739.1 | 13.7 | 1.000x | 23.904x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 51.3 | 51.2 | 63.5 | 4.8 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.5 | 51.2 | 51.6 | 0.2 | 0.073x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.6 | 51.4 | 52.5 | 0.4 | 0.073x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.7 | 51.5 | 52.8 | 0.5 | 0.073x | 1.008x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 62.7 | 61.4 | 70.0 | 3.1 | 0.089x | 1.222x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 64.4 | 61.0 | 69.8 | 3.2 | 0.091x | 1.255x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 74.3 | 74.2 | 76.1 | 0.7 | 0.105x | 1.447x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 90.1 | 89.9 | 97.0 | 2.8 | 0.128x | 1.755x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 93.6 | 92.5 | 94.9 | 0.9 | 0.133x | 1.823x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 705.9 | 696.9 | 709.2 | 4.9 | 1.000x | 13.750x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.1 | 35.7 | 36.4 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 36.6 | 36.4 | 37.8 | 0.5 | 0.081x | 1.013x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 38.0 | 37.8 | 38.1 | 0.1 | 0.084x | 1.052x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.3 | 38.2 | 38.5 | 0.1 | 0.085x | 1.060x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.6 | 41.6 | 41.6 | 0.0 | 0.092x | 1.151x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.6 | 41.4 | 41.9 | 0.2 | 0.092x | 1.152x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.7 | 41.6 | 43.5 | 0.7 | 0.092x | 1.153x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.5 | 42.0 | 0.2 | 0.093x | 1.155x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 445.6 | 444.5 | 451.6 | 2.8 | 0.989x | 12.329x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 450.7 | 449.8 | 465.6 | 6.0 | 1.000x | 12.468x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 40.4 | 40.3 | 46.4 | 2.4 | 0.090x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 40.9 | 40.2 | 46.4 | 2.4 | 0.091x | 1.011x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 41.9 | 41.0 | 41.9 | 0.4 | 0.093x | 1.036x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 42.2 | 41.9 | 42.2 | 0.1 | 0.094x | 1.044x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.4 | 70.0 | 76.4 | 2.3 | 0.158x | 1.768x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 80.3 | 80.0 | 84.4 | 1.7 | 0.178x | 1.986x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.4 | 80.3 | 80.5 | 0.1 | 0.178x | 1.989x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 80.6 | 80.2 | 91.5 | 4.4 | 0.179x | 1.993x |
| 9 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.7 | 80.3 | 80.9 | 0.2 | 0.179x | 1.996x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 450.8 | 443.3 | 454.7 | 4.0 | 1.000x | 11.155x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.053x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.053x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.5 | 35.3 | 36.0 | 0.3 | 0.053x | 1.005x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.8 | 0.2 | 0.053x | 1.006x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 76.6 | 76.4 | 77.2 | 0.3 | 0.114x | 2.171x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 77.3 | 76.7 | 84.3 | 2.9 | 0.115x | 2.191x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 84.7 | 84.3 | 86.1 | 0.7 | 0.126x | 2.400x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 84.9 | 84.3 | 85.1 | 0.3 | 0.126x | 2.405x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 670.2 | 665.6 | 674.6 | 2.9 | 0.997x | 18.992x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 672.0 | 670.1 | 688.4 | 7.8 | 1.000x | 19.044x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.6 | 65.6 | 65.7 | 0.1 | 0.098x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 65.8 | 65.7 | 78.1 | 4.9 | 0.099x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.9 | 65.7 | 67.7 | 0.8 | 0.099x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 65.9 | 65.7 | 66.3 | 0.2 | 0.099x | 1.005x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 67.5 | 62.8 | 70.8 | 2.7 | 0.101x | 1.028x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 72.1 | 62.4 | 72.8 | 4.9 | 0.108x | 1.100x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 74.8 | 74.5 | 75.3 | 0.3 | 0.112x | 1.140x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 83.5 | 82.8 | 90.7 | 3.0 | 0.125x | 1.273x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 94.4 | 92.7 | 94.8 | 0.7 | 0.142x | 1.439x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 667.2 | 661.9 | 675.6 | 4.7 | 1.000x | 10.169x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.041x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 0.041x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.041x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 77.2 | 76.9 | 79.9 | 1.1 | 0.107x | 2.613x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 79.1 | 78.2 | 80.1 | 0.6 | 0.110x | 2.675x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 88.0 | 84.6 | 89.1 | 1.8 | 0.122x | 2.976x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 88.4 | 88.0 | 89.5 | 0.6 | 0.123x | 2.989x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 707.6 | 701.3 | 713.3 | 4.4 | 0.981x | 23.932x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 721.4 | 714.7 | 742.4 | 9.8 | 1.000x | 24.398x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 51.4 | 51.4 | 63.8 | 4.9 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 51.5 | 51.4 | 51.8 | 0.2 | 0.073x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 51.8 | 51.3 | 52.3 | 0.3 | 0.073x | 1.007x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 51.8 | 51.5 | 51.9 | 0.2 | 0.073x | 1.008x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 66.3 | 65.7 | 68.7 | 1.1 | 0.094x | 1.290x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 87.5 | 86.8 | 89.1 | 0.8 | 0.124x | 1.701x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 89.7 | 89.1 | 96.3 | 2.8 | 0.127x | 1.745x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 90.1 | 89.4 | 93.1 | 1.3 | 0.127x | 1.752x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 97.1 | 96.4 | 97.4 | 0.4 | 0.137x | 1.888x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 708.0 | 703.5 | 720.2 | 5.7 | 1.000x | 13.765x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.047x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.3 | 0.0 | 0.047x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.048x | 1.003x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.5 | 0.1 | 0.048x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 78.8 | 78.3 | 79.0 | 0.3 | 0.106x | 2.233x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 79.7 | 79.4 | 80.1 | 0.2 | 0.107x | 2.259x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 86.3 | 86.2 | 86.3 | 0.1 | 0.116x | 2.444x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 91.6 | 91.0 | 92.7 | 0.6 | 0.123x | 2.595x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 724.6 | 722.5 | 733.9 | 4.3 | 0.974x | 20.533x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 743.6 | 727.3 | 750.5 | 7.9 | 1.000x | 21.071x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.5 | 65.7 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 65.7 | 65.4 | 65.8 | 0.2 | 0.090x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 66.1 | 65.9 | 66.5 | 0.2 | 0.091x | 1.007x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 66.4 | 66.3 | 66.7 | 0.1 | 0.091x | 1.012x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 66.4 | 65.8 | 77.5 | 4.5 | 0.091x | 1.012x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 84.1 | 83.9 | 100.7 | 6.6 | 0.115x | 1.281x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 87.9 | 83.9 | 88.9 | 2.0 | 0.120x | 1.339x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 91.0 | 90.4 | 93.2 | 1.1 | 0.125x | 1.386x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 96.1 | 95.6 | 96.5 | 0.3 | 0.132x | 1.464x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 730.1 | 725.0 | 734.2 | 2.9 | 1.000x | 11.118x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 36.0 | 35.7 | 36.1 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.1 | 36.6 | 37.3 | 0.3 | 0.082x | 1.030x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 37.8 | 37.6 | 38.1 | 0.2 | 0.084x | 1.048x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 38.3 | 38.2 | 39.5 | 0.5 | 0.085x | 1.063x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.6 | 41.4 | 42.1 | 0.2 | 0.092x | 1.156x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.8 | 0.1 | 0.092x | 1.157x |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.9 | 0.1 | 0.092x | 1.157x |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.8 | 0.1 | 0.092x | 1.158x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 446.8 | 442.5 | 453.2 | 3.7 | 0.989x | 12.403x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 451.7 | 445.1 | 464.8 | 7.0 | 1.000x | 12.537x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 40.5 | 40.4 | 46.4 | 2.4 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 41.3 | 39.5 | 46.3 | 2.4 | 0.092x | 1.019x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 41.7 | 41.0 | 42.0 | 0.4 | 0.093x | 1.028x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 42.3 | 42.1 | 43.0 | 0.3 | 0.095x | 1.043x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.2 | 69.9 | 77.1 | 2.7 | 0.159x | 1.757x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 80.2 | 80.0 | 84.6 | 1.8 | 0.179x | 1.979x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.4 | 80.3 | 80.6 | 0.1 | 0.180x | 1.984x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 80.5 | 80.3 | 91.6 | 4.4 | 0.180x | 1.986x |
| 9 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.5 | 80.4 | 80.7 | 0.1 | 0.180x | 1.986x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 446.9 | 443.5 | 455.2 | 3.9 | 1.000x | 11.028x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.9 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.8 | 0.1 | 0.065x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.7 | 41.3 | 41.8 | 0.2 | 0.065x | 1.003x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.8 | 0.1 | 0.065x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73.2 | 71.7 | 74.1 | 0.9 | 0.114x | 1.759x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73.7 | 72.6 | 74.6 | 0.7 | 0.115x | 1.772x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 85.1 | 85.0 | 85.3 | 0.1 | 0.133x | 2.045x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 87.1 | 84.5 | 88.1 | 1.4 | 0.136x | 2.095x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 628.6 | 623.0 | 637.1 | 4.7 | 0.981x | 15.112x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 640.5 | 626.2 | 654.9 | 10.7 | 1.000x | 15.399x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 62.0 | 61.8 | 66.6 | 1.9 | 0.098x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 63.3 | 63.1 | 63.4 | 0.1 | 0.100x | 1.021x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 74.1 | 73.1 | 75.7 | 0.8 | 0.117x | 1.194x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 80.3 | 79.9 | 81.8 | 0.7 | 0.127x | 1.294x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 80.5 | 80.3 | 80.7 | 0.2 | 0.127x | 1.297x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 80.7 | 80.4 | 81.1 | 0.2 | 0.127x | 1.301x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 80.8 | 80.4 | 91.9 | 4.5 | 0.127x | 1.302x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 81.5 | 81.3 | 90.8 | 3.7 | 0.128x | 1.313x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 89.0 | 88.8 | 89.3 | 0.2 | 0.140x | 1.434x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 633.9 | 625.9 | 639.5 | 4.6 | 1.000x | 10.217x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.006x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.044x | 1.012x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.044x | 1.017x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.4 | 33.9 | 35.0 | 0.4 | 0.114x | 2.607x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.0 | 0.1 | 0.115x | 2.641x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.9 | 34.7 | 35.2 | 0.2 | 0.115x | 2.644x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.1 | 33.6 | 36.8 | 1.1 | 0.116x | 2.664x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 295.7 | 292.9 | 302.4 | 3.4 | 0.977x | 22.424x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 302.6 | 295.3 | 322.3 | 9.6 | 1.000x | 22.948x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 22.2 | 22.2 | 22.4 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 22.2 | 22.2 | 25.0 | 1.1 | 0.021x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 22.3 | 22.1 | 30.6 | 3.3 | 0.021x | 1.004x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 22.3 | 22.2 | 22.5 | 0.1 | 0.021x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 69.0 | 67.5 | 76.8 | 3.3 | 0.064x | 3.108x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 252.6 | 249.4 | 258.3 | 3.2 | 0.235x | 11.386x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 258.4 | 254.8 | 259.0 | 1.5 | 0.241x | 11.649x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 260.4 | 253.5 | 265.1 | 4.1 | 0.243x | 11.740x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 260.5 | 258.8 | 262.9 | 1.4 | 0.243x | 11.745x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,073.1 | 1,066.8 | 1,085.8 | 7.1 | 1.000x | 48.379x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.8 | 0.6 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.005x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.044x | 1.006x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.044x | 1.008x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.5 | 33.1 | 35.7 | 1.0 | 0.111x | 2.536x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.7 | 32.9 | 36.0 | 1.1 | 0.112x | 2.553x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.1 | 0.1 | 0.116x | 2.643x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.0 | 0.1 | 0.116x | 2.646x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 295.8 | 294.8 | 299.7 | 1.8 | 0.980x | 22.380x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 301.8 | 296.3 | 316.5 | 7.4 | 1.000x | 22.835x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 45.3 | 45.1 | 45.3 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 45.3 | 45.3 | 46.3 | 0.4 | 0.042x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 45.4 | 45.3 | 45.5 | 0.0 | 0.043x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 45.4 | 45.2 | 54.9 | 3.8 | 0.043x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.9 | 70.2 | 77.6 | 2.6 | 0.067x | 1.588x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 530.2 | 528.4 | 538.3 | 3.5 | 0.497x | 11.702x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 532.9 | 528.8 | 538.4 | 3.3 | 0.500x | 11.762x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 535.6 | 529.5 | 537.5 | 3.5 | 0.502x | 11.820x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 537.7 | 536.0 | 539.2 | 1.0 | 0.504x | 11.868x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,066.4 | 1,062.8 | 1,089.0 | 9.6 | 1.000x | 23.538x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.7 | 0.6 | 0.044x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.044x | 1.007x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.3 | 0.4 | 0.045x | 1.016x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.0 | 33.7 | 34.9 | 0.5 | 0.113x | 2.573x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.6 | 33.5 | 35.4 | 0.6 | 0.115x | 2.621x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 34.7 | 34.6 | 34.8 | 0.1 | 0.115x | 2.632x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.6 | 0.4 | 0.116x | 2.633x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 298.5 | 294.8 | 299.4 | 1.8 | 0.992x | 22.602x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 300.9 | 295.8 | 317.0 | 7.5 | 1.000x | 22.789x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 22.1 | 22.0 | 22.1 | 0.0 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 22.3 | 22.1 | 23.1 | 0.4 | 0.021x | 1.006x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 22.3 | 22.1 | 23.1 | 0.3 | 0.021x | 1.008x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 22.4 | 22.1 | 31.4 | 3.6 | 0.021x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 68.7 | 68.6 | 76.6 | 3.1 | 0.064x | 3.105x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 257.5 | 249.8 | 259.2 | 3.7 | 0.241x | 11.640x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 257.8 | 254.3 | 267.9 | 5.3 | 0.241x | 11.653x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 266.0 | 254.3 | 271.0 | 5.5 | 0.249x | 12.023x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 267.0 | 258.7 | 271.2 | 4.6 | 0.250x | 12.068x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,069.9 | 1,057.0 | 1,090.1 | 12.0 | 1.000x | 48.355x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.8 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.005x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.044x | 1.006x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.044x | 1.007x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.7 | 32.9 | 33.9 | 0.5 | 0.112x | 2.547x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.9 | 33.6 | 35.7 | 0.8 | 0.112x | 2.558x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.0 | 0.0 | 0.116x | 2.639x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.0 | 34.7 | 35.9 | 0.4 | 0.116x | 2.642x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 295.6 | 294.0 | 298.7 | 1.7 | 0.981x | 22.323x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 301.2 | 297.0 | 314.7 | 6.4 | 1.000x | 22.748x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 29.6 | 29.5 | 30.0 | 0.2 | 0.028x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 29.8 | 29.4 | 40.4 | 4.3 | 0.028x | 1.004x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 29.9 | 29.3 | 30.5 | 0.4 | 0.028x | 1.008x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 30.0 | 29.9 | 30.3 | 0.2 | 0.028x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 72.2 | 70.4 | 77.9 | 2.5 | 0.068x | 2.438x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 332.3 | 330.6 | 334.2 | 1.5 | 0.313x | 11.213x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 332.6 | 326.3 | 432.4 | 40.6 | 0.313x | 11.224x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 334.5 | 330.7 | 336.4 | 2.1 | 0.315x | 11.288x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 336.1 | 327.0 | 342.9 | 5.5 | 0.317x | 11.342x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,062.0 | 1,057.5 | 1,080.6 | 8.0 | 1.000x | 35.835x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.045x | 1.005x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 0.045x | 1.005x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 46.4 | 45.3 | 47.3 | 0.7 | 0.129x | 2.884x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 54.6 | 54.2 | 57.4 | 1.2 | 0.152x | 3.392x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 57.4 | 53.1 | 57.6 | 1.8 | 0.160x | 3.566x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 58.5 | 58.2 | 60.3 | 0.8 | 0.163x | 3.637x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 356.8 | 352.4 | 361.4 | 2.9 | 0.993x | 22.174x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 359.4 | 349.7 | 380.0 | 10.1 | 1.000x | 22.333x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.4 | 26.3 | 26.7 | 0.1 | 0.020x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.4 | 26.2 | 26.7 | 0.2 | 0.020x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.6 | 26.1 | 35.2 | 3.5 | 0.020x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.6 | 71.1 | 79.1 | 3.0 | 0.055x | 2.719x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 381.1 | 377.0 | 381.3 | 1.6 | 0.293x | 14.462x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 383.8 | 382.6 | 388.3 | 2.1 | 0.295x | 14.565x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 395.6 | 394.8 | 398.7 | 1.4 | 0.304x | 15.014x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 399.1 | 394.8 | 404.8 | 3.2 | 0.307x | 15.145x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,299.4 | 1,294.6 | 1,301.5 | 2.4 | 1.000x | 49.313x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.0 | 17.5 | 0.6 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 0.051x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 0.051x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.051x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.4 | 41.6 | 47.3 | 2.1 | 0.137x | 2.698x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 50.2 | 48.0 | 52.0 | 1.3 | 0.158x | 3.124x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 51.9 | 48.8 | 53.1 | 1.7 | 0.164x | 3.233x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.3 | 54.8 | 55.6 | 0.3 | 0.174x | 3.445x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 312.6 | 307.9 | 318.2 | 3.9 | 0.984x | 19.459x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 317.6 | 312.5 | 334.9 | 8.1 | 1.000x | 19.766x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.1 | 25.8 | 26.7 | 0.3 | 0.023x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.023x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 25.9 | 26.4 | 0.2 | 0.023x | 1.006x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.5 | 26.0 | 34.9 | 3.3 | 0.023x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.0 | 70.7 | 78.7 | 3.1 | 0.063x | 2.719x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 357.5 | 355.7 | 363.2 | 2.9 | 0.316x | 13.696x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 359.1 | 353.5 | 364.7 | 3.9 | 0.317x | 13.758x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 360.8 | 360.0 | 364.2 | 1.6 | 0.318x | 13.824x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 368.4 | 366.9 | 372.9 | 2.1 | 0.325x | 14.115x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,133.0 | 1,129.5 | 1,140.8 | 3.7 | 1.000x | 43.408x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.2 | 20.1 | 21.4 | 0.5 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.034x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.1 | 0.034x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.034x | 1.002x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.6 | 25.5 | 26.4 | 0.4 | 0.044x | 1.269x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 25.7 | 25.6 | 26.0 | 0.2 | 0.044x | 1.272x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 25.9 | 26.2 | 0.1 | 0.044x | 1.293x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.8 | 0.3 | 0.044x | 1.295x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 570.5 | 565.7 | 587.3 | 7.9 | 0.970x | 28.246x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 588.2 | 573.0 | 598.6 | 8.8 | 1.000x | 29.119x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.0 | 19.0 | 19.1 | 0.0 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.1 | 19.0 | 19.4 | 0.2 | 0.009x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.1 | 19.0 | 19.4 | 0.1 | 0.009x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 19.2 | 19.0 | 26.6 | 3.0 | 0.009x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.1 | 97.4 | 101.1 | 1.4 | 0.045x | 5.149x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 176.1 | 174.4 | 181.1 | 2.3 | 0.081x | 9.244x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 179.5 | 178.8 | 183.2 | 1.7 | 0.083x | 9.426x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 182.3 | 170.5 | 185.0 | 5.2 | 0.084x | 9.572x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 184.7 | 174.6 | 188.6 | 4.8 | 0.085x | 9.699x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,170.6 | 2,151.6 | 2,185.1 | 10.7 | 1.000x | 113.967x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.029x | 1.000x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.0 | 0.029x | 1.001x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 127.1 | 123.5 | 127.6 | 1.5 | 0.159x | 5.512x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 128.4 | 115.5 | 132.9 | 6.4 | 0.161x | 5.566x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 129.6 | 129.0 | 130.0 | 0.3 | 0.162x | 5.619x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 135.3 | 135.0 | 136.5 | 0.5 | 0.169x | 5.865x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 791.9 | 790.9 | 794.5 | 1.3 | 0.992x | 34.330x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 798.4 | 786.8 | 815.9 | 10.2 | 1.000x | 34.614x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 25.2 | 25.2 | 25.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 0.008x | 1.006x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 25.4 | 25.3 | 37.3 | 4.8 | 0.008x | 1.006x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 0.008x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 133.2 | 133.0 | 134.5 | 0.6 | 0.044x | 5.277x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 693.7 | 685.7 | 698.8 | 5.0 | 0.231x | 27.491x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 702.9 | 697.4 | 704.3 | 2.8 | 0.234x | 27.854x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 703.6 | 686.3 | 705.6 | 7.2 | 0.234x | 27.881x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 714.5 | 710.8 | 722.1 | 3.7 | 0.238x | 28.315x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,007.1 | 2,991.5 | 3,018.2 | 9.6 | 1.000x | 119.168x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.2 | 11.8 | 12.5 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.059x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.5 | 12.4 | 13.0 | 0.2 | 0.060x | 1.023x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.5 | 12.9 | 0.1 | 0.061x | 1.036x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.7 | 0.2 | 0.122x | 2.066x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.6 | 0.2 | 0.125x | 2.124x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.0 | 27.0 | 0.4 | 0.125x | 2.128x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.3 | 25.1 | 27.4 | 0.9 | 0.126x | 2.143x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 205.7 | 204.6 | 216.4 | 4.4 | 0.990x | 16.797x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 207.7 | 206.1 | 221.5 | 6.0 | 1.000x | 16.961x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.0 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.9 | 26.7 | 32.9 | 2.4 | 0.037x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.0 | 0.037x | 1.003x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 27.0 | 26.8 | 27.2 | 0.1 | 0.037x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 69.2 | 65.7 | 72.5 | 2.7 | 0.094x | 2.581x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 239.7 | 239.4 | 247.0 | 3.1 | 0.327x | 8.940x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 240.9 | 238.9 | 241.2 | 1.1 | 0.328x | 8.985x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 242.2 | 238.3 | 246.8 | 3.3 | 0.330x | 9.032x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 248.2 | 243.6 | 250.7 | 2.3 | 0.338x | 9.256x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 733.5 | 721.7 | 738.0 | 6.6 | 1.000x | 27.357x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.7 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.042x | 1.006x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 0.042x | 1.010x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.8 | 14.5 | 14.8 | 0.1 | 0.043x | 1.016x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 40.4 | 39.4 | 41.2 | 0.6 | 0.117x | 2.780x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 40.7 | 40.2 | 41.2 | 0.4 | 0.118x | 2.800x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.4 | 40.9 | 42.7 | 0.7 | 0.120x | 2.850x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.9 | 39.7 | 42.5 | 1.0 | 0.121x | 2.883x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 337.5 | 336.0 | 339.8 | 1.4 | 0.975x | 23.233x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 346.1 | 334.1 | 360.6 | 9.4 | 1.000x | 23.825x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.9 | 20.7 | 29.7 | 3.5 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 21.0 | 20.9 | 21.2 | 0.1 | 0.017x | 1.004x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 21.1 | 20.9 | 21.4 | 0.2 | 0.017x | 1.008x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 21.1 | 21.0 | 21.4 | 0.1 | 0.017x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 67.8 | 66.2 | 76.2 | 3.5 | 0.056x | 3.238x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 294.2 | 290.4 | 298.7 | 2.7 | 0.242x | 14.057x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 303.0 | 302.3 | 305.3 | 1.2 | 0.249x | 14.476x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 307.0 | 302.3 | 310.6 | 2.7 | 0.253x | 14.669x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 310.4 | 306.0 | 313.7 | 2.7 | 0.255x | 14.829x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,215.0 | 1,204.7 | 1,222.0 | 6.7 | 1.000x | 58.053x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.047x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.047x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.1 | 0.047x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.7 | 0.3 | 0.047x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 71.7 | 71.4 | 71.8 | 0.1 | 0.145x | 3.114x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 72.0 | 71.6 | 72.5 | 0.3 | 0.146x | 3.127x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 74.1 | 74.0 | 74.7 | 0.3 | 0.150x | 3.218x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 74.3 | 74.1 | 82.8 | 3.3 | 0.150x | 3.228x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 485.4 | 484.5 | 502.3 | 6.8 | 0.983x | 21.095x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 494.0 | 486.1 | 495.4 | 3.6 | 1.000x | 21.468x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.8 | 26.6 | 38.5 | 4.7 | 0.015x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.7 | 27.0 | 0.1 | 0.015x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.1 | 0.015x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.9 | 26.7 | 27.5 | 0.3 | 0.015x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 95.7 | 90.3 | 98.6 | 2.9 | 0.053x | 3.570x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 577.9 | 574.0 | 586.2 | 4.6 | 0.319x | 21.547x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 598.2 | 594.8 | 607.9 | 4.7 | 0.330x | 22.303x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 600.5 | 592.7 | 610.5 | 6.4 | 0.331x | 22.388x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 611.8 | 584.3 | 613.4 | 10.9 | 0.337x | 22.811x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,813.6 | 1,799.7 | 1,818.1 | 6.8 | 1.000x | 67.622x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.5 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.3 | 0.1 | 0.054x | 1.006x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.2 | 0.1 | 0.058x | 1.076x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 0.058x | 1.077x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 26.1 | 27.8 | 0.7 | 0.128x | 2.365x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.4 | 26.2 | 27.2 | 0.4 | 0.129x | 2.389x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.4 | 26.1 | 27.9 | 0.6 | 0.130x | 2.392x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 27.2 | 26.3 | 28.8 | 1.0 | 0.133x | 2.462x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 204.2 | 198.6 | 211.9 | 4.5 | 1.000x | 18.470x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 205.0 | 202.1 | 207.7 | 1.8 | 1.004x | 18.548x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.9 | 58.9 | 64.1 | 2.1 | 0.063x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 59.0 | 58.9 | 76.7 | 7.1 | 0.063x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.063x | 1.001x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 59.2 | 59.0 | 59.4 | 0.1 | 0.063x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 99.7 | 98.9 | 100.6 | 0.6 | 0.106x | 1.692x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 100.7 | 99.1 | 102.7 | 1.2 | 0.107x | 1.708x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 102.2 | 101.3 | 116.4 | 5.7 | 0.109x | 1.735x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 107.4 | 105.7 | 112.6 | 2.5 | 0.115x | 1.823x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 113.1 | 112.4 | 114.0 | 0.5 | 0.121x | 1.919x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 937.3 | 927.6 | 939.4 | 4.5 | 1.000x | 15.902x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.2 | 0.1 | 0.660x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.5 | 23.2 | 23.8 | 0.2 | 0.673x | 1.020x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.4 | 0.1 | 0.725x | 1.098x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.4 | 0.1 | 0.727x | 1.102x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.0 | 0.746x | 1.132x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.748x | 1.133x |
| 7 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.1 | 27.8 | 0.7 | 0.749x | 1.136x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.750x | 1.138x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 34.1 | 33.6 | 35.0 | 0.5 | 0.977x | 1.482x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 34.9 | 34.2 | 38.8 | 2.0 | 1.000x | 1.516x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 23.6 | 23.6 | 30.4 | 2.7 | 0.651x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 23.8 | 23.7 | 24.2 | 0.2 | 0.655x | 1.006x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 23.8 | 23.8 | 33.1 | 3.7 | 0.657x | 1.009x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 23.9 | 23.8 | 25.0 | 0.5 | 0.659x | 1.013x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 36.3 | 35.0 | 39.0 | 1.4 | 1.000x | 1.537x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 36.5 | 36.2 | 47.6 | 4.5 | 1.005x | 1.544x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 194.8 | 194.4 | 198.5 | 1.8 | 5.362x | 8.240x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 197.2 | 194.8 | 199.7 | 1.8 | 5.430x | 8.344x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 198.0 | 196.4 | 200.4 | 1.4 | 5.450x | 8.375x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 199.8 | 198.1 | 200.8 | 0.9 | 5.499x | 8.451x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.1 | 0.333x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.4 | 9.8 | 10.7 | 0.3 | 0.344x | 1.032x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 0.346x | 1.038x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.2 | 0.3 | 0.350x | 1.050x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 15.1 | 15.0 | 15.6 | 0.2 | 0.500x | 1.499x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 15.4 | 15.1 | 16.2 | 0.4 | 0.512x | 1.537x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.5 | 0.1 | 0.542x | 1.627x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.4 | 0.0 | 0.543x | 1.629x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 29.3 | 28.9 | 29.6 | 0.3 | 0.972x | 2.915x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.1 | 28.9 | 30.4 | 0.5 | 1.000x | 2.999x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 18.5 | 18.3 | 18.9 | 0.2 | 0.499x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 18.7 | 18.4 | 25.4 | 2.7 | 0.504x | 1.009x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 18.9 | 18.5 | 18.9 | 0.2 | 0.508x | 1.019x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.0 | 18.5 | 19.3 | 0.3 | 0.511x | 1.023x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 37.2 | 36.3 | 40.7 | 1.6 | 1.000x | 2.003x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 37.4 | 37.1 | 47.8 | 4.2 | 1.007x | 2.017x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 142.8 | 142.6 | 147.4 | 1.9 | 3.842x | 7.697x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 143.0 | 142.2 | 143.3 | 0.4 | 3.847x | 7.708x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 143.9 | 142.7 | 144.4 | 0.7 | 3.871x | 7.755x |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 149.1 | 147.0 | 150.1 | 1.2 | 4.012x | 8.039x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.5 | 13.4 | 14.5 | 0.5 | 0.064x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.6 | 13.6 | 13.8 | 0.1 | 0.065x | 1.011x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.8 | 0.1 | 0.065x | 1.016x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.8 | 13.3 | 14.3 | 0.4 | 0.066x | 1.026x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.1 | 0.1 | 0.081x | 1.265x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 17.5 | 16.9 | 17.7 | 0.3 | 0.083x | 1.296x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.7 | 18.7 | 18.9 | 0.1 | 0.089x | 1.388x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.9 | 0.1 | 0.090x | 1.393x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 208.5 | 205.9 | 217.9 | 4.2 | 0.994x | 15.467x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 209.7 | 208.1 | 212.7 | 1.7 | 1.000x | 15.555x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 11.6 | 11.4 | 13.0 | 0.7 | 0.053x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 12.0 | 11.9 | 12.6 | 0.2 | 0.055x | 1.034x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 12.1 | 11.9 | 13.1 | 0.5 | 0.056x | 1.042x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 12.3 | 11.4 | 12.9 | 0.5 | 0.056x | 1.055x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 53.2 | 51.3 | 58.2 | 2.4 | 0.245x | 4.573x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 61.5 | 61.1 | 63.0 | 0.6 | 0.283x | 5.293x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 62.4 | 62.1 | 62.9 | 0.3 | 0.287x | 5.369x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 67.7 | 67.0 | 68.1 | 0.4 | 0.312x | 5.827x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 67.8 | 67.2 | 68.8 | 0.6 | 0.312x | 5.831x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 217.4 | 214.8 | 218.1 | 1.1 | 1.000x | 18.695x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.5 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.081x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.8 | 12.6 | 13.0 | 0.1 | 0.084x | 1.041x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.8 | 12.5 | 12.9 | 0.1 | 0.084x | 1.046x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.6 | 23.3 | 25.3 | 0.8 | 0.155x | 1.922x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.6 | 23.4 | 23.9 | 0.2 | 0.155x | 1.923x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.6 | 23.3 | 24.7 | 0.5 | 0.155x | 1.924x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.8 | 23.6 | 25.5 | 0.7 | 0.156x | 1.937x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 152.4 | 150.8 | 158.2 | 2.6 | 1.000x | 12.412x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 153.6 | 148.5 | 155.1 | 2.3 | 1.008x | 12.512x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 71.1 | 71.0 | 71.2 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 71.2 | 70.9 | 71.5 | 0.2 | 0.067x | 1.001x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 71.2 | 71.1 | 82.3 | 4.5 | 0.067x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 71.3 | 71.2 | 71.5 | 0.1 | 0.067x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 100.4 | 98.9 | 107.0 | 3.1 | 0.094x | 1.411x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 147.8 | 147.0 | 149.0 | 0.8 | 0.138x | 2.079x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 148.1 | 147.6 | 149.9 | 0.8 | 0.138x | 2.083x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 149.3 | 148.4 | 153.5 | 1.9 | 0.139x | 2.099x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 160.5 | 160.0 | 162.3 | 0.8 | 0.150x | 2.258x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,070.4 | 1,060.9 | 1,071.8 | 4.1 | 1.000x | 15.054x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.5 | 0.3 | 0.329x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.1 | 0.1 | 0.333x | 1.011x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.2 | 0.3 | 0.344x | 1.046x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.6 | 10.3 | 10.7 | 0.1 | 0.351x | 1.067x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 15.0 | 14.9 | 15.9 | 0.4 | 0.499x | 1.516x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 15.5 | 15.3 | 16.2 | 0.3 | 0.515x | 1.565x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.542x | 1.647x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.5 | 0.1 | 0.543x | 1.649x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 29.5 | 29.2 | 29.5 | 0.1 | 0.978x | 2.970x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.1 | 29.2 | 30.8 | 0.5 | 1.000x | 3.037x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 61.9 | 61.7 | 61.9 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 61.9 | 61.7 | 62.2 | 0.2 | 0.115x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 61.9 | 61.8 | 62.3 | 0.2 | 0.115x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.0 | 61.8 | 74.1 | 4.8 | 0.115x | 1.002x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 71.4 | 70.0 | 87.0 | 6.3 | 0.133x | 1.154x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 71.5 | 68.3 | 72.8 | 1.6 | 0.133x | 1.156x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 72.2 | 71.0 | 73.8 | 1.0 | 0.134x | 1.167x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 77.7 | 77.2 | 87.3 | 3.8 | 0.144x | 1.257x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 87.8 | 87.0 | 100.0 | 5.0 | 0.163x | 1.419x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 538.8 | 538.2 | 546.0 | 3.5 | 1.000x | 8.710x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.6 | 0.2 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.081x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.5 | 13.1 | 0.2 | 0.083x | 1.029x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.084x | 1.035x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.6 | 23.5 | 23.6 | 0.0 | 0.155x | 1.917x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.6 | 23.6 | 23.8 | 0.1 | 0.156x | 1.922x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.9 | 23.8 | 26.6 | 1.1 | 0.157x | 1.942x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 24.0 | 23.3 | 24.7 | 0.5 | 0.158x | 1.951x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 151.6 | 150.0 | 157.9 | 2.9 | 1.000x | 12.334x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 152.5 | 147.8 | 155.3 | 2.4 | 1.006x | 12.407x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 25.7 | 25.6 | 25.8 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 25.8 | 25.2 | 31.5 | 2.3 | 0.052x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 25.8 | 25.6 | 26.1 | 0.2 | 0.052x | 1.004x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 25.9 | 25.7 | 26.0 | 0.1 | 0.052x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 68.1 | 65.5 | 73.0 | 2.5 | 0.137x | 2.648x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 223.7 | 222.8 | 232.0 | 3.5 | 0.448x | 8.695x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 225.0 | 224.7 | 232.7 | 3.1 | 0.451x | 8.747x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 225.5 | 223.5 | 227.2 | 1.4 | 0.452x | 8.765x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 227.7 | 224.9 | 255.7 | 11.6 | 0.456x | 8.851x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 499.0 | 497.7 | 510.5 | 4.8 | 1.000x | 19.395x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.8 | 21.7 | 22.0 | 0.1 | 0.046x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.8 | 21.6 | 24.2 | 1.0 | 0.046x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 0.046x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 50.5 | 49.8 | 54.7 | 1.8 | 0.107x | 2.322x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 50.9 | 50.5 | 52.4 | 0.7 | 0.107x | 2.339x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 52.1 | 52.0 | 54.9 | 1.1 | 0.110x | 2.394x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 52.6 | 51.9 | 53.5 | 0.5 | 0.111x | 2.417x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 467.4 | 464.4 | 472.3 | 2.8 | 0.987x | 21.475x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 473.7 | 468.1 | 486.2 | 7.6 | 1.000x | 21.764x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 19.0 | 18.8 | 26.6 | 3.0 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.0 | 18.9 | 19.3 | 0.1 | 0.011x | 1.002x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.1 | 18.8 | 19.8 | 0.4 | 0.011x | 1.008x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.5 | 19.0 | 20.0 | 0.4 | 0.011x | 1.025x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 85.5 | 85.0 | 93.1 | 3.1 | 0.049x | 4.505x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 348.2 | 346.6 | 350.1 | 1.4 | 0.199x | 18.344x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 350.0 | 347.4 | 350.5 | 1.1 | 0.200x | 18.438x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 351.5 | 349.4 | 352.4 | 1.2 | 0.201x | 18.518x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 360.9 | 356.5 | 366.6 | 3.3 | 0.207x | 19.011x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,745.8 | 1,737.9 | 1,758.3 | 7.0 | 1.000x | 91.968x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.029x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 0.029x | 1.005x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.7 | 25.5 | 26.6 | 0.4 | 0.032x | 1.115x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.033x | 1.135x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.3 | 26.1 | 28.1 | 0.8 | 0.033x | 1.140x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.7 | 26.1 | 27.1 | 0.4 | 0.034x | 1.157x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 785.7 | 780.8 | 800.2 | 7.6 | 0.989x | 34.052x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 794.5 | 783.2 | 807.3 | 9.0 | 1.000x | 34.435x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 20.4 | 20.3 | 20.8 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.4 | 20.2 | 28.6 | 3.3 | 0.007x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 20.7 | 20.5 | 20.7 | 0.1 | 0.007x | 1.014x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 20.7 | 20.6 | 21.2 | 0.2 | 0.007x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 118.3 | 116.7 | 119.8 | 1.0 | 0.039x | 5.807x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 186.3 | 185.5 | 192.1 | 2.9 | 0.061x | 9.142x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 187.2 | 184.1 | 192.1 | 3.0 | 0.062x | 9.189x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 188.5 | 185.6 | 189.2 | 1.6 | 0.062x | 9.253x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 190.9 | 187.6 | 193.4 | 2.2 | 0.063x | 9.367x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,034.5 | 3,008.6 | 3,060.5 | 19.5 | 1.000x | 148.928x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.044x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.5 | 0.1 | 0.044x | 1.003x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.3 | 0.4 | 0.045x | 1.020x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.3 | 0.1 | 0.056x | 1.290x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 17.3 | 17.0 | 17.8 | 0.3 | 0.057x | 1.311x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.7 | 18.7 | 18.8 | 0.0 | 0.062x | 1.423x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.8 | 0.1 | 0.062x | 1.425x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 297.5 | 290.4 | 299.5 | 3.1 | 0.987x | 22.584x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 301.4 | 293.1 | 317.7 | 8.7 | 1.000x | 22.879x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 12.1 | 12.0 | 12.3 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 12.7 | 12.5 | 13.3 | 0.3 | 0.016x | 1.049x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 12.8 | 12.4 | 18.4 | 2.3 | 0.016x | 1.057x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 12.8 | 12.4 | 13.0 | 0.2 | 0.016x | 1.061x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 61.6 | 60.0 | 68.7 | 3.1 | 0.077x | 5.103x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 88.5 | 86.2 | 92.0 | 2.1 | 0.110x | 7.331x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 88.6 | 86.0 | 92.4 | 2.1 | 0.110x | 7.343x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 90.6 | 88.5 | 92.7 | 1.5 | 0.113x | 7.503x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 93.6 | 92.6 | 95.0 | 0.9 | 0.116x | 7.752x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 803.6 | 801.4 | 812.2 | 3.7 | 1.000x | 66.584x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.4 | 12.4 | 0.4 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.6 | 0.0 | 0.080x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.4 | 0.1 | 0.085x | 1.055x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.086x | 1.067x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.0 | 21.0 | 21.5 | 0.2 | 0.146x | 1.818x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.4 | 21.3 | 22.4 | 0.4 | 0.149x | 1.857x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.0 | 0.155x | 1.935x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.0 | 0.155x | 1.935x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 143.8 | 142.0 | 145.1 | 1.3 | 1.000x | 12.472x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 143.8 | 142.6 | 148.1 | 2.0 | 1.000x | 12.473x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 68.6 | 68.5 | 68.8 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 68.7 | 68.4 | 69.2 | 0.3 | 0.067x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.8 | 68.5 | 69.0 | 0.2 | 0.067x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 68.9 | 68.3 | 80.5 | 4.7 | 0.067x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.6 | 97.2 | 105.6 | 3.1 | 0.096x | 1.438x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 127.7 | 127.4 | 128.8 | 0.5 | 0.124x | 1.862x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 127.8 | 126.7 | 128.9 | 0.7 | 0.124x | 1.863x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 128.9 | 128.7 | 134.9 | 2.4 | 0.125x | 1.880x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 140.2 | 139.4 | 185.1 | 17.9 | 0.136x | 2.044x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,031.5 | 1,019.9 | 1,039.8 | 7.3 | 1.000x | 15.042x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.6 | 0.0 | 0.048x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 0.048x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 14.7 | 14.7 | 14.7 | 0.0 | 0.048x | 1.005x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.1 | 0.049x | 1.009x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 41.4 | 41.2 | 42.1 | 0.3 | 0.137x | 2.839x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 41.7 | 41.1 | 43.8 | 1.0 | 0.138x | 2.860x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.2 | 40.4 | 44.5 | 1.3 | 0.139x | 2.888x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 42.8 | 41.6 | 43.4 | 0.6 | 0.141x | 2.935x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 300.0 | 298.6 | 301.4 | 1.1 | 0.990x | 20.552x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 303.1 | 296.8 | 309.7 | 4.4 | 1.000x | 20.767x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 53.7 | 53.4 | 53.8 | 0.2 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 53.8 | 53.7 | 67.5 | 5.4 | 0.033x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 53.9 | 53.7 | 54.2 | 0.2 | 0.033x | 1.004x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 53.9 | 53.7 | 54.5 | 0.3 | 0.033x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 103.9 | 102.5 | 112.1 | 3.5 | 0.064x | 1.936x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 297.8 | 290.7 | 302.6 | 4.4 | 0.182x | 5.549x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 299.2 | 297.8 | 302.5 | 1.9 | 0.183x | 5.575x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 299.8 | 298.7 | 305.0 | 2.2 | 0.184x | 5.586x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 302.6 | 300.4 | 316.5 | 6.0 | 0.185x | 5.640x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,632.5 | 1,617.5 | 1,637.8 | 7.4 | 1.000x | 30.423x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.5 | 0.0 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.9 | 0.1 | 0.080x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.4 | 0.1 | 0.084x | 1.056x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.085x | 1.071x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.6 | 21.4 | 22.3 | 0.3 | 0.150x | 1.882x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.7 | 21.0 | 22.3 | 0.4 | 0.150x | 1.887x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 22.3 | 22.2 | 22.4 | 0.1 | 0.154x | 1.937x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 22.3 | 22.2 | 22.5 | 0.1 | 0.155x | 1.942x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 142.2 | 138.7 | 145.1 | 2.1 | 0.984x | 12.367x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 144.6 | 143.7 | 148.0 | 1.5 | 1.000x | 12.573x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 68.6 | 68.6 | 68.8 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 68.6 | 68.5 | 68.9 | 0.1 | 0.068x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 68.7 | 68.4 | 68.8 | 0.1 | 0.068x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 68.8 | 68.6 | 80.5 | 4.7 | 0.068x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 98.8 | 97.1 | 106.7 | 3.4 | 0.097x | 1.439x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 127.6 | 126.9 | 128.1 | 0.5 | 0.126x | 1.860x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 128.2 | 127.8 | 128.6 | 0.3 | 0.126x | 1.868x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 129.1 | 127.7 | 136.4 | 3.2 | 0.127x | 1.881x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 139.4 | 138.8 | 139.9 | 0.4 | 0.137x | 2.032x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,014.0 | 1,006.3 | 1,023.0 | 6.1 | 1.000x | 14.776x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.7 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.8 | 0.2 | 0.045x | 1.003x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.7 | 0.2 | 0.045x | 1.008x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.5 | 13.3 | 14.7 | 0.5 | 0.045x | 1.013x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.5 | 25.4 | 26.4 | 0.4 | 0.086x | 1.912x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.962x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.088x | 1.966x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.9 | 0.4 | 0.088x | 1.968x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 295.8 | 294.2 | 302.0 | 2.9 | 0.996x | 22.207x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 297.2 | 293.1 | 316.4 | 8.3 | 1.000x | 22.307x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 19.6 | 19.5 | 19.9 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 19.7 | 19.7 | 27.7 | 3.2 | 0.018x | 1.004x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 19.7 | 19.7 | 20.1 | 0.1 | 0.018x | 1.007x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 19.8 | 19.5 | 19.9 | 0.1 | 0.018x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 68.8 | 68.2 | 81.1 | 5.0 | 0.064x | 3.507x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 176.3 | 175.4 | 178.9 | 1.2 | 0.165x | 8.993x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 179.7 | 177.9 | 187.6 | 3.5 | 0.168x | 9.167x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 180.9 | 180.5 | 184.9 | 1.7 | 0.169x | 9.224x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 184.6 | 181.0 | 187.3 | 2.1 | 0.172x | 9.415x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,071.8 | 1,066.7 | 1,085.4 | 6.5 | 1.000x | 54.663x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.045x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.045x | 1.007x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.6 | 0.1 | 0.086x | 1.911x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.3 | 0.1 | 0.088x | 1.957x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.088x | 1.962x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.8 | 0.4 | 0.088x | 1.963x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 295.9 | 294.2 | 316.3 | 8.3 | 1.000x | 22.198x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 296.0 | 292.8 | 300.2 | 2.8 | 1.000x | 22.205x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.2 | 14.1 | 20.1 | 2.3 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.5 | 14.2 | 22.2 | 3.1 | 0.014x | 1.018x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.6 | 14.5 | 14.9 | 0.1 | 0.014x | 1.023x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.6 | 14.5 | 15.3 | 0.3 | 0.014x | 1.024x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 67.5 | 67.2 | 74.9 | 2.9 | 0.063x | 4.743x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 167.2 | 164.4 | 171.3 | 2.3 | 0.157x | 11.753x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 167.4 | 165.0 | 171.1 | 2.1 | 0.157x | 11.765x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 167.5 | 165.8 | 171.3 | 2.1 | 0.157x | 11.773x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 168.0 | 166.6 | 182.8 | 6.1 | 0.157x | 11.807x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,067.9 | 1,056.4 | 1,080.2 | 7.8 | 1.000x | 75.043x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 0.045x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.4 | 13.5 | 0.1 | 0.045x | 1.005x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.7 | 0.1 | 0.086x | 1.910x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 25.9 | 26.2 | 0.1 | 0.088x | 1.957x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 25.7 | 26.9 | 0.4 | 0.088x | 1.957x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.4 | 26.1 | 28.7 | 1.0 | 0.089x | 1.978x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 295.5 | 291.6 | 302.0 | 3.5 | 0.994x | 22.142x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 297.3 | 294.9 | 315.0 | 7.5 | 1.000x | 22.270x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.2 | 14.0 | 16.8 | 1.1 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.3 | 14.0 | 21.4 | 2.9 | 0.013x | 1.013x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.4 | 14.3 | 14.5 | 0.1 | 0.014x | 1.020x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.5 | 14.2 | 14.6 | 0.1 | 0.014x | 1.027x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 67.3 | 67.1 | 75.4 | 3.3 | 0.063x | 4.758x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 166.8 | 163.9 | 167.9 | 1.5 | 0.156x | 11.785x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 167.3 | 163.5 | 169.0 | 2.0 | 0.157x | 11.822x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 168.2 | 165.8 | 169.5 | 1.3 | 0.157x | 11.884x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 169.3 | 164.5 | 170.0 | 2.1 | 0.158x | 11.962x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,068.4 | 1,057.2 | 1,078.9 | 7.5 | 1.000x | 75.495x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.5 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 0.045x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.5 | 13.2 | 13.5 | 0.1 | 0.045x | 1.008x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.7 | 0.1 | 0.086x | 1.908x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.952x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.9 | 0.4 | 0.088x | 1.963x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.3 | 26.1 | 27.1 | 0.3 | 0.089x | 1.971x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 294.6 | 292.6 | 297.2 | 1.8 | 0.993x | 22.071x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 296.6 | 295.2 | 315.8 | 7.8 | 1.000x | 22.222x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 14.1 | 14.0 | 21.3 | 2.9 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 14.2 | 14.1 | 18.0 | 1.5 | 0.013x | 1.004x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 14.3 | 14.2 | 14.5 | 0.1 | 0.013x | 1.014x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 14.4 | 14.3 | 14.7 | 0.1 | 0.013x | 1.019x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 67.5 | 66.9 | 77.0 | 3.9 | 0.063x | 4.785x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 166.7 | 166.0 | 170.8 | 1.7 | 0.156x | 11.815x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 166.7 | 163.1 | 168.0 | 1.7 | 0.156x | 11.817x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 167.4 | 166.0 | 170.5 | 1.5 | 0.157x | 11.869x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 169.9 | 166.4 | 171.1 | 1.8 | 0.159x | 12.042x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,067.9 | 1,048.7 | 1,075.0 | 10.3 | 1.000x | 75.702x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.045x | 1.005x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 0.045x | 1.008x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 0.045x | 1.008x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.4 | 25.4 | 25.7 | 0.1 | 0.085x | 1.919x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.972x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.8 | 0.4 | 0.088x | 1.979x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.3 | 26.0 | 26.4 | 0.1 | 0.088x | 1.981x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 294.3 | 293.6 | 302.6 | 3.4 | 0.985x | 22.194x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 298.7 | 294.7 | 310.8 | 5.8 | 1.000x | 22.530x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 16.3 | 16.2 | 16.4 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 16.3 | 16.2 | 24.8 | 3.4 | 0.015x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 16.4 | 16.1 | 16.9 | 0.2 | 0.015x | 1.006x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 16.7 | 16.4 | 16.9 | 0.2 | 0.016x | 1.023x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 67.4 | 67.2 | 77.1 | 3.8 | 0.063x | 4.139x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 158.5 | 156.6 | 159.9 | 1.1 | 0.149x | 9.732x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 159.9 | 159.0 | 162.8 | 1.5 | 0.150x | 9.814x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 160.1 | 157.3 | 162.1 | 1.6 | 0.150x | 9.828x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 161.7 | 157.9 | 162.1 | 1.5 | 0.152x | 9.928x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,064.0 | 1,056.1 | 1,075.7 | 6.7 | 1.000x | 65.320x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,668.3 | 7,662.7 | 7,670.7 | 2.9 | 0.778x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,668.9 | 7,665.5 | 7,673.1 | 2.7 | 0.778x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,685.9 | 7,683.7 | 7,703.4 | 7.5 | 0.780x | 1.002x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,697.9 | 7,678.5 | 7,711.6 | 13.9 | 0.781x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 9,807.6 | 9,803.5 | 9,928.5 | 48.1 | 0.995x | 1.279x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 9,855.2 | 9,806.5 | 12,656.5 | 1,195.4 | 1.000x | 1.285x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,068.7 | 19,066.2 | 19,079.4 | 4.8 | 1.935x | 2.487x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,073.6 | 19,067.2 | 19,077.9 | 3.5 | 1.935x | 2.487x |
| 9 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,092.5 | 19,090.6 | 19,107.2 | 6.1 | 1.937x | 2.490x |
| 10 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,105.8 | 19,087.6 | 19,152.9 | 23.1 | 1.939x | 2.492x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 5,888.7 | 5,860.8 | 5,899.5 | 13.0 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 5,917.4 | 5,896.0 | 5,953.2 | 19.3 | 0.081x | 1.005x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6,269.8 | 6,209.5 | 6,282.4 | 26.0 | 0.086x | 1.065x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 6,291.7 | 6,228.6 | 6,309.8 | 28.2 | 0.087x | 1.068x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,460.4 | 7,458.6 | 7,505.9 | 18.6 | 0.103x | 1.267x |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,465.1 | 7,460.3 | 7,468.6 | 3.2 | 0.103x | 1.268x |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,470.8 | 7,465.7 | 7,474.2 | 3.5 | 0.103x | 1.269x |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,472.3 | 7,470.6 | 7,479.3 | 3.1 | 0.103x | 1.269x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 72,378.4 | 72,269.0 | 74,027.3 | 754.0 | 0.996x | 12.291x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 72,689.9 | 72,672.9 | 73,928.7 | 484.2 | 1.000x | 12.344x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9,548.6 | 9,546.6 | 9,554.0 | 2.5 | 0.060x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 9,548.8 | 9,546.9 | 9,559.4 | 4.6 | 0.060x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9,559.1 | 9,552.7 | 9,593.2 | 14.6 | 0.060x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9,564.1 | 9,554.2 | 9,650.2 | 35.7 | 0.060x | 1.002x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13,701.6 | 13,698.1 | 13,730.8 | 12.2 | 0.086x | 1.435x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13,706.2 | 13,693.4 | 13,720.6 | 8.9 | 0.086x | 1.435x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13,728.3 | 13,720.0 | 13,755.6 | 14.4 | 0.086x | 1.438x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13,729.4 | 13,711.3 | 14,365.3 | 254.4 | 0.086x | 1.438x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 158,736.5 | 158,161.5 | 159,418.1 | 434.7 | 1.000x | 16.624x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 159,127.1 | 157,791.5 | 162,247.5 | 1,654.8 | 1.002x | 16.665x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,633.0 | 7,631.9 | 7,639.4 | 3.1 | 0.810x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,637.4 | 7,632.5 | 7,659.4 | 10.0 | 0.811x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,657.4 | 7,653.2 | 7,675.6 | 8.2 | 0.813x | 1.003x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,661.4 | 7,645.7 | 7,675.7 | 10.4 | 0.813x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 9,415.1 | 9,403.1 | 9,437.9 | 11.6 | 1.000x | 1.233x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 9,419.3 | 9,412.3 | 9,426.6 | 4.7 | 1.000x | 1.234x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,044.4 | 19,039.5 | 19,053.2 | 5.3 | 2.022x | 2.495x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19,051.1 | 19,044.7 | 19,054.8 | 4.0 | 2.023x | 2.496x |
| 9 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,072.0 | 19,066.0 | 19,145.5 | 29.7 | 2.025x | 2.499x |
| 10 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19,073.6 | 19,064.1 | 19,094.2 | 10.8 | 2.025x | 2.499x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 3,736.2 | 3,734.1 | 3,739.7 | 1.8 | 0.084x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 3,736.4 | 3,733.8 | 3,741.9 | 2.7 | 0.084x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 3,742.0 | 3,739.6 | 3,797.5 | 22.3 | 0.084x | 1.002x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 3,742.5 | 3,739.6 | 3,746.0 | 2.4 | 0.084x | 1.002x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6,132.8 | 6,130.4 | 6,134.4 | 1.5 | 0.138x | 1.641x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 6,147.5 | 6,143.5 | 6,215.0 | 27.7 | 0.138x | 1.645x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 6,561.0 | 6,548.9 | 6,574.1 | 8.8 | 0.147x | 1.756x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6,590.8 | 6,537.0 | 6,909.6 | 136.0 | 0.148x | 1.764x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 44,486.7 | 44,477.2 | 45,695.2 | 497.0 | 1.000x | 11.907x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 44,565.1 | 44,446.3 | 44,670.6 | 90.2 | 1.002x | 11.928x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.0 | 17.6 | 0.6 | 0.049x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.050x | 1.006x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.6 | 0.2 | 0.050x | 1.008x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.3 | 0.0 | 0.050x | 1.011x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 43.8 | 43.0 | 45.5 | 0.8 | 0.135x | 2.729x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 49.9 | 48.8 | 53.2 | 1.6 | 0.154x | 3.109x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 53.4 | 48.5 | 54.1 | 2.1 | 0.164x | 3.325x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 54.9 | 54.6 | 57.1 | 0.9 | 0.169x | 3.422x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 321.3 | 320.1 | 328.3 | 2.9 | 0.989x | 20.011x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 325.0 | 317.0 | 333.0 | 5.1 | 1.000x | 20.238x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 4,786.9 | 4,785.7 | 4,788.4 | 1.1 | 0.043x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 4,787.6 | 4,787.1 | 4,790.1 | 1.1 | 0.043x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 4,792.7 | 4,790.0 | 4,810.0 | 7.3 | 0.043x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 4,793.1 | 4,792.0 | 4,852.8 | 23.8 | 0.043x | 1.001x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6,847.9 | 6,844.0 | 6,852.5 | 3.2 | 0.062x | 1.431x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 6,847.9 | 6,846.3 | 6,856.6 | 4.7 | 0.062x | 1.431x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 6,866.0 | 6,861.1 | 6,876.9 | 5.6 | 0.062x | 1.434x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 6,870.6 | 6,858.9 | 7,162.9 | 117.0 | 0.062x | 1.435x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 109,919.6 | 108,684.5 | 110,183.5 | 547.2 | 0.997x | 22.963x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 110,242.2 | 109,781.6 | 110,939.9 | 446.6 | 1.000x | 23.030x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,643.7 | 7,642.9 | 7,646.9 | 1.5 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 7,648.6 | 7,645.3 | 7,656.5 | 3.8 | 0.080x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,654.1 | 7,651.0 | 7,659.8 | 3.0 | 0.080x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 7,654.7 | 7,652.1 | 7,659.3 | 2.5 | 0.080x | 1.001x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10,575.4 | 10,571.2 | 10,615.4 | 16.8 | 0.111x | 1.384x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10,582.4 | 10,573.2 | 10,663.4 | 39.3 | 0.111x | 1.384x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10,595.0 | 10,583.7 | 10,924.6 | 133.3 | 0.111x | 1.386x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10,660.1 | 10,596.2 | 10,682.8 | 36.6 | 0.112x | 1.395x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 94,708.6 | 94,592.0 | 95,802.6 | 542.7 | 0.994x | 12.390x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 95,310.1 | 94,721.9 | 95,982.9 | 470.3 | 1.000x | 12.469x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.333x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.1 | 0.340x | 1.022x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.9 | 0.2 | 0.357x | 1.075x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.2 | 0.3 | 0.359x | 1.080x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 15.4 | 15.4 | 15.9 | 0.2 | 0.526x | 1.580x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 15.5 | 15.1 | 16.1 | 0.4 | 0.528x | 1.588x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.557x | 1.675x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.2 | 0.7 | 0.558x | 1.678x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 29.0 | 29.0 | 29.8 | 0.4 | 0.991x | 2.978x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 29.3 | 29.1 | 29.7 | 0.2 | 1.000x | 3.006x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 21.3 | 21.2 | 21.4 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 21.3 | 21.3 | 21.5 | 0.1 | 0.038x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 21.4 | 21.2 | 26.5 | 2.1 | 0.038x | 1.004x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 21.4 | 21.2 | 21.8 | 0.2 | 0.038x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 62.0 | 61.4 | 71.4 | 3.8 | 0.110x | 2.915x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 227.3 | 224.8 | 229.1 | 1.6 | 0.404x | 10.683x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 228.8 | 224.8 | 231.0 | 2.1 | 0.407x | 10.753x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 229.9 | 229.3 | 231.3 | 0.7 | 0.409x | 10.806x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 232.4 | 230.1 | 233.9 | 1.3 | 0.414x | 10.925x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 562.1 | 553.4 | 580.2 | 8.8 | 1.000x | 26.418x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.7 | 33.6 | 35.0 | 0.5 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.7 | 33.7 | 34.5 | 0.3 | 0.052x | 1.000x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.7 | 0.0 | 0.052x | 1.000x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.1 | 0.1 | 0.052x | 1.004x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 57.9 | 57.8 | 62.4 | 1.8 | 0.089x | 1.720x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 66.7 | 66.6 | 67.0 | 0.2 | 0.102x | 1.981x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 67.5 | 66.9 | 73.1 | 2.3 | 0.103x | 2.006x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 67.8 | 67.5 | 68.2 | 0.3 | 0.104x | 2.015x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 653.3 | 647.6 | 667.6 | 7.8 | 1.000x | 19.409x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 659.4 | 653.3 | 669.0 | 5.5 | 1.009x | 19.591x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 61.4 | 61.1 | 62.1 | 0.3 | 0.092x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 61.9 | 61.8 | 62.9 | 0.5 | 0.093x | 1.008x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 62.3 | 62.3 | 62.4 | 0.1 | 0.094x | 1.014x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 62.7 | 62.6 | 74.1 | 4.5 | 0.094x | 1.021x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 62.7 | 62.0 | 62.8 | 0.3 | 0.094x | 1.021x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 62.8 | 62.6 | 63.3 | 0.2 | 0.094x | 1.022x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 65.8 | 64.4 | 67.0 | 1.0 | 0.099x | 1.070x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 80.5 | 80.3 | 80.8 | 0.2 | 0.121x | 1.310x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 83.4 | 79.1 | 88.9 | 3.5 | 0.125x | 1.357x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 664.9 | 659.9 | 667.4 | 2.5 | 1.000x | 10.824x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.7 | 0.2 | 0.051x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.051x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 71.5 | 70.9 | 74.0 | 1.2 | 0.112x | 2.213x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73.6 | 71.3 | 74.6 | 1.1 | 0.115x | 2.278x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 81.7 | 81.0 | 82.3 | 0.6 | 0.128x | 2.529x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 83.0 | 82.0 | 84.2 | 0.8 | 0.130x | 2.571x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 637.8 | 635.0 | 644.5 | 3.2 | 0.999x | 19.748x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 638.2 | 630.8 | 645.8 | 6.5 | 1.000x | 19.760x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.3 | 58.2 | 58.9 | 0.2 | 0.090x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.5 | 58.4 | 58.8 | 0.2 | 0.091x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.7 | 58.2 | 66.0 | 3.0 | 0.091x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 80.8 | 79.9 | 88.9 | 4.1 | 0.125x | 1.387x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 88.0 | 88.0 | 88.1 | 0.0 | 0.136x | 1.510x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 88.2 | 88.2 | 90.7 | 1.0 | 0.137x | 1.514x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 90.3 | 90.1 | 91.4 | 0.5 | 0.140x | 1.549x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 90.4 | 90.3 | 91.5 | 0.5 | 0.140x | 1.551x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 644.7 | 635.0 | 647.7 | 5.2 | 1.000x | 11.063x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.0 | 0.040x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.0 | 0.041x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.9 | 0.1 | 0.041x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.1 | 0.041x | 1.001x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 18.2 | 18.0 | 18.8 | 0.3 | 0.044x | 1.083x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 18.5 | 18.3 | 18.9 | 0.2 | 0.045x | 1.101x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 20.7 | 20.7 | 20.8 | 0.0 | 0.050x | 1.236x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.8 | 20.7 | 20.9 | 0.1 | 0.050x | 1.238x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 414.2 | 410.3 | 424.4 | 4.9 | 1.000x | 24.698x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 418.6 | 412.3 | 422.2 | 3.2 | 1.011x | 24.958x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 23.0 | 23.0 | 29.3 | 2.5 | 0.056x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 23.0 | 23.0 | 23.2 | 0.1 | 0.056x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 23.2 | 23.0 | 28.0 | 1.9 | 0.056x | 1.008x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 23.2 | 23.1 | 23.3 | 0.1 | 0.056x | 1.008x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 23.7 | 23.7 | 23.8 | 0.1 | 0.058x | 1.029x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 23.7 | 23.6 | 23.9 | 0.1 | 0.058x | 1.030x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 26.0 | 26.0 | 26.1 | 0.0 | 0.063x | 1.130x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 26.0 | 26.0 | 26.0 | 0.0 | 0.063x | 1.130x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 59.0 | 56.3 | 67.5 | 3.9 | 0.144x | 2.565x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 410.9 | 406.6 | 415.6 | 3.2 | 1.000x | 17.859x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.4 | 11.8 | 12.8 | 0.3 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 12.5 | 12.0 | 14.3 | 0.8 | 0.059x | 1.006x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.6 | 12.4 | 14.0 | 0.6 | 0.060x | 1.017x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.0 | 12.5 | 13.5 | 0.4 | 0.062x | 1.048x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.9 | 25.4 | 36.4 | 4.2 | 0.123x | 2.086x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.124x | 2.106x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.0 | 0.124x | 2.110x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 27.8 | 25.1 | 28.4 | 1.2 | 0.132x | 2.244x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 210.6 | 205.8 | 212.6 | 2.4 | 1.000x | 16.981x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 212.7 | 206.5 | 223.5 | 6.0 | 1.010x | 17.151x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 27.0 | 27.0 | 27.2 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 27.1 | 27.0 | 27.5 | 0.2 | 0.037x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 27.1 | 26.9 | 27.2 | 0.1 | 0.038x | 1.004x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 28.3 | 27.1 | 37.0 | 3.7 | 0.039x | 1.049x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 69.5 | 68.3 | 73.8 | 2.0 | 0.096x | 2.572x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 243.2 | 243.2 | 245.4 | 0.9 | 0.336x | 9.007x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 245.9 | 243.1 | 249.5 | 2.1 | 0.340x | 9.107x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 246.7 | 241.9 | 252.7 | 3.7 | 0.341x | 9.137x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 247.3 | 244.6 | 257.4 | 4.5 | 0.342x | 9.157x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 723.0 | 711.0 | 737.7 | 9.4 | 1.000x | 26.772x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 27.9 | 27.9 | 28.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.0 | 0.052x | 1.003x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 28.1 | 28.0 | 28.3 | 0.1 | 0.052x | 1.006x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.3 | 0.2 | 0.052x | 1.006x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.3 | 42.0 | 42.7 | 0.3 | 0.078x | 1.514x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.4 | 42.3 | 43.6 | 0.5 | 0.080x | 1.555x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 44.4 | 44.1 | 44.7 | 0.2 | 0.082x | 1.591x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 44.6 | 44.2 | 47.6 | 1.3 | 0.082x | 1.599x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 540.6 | 533.2 | 545.8 | 4.6 | 0.999x | 19.367x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 541.0 | 537.4 | 547.8 | 3.8 | 1.000x | 19.381x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 48.4 | 48.3 | 48.7 | 0.1 | 0.089x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 48.4 | 48.4 | 48.7 | 0.1 | 0.089x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 48.5 | 48.3 | 49.0 | 0.2 | 0.089x | 1.003x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 48.7 | 48.4 | 55.3 | 2.7 | 0.090x | 1.006x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 50.0 | 49.6 | 50.9 | 0.4 | 0.092x | 1.033x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 50.2 | 49.2 | 50.5 | 0.5 | 0.092x | 1.037x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 52.7 | 51.5 | 56.0 | 1.6 | 0.097x | 1.090x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 70.5 | 70.2 | 71.2 | 0.3 | 0.130x | 1.458x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 77.7 | 74.6 | 86.1 | 4.2 | 0.143x | 1.606x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 542.4 | 538.1 | 543.6 | 2.1 | 1.000x | 11.212x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.4 | 55.4 | 56.3 | 0.3 | 0.099x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.5 | 55.5 | 55.6 | 0.0 | 0.100x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.7 | 55.5 | 55.8 | 0.1 | 0.100x | 1.005x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.7 | 55.4 | 55.9 | 0.2 | 0.100x | 1.006x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.7 | 55.2 | 56.4 | 0.4 | 0.100x | 1.006x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.9 | 55.6 | 56.7 | 0.4 | 0.100x | 1.008x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 58.0 | 57.6 | 62.0 | 1.6 | 0.104x | 1.046x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 58.0 | 57.2 | 58.7 | 0.5 | 0.104x | 1.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 557.3 | 555.8 | 565.7 | 3.6 | 1.000x | 10.057x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 561.5 | 550.1 | 568.4 | 7.0 | 1.008x | 10.132x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 64.1 | 64.0 | 64.9 | 0.3 | 0.115x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 65.0 | 63.6 | 65.7 | 0.7 | 0.116x | 1.013x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 66.7 | 64.7 | 70.7 | 2.0 | 0.120x | 1.040x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 90.1 | 89.7 | 90.5 | 0.3 | 0.161x | 1.404x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 90.4 | 88.4 | 97.4 | 3.1 | 0.162x | 1.410x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 109.6 | 109.5 | 116.3 | 2.7 | 0.196x | 1.709x |
| 7 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 109.7 | 109.6 | 109.9 | 0.1 | 0.197x | 1.710x |
| 8 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 109.9 | 109.5 | 110.1 | 0.2 | 0.197x | 1.713x |
| 9 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 110.0 | 109.6 | 110.3 | 0.3 | 0.197x | 1.715x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 558.0 | 554.1 | 566.5 | 4.2 | 1.000x | 8.699x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.8 | 42.7 | 43.1 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 42.8 | 42.6 | 43.8 | 0.4 | 0.035x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 42.8 | 42.6 | 43.4 | 0.3 | 0.035x | 1.000x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 43.0 | 42.8 | 44.5 | 0.6 | 0.035x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 65.1 | 64.7 | 65.3 | 0.2 | 0.054x | 1.520x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 66.0 | 65.9 | 66.3 | 0.1 | 0.054x | 1.543x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 67.0 | 67.0 | 67.2 | 0.1 | 0.055x | 1.565x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 67.1 | 67.0 | 72.5 | 2.1 | 0.055x | 1.567x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,212.7 | 1,178.7 | 1,220.6 | 17.0 | 1.000x | 28.327x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,224.0 | 1,180.2 | 1,271.5 | 29.8 | 1.009x | 28.589x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 89.3 | 89.3 | 89.5 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 89.4 | 89.3 | 90.0 | 0.3 | 0.052x | 1.000x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 89.6 | 89.2 | 89.6 | 0.2 | 0.052x | 1.003x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 89.6 | 89.4 | 101.6 | 4.8 | 0.052x | 1.003x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 135.9 | 133.4 | 142.0 | 3.6 | 0.078x | 1.521x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 136.1 | 133.9 | 140.3 | 2.6 | 0.079x | 1.523x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 139.2 | 134.3 | 143.8 | 3.5 | 0.080x | 1.558x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 149.3 | 149.0 | 149.6 | 0.2 | 0.086x | 1.672x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 171.8 | 169.2 | 178.6 | 3.2 | 0.099x | 1.923x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,731.7 | 1,725.9 | 1,740.8 | 5.6 | 1.000x | 19.381x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.004x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.006x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.045x | 1.008x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 25.8 | 25.4 | 26.7 | 0.5 | 0.087x | 1.949x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.968x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.088x | 1.978x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 26.8 | 25.5 | 28.6 | 1.0 | 0.090x | 2.018x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 296.9 | 296.5 | 305.7 | 3.5 | 1.000x | 22.400x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 301.0 | 296.9 | 305.1 | 2.9 | 1.014x | 22.706x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 20.5 | 20.3 | 20.5 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.1 | 0.019x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 20.7 | 20.3 | 20.9 | 0.2 | 0.019x | 1.012x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 20.7 | 20.6 | 27.9 | 2.9 | 0.019x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 68.6 | 68.0 | 76.6 | 3.2 | 0.064x | 3.356x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 190.0 | 187.6 | 193.5 | 2.4 | 0.176x | 9.290x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 190.2 | 189.4 | 192.5 | 1.2 | 0.176x | 9.299x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 191.7 | 187.6 | 194.3 | 2.3 | 0.178x | 9.373x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 193.4 | 188.6 | 195.4 | 2.3 | 0.179x | 9.453x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,078.6 | 1,068.6 | 1,092.8 | 8.3 | 1.000x | 52.727x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.5 | 0.5 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.2 | 15.7 | 1.0 | 0.045x | 1.003x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.004x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.045x | 1.005x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.6 | 0.3 | 0.117x | 2.632x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.1 | 0.1 | 0.118x | 2.638x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 35.0 | 33.9 | 36.3 | 1.0 | 0.118x | 2.638x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 35.6 | 35.1 | 36.4 | 0.5 | 0.119x | 2.680x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 297.9 | 295.6 | 302.4 | 2.5 | 1.000x | 22.446x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 302.1 | 296.0 | 304.2 | 3.4 | 1.014x | 22.761x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.8 | 26.6 | 27.1 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.1 | 0.025x | 1.003x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.9 | 26.8 | 36.8 | 4.0 | 0.025x | 1.005x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.9 | 26.8 | 27.2 | 0.1 | 0.025x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 73.2 | 70.7 | 77.7 | 2.5 | 0.068x | 2.737x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 305.0 | 300.8 | 308.3 | 2.7 | 0.283x | 11.400x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 306.8 | 301.1 | 317.8 | 5.8 | 0.285x | 11.466x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 311.3 | 306.1 | 313.2 | 2.4 | 0.289x | 11.634x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 311.6 | 303.6 | 312.8 | 3.5 | 0.289x | 11.646x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,077.1 | 1,055.2 | 1,080.5 | 9.1 | 1.000x | 40.255x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.6 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.051x | 1.000x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 0.051x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.051x | 1.001x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 86.4 | 86.2 | 86.6 | 0.2 | 0.136x | 2.673x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 88.8 | 88.8 | 88.9 | 0.0 | 0.140x | 2.749x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 89.2 | 89.1 | 89.8 | 0.3 | 0.140x | 2.761x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 91.0 | 90.9 | 92.6 | 0.7 | 0.143x | 2.815x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 631.8 | 625.6 | 638.4 | 4.4 | 0.993x | 19.547x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 636.4 | 628.8 | 639.5 | 3.8 | 1.000x | 19.691x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.3 | 58.8 | 0.2 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.4 | 58.2 | 62.8 | 1.8 | 0.091x | 1.002x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.2 | 70.9 | 5.0 | 0.091x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 59.0 | 58.4 | 67.4 | 3.5 | 0.092x | 1.011x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 68.4 | 68.1 | 74.3 | 2.4 | 0.106x | 1.172x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 68.5 | 67.7 | 74.2 | 2.4 | 0.106x | 1.175x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 87.4 | 87.3 | 97.4 | 4.0 | 0.136x | 1.499x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 90.5 | 90.4 | 90.6 | 0.1 | 0.141x | 1.552x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 102.0 | 102.0 | 102.5 | 0.2 | 0.158x | 1.750x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 643.9 | 636.7 | 657.9 | 7.5 | 1.000x | 11.043x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 0.051x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.3 | 33.0 | 0.3 | 0.051x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.6 | 32.3 | 32.7 | 0.2 | 0.051x | 1.011x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 86.3 | 86.2 | 86.8 | 0.2 | 0.136x | 2.676x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 88.9 | 88.8 | 89.0 | 0.1 | 0.140x | 2.756x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 89.2 | 89.0 | 89.4 | 0.1 | 0.140x | 2.766x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 90.9 | 90.9 | 91.1 | 0.1 | 0.143x | 2.818x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 633.6 | 624.8 | 641.1 | 5.9 | 0.996x | 19.639x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 636.2 | 625.6 | 638.0 | 4.4 | 1.000x | 19.718x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.3 | 58.2 | 71.0 | 5.1 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.1 | 58.5 | 0.1 | 0.091x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.4 | 58.3 | 62.7 | 1.7 | 0.091x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.3 | 58.7 | 0.2 | 0.091x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 68.4 | 67.9 | 75.3 | 2.8 | 0.107x | 1.174x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 68.6 | 68.1 | 74.7 | 2.4 | 0.107x | 1.178x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 87.4 | 87.3 | 93.4 | 2.4 | 0.136x | 1.500x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 90.6 | 90.4 | 90.9 | 0.2 | 0.141x | 1.554x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 102.0 | 101.9 | 103.2 | 0.5 | 0.159x | 1.751x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 641.6 | 634.3 | 653.9 | 6.7 | 1.000x | 11.012x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.046x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.7 | 0.1 | 0.046x | 1.002x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.4 | 32.2 | 32.5 | 0.1 | 0.046x | 1.003x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 75.1 | 74.7 | 75.3 | 0.2 | 0.108x | 2.324x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 76.5 | 75.5 | 77.4 | 0.7 | 0.110x | 2.368x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 85.5 | 84.5 | 86.6 | 0.7 | 0.123x | 2.647x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 85.8 | 85.1 | 94.0 | 3.4 | 0.123x | 2.657x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 696.2 | 690.0 | 707.4 | 6.4 | 0.998x | 21.555x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 697.7 | 690.4 | 704.1 | 4.9 | 1.000x | 21.603x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.3 | 70.9 | 5.0 | 0.083x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.4 | 59.2 | 0.3 | 0.084x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.5 | 58.2 | 60.8 | 1.0 | 0.084x | 1.002x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.5 | 58.2 | 58.8 | 0.2 | 0.084x | 1.002x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 62.2 | 61.5 | 64.2 | 1.0 | 0.089x | 1.065x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 65.5 | 60.7 | 70.7 | 3.2 | 0.094x | 1.123x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 74.7 | 74.6 | 77.0 | 0.9 | 0.107x | 1.279x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 88.8 | 88.3 | 93.5 | 2.0 | 0.127x | 1.521x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 94.0 | 92.8 | 94.7 | 0.6 | 0.134x | 1.611x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 699.8 | 695.3 | 711.8 | 7.1 | 1.000x | 11.989x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.045x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.4 | 0.0 | 0.045x | 1.002x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.5 | 0.1 | 0.045x | 1.003x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 55.0 | 54.0 | 56.5 | 0.9 | 0.076x | 1.703x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 56.0 | 53.7 | 66.2 | 4.4 | 0.077x | 1.733x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72.4 | 72.3 | 72.6 | 0.1 | 0.100x | 2.242x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 72.7 | 72.4 | 73.3 | 0.3 | 0.100x | 2.252x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 721.4 | 714.8 | 732.3 | 5.8 | 0.996x | 22.337x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 724.1 | 711.0 | 728.9 | 6.6 | 1.000x | 22.418x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.4 | 58.2 | 58.6 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.2 | 71.4 | 5.2 | 0.081x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.6 | 58.3 | 60.5 | 0.9 | 0.081x | 1.005x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.6 | 58.3 | 58.9 | 0.2 | 0.081x | 1.005x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 65.6 | 58.2 | 74.7 | 5.7 | 0.090x | 1.125x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 69.7 | 66.7 | 74.5 | 2.5 | 0.096x | 1.194x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 73.5 | 70.4 | 78.8 | 3.1 | 0.101x | 1.259x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 83.4 | 82.9 | 93.3 | 4.9 | 0.115x | 1.429x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 85.9 | 85.6 | 86.2 | 0.2 | 0.118x | 1.471x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 725.5 | 723.7 | 726.3 | 1.0 | 1.000x | 12.433x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.045x | 1.000x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.045x | 1.001x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.045x | 1.001x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 53.8 | 53.7 | 55.2 | 0.6 | 0.074x | 1.666x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 54.2 | 54.1 | 55.0 | 0.3 | 0.075x | 1.680x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 72.4 | 72.3 | 73.4 | 0.4 | 0.100x | 2.243x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 72.7 | 72.6 | 74.3 | 0.6 | 0.100x | 2.252x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 723.2 | 715.7 | 729.5 | 5.0 | 0.999x | 22.403x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 724.0 | 714.6 | 730.6 | 5.8 | 1.000x | 22.428x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 58.2 | 58.1 | 70.8 | 5.1 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 58.3 | 58.2 | 58.7 | 0.2 | 0.081x | 1.001x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 58.4 | 58.3 | 58.6 | 0.1 | 0.081x | 1.004x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 58.6 | 58.1 | 60.7 | 1.0 | 0.081x | 1.007x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 66.6 | 66.4 | 70.0 | 1.4 | 0.092x | 1.144x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 67.9 | 59.4 | 69.8 | 3.8 | 0.094x | 1.167x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 75.7 | 72.9 | 79.4 | 2.7 | 0.105x | 1.300x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 83.2 | 83.0 | 94.3 | 4.6 | 0.115x | 1.431x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 85.6 | 85.2 | 86.1 | 0.3 | 0.118x | 1.470x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 723.4 | 721.7 | 726.2 | 1.7 | 1.000x | 12.433x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.046x | 1.001x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.046x | 1.001x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.5 | 0.1 | 0.046x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 47.0 | 45.7 | 48.6 | 1.1 | 0.134x | 2.922x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 55.9 | 55.3 | 57.1 | 0.8 | 0.159x | 3.473x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 57.0 | 52.8 | 58.3 | 2.0 | 0.163x | 3.540x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 58.2 | 57.8 | 60.5 | 1.0 | 0.166x | 3.615x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 350.8 | 345.6 | 364.4 | 6.6 | 1.000x | 21.785x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 352.6 | 349.8 | 358.5 | 3.0 | 1.005x | 21.898x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 26.3 | 26.0 | 26.6 | 0.2 | 0.021x | 1.002x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 26.5 | 26.3 | 27.9 | 0.6 | 0.021x | 1.011x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 26.7 | 26.3 | 35.3 | 3.5 | 0.021x | 1.017x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 71.7 | 70.9 | 79.0 | 3.0 | 0.056x | 2.731x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 377.8 | 375.7 | 399.7 | 8.9 | 0.295x | 14.388x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 381.8 | 377.8 | 385.6 | 3.0 | 0.298x | 14.540x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 383.8 | 380.4 | 386.4 | 2.5 | 0.300x | 14.619x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 396.9 | 393.8 | 399.2 | 2.0 | 0.310x | 15.116x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,280.1 | 1,263.2 | 1,288.8 | 8.8 | 1.000x | 48.754x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.0 | 10.8 | 11.6 | 0.3 | 0.376x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.2 | 12.0 | 0.4 | 0.382x | 1.016x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.4 | 10.9 | 11.4 | 0.2 | 0.390x | 1.036x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.5 | 11.0 | 12.1 | 0.4 | 0.392x | 1.043x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.8 | 0.0 | 0.468x | 1.244x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 14.2 | 14.1 | 14.6 | 0.2 | 0.486x | 1.293x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 15.6 | 15.6 | 15.6 | 0.0 | 0.534x | 1.418x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 15.6 | 15.6 | 15.7 | 0.1 | 0.534x | 1.421x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 28.9 | 28.9 | 29.1 | 0.1 | 0.991x | 2.633x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 29.2 | 29.2 | 29.3 | 0.0 | 1.000x | 2.658x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 4.5 | 4.4 | 4.6 | 0.1 | 0.148x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 4.6 | 4.5 | 4.7 | 0.1 | 0.151x | 1.026x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 5.6 | 5.6 | 5.7 | 0.1 | 0.184x | 1.249x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.184x | 1.250x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 14.9 | 14.9 | 15.1 | 0.1 | 0.490x | 3.323x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 15.1 | 14.9 | 15.2 | 0.1 | 0.496x | 3.362x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 17.3 | 17.3 | 17.6 | 0.1 | 0.569x | 3.856x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17.3 | 17.3 | 17.4 | 0.0 | 0.569x | 3.860x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.4 | 30.2 | 31.0 | 0.4 | 1.000x | 6.779x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 37.5 | 34.9 | 48.5 | 4.8 | 1.230x | 8.340x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.1 | 0.1 | 0.328x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.334x | 1.020x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.0 | 0.3 | 0.346x | 1.055x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 10.6 | 10.6 | 11.2 | 0.2 | 0.354x | 1.081x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 15.8 | 14.9 | 17.0 | 0.7 | 0.525x | 1.603x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.2 | 15.2 | 17.5 | 0.9 | 0.538x | 1.644x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.544x | 1.661x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.7 | 0.1 | 0.545x | 1.664x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 29.6 | 28.9 | 29.8 | 0.3 | 0.987x | 3.011x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 30.0 | 29.6 | 30.2 | 0.2 | 1.000x | 3.052x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 5.1 | 5.0 | 5.9 | 0.4 | 0.163x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 5.3 | 5.0 | 5.4 | 0.2 | 0.171x | 1.049x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 6.5 | 5.9 | 7.2 | 0.4 | 0.209x | 1.282x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 6.5 | 6.5 | 6.5 | 0.0 | 0.209x | 1.282x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 22.4 | 22.4 | 22.5 | 0.0 | 0.724x | 4.431x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 23.7 | 23.6 | 24.9 | 0.5 | 0.763x | 4.671x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 24.3 | 24.0 | 26.9 | 1.1 | 0.783x | 4.792x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 24.6 | 24.5 | 25.0 | 0.2 | 0.792x | 4.852x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 31.0 | 31.0 | 35.1 | 1.6 | 1.000x | 6.124x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 38.8 | 36.4 | 49.7 | 4.9 | 1.250x | 7.656x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.8 | 0.3 | 0.288x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 11.2 | 11.0 | 11.2 | 0.1 | 0.291x | 1.008x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.3 | 0.2 | 0.308x | 1.069x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.8 | 0.4 | 0.310x | 1.076x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.3 | 21.0 | 23.8 | 1.0 | 0.551x | 1.910x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.5 | 21.1 | 22.5 | 0.5 | 0.556x | 1.927x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.559x | 1.937x |
| 8 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 21.6 | 21.5 | 21.7 | 0.1 | 0.559x | 1.938x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 36.3 | 35.2 | 40.6 | 1.9 | 0.939x | 3.256x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 38.6 | 35.7 | 41.6 | 2.4 | 1.000x | 3.467x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 37.0 | 36.6 | 40.7 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 38.4 | 37.0 | 50.0 | 5.1 | 1.038x | 1.038x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 73.3 | 72.4 | 79.8 | 2.7 | 1.983x | 1.983x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 73.4 | 73.3 | 73.7 | 0.1 | 1.985x | 1.985x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 73.5 | 72.9 | 74.0 | 0.4 | 1.988x | 1.988x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 73.6 | 73.3 | 73.7 | 0.1 | 1.990x | 1.990x |
| 7 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 618.9 | 612.9 | 635.6 | 7.7 | 16.744x | 16.744x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 620.4 | 616.2 | 635.3 | 7.4 | 16.784x | 16.784x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 624.1 | 614.6 | 638.4 | 8.6 | 16.885x | 16.885x |
| 10 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 626.6 | 616.0 | 633.7 | 6.0 | 16.953x | 16.953x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.2 | 0.0 | 0.506x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.3 | 0.1 | 0.508x | 1.003x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 19.2 | 19.2 | 19.3 | 0.1 | 0.508x | 1.003x |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 19.2 | 19.2 | 20.7 | 0.6 | 0.508x | 1.004x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 20.8 | 20.4 | 21.0 | 0.2 | 0.551x | 1.089x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 21.1 | 21.0 | 21.6 | 0.2 | 0.559x | 1.105x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 23.0 | 22.8 | 23.1 | 0.1 | 0.608x | 1.202x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.8 | 0.3 | 0.609x | 1.204x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 34.6 | 34.1 | 35.2 | 0.4 | 0.915x | 1.809x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 37.8 | 35.2 | 40.1 | 1.8 | 1.000x | 1.976x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 16.1 | 16.0 | 20.2 | 1.6 | 0.444x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 16.2 | 16.1 | 16.3 | 0.1 | 0.446x | 1.003x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 16.2 | 16.0 | 16.9 | 0.3 | 0.448x | 1.008x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 16.5 | 16.1 | 17.6 | 0.5 | 0.454x | 1.021x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 36.3 | 35.7 | 40.3 | 1.7 | 1.000x | 2.250x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 36.5 | 36.1 | 49.7 | 5.2 | 1.006x | 2.264x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 122.8 | 121.7 | 123.9 | 0.7 | 3.386x | 7.620x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 123.3 | 120.6 | 124.6 | 1.4 | 3.399x | 7.649x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 125.5 | 125.1 | 126.1 | 0.3 | 3.459x | 7.783x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 126.4 | 125.6 | 127.6 | 0.7 | 3.484x | 7.841x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,576,575.8 | 3,574,991.7 | 3,589,725.4 | 6,003.4 | 0.125x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,583,848.6 | 3,574,796.0 | 3,610,612.4 | 12,224.7 | 0.125x | 1.002x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,584,125.0 | 3,575,522.4 | 3,586,988.7 | 4,723.2 | 0.125x | 1.002x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,587,388.5 | 3,581,768.5 | 3,621,958.1 | 14,392.7 | 0.125x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 3,700,507.0 | 3,619,299.0 | 3,704,156.4 | 32,418.7 | 0.129x | 1.035x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 5,069,643.3 | 4,986,086.0 | 5,514,422.7 | 194,215.8 | 0.177x | 1.417x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 5,179,320.7 | 5,134,193.7 | 7,682,122.0 | 1,000,435.5 | 0.181x | 1.448x |
| 8 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 5,186,766.7 | 5,166,419.7 | 5,215,883.3 | 17,324.0 | 0.181x | 1.450x |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 5,260,367.7 | 5,226,587.7 | 5,399,742.0 | 61,422.8 | 0.184x | 1.471x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 28,638,016.7 | 28,601,379.1 | 29,677,306.8 | 409,825.4 | 1.000x | 8.007x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,983.0 | 17,950.2 | 18,048.6 | 35.9 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 1,886,284.8 | 1,884,519.8 | 1,912,248.1 | 10,362.9 | 104.892x | 104.892x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 1,887,163.0 | 1,885,469.8 | 1,921,983.8 | 13,910.1 | 104.941x | 104.941x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 1,888,192.1 | 1,884,753.9 | 1,905,477.8 | 7,414.1 | 104.999x | 104.999x |
| 5 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 1,892,471.5 | 1,887,969.1 | 1,895,532.6 | 2,576.6 | 105.236x | 105.236x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 2,559,712.1 | 2,540,969.5 | 2,565,705.2 | 11,254.9 | 142.340x | 142.340x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 15,989,261.3 | 15,918,127.7 | 16,089,628.7 | 66,429.2 | 889.130x | 889.130x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 16,042,291.3 | 15,929,887.3 | 16,079,748.0 | 54,548.4 | 892.079x | 892.079x |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16,092,335.0 | 15,990,307.7 | 16,139,312.0 | 60,723.6 | 894.862x | 894.862x |
| 10 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 16,108,472.3 | 15,958,645.0 | 16,485,861.3 | 192,675.5 | 895.759x | 895.759x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,933.2 | 17,893.8 | 18,022.1 | 43.7 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 1,875,429.5 | 1,874,090.8 | 1,890,585.2 | 6,248.7 | 104.579x | 104.579x | 5 | 100% |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 1,875,730.8 | 1,873,708.4 | 1,878,721.4 | 1,667.7 | 104.596x | 104.596x | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 1,875,774.8 | 1,875,332.2 | 1,877,435.4 | 743.3 | 104.598x | 104.598x | 5 | 100% |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 1,876,250.4 | 1,873,584.1 | 1,918,973.8 | 17,329.2 | 104.625x | 104.625x | 5 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 2,818,428.0 | 2,816,233.6 | 2,822,301.8 | 2,573.3 | 157.163x | 157.163x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,135,589.7 | 3,132,307.1 | 3,145,628.4 | 4,981.3 | 0.033x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,137,544.3 | 3,124,093.6 | 3,148,941.8 | 8,618.0 | 0.033x | 1.001x |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,137,862.7 | 3,136,574.5 | 3,142,649.2 | 2,109.9 | 0.033x | 1.001x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,148,674.1 | 3,134,659.6 | 3,183,629.3 | 17,250.0 | 0.034x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 5,966,791.7 | 5,961,199.2 | 6,000,178.1 | 14,414.3 | 0.064x | 1.903x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17,151,501.3 | 16,742,832.3 | 17,601,914.0 | 289,537.3 | 0.183x | 5.470x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 17,162,935.3 | 16,945,837.3 | 17,607,011.0 | 256,161.1 | 0.183x | 5.474x |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 17,380,189.0 | 16,832,286.0 | 17,644,394.0 | 320,359.9 | 0.185x | 5.543x |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 17,416,373.0 | 16,639,741.7 | 17,620,677.7 | 354,885.3 | 0.185x | 5.554x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 93,901,018.6 | 93,759,164.2 | 99,292,858.2 | 2,164,943.1 | 1.000x | 29.947x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 17,971.3 | 17,957.5 | 17,984.6 | 10.9 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,093,057.1 | 3,084,898.9 | 3,098,371.3 | 5,107.4 | 172.111x | 172.111x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,094,784.0 | 3,079,311.4 | 3,116,634.8 | 13,242.1 | 172.207x | 172.207x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,095,070.0 | 3,090,272.4 | 3,104,000.7 | 5,153.8 | 172.223x | 172.223x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,097,595.6 | 3,091,457.5 | 3,110,152.6 | 6,472.4 | 172.363x | 172.363x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 3,159,050.0 | 3,155,013.8 | 3,180,387.1 | 9,183.7 | 175.783x | 175.783x |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16,977,360.3 | 16,679,475.0 | 17,742,841.3 | 393,864.9 | 944.691x | 944.691x |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 17,088,094.0 | 16,560,657.7 | 17,648,674.0 | 344,244.7 | 950.853x | 950.853x |
| 9 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 17,610,014.7 | 17,112,101.7 | 17,692,555.0 | 233,472.4 | 979.895x | 979.895x |
| 10 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 17,636,524.3 | 16,556,841.3 | 17,675,714.3 | 441,749.5 | 981.370x | 981.370x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_1989c62_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 164,915,127.0 | 156,981,861.0 | 182,641,919.0 | 8,625,738.7 | 5 | 43,344 | 82,314 | 13,620 | 0.052 | compiled=5 | 21,246,982.0 | 147,074,564.0 | 190,671.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 173,581,817.0 | 166,130,205.0 | 183,948,586.0 | 6,720,513.4 | 5 | 47,584 | 94,525 | 15,536 | 0.039 | compiled=5 | 12,067,839.0 | 161,425,557.0 | 109,531.0 |
| `factored` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 151,621,570.0 | 150,070,112.0 | 160,325,170.0 | 3,773,314.3 | 5 | 47,440 | 82,131 | 13,433 | 0.025 | compiled=5 | 10,169,728.0 | 140,530,217.0 | 114,060.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,328,764.0 | 154,959,980.0 | 186,417,630.0 | 10,113,724.8 | 5 | 47,584 | 94,342 | 15,349 | 0.059 (max is trial 1) | compiled=5 | 12,979,624.0 | 158,353,199.0 | 192,941.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 557,601,392.0 | 549,327,714.0 | 569,843,521.0 | 7,315,769.4 | 5 | 39,248 | 58,359 | 56,805 | 0.013 | compiled=5 | 2,524,514.0 | 554,883,877.0 | 193,001.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 565,207,216.0 | 558,228,695.0 | 571,057,819.0 | 4,268,779.8 | 5 | 39,248 | 58,475 | 56,921 | 0.008 | compiled=5 | 2,169,652.0 | 561,344,614.0 | 200,541.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 557,938,347.0 | 546,318,699.0 | 563,311,338.0 | 6,106,183.7 | 5 | 39,248 | 58,359 | 56,805 | 0.011 | compiled=5 | 2,326,253.0 | 555,627,603.0 | 108,241.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 561,136,606.0 | 549,125,744.0 | 565,607,772.0 | 5,693,701.3 | 5 | 39,248 | 58,475 | 56,921 | 0.010 | compiled=5 | 2,209,483.0 | 558,601,840.0 | 106,210.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 161,367,376.0 | 160,364,191.0 | 168,045,206.0 | 2,768,245.7 | 5 | 43,224 | 82,080 | 13,386 | 0.017 | compiled=5 | 9,593,116.0 | 150,683,764.0 | 199,961.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 173,642,569.0 | 162,000,350.0 | 195,343,764.0 | 11,832,867.7 | 5 | 47,464 | 94,291 | 15,302 | 0.068 (max is trial 1) | compiled=5 | 17,795,364.0 | 160,135,889.0 | 196,911.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 156,332,757.0 | 146,742,271.0 | 169,572,655.0 | 8,313,785.5 | 5 | 43,224 | 81,897 | 13,199 | 0.053 | compiled=5 | 9,544,566.0 | 146,686,991.0 | 187,602.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 169,353,324.0 | 158,336,598.0 | 175,847,071.0 | 6,277,917.7 | 5 | 47,464 | 94,108 | 15,115 | 0.037 | compiled=5 | 11,953,990.0 | 157,465,023.0 | 179,471.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 560,952,030.0 | 552,401,499.0 | 574,504,699.0 | 7,800,620.7 | 5 | 39,128 | 58,254 | 56,700 | 0.014 | compiled=5 | 2,163,513.0 | 558,645,066.0 | 198,721.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 561,262,931.0 | 553,920,967.0 | 566,432,401.0 | 4,509,880.6 | 5 | 39,128 | 58,370 | 56,816 | 0.008 | compiled=5 | 2,579,045.0 | 557,399,298.0 | 90,240.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 549,464,481.0 | 548,090,774.0 | 552,673,581.0 | 1,655,066.8 | 5 | 39,128 | 58,254 | 56,700 | 0.003 (max is trial 1) | compiled=5 | 2,182,383.0 | 545,859,350.0 | 188,261.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 568,066,400.0 | 554,524,271.0 | 569,803,801.0 | 5,749,619.0 | 5 | 39,128 | 58,370 | 56,816 | 0.010 | compiled=5 | 2,302,993.0 | 565,593,376.0 | 100,111.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 138,937,769.0 | 130,915,322.0 | 149,545,609.0 | 6,514,661.1 | 5 | 22,832 | 17,965 | 12,968 | 0.047 | compiled=5 | 1,809,261.0 | 137,082,487.0 | 189,661.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 149,982,771.0 | 145,127,543.0 | 155,552,133.0 | 3,491,085.5 | 5 | 22,968 | 20,308 | 14,985 | 0.023 | compiled=5 | 1,692,279.0 | 148,114,051.0 | 96,651.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 139,949,224.0 | 130,838,550.0 | 142,838,561.0 | 4,676,626.4 | 5 | 22,832 | 17,965 | 12,968 | 0.033 | compiled=5 | 1,653,409.0 | 136,240,052.0 | 109,170.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 148,273,931.0 | 141,076,649.0 | 152,803,577.0 | 4,745,842.6 | 5 | 22,968 | 20,308 | 14,985 | 0.032 | compiled=5 | 1,822,371.0 | 146,451,511.0 | 183,361.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 128,967,530.0 | 124,322,624.0 | 137,012,847.0 | 4,823,380.7 | 5 | 22,376 | 17,258 | 17,258 | 0.037 | compiled=5 | 1,429,138.0 | 127,548,612.0 | 182,731.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 137,382,550.0 | 121,509,347.0 | 142,162,417.0 | 7,505,540.6 | 5 | 22,376 | 17,369 | 17,369 | 0.055 | compiled=5 | 1,457,899.0 | 135,826,510.0 | 98,900.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 136,759,498.0 | 133,740,580.0 | 137,964,826.0 | 1,824,242.0 | 5 | 22,376 | 17,258 | 17,258 | 0.013 | compiled=5 | 1,467,469.0 | 135,122,328.0 | 196,311.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 136,344,905.0 | 128,201,518.0 | 141,820,418.0 | 5,034,770.1 | 5 | 22,376 | 17,369 | 17,369 | 0.037 | compiled=5 | 1,755,101.0 | 133,278,078.0 | 190,831.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 133,986,396.0 | 129,174,899.0 | 142,126,773.0 | 4,614,847.4 | 5 | 22,712 | 17,731 | 12,734 | 0.034 | compiled=5 | 1,734,020.0 | 132,040,485.0 | 188,771.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 147,942,328.0 | 144,005,944.0 | 154,591,887.0 | 3,790,768.5 | 5 | 22,856 | 20,074 | 14,751 | 0.026 | compiled=5 | 1,672,159.0 | 145,940,916.0 | 99,891.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 131,184,190.0 | 124,625,080.0 | 138,781,244.0 | 5,533,696.7 | 5 | 22,712 | 17,731 | 12,734 | 0.042 | compiled=5 | 1,680,810.0 | 129,391,839.0 | 117,511.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 149,578,517.0 | 143,713,063.0 | 151,059,906.0 | 2,757,231.6 | 5 | 22,856 | 20,074 | 14,751 | 0.018 | compiled=5 | 1,678,290.0 | 147,514,265.0 | 102,211.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 144,984,105.0 | 140,000,455.0 | 155,450,617.0 | 5,526,755.8 | 5 | 22,344 | 17,660 | 17,660 | 0.038 | compiled=5 | 1,620,700.0 | 143,173,954.0 | 186,041.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 149,400,661.0 | 140,726,940.0 | 152,597,870.0 | 4,214,821.7 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 1,528,869.0 | 147,835,302.0 | 106,611.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 143,038,783.0 | 142,028,867.0 | 152,074,138.0 | 3,847,908.1 | 5 | 22,344 | 17,660 | 17,660 | 0.027 | compiled=5 | 1,451,489.0 | 140,558,609.0 | 190,721.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 149,887,504.0 | 141,599,525.0 | 152,215,158.0 | 4,185,187.6 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 2,899,487.0 | 146,859,346.0 | 187,241.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 156,626,339.0 | 152,463,315.0 | 162,571,233.0 | 3,827,137.0 | 5 | 43,304 | 81,907 | 13,380 | 0.024 | compiled=5 | 9,352,623.0 | 147,153,485.0 | 107,731.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 169,897,296.0 | 158,601,931.0 | 180,453,986.0 | 7,594,084.9 | 5 | 47,544 | 94,118 | 15,296 | 0.045 (max is trial 1) | compiled=5 | 11,432,616.0 | 150,413,164.0 | 196,642.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 155,645,893.0 | 148,604,192.0 | 161,597,979.0 | 5,318,300.2 | 5 | 43,304 | 81,907 | 13,380 | 0.034 | compiled=5 | 9,623,285.0 | 139,588,191.0 | 112,860.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,558,255.0 | 168,392,047.0 | 174,796,025.0 | 2,301,945.8 | 5 | 47,544 | 94,118 | 15,296 | 0.013 | compiled=5 | 11,420,075.0 | 157,236,173.0 | 193,971.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 432,550,604.0 | 423,790,122.0 | 432,981,428.0 | 3,557,204.4 | 5 | 30,976 | 47,188 | 45,801 | 0.008 | compiled=5 | 1,953,732.0 | 430,495,102.0 | 115,240.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 432,168,521.0 | 409,864,175.0 | 439,547,864.0 | 11,267,008.2 | 5 | 30,976 | 47,306 | 45,919 | 0.026 | compiled=5 | 1,929,061.0 | 430,050,959.0 | 192,691.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 437,531,255.0 | 432,370,325.0 | 447,960,387.0 | 5,531,367.4 | 5 | 30,976 | 47,188 | 45,801 | 0.013 | compiled=5 | 2,042,772.0 | 433,210,960.0 | 188,701.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 429,579,968.0 | 421,616,232.0 | 432,505,467.0 | 3,830,835.1 | 5 | 30,976 | 47,306 | 45,919 | 0.009 | compiled=5 | 2,052,033.0 | 427,185,674.0 | 197,772.0 |
| `orig` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 155,909,854.0 | 148,124,119.0 | 161,865,359.0 | 4,560,674.0 | 5 | 43,184 | 81,673 | 13,146 | 0.029 (max is trial 1) | compiled=5 | 9,193,534.0 | 145,299,572.0 | 112,481.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 166,269,755.0 | 157,823,085.0 | 187,526,990.0 | 11,174,706.0 | 5 | 47,424 | 93,884 | 15,062 | 0.067 | compiled=5 | 11,325,736.0 | 154,860,548.0 | 190,591.0 |
| `orig` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 158,494,010.0 | 153,283,090.0 | 159,820,747.0 | 2,292,895.1 | 5 | 43,184 | 81,673 | 13,146 | 0.014 | compiled=5 | 15,270,279.0 | 143,030,149.0 | 193,582.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 170,588,431.0 | 165,958,083.0 | 174,447,733.0 | 3,451,250.8 | 5 | 47,424 | 93,884 | 15,062 | 0.020 | compiled=5 | 11,299,856.0 | 155,813,914.0 | 176,731.0 |
| `orig` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 432,252,700.0 | 428,192,665.0 | 440,587,819.0 | 4,944,494.4 | 5 | 30,856 | 47,083 | 45,696 | 0.011 (max is trial 1) | compiled=5 | 1,940,911.0 | 430,240,938.0 | 183,021.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 439,477,152.0 | 427,270,060.0 | 440,660,949.0 | 5,186,906.2 | 5 | 30,856 | 47,201 | 45,814 | 0.012 | compiled=5 | 3,999,074.0 | 435,747,821.0 | 201,951.0 |
| `orig` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 432,276,781.0 | 422,582,502.0 | 440,401,109.0 | 6,161,203.2 | 5 | 30,856 | 47,083 | 45,696 | 0.014 | compiled=5 | 1,970,322.0 | 430,082,787.0 | 108,371.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 418,893,331.0 | 418,489,718.0 | 421,067,724.0 | 1,080,686.2 | 5 | 30,856 | 47,201 | 45,814 | 0.003 | compiled=5 | 2,167,223.0 | 416,497,917.0 | 186,551.0 |

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

