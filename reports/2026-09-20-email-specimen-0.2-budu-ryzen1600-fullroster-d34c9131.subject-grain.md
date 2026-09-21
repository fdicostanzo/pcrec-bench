# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=email-specimen, version=0.2, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_d34c9131_auto-caps-simdna, testee=pcrec_1989c62_auto-nocaps-simdna, testee=pcrec_1989c62_vm-caps-simdna, testee=pcrec_1989c62_vm-in-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (14 record(s) matching this query)
- records included: 7
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-nocaps-simdna/email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-in-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.5, 1.6
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 7 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.6 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.1 | 0.040x | 1.066x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 150.7 | 150.3 | 152.6 | 0.9 | 0.173x | 4.630x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.6 | 151.6 | 153.3 | 0.7 | 0.175x | 4.687x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 863.9 | 857.9 | 884.2 | 9.0 | 0.991x | 26.533x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.6 | 865.8 | 882.8 | 6.0 | 1.000x | 26.771x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.5 | 58.9 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.9 | 62.4 | 63.4 | 0.3 | 0.073x | 1.071x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 148.2 | 147.9 | 148.5 | 0.2 | 0.172x | 2.524x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 151.9 | 151.5 | 152.3 | 0.3 | 0.176x | 2.588x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.1 | 153.9 | 154.6 | 0.3 | 0.178x | 2.626x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 863.8 | 854.6 | 872.1 | 6.6 | 1.000x | 14.714x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.1 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.0 | 44.4 | 0.5 | 0.036x | 1.098x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.7 | 197.4 | 199.3 | 0.7 | 0.163x | 4.978x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.3 | 198.7 | 199.4 | 0.3 | 0.163x | 4.994x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,217.2 | 1,214.6 | 1,229.8 | 5.5 | 0.997x | 30.498x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,220.7 | 1,210.7 | 1,258.3 | 17.5 | 1.000x | 30.585x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 77.6 | 77.5 | 78.1 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 79.9 | 80.5 | 0.2 | 0.066x | 1.036x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.4 | 175.0 | 176.0 | 0.3 | 0.144x | 2.259x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 201.1 | 200.1 | 202.1 | 0.7 | 0.165x | 2.591x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 205.0 | 204.8 | 206.3 | 0.6 | 0.168x | 2.641x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,219.9 | 1,219.7 | 1,231.7 | 5.8 | 1.000x | 15.716x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.3 | 20.6 | 0.1 | 0.028x | 1.126x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.3 | 104.5 | 0.1 | 0.140x | 5.701x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.0 | 104.8 | 105.5 | 0.2 | 0.140x | 5.737x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 747.6 | 744.6 | 764.3 | 7.0 | 1.000x | 40.863x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 752.1 | 743.8 | 753.1 | 3.9 | 1.006x | 41.107x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.0 | 0.0 | 0.035x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.9 | 0.6 | 0.038x | 1.100x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 101.9 | 101.8 | 102.2 | 0.1 | 0.135x | 3.919x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 105.4 | 105.4 | 105.6 | 0.1 | 0.140x | 4.055x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.3 | 121.4 | 124.5 | 1.2 | 0.164x | 4.741x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 752.1 | 747.7 | 765.2 | 5.9 | 1.000x | 28.927x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 44.4 | 0.4 | 0.033x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.2 | 46.5 | 0.1 | 0.035x | 1.069x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 211.4 | 211.2 | 215.4 | 1.6 | 0.159x | 4.881x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 213.0 | 212.3 | 216.2 | 1.7 | 0.160x | 4.918x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,327.5 | 1,316.0 | 1,336.1 | 6.9 | 1.000x | 30.649x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,335.8 | 1,327.9 | 1,342.2 | 5.0 | 1.006x | 30.842x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 86.6 | 86.1 | 87.0 | 0.4 | 0.066x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 87.7 | 87.5 | 89.5 | 0.7 | 0.067x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 184.4 | 183.4 | 185.1 | 0.6 | 0.140x | 2.130x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 220.5 | 219.6 | 220.9 | 0.5 | 0.167x | 2.546x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 224.8 | 224.7 | 227.2 | 1.0 | 0.170x | 2.596x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,318.5 | 1,309.2 | 1,328.7 | 6.7 | 1.000x | 15.228x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.8 | 61.4 | 0.2 | 0.069x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 64.9 | 64.8 | 67.2 | 0.9 | 0.074x | 1.062x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.0 | 163.7 | 164.2 | 0.2 | 0.186x | 2.686x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 166.2 | 165.6 | 166.9 | 0.4 | 0.189x | 2.721x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.9 | 867.2 | 884.9 | 6.8 | 0.997x | 14.360x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 879.8 | 865.0 | 881.1 | 6.1 | 1.000x | 14.409x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 120.1 | 119.9 | 122.0 | 0.8 | 0.137x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 123.5 | 123.3 | 123.8 | 0.2 | 0.141x | 1.028x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.2 | 166.1 | 169.0 | 1.0 | 0.191x | 1.392x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 167.7 | 167.4 | 168.4 | 0.4 | 0.191x | 1.396x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 171.5 | 169.8 | 210.1 | 15.6 | 0.196x | 1.428x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 877.0 | 872.0 | 886.0 | 5.8 | 1.000x | 7.300x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.1 | 18.3 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.5 | 20.6 | 0.0 | 0.027x | 1.123x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.2 | 104.4 | 0.1 | 0.139x | 5.698x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.8 | 107.6 | 1.1 | 0.140x | 5.728x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.0 | 731.8 | 758.4 | 8.9 | 1.000x | 40.983x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 750.8 | 741.8 | 754.9 | 4.6 | 1.001x | 41.029x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 0.035x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.2 | 28.2 | 28.3 | 0.0 | 0.037x | 1.082x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 102.0 | 101.8 | 102.1 | 0.1 | 0.135x | 3.911x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 105.4 | 105.4 | 106.9 | 0.7 | 0.140x | 4.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.5 | 122.5 | 124.5 | 0.8 | 0.164x | 4.736x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 753.3 | 745.7 | 754.4 | 3.5 | 1.000x | 28.876x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 30.9 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.8 | 33.2 | 0.2 | 0.025x | 1.067x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 226.3 | 225.8 | 230.4 | 1.7 | 0.169x | 7.320x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 227.5 | 227.2 | 228.9 | 0.6 | 0.169x | 7.360x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,342.6 | 1,332.9 | 1,348.7 | 5.3 | 1.000x | 43.432x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,351.8 | 1,348.6 | 1,360.8 | 4.9 | 1.007x | 43.731x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 55.8 | 55.7 | 56.1 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.9 | 58.8 | 59.0 | 0.1 | 0.044x | 1.056x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.1 | 163.7 | 171.5 | 2.9 | 0.122x | 2.942x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 225.6 | 225.0 | 228.5 | 1.3 | 0.168x | 4.046x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 228.0 | 227.6 | 228.9 | 0.5 | 0.170x | 4.087x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,341.0 | 1,339.3 | 1,349.0 | 3.4 | 1.000x | 24.042x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.5 | 46.9 | 0.2 | 0.048x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.4 | 0.1 | 0.052x | 1.070x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.1 | 167.4 | 168.4 | 0.4 | 0.173x | 3.583x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.7 | 175.7 | 2.3 | 0.175x | 3.622x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 970.7 | 964.5 | 972.0 | 2.8 | 0.998x | 20.695x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.6 | 967.5 | 977.1 | 3.3 | 1.000x | 20.736x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 92.0 | 91.9 | 92.2 | 0.1 | 0.095x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 94.4 | 94.3 | 95.1 | 0.3 | 0.097x | 1.026x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 172.3 | 171.8 | 173.7 | 0.7 | 0.177x | 1.872x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.7 | 171.3 | 180.9 | 3.3 | 0.179x | 1.888x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 177.3 | 176.5 | 178.1 | 0.5 | 0.182x | 1.926x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.5 | 959.3 | 979.6 | 6.7 | 1.000x | 10.566x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 37.8 | 0.5 | 0.042x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.2 | 39.2 | 40.0 | 0.3 | 0.045x | 1.071x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 155.6 | 155.5 | 156.4 | 0.3 | 0.180x | 4.248x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 158.2 | 156.9 | 158.5 | 0.7 | 0.183x | 4.319x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.2 | 854.5 | 872.4 | 6.0 | 0.996x | 23.455x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.5 | 848.8 | 881.0 | 10.3 | 1.000x | 23.547x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.6 | 69.7 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.5 | 73.9 | 0.1 | 0.086x | 1.059x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 149.5 | 148.8 | 150.9 | 0.8 | 0.174x | 2.148x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 153.5 | 152.5 | 153.8 | 0.6 | 0.179x | 2.205x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 157.8 | 157.7 | 158.0 | 0.1 | 0.184x | 2.266x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.4 | 853.9 | 863.0 | 3.3 | 1.000x | 12.344x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.034x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 0.037x | 1.069x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.4 | 147.0 | 157.2 | 4.0 | 0.171x | 4.989x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.5 | 148.8 | 150.2 | 0.5 | 0.174x | 5.059x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 855.1 | 854.3 | 868.6 | 5.6 | 0.995x | 28.942x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.7 | 847.1 | 873.7 | 9.9 | 1.000x | 29.097x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 56.2 | 0.3 | 0.065x | 1.079x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 146.7 | 146.3 | 146.7 | 0.2 | 0.171x | 2.854x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.4 | 147.3 | 147.9 | 0.2 | 0.172x | 2.869x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 150.3 | 149.7 | 151.0 | 0.4 | 0.175x | 2.925x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 858.2 | 849.6 | 864.9 | 5.6 | 1.000x | 16.703x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 30.1 | 0.2 | 0.042x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 0.044x | 1.067x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 106.6 | 104.8 | 106.8 | 0.7 | 0.150x | 3.598x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.2 | 105.3 | 107.7 | 0.8 | 0.151x | 3.618x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 710.7 | 703.7 | 715.5 | 4.1 | 0.999x | 23.993x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.7 | 701.7 | 717.9 | 6.0 | 1.000x | 24.028x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.5 | 51.9 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 54.9 | 56.1 | 0.4 | 0.078x | 1.077x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 102.7 | 102.6 | 102.9 | 0.1 | 0.145x | 1.989x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 102.7 | 102.1 | 102.8 | 0.3 | 0.145x | 1.990x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.3 | 118.4 | 119.7 | 0.5 | 0.168x | 2.311x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 709.6 | 708.2 | 713.2 | 1.7 | 1.000x | 13.745x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 13.4 | 0.6 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.020x | 1.042x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 211.3 | 209.6 | 221.9 | 4.5 | 0.341x | 17.343x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 212.9 | 211.4 | 215.1 | 1.6 | 0.343x | 17.471x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.6 | 609.0 | 614.2 | 2.0 | 0.988x | 50.276x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.0 | 609.9 | 625.0 | 5.0 | 1.000x | 50.880x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 35.2 | 0.3 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.1 | 0.2 | 0.007x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.2 | 433.4 | 440.1 | 2.6 | 0.093x | 12.619x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 2,018.9 | 1,945.7 | 2,063.5 | 48.1 | 0.429x | 58.275x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 2,047.2 | 2,008.0 | 2,086.1 | 27.4 | 0.435x | 59.093x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,706.6 | 4,685.1 | 4,746.1 | 22.6 | 1.000x | 135.857x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.5 | 37.8 | 0.1 | 0.034x | 1.064x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.6 | 200.4 | 201.3 | 0.3 | 0.183x | 5.678x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.3 | 201.6 | 204.2 | 0.9 | 0.186x | 5.756x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,090.9 | 1,084.9 | 1,120.3 | 12.7 | 0.996x | 30.878x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,095.8 | 1,088.7 | 1,099.9 | 4.0 | 1.000x | 31.016x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.4 | 65.3 | 65.7 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.8 | 69.2 | 0.1 | 0.063x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.6 | 170.0 | 174.3 | 1.6 | 0.155x | 2.609x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 206.8 | 205.9 | 206.9 | 0.5 | 0.188x | 3.162x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 207.0 | 206.1 | 209.0 | 1.0 | 0.188x | 3.166x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,100.5 | 1,085.6 | 1,108.0 | 8.6 | 1.000x | 16.831x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.8 | 0.6 | 0.034x | 1.058x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.5 | 200.3 | 201.0 | 0.2 | 0.184x | 5.675x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.7 | 202.3 | 207.5 | 1.7 | 0.187x | 5.765x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,087.4 | 1,080.2 | 1,100.2 | 7.0 | 1.000x | 30.773x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,097.3 | 1,084.6 | 1,106.9 | 7.7 | 1.009x | 31.053x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 66.0 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.9 | 69.3 | 0.2 | 0.063x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.2 | 169.9 | 174.2 | 1.6 | 0.155x | 2.592x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 205.9 | 205.5 | 206.7 | 0.4 | 0.187x | 3.135x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 206.1 | 205.3 | 210.4 | 1.8 | 0.187x | 3.137x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,101.9 | 1,093.7 | 1,110.4 | 5.5 | 1.000x | 16.773x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.5 | 31.8 | 0.1 | 0.037x | 1.074x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 154.7 | 153.9 | 155.1 | 0.4 | 0.178x | 5.230x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 156.9 | 156.2 | 165.4 | 3.5 | 0.181x | 5.304x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 868.0 | 857.9 | 875.6 | 7.3 | 1.000x | 29.343x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.3 | 853.2 | 881.5 | 10.6 | 1.000x | 29.353x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.9 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.3 | 55.2 | 55.7 | 0.2 | 0.064x | 1.076x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.2 | 154.0 | 156.5 | 0.9 | 0.177x | 2.999x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 160.3 | 160.2 | 163.0 | 1.1 | 0.184x | 3.117x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 165.5 | 165.3 | 165.7 | 0.1 | 0.190x | 3.220x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.3 | 861.9 | 881.8 | 7.5 | 1.000x | 16.947x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.8 | 35.8 | 36.0 | 0.1 | 0.034x | 1.062x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.3 | 199.2 | 200.1 | 0.3 | 0.190x | 5.906x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 202.4 | 202.4 | 202.8 | 0.2 | 0.193x | 5.997x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,050.5 | 1,045.1 | 1,057.8 | 4.3 | 1.000x | 31.124x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,059.9 | 1,047.0 | 1,065.3 | 6.7 | 1.009x | 31.402x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.8 | 62.5 | 63.1 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.6 | 0.3 | 0.063x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.6 | 172.9 | 174.0 | 0.4 | 0.164x | 2.766x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 205.3 | 204.3 | 205.7 | 0.5 | 0.194x | 3.271x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 205.6 | 205.0 | 207.1 | 0.7 | 0.195x | 3.276x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.6 | 1,047.9 | 1,069.8 | 8.8 | 1.000x | 16.822x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 10.9 | 13.1 | 0.8 | 0.031x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.6 | 11.7 | 0.1 | 0.032x | 1.048x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.2 | 103.9 | 104.9 | 0.4 | 0.291x | 9.404x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.7 | 105.8 | 106.9 | 0.4 | 0.298x | 9.627x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 358.0 | 354.6 | 363.5 | 3.0 | 1.000x | 32.311x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 362.1 | 357.4 | 363.6 | 2.1 | 1.012x | 32.684x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.7 | 0.2 | 0.011x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 260.9 | 257.9 | 275.4 | 6.5 | 0.109x | 9.957x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,420.0 | 1,347.6 | 1,552.3 | 80.7 | 0.595x | 54.182x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,496.7 | 1,389.6 | 1,513.8 | 45.1 | 0.628x | 57.110x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,384.8 | 2,372.2 | 2,393.7 | 7.9 | 1.000x | 90.998x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 37.3 | 37.6 | 0.1 | 0.034x | 1.063x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.5 | 200.3 | 200.9 | 0.2 | 0.183x | 5.686x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.2 | 201.9 | 204.0 | 0.7 | 0.186x | 5.762x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.6 | 1,084.3 | 1,097.7 | 5.6 | 1.000x | 31.007x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,104.8 | 1,084.9 | 1,118.4 | 11.0 | 1.010x | 31.325x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 66.0 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.8 | 69.2 | 0.2 | 0.063x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.4 | 170.3 | 174.3 | 1.6 | 0.156x | 2.593x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 206.0 | 205.9 | 206.5 | 0.2 | 0.189x | 3.134x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 206.5 | 205.9 | 207.6 | 0.6 | 0.189x | 3.142x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.4 | 1,083.1 | 1,119.1 | 12.3 | 1.000x | 16.604x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 34.5 | 0.3 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.7 | 36.3 | 0.2 | 0.034x | 1.061x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.8 | 199.6 | 207.0 | 2.9 | 0.189x | 5.905x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 202.4 | 202.2 | 203.0 | 0.3 | 0.191x | 5.981x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.9 | 1,049.8 | 1,059.0 | 3.7 | 1.000x | 31.267x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,065.4 | 1,049.8 | 1,067.3 | 6.5 | 1.007x | 31.487x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.8 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.9 | 66.1 | 0.1 | 0.062x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.1 | 172.4 | 173.9 | 0.5 | 0.163x | 2.764x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 205.4 | 204.7 | 206.5 | 0.6 | 0.193x | 3.280x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 205.8 | 205.5 | 206.7 | 0.4 | 0.194x | 3.286x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,061.8 | 1,054.2 | 1,063.1 | 3.2 | 1.000x | 16.953x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.4 | 12.8 | 0.5 | 0.030x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.5 | 12.1 | 0.2 | 0.031x | 1.031x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.5 | 104.2 | 107.4 | 1.0 | 0.273x | 9.094x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.3 | 107.5 | 108.8 | 0.4 | 0.280x | 9.335x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 386.2 | 381.4 | 392.7 | 4.3 | 1.000x | 33.287x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 388.8 | 386.9 | 390.6 | 1.5 | 1.007x | 33.512x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.4 | 27.7 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.8 | 28.1 | 0.1 | 0.011x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 264.0 | 260.1 | 271.3 | 3.8 | 0.104x | 9.532x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,524.3 | 1,511.1 | 1,551.7 | 14.3 | 0.599x | 55.043x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,560.7 | 1,516.3 | 1,585.8 | 23.1 | 0.614x | 56.360x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,543.0 | 2,529.9 | 2,546.0 | 6.0 | 1.000x | 91.829x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.2 | 39.4 | 0.4 | 0.035x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.1 | 41.0 | 41.5 | 0.2 | 0.037x | 1.071x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 223.4 | 223.2 | 233.4 | 4.0 | 0.201x | 5.827x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 227.7 | 226.5 | 230.6 | 1.4 | 0.205x | 5.939x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,111.3 | 1,102.1 | 1,116.1 | 5.1 | 1.000x | 28.982x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,114.8 | 1,104.3 | 1,119.3 | 5.9 | 1.003x | 29.074x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 72.9 | 72.8 | 73.0 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 76.8 | 76.7 | 77.0 | 0.1 | 0.069x | 1.053x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.9 | 174.7 | 177.5 | 1.1 | 0.157x | 2.414x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 212.0 | 211.5 | 214.5 | 1.1 | 0.190x | 2.909x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 212.1 | 211.1 | 212.9 | 0.6 | 0.190x | 2.911x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,117.3 | 1,112.7 | 1,128.4 | 6.4 | 1.000x | 15.331x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.026x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.1 | 0.028x | 1.067x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.5 | 166.7 | 173.2 | 2.3 | 0.148x | 5.689x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 170.3 | 167.9 | 208.4 | 15.7 | 0.149x | 5.750x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,134.5 | 1,163.8 | 9.8 | 1.000x | 38.566x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,138.1 | 1,158.8 | 7.7 | 1.000x | 38.567x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 51.7 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.3 | 56.0 | 0.2 | 0.048x | 1.077x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.6 | 109.4 | 112.5 | 1.3 | 0.095x | 2.129x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 169.5 | 169.4 | 170.0 | 0.2 | 0.148x | 3.292x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 171.0 | 170.9 | 171.0 | 0.0 | 0.149x | 3.321x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,146.2 | 1,159.2 | 4.9 | 1.000x | 22.307x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.4 | 41.8 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.9 | 0.5 | 0.065x | 1.072x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 136.6 | 136.6 | 181.6 | 18.0 | 0.199x | 3.272x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 140.3 | 137.6 | 145.6 | 3.4 | 0.205x | 3.359x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.9 | 682.6 | 690.0 | 2.4 | 1.000x | 16.401x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 686.0 | 675.7 | 692.9 | 5.5 | 1.002x | 16.426x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 79.9 | 80.7 | 0.3 | 0.119x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.6 | 83.2 | 84.0 | 0.3 | 0.123x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 98.1 | 98.5 | 0.1 | 0.145x | 1.221x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 139.7 | 139.6 | 140.0 | 0.2 | 0.206x | 1.734x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 141.2 | 141.0 | 141.6 | 0.2 | 0.208x | 1.753x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.1 | 674.1 | 687.8 | 5.6 | 1.000x | 8.408x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.3 | 37.4 | 0.0 | 0.033x | 1.056x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 169.1 | 168.9 | 216.1 | 18.6 | 0.150x | 4.788x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 168.2 | 174.4 | 2.1 | 0.150x | 4.808x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,129.8 | 1,119.5 | 1,131.9 | 4.6 | 1.000x | 31.984x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,130.3 | 1,121.2 | 1,145.5 | 9.8 | 1.000x | 31.998x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.2 | 65.9 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.8 | 69.4 | 0.2 | 0.061x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.2 | 106.5 | 108.1 | 0.6 | 0.095x | 1.631x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 170.5 | 170.3 | 172.7 | 1.0 | 0.151x | 2.594x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 171.9 | 171.8 | 172.0 | 0.0 | 0.152x | 2.616x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.1 | 1,126.6 | 1,134.3 | 2.7 | 1.000x | 17.184x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.026x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.5 | 31.8 | 0.1 | 0.028x | 1.075x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 172.3 | 172.3 | 219.2 | 18.7 | 0.150x | 5.833x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.1 | 172.7 | 177.7 | 1.9 | 0.151x | 5.857x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,137.8 | 1,154.1 | 5.3 | 0.999x | 38.870x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,149.7 | 1,143.9 | 1,171.8 | 10.6 | 1.000x | 38.912x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.2 | 55.5 | 0.1 | 0.048x | 1.077x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.8 | 108.4 | 114.2 | 2.2 | 0.095x | 2.115x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 173.5 | 173.3 | 173.7 | 0.2 | 0.151x | 3.371x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 174.9 | 174.7 | 175.1 | 0.2 | 0.152x | 3.398x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.7 | 1,141.7 | 1,157.2 | 5.1 | 1.000x | 22.320x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.3 | 0.1 | 0.033x | 1.056x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 175.2 | 175.0 | 223.8 | 19.5 | 0.154x | 4.959x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.9 | 175.5 | 180.4 | 1.8 | 0.155x | 4.980x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,136.6 | 1,132.6 | 1,146.8 | 5.1 | 1.000x | 32.176x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,136.9 | 1,131.5 | 1,154.4 | 8.2 | 1.000x | 32.187x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.1 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.8 | 69.3 | 0.2 | 0.061x | 1.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.6 | 106.4 | 106.9 | 0.2 | 0.094x | 1.621x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 176.0 | 175.6 | 176.2 | 0.2 | 0.155x | 2.675x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 177.4 | 177.1 | 177.6 | 0.2 | 0.156x | 2.697x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.4 | 1,133.5 | 1,147.7 | 5.3 | 1.000x | 17.246x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.4 | 41.9 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.1 | 0.2 | 0.065x | 1.069x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 136.7 | 136.6 | 181.4 | 17.9 | 0.200x | 3.274x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 137.7 | 137.6 | 144.9 | 2.8 | 0.201x | 3.297x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.4 | 675.6 | 684.3 | 3.6 | 0.994x | 16.291x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.8 | 678.3 | 688.0 | 3.3 | 1.000x | 16.396x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.1 | 81.4 | 0.4 | 0.119x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.4 | 83.3 | 84.0 | 0.2 | 0.123x | 1.036x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.4 | 98.2 | 100.9 | 1.0 | 0.145x | 1.222x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 139.6 | 139.6 | 139.8 | 0.1 | 0.206x | 1.733x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 141.1 | 141.1 | 141.4 | 0.1 | 0.208x | 1.752x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.5 | 678.9 | 684.4 | 2.1 | 1.000x | 8.434x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 42.4 | 0.3 | 0.039x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.5 | 44.7 | 0.0 | 0.041x | 1.069x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 170.4 | 168.2 | 215.2 | 18.0 | 0.158x | 4.085x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.0 | 170.9 | 175.6 | 1.9 | 0.159x | 4.100x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.9 | 1,067.5 | 1,083.2 | 5.1 | 0.996x | 25.748x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.9 | 1,060.7 | 1,091.5 | 11.7 | 1.000x | 25.846x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.3 | 81.4 | 0.4 | 0.075x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 83.5 | 83.3 | 84.8 | 0.6 | 0.077x | 1.037x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.3 | 104.1 | 104.4 | 0.1 | 0.097x | 1.295x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 171.4 | 171.2 | 171.6 | 0.2 | 0.159x | 2.129x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 172.9 | 172.7 | 211.4 | 15.4 | 0.160x | 2.147x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.2 | 1,072.2 | 1,083.9 | 3.9 | 1.000x | 13.388x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.7 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.006x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194.2 | 184.8 | 195.5 | 3.9 | 0.247x | 14.664x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 196.1 | 191.1 | 199.8 | 3.2 | 0.249x | 14.808x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 775.2 | 784.0 | 2.8 | 0.991x | 58.829x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 786.1 | 779.8 | 788.9 | 3.2 | 1.000x | 59.358x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.0 | 22.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 22.4 | 22.1 | 22.5 | 0.2 | 0.008x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.1 | 213.5 | 236.8 | 8.2 | 0.082x | 9.814x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 959.2 | 901.2 | 1,268.1 | 135.6 | 0.359x | 42.973x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 960.5 | 892.1 | 997.0 | 36.3 | 0.359x | 43.030x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.2 | 2,664.8 | 2,724.5 | 21.9 | 1.000x | 119.712x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.9 | 0.3 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.017x | 1.016x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 191.9 | 189.6 | 192.7 | 1.1 | 0.243x | 14.510x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194.8 | 190.3 | 197.1 | 2.5 | 0.246x | 14.723x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.5 | 771.4 | 783.5 | 4.1 | 0.987x | 59.001x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.5 | 778.9 | 809.5 | 10.9 | 1.000x | 59.754x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 45.5 | 45.2 | 45.9 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 45.7 | 45.6 | 45.8 | 0.1 | 0.017x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 235.0 | 229.5 | 236.2 | 2.4 | 0.088x | 5.165x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.5 | 2,654.4 | 2,701.7 | 16.5 | 1.000x | 58.535x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 3,261.6 | 3,149.8 | 3,326.2 | 58.2 | 1.225x | 71.677x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 3,274.2 | 3,187.9 | 3,337.5 | 56.5 | 1.229x | 71.955x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.7 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194.5 | 184.4 | 206.1 | 7.0 | 0.250x | 14.659x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 195.6 | 192.7 | 201.4 | 2.9 | 0.251x | 14.738x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.3 | 774.4 | 792.8 | 7.0 | 1.000x | 58.653x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.9 | 773.4 | 781.0 | 2.7 | 1.002x | 58.774x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.1 | 22.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 22.7 | 0.1 | 0.008x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 214.4 | 220.1 | 2.1 | 0.082x | 9.908x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 850.0 | 791.2 | 892.1 | 36.9 | 0.319x | 38.482x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 925.6 | 826.8 | 945.6 | 45.2 | 0.347x | 41.905x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.6 | 2,657.4 | 2,687.5 | 10.9 | 1.000x | 120.772x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.7 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.3 | 0.0 | 0.017x | 1.005x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 191.0 | 189.5 | 191.7 | 0.8 | 0.244x | 14.415x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.4 | 191.1 | 194.9 | 1.4 | 0.247x | 14.597x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.6 | 771.1 | 782.9 | 4.1 | 0.996x | 58.748x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.7 | 777.5 | 789.0 | 3.8 | 1.000x | 58.987x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.1 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 29.7 | 29.4 | 29.9 | 0.2 | 0.011x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.8 | 229.1 | 235.8 | 2.5 | 0.088x | 7.882x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,450.7 | 1,351.3 | 1,512.1 | 59.3 | 0.544x | 48.915x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,511.0 | 1,372.2 | 1,617.5 | 78.8 | 0.566x | 50.945x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.5 | 2,648.2 | 2,674.4 | 8.9 | 1.000x | 89.940x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 0.017x | 1.006x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 298.4 | 288.0 | 308.9 | 7.5 | 0.322x | 18.556x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.3 | 287.4 | 311.4 | 8.8 | 0.325x | 18.738x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 921.5 | 918.9 | 931.7 | 5.0 | 0.995x | 57.309x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 925.8 | 919.6 | 931.8 | 4.1 | 1.000x | 57.576x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.7 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 31.0 | 1.9 | 0.008x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.9 | 316.3 | 324.4 | 3.0 | 0.098x | 12.250x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,741.8 | 1,734.3 | 1,756.6 | 8.3 | 0.533x | 66.276x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,749.6 | 1,732.5 | 1,775.6 | 14.5 | 0.535x | 66.575x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,270.2 | 3,237.5 | 3,336.2 | 32.9 | 1.000x | 124.435x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 15.9 | 16.1 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.018x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.3 | 286.9 | 304.0 | 7.0 | 0.335x | 18.246x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 310.0 | 279.9 | 312.9 | 12.2 | 0.355x | 19.288x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 874.2 | 871.2 | 880.7 | 3.3 | 1.000x | 54.391x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 875.4 | 869.8 | 880.2 | 3.5 | 1.001x | 54.470x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 39.0 | 5.1 | 0.009x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 322.4 | 315.7 | 336.2 | 7.0 | 0.106x | 12.337x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,729.9 | 1,668.7 | 1,747.9 | 28.1 | 0.570x | 66.204x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,741.2 | 1,721.9 | 1,762.9 | 13.5 | 0.574x | 66.639x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,032.6 | 3,026.0 | 3,039.4 | 5.6 | 1.000x | 116.063x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.4 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.016x | 1.002x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.3 | 145.0 | 151.8 | 2.5 | 0.117x | 7.303x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.0 | 155.1 | 3.3 | 0.118x | 7.358x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,254.6 | 1,246.1 | 1,280.1 | 12.6 | 1.000x | 62.198x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,254.9 | 1,244.7 | 1,268.0 | 7.8 | 1.000x | 62.213x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.1 | 19.1 | 32.7 | 5.5 | 0.004x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.3 | 19.1 | 19.5 | 0.1 | 0.004x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.1 | 381.6 | 392.8 | 4.2 | 0.084x | 20.240x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 630.8 | 612.7 | 743.7 | 47.6 | 0.136x | 32.984x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 683.6 | 611.9 | 697.8 | 35.9 | 0.148x | 35.747x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,621.5 | 4,601.2 | 4,628.4 | 11.8 | 1.000x | 241.662x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.014x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 24.3 | 0.5 | 0.015x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 479.9 | 472.2 | 497.1 | 8.9 | 0.302x | 20.841x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 487.8 | 487.2 | 493.3 | 2.2 | 0.307x | 21.186x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,581.8 | 1,579.2 | 1,643.6 | 24.4 | 0.995x | 68.695x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,589.1 | 1,573.4 | 1,592.3 | 6.7 | 1.000x | 69.012x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.4 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 25.6 | 25.2 | 37.2 | 4.7 | 0.004x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 477.9 | 474.7 | 501.6 | 11.0 | 0.081x | 18.887x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,762.8 | 1,750.8 | 1,791.5 | 14.0 | 0.300x | 69.669x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,766.9 | 1,756.1 | 1,772.1 | 5.4 | 0.301x | 69.831x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,867.4 | 5,866.0 | 5,911.6 | 19.5 | 1.000x | 231.887x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 13.0 | 0.4 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.9 | 0.2 | 0.020x | 1.035x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.4 | 144.2 | 145.9 | 0.6 | 0.231x | 11.932x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.6 | 147.4 | 151.0 | 1.2 | 0.238x | 12.279x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.9 | 626.0 | 639.5 | 5.5 | 1.000x | 51.612x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.8 | 630.9 | 643.0 | 4.2 | 1.008x | 52.008x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 38.4 | 4.6 | 0.013x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.2 | 0.1 | 0.013x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 194.0 | 187.9 | 195.1 | 2.6 | 0.093x | 7.238x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,469.0 | 1,423.6 | 1,617.1 | 73.4 | 0.707x | 54.815x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,484.1 | 1,400.1 | 1,597.3 | 65.1 | 0.714x | 55.381x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,077.7 | 2,061.7 | 2,099.7 | 12.7 | 1.000x | 77.531x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.7 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.7 | 14.8 | 0.1 | 0.017x | 1.011x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 207.7 | 207.3 | 208.8 | 0.5 | 0.245x | 14.258x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 211.1 | 208.0 | 213.9 | 1.9 | 0.249x | 14.490x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 846.0 | 839.5 | 847.9 | 3.4 | 0.997x | 58.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 848.6 | 843.5 | 854.9 | 4.0 | 1.000x | 58.250x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.7 | 20.9 | 0.0 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.9 | 34.6 | 5.4 | 0.007x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 282.8 | 279.5 | 306.2 | 10.0 | 0.097x | 13.579x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,323.9 | 1,299.4 | 1,341.9 | 14.8 | 0.454x | 63.576x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,343.2 | 1,321.7 | 1,351.7 | 10.2 | 0.461x | 64.501x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,914.4 | 2,902.0 | 2,937.3 | 12.3 | 1.000x | 139.952x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.2 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.023x | 1.004x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 473.7 | 463.6 | 521.4 | 24.8 | 0.471x | 20.578x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 488.5 | 472.3 | 520.6 | 17.4 | 0.485x | 21.219x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,006.6 | 994.3 | 1,029.1 | 11.3 | 1.000x | 43.727x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,009.0 | 1,002.1 | 1,021.5 | 6.3 | 1.002x | 43.832x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 38.4 | 4.6 | 0.007x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.4 | 0.2 | 0.007x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.0 | 561.9 | 576.0 | 4.8 | 0.158x | 21.116x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 2,837.3 | 2,830.1 | 2,861.3 | 11.3 | 0.789x | 105.291x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 2,879.1 | 2,874.2 | 2,880.7 | 2.7 | 0.801x | 106.846x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,594.7 | 3,549.9 | 3,615.4 | 25.2 | 1.000x | 133.399x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.6 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.0 | 0.1 | 0.032x | 1.046x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.9 | 104.5 | 109.7 | 1.8 | 0.281x | 9.232x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.9 | 104.9 | 107.2 | 0.8 | 0.281x | 9.233x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 376.5 | 374.4 | 379.8 | 1.8 | 0.999x | 32.827x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 377.0 | 375.5 | 381.6 | 2.1 | 1.000x | 32.872x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.5 | 0.1 | 0.040x | 1.055x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 209.5 | 208.6 | 211.7 | 1.0 | 0.135x | 3.548x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 298.2 | 297.5 | 298.5 | 0.3 | 0.193x | 5.051x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 298.6 | 298.3 | 300.2 | 0.7 | 0.193x | 5.059x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,547.8 | 1,538.0 | 1,562.7 | 9.8 | 1.000x | 26.217x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 0.788x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 0.789x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 33.7 | 0.4 | 1.000x | 1.268x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.0 | 33.3 | 35.0 | 0.5 | 1.029x | 1.306x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.4 | 255.7 | 265.3 | 3.6 | 7.773x | 9.859x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 256.9 | 255.9 | 269.5 | 5.2 | 7.788x | 9.878x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.7 | 23.7 | 23.8 | 0.1 | 0.696x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 24.1 | 23.8 | 25.2 | 0.5 | 0.707x | 1.016x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 33.9 | 35.1 | 0.4 | 1.000x | 1.437x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 44.4 | 0.0 | 1.301x | 1.870x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,703.9 | 1,682.7 | 1,725.4 | 14.2 | 49.979x | 71.824x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,808.4 | 1,730.1 | 1,860.2 | 44.8 | 53.043x | 76.228x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.1 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.2 | 0.3 | 0.065x | 1.054x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.7 | 48.2 | 0.2 | 0.296x | 4.822x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.5 | 49.3 | 245.4 | 78.0 | 0.305x | 4.962x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.2 | 161.1 | 164.0 | 0.9 | 1.000x | 16.269x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.9 | 161.6 | 167.7 | 2.1 | 1.004x | 16.336x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.6 | 19.0 | 0.1 | 0.106x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.6 | 19.0 | 0.1 | 0.106x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.6 | 54.7 | 0.0 | 0.309x | 2.922x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 177.1 | 177.0 | 179.9 | 1.3 | 1.000x | 9.468x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 970.9 | 885.3 | 1,047.9 | 59.3 | 5.482x | 51.905x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 991.6 | 952.8 | 1,013.1 | 20.9 | 5.599x | 53.010x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.0 | 13.5 | 0.2 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.2 | 13.3 | 14.6 | 0.4 | 0.023x | 1.075x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 96.3 | 99.0 | 0.9 | 0.160x | 7.379x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 97.8 | 95.6 | 98.0 | 1.0 | 0.161x | 7.423x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 608.9 | 607.3 | 617.2 | 3.8 | 1.000x | 46.209x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 611.9 | 604.7 | 614.7 | 3.5 | 1.005x | 46.438x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.1 | 0.1 | 0.019x | 1.043x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.5 | 85.0 | 0.5 | 0.135x | 7.313x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 169.3 | 168.8 | 174.0 | 1.9 | 0.271x | 14.707x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 184.8 | 181.7 | 189.6 | 3.3 | 0.296x | 16.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 624.7 | 620.6 | 627.7 | 2.5 | 1.000x | 54.253x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.5 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.9 | 12.6 | 13.0 | 0.1 | 0.022x | 1.054x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.2 | 144.6 | 153.4 | 3.2 | 0.254x | 11.969x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.5 | 146.7 | 152.7 | 2.3 | 0.256x | 12.077x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.2 | 571.8 | 582.2 | 3.7 | 1.000x | 47.111x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 575.5 | 574.1 | 594.4 | 7.7 | 1.000x | 47.127x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 71.1 | 71.0 | 71.1 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.3 | 73.8 | 0.2 | 0.026x | 1.037x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 292.5 | 290.5 | 293.0 | 1.0 | 0.105x | 4.117x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 733.9 | 700.2 | 748.7 | 19.8 | 0.263x | 10.328x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 737.1 | 715.0 | 774.3 | 19.8 | 0.264x | 10.373x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,793.1 | 2,776.7 | 2,800.6 | 8.7 | 1.000x | 39.306x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.7 | 10.3 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 0.065x | 1.034x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.9 | 56.9 | 3.6 | 0.298x | 4.761x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.6 | 48.9 | 49.8 | 0.3 | 0.308x | 4.914x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 161.1 | 159.1 | 166.5 | 2.5 | 1.000x | 15.951x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.5 | 161.7 | 166.1 | 1.6 | 1.009x | 16.089x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 62.2 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 64.1 | 64.1 | 64.4 | 0.1 | 0.063x | 1.036x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.3 | 157.8 | 160.1 | 0.9 | 0.156x | 2.558x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 162.9 | 162.7 | 164.0 | 0.5 | 0.161x | 2.632x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 165.0 | 164.7 | 165.5 | 0.3 | 0.163x | 2.665x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.3 | 1,007.7 | 1,027.6 | 6.8 | 1.000x | 16.387x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.5 | 13.0 | 0.1 | 0.022x | 1.052x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.1 | 144.5 | 154.7 | 3.9 | 0.253x | 12.032x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.1 | 148.3 | 153.4 | 1.9 | 0.258x | 12.281x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.8 | 571.6 | 580.1 | 3.3 | 0.993x | 47.180x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.0 | 569.8 | 577.4 | 2.9 | 1.000x | 47.531x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 25.7 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 26.2 | 0.2 | 0.013x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 199.6 | 187.5 | 200.0 | 4.9 | 0.100x | 7.808x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,456.5 | 1,310.5 | 1,560.0 | 85.4 | 0.732x | 56.966x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,503.4 | 1,396.3 | 1,560.3 | 65.5 | 0.756x | 58.801x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,989.4 | 1,956.6 | 1,997.6 | 14.6 | 1.000x | 77.809x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.9 | 0.1 | 0.022x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 22.0 | 0.1 | 0.022x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 364.3 | 361.2 | 372.4 | 4.1 | 0.363x | 16.784x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 375.2 | 341.1 | 404.0 | 20.7 | 0.374x | 17.285x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.5 | 990.6 | 1,013.8 | 8.5 | 0.994x | 46.003x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,004.2 | 989.0 | 1,018.7 | 10.9 | 1.000x | 46.267x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.1 | 18.8 | 19.3 | 0.2 | 0.005x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.0 | 19.9 | 20.3 | 0.2 | 0.006x | 1.045x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 533.5 | 528.2 | 537.1 | 2.9 | 0.151x | 27.893x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,727.2 | 1,699.4 | 1,742.6 | 16.2 | 0.490x | 90.311x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,729.0 | 1,708.7 | 1,741.7 | 12.7 | 0.490x | 90.402x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,525.7 | 3,516.8 | 3,538.9 | 7.1 | 1.000x | 184.348x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.014x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.014x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 144.7 | 155.5 | 4.0 | 0.090x | 6.316x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 147.5 | 151.7 | 1.5 | 0.092x | 6.482x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,614.4 | 1,603.2 | 1,635.6 | 10.7 | 0.998x | 70.084x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,617.7 | 1,603.4 | 1,628.1 | 9.7 | 1.000x | 70.226x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.4 | 20.6 | 0.1 | 0.003x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 20.8 | 0.1 | 0.003x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 466.5 | 464.0 | 471.2 | 2.4 | 0.077x | 22.849x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 751.3 | 692.9 | 804.6 | 37.4 | 0.124x | 36.795x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 817.8 | 700.5 | 824.3 | 46.6 | 0.135x | 40.052x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,063.9 | 6,004.3 | 6,176.9 | 61.1 | 1.000x | 296.989x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 106.6 | 104.6 | 112.9 | 2.9 | 0.138x | 8.085x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.1 | 105.8 | 111.7 | 2.0 | 0.140x | 8.198x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 774.2 | 773.1 | 784.9 | 5.2 | 1.000x | 58.724x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.0 | 775.8 | 792.8 | 6.3 | 1.005x | 59.009x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 12.5 | 0.2 | 0.006x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 12.8 | 12.5 | 13.4 | 0.3 | 0.006x | 1.058x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 183.1 | 181.3 | 186.4 | 1.8 | 0.090x | 15.084x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 302.7 | 301.1 | 321.0 | 7.6 | 0.149x | 24.937x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 332.1 | 312.2 | 362.2 | 17.4 | 0.164x | 27.360x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,027.1 | 2,020.1 | 2,096.4 | 33.4 | 1.000x | 167.013x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 11.9 | 0.1 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.023x | 1.058x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.5 | 127.5 | 135.2 | 2.8 | 0.237x | 11.016x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 131.3 | 130.1 | 135.5 | 2.0 | 0.242x | 11.253x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.8 | 540.1 | 578.0 | 14.5 | 1.000x | 46.449x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 549.6 | 546.1 | 556.3 | 3.6 | 1.014x | 47.116x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.2 | 68.8 | 0.2 | 0.027x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.8 | 72.4 | 0.2 | 0.028x | 1.050x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 271.3 | 270.7 | 274.6 | 1.8 | 0.106x | 3.953x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 597.8 | 587.1 | 600.2 | 4.7 | 0.234x | 8.709x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 602.4 | 554.4 | 613.6 | 20.7 | 0.235x | 8.776x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,559.3 | 2,541.1 | 2,580.9 | 13.4 | 1.000x | 37.285x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.7 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.019x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.4 | 214.9 | 304.6 | 30.8 | 0.321x | 16.869x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 246.1 | 221.9 | 287.3 | 24.3 | 0.321x | 16.917x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 765.4 | 762.2 | 802.1 | 14.8 | 1.000x | 52.608x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 765.8 | 763.2 | 772.6 | 3.6 | 1.000x | 52.633x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 54.0 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 56.9 | 56.7 | 57.1 | 0.1 | 0.016x | 1.058x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 378.3 | 372.4 | 381.5 | 3.4 | 0.107x | 7.033x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,019.2 | 996.7 | 1,033.7 | 14.3 | 0.290x | 18.948x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,027.7 | 1,010.9 | 1,047.2 | 13.8 | 0.292x | 19.108x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,519.7 | 3,513.1 | 3,537.6 | 8.7 | 1.000x | 65.438x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.5 | 12.0 | 0.2 | 0.022x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.3 | 0.0 | 0.022x | 1.042x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.5 | 128.1 | 133.9 | 2.2 | 0.235x | 10.924x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 132.1 | 129.7 | 134.9 | 1.9 | 0.242x | 11.227x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.6 | 538.1 | 547.8 | 3.6 | 1.000x | 46.468x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.6 | 545.3 | 552.4 | 2.7 | 1.004x | 46.635x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 69.0 | 68.7 | 69.2 | 0.2 | 0.027x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.9 | 72.3 | 0.2 | 0.028x | 1.045x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.3 | 270.8 | 283.7 | 4.6 | 0.107x | 3.962x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 593.4 | 590.9 | 619.5 | 10.8 | 0.231x | 8.605x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 595.9 | 570.6 | 599.3 | 10.8 | 0.232x | 8.641x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,564.9 | 2,544.1 | 2,577.3 | 10.9 | 1.000x | 37.191x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.2 | 0.4 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.3 | 13.8 | 0.2 | 0.017x | 1.015x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.0 | 146.1 | 151.2 | 1.8 | 0.189x | 11.095x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.0 | 144.7 | 155.0 | 3.7 | 0.189x | 11.097x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.2 | 766.6 | 785.4 | 8.1 | 1.000x | 58.653x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 787.0 | 773.9 | 792.2 | 6.5 | 1.013x | 59.388x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.8 | 19.5 | 19.9 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.8 | 20.1 | 0.2 | 0.007x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.3 | 213.4 | 228.1 | 4.9 | 0.082x | 11.121x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 662.9 | 600.7 | 705.8 | 41.9 | 0.247x | 33.467x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 721.1 | 616.2 | 749.6 | 48.8 | 0.268x | 36.409x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.4 | 2,658.3 | 2,692.7 | 12.7 | 1.000x | 135.684x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.2 | 0.017x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 143.7 | 155.2 | 4.0 | 0.188x | 11.036x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.6 | 147.0 | 154.4 | 2.6 | 0.193x | 11.318x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.4 | 769.5 | 787.0 | 5.9 | 1.000x | 58.739x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 770.3 | 799.3 | 11.3 | 1.003x | 58.937x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.9 | 0.2 | 0.005x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.5 | 14.4 | 14.8 | 0.2 | 0.005x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.9 | 215.0 | 221.4 | 2.3 | 0.082x | 15.107x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 550.4 | 526.8 | 697.4 | 63.5 | 0.207x | 38.159x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 629.4 | 545.2 | 691.9 | 47.9 | 0.236x | 43.638x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.7 | 2,651.0 | 2,690.4 | 13.7 | 1.000x | 184.671x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.1 | 145.4 | 153.2 | 2.8 | 0.191x | 11.085x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.6 | 146.9 | 151.5 | 1.8 | 0.194x | 11.271x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.8 | 763.4 | 784.8 | 7.5 | 1.000x | 58.161x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.1 | 770.5 | 785.3 | 5.5 | 1.013x | 58.938x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.3 | 14.2 | 14.4 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.9 | 0.2 | 0.005x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.5 | 215.3 | 220.7 | 2.0 | 0.082x | 15.175x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 595.9 | 526.1 | 693.9 | 64.7 | 0.224x | 41.577x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 639.9 | 556.0 | 703.0 | 47.8 | 0.241x | 44.645x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,660.0 | 2,652.5 | 2,670.4 | 6.1 | 1.000x | 185.590x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.9 | 0.2 | 0.017x | 1.006x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.6 | 145.4 | 150.8 | 1.9 | 0.190x | 11.073x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.8 | 144.4 | 149.8 | 2.0 | 0.190x | 11.084x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 772.1 | 770.4 | 781.3 | 4.7 | 1.000x | 58.316x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.5 | 772.8 | 787.2 | 4.7 | 1.008x | 58.795x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.3 | 14.3 | 14.4 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.4 | 0.1 | 0.005x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 214.2 | 211.5 | 220.0 | 3.2 | 0.080x | 14.952x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 592.0 | 522.6 | 660.8 | 53.3 | 0.222x | 41.312x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 600.3 | 542.2 | 655.0 | 39.5 | 0.225x | 41.893x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.4 | 2,641.5 | 2,686.6 | 14.6 | 1.000x | 186.083x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.8 | 0.2 | 0.017x | 1.007x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 143.5 | 155.4 | 4.1 | 0.188x | 10.992x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.6 | 147.2 | 150.5 | 1.2 | 0.192x | 11.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.8 | 767.3 | 785.3 | 5.9 | 1.000x | 58.410x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.0 | 778.1 | 819.8 | 16.0 | 1.008x | 58.878x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.8 | 0.3 | 0.006x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.6 | 16.4 | 17.1 | 0.3 | 0.006x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.6 | 209.8 | 221.9 | 4.5 | 0.082x | 13.403x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 536.8 | 526.6 | 666.3 | 64.0 | 0.201x | 32.921x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 616.7 | 568.2 | 657.7 | 31.4 | 0.231x | 37.817x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,674.0 | 2,643.3 | 2,679.8 | 13.6 | 1.000x | 163.983x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,745.9 | 7,738.4 | 7,790.2 | 19.4 | 0.762x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,749.4 | 7,745.0 | 7,756.2 | 3.7 | 0.762x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,167.1 | 10,130.0 | 10,215.3 | 28.3 | 1.000x | 1.313x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,206.4 | 10,113.3 | 10,239.2 | 44.8 | 1.004x | 1.318x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,070.0 | 19,067.1 | 19,075.8 | 3.3 | 1.876x | 2.462x |
| 6 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,081.1 | 19,078.9 | 19,086.9 | 2.9 | 1.877x | 2.463x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,464.2 | 7,461.4 | 7,620.5 | 62.9 | 0.041x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,466.4 | 7,465.9 | 7,468.5 | 1.1 | 0.041x | 1.000x | 5 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,179.8 | 28,990.6 | 29,201.7 | 78.1 | 0.161x | 3.909x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 181,474.8 | 180,540.0 | 186,600.1 | 2,137.3 | 1.000x | 24.313x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 181,728.2 | 180,968.3 | 183,515.5 | 889.0 | 1.001x | 24.347x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,550.5 | 9,549.3 | 9,557.8 | 3.1 | 0.033x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,556.6 | 9,555.2 | 9,578.7 | 8.9 | 0.033x | 1.001x | 5 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,154.8 | 71,883.0 | 73,275.2 | 601.0 | 0.248x | 7.555x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290,683.7 | 289,035.8 | 293,222.9 | 1,369.0 | 0.999x | 30.436x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 290,975.4 | 289,240.3 | 291,726.3 | 875.3 | 1.000x | 30.467x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,047.2 | 19,041.4 | 19,054.1 | 4.3 | 0.022x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,058.2 | 19,052.9 | 19,058.7 | 2.3 | 0.022x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194,185.2 | 194,072.3 | 204,946.7 | 4,278.6 | 0.227x | 10.195x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,364.9 | 193,853.4 | 220,653.9 | 10,564.8 | 0.228x | 10.204x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853,818.0 | 846,089.0 | 884,443.3 | 16,079.4 | 1.000x | 44.826x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856,424.9 | 843,206.8 | 891,748.0 | 17,490.2 | 1.003x | 44.963x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,738.1 | 3,735.2 | 3,740.5 | 1.8 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,741.8 | 3,739.7 | 3,742.8 | 1.1 | 0.052x | 1.001x | 5 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,980.5 | 10,949.7 | 11,026.1 | 24.5 | 0.152x | 2.937x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,436.0 | 71,551.3 | 73,986.6 | 791.3 | 1.000x | 19.378x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73,033.2 | 71,908.1 | 74,142.9 | 802.6 | 1.008x | 19.538x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 17.1 | 0.4 | 0.018x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.018x | 1.007x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 299.9 | 284.9 | 309.2 | 7.9 | 0.341x | 18.615x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 310.5 | 296.6 | 321.8 | 9.8 | 0.353x | 19.273x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.5 | 874.3 | 904.1 | 13.2 | 1.000x | 54.534x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 904.1 | 874.6 | 941.5 | 22.2 | 1.029x | 56.123x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,787.8 | 4,784.4 | 4,788.6 | 1.5 | 0.023x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,791.6 | 4,788.6 | 4,807.4 | 6.8 | 0.023x | 1.001x | 5 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99,310.0 | 93,823.6 | 100,357.4 | 2,811.4 | 0.469x | 20.742x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211,624.0 | 211,459.2 | 213,818.0 | 912.0 | 1.000x | 44.201x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,821.7 | 211,105.6 | 215,922.3 | 1,579.6 | 1.006x | 44.451x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,645.4 | 7,643.8 | 7,649.2 | 1.9 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,651.0 | 7,649.2 | 7,651.8 | 0.9 | 0.052x | 1.001x | 5 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,715.8 | 32,654.9 | 32,876.9 | 76.5 | 0.220x | 4.279x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 148,371.8 | 148,032.4 | 149,375.9 | 456.4 | 1.000x | 19.407x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,600.9 | 147,906.3 | 150,185.6 | 811.3 | 1.002x | 19.437x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.2 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 0.064x | 1.047x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.6 | 57.0 | 3.6 | 0.296x | 4.839x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.3 | 48.8 | 49.7 | 0.3 | 0.303x | 4.963x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.5 | 161.0 | 167.3 | 2.2 | 1.000x | 16.364x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.1 | 162.0 | 168.9 | 2.4 | 1.016x | 16.621x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.4 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.0 | 21.3 | 0.1 | 0.013x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.8 | 141.4 | 142.5 | 0.4 | 0.088x | 6.665x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,180.1 | 1,170.4 | 1,288.4 | 44.3 | 0.730x | 55.477x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,195.8 | 1,108.0 | 1,255.6 | 53.4 | 0.740x | 56.216x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,616.9 | 1,602.1 | 1,626.3 | 7.8 | 1.000x | 76.007x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 34.1 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.3 | 36.0 | 36.8 | 0.3 | 0.034x | 1.076x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.5 | 199.3 | 209.9 | 4.2 | 0.187x | 5.920x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 202.2 | 202.1 | 202.9 | 0.3 | 0.189x | 6.002x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.2 | 1,057.1 | 1,077.7 | 6.5 | 1.000x | 31.675x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,071.4 | 1,055.1 | 1,089.6 | 11.0 | 1.004x | 31.799x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.1 | 66.2 | 0.4 | 0.062x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.8 | 172.3 | 174.2 | 0.7 | 0.162x | 2.759x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 205.7 | 205.5 | 206.4 | 0.4 | 0.193x | 3.286x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 205.8 | 205.1 | 207.9 | 1.0 | 0.193x | 3.287x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.5 | 1,058.4 | 1,078.4 | 7.8 | 1.000x | 17.049x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.3 | 34.8 | 0.2 | 0.034x | 1.067x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 175.1 | 174.7 | 179.5 | 1.8 | 0.174x | 5.427x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.2 | 175.9 | 177.6 | 0.6 | 0.176x | 5.462x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,003.9 | 997.4 | 1,012.1 | 4.8 | 1.000x | 31.120x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,008.2 | 1,001.2 | 1,021.6 | 6.7 | 1.004x | 31.255x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 63.0 | 0.4 | 0.062x | 1.075x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.6 | 157.9 | 160.8 | 1.1 | 0.158x | 2.739x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 167.5 | 166.9 | 168.2 | 0.4 | 0.166x | 2.874x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 170.3 | 169.9 | 172.4 | 0.9 | 0.168x | 2.922x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,010.9 | 1,002.4 | 1,013.2 | 3.8 | 1.000x | 17.346x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.7 | 16.7 | 16.8 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.3 | 0.1 | 0.028x | 1.139x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.4 | 75.6 | 80.3 | 1.7 | 0.112x | 4.564x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.1 | 76.8 | 82.1 | 2.0 | 0.113x | 4.606x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 681.3 | 690.2 | 3.5 | 1.000x | 40.740x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 687.9 | 678.3 | 702.4 | 8.7 | 1.009x | 41.096x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 23.4 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.4 | 26.6 | 0.5 | 0.037x | 1.096x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 81.9 | 81.7 | 82.2 | 0.2 | 0.120x | 3.531x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 84.2 | 84.2 | 85.6 | 0.5 | 0.123x | 3.631x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 109.3 | 2.1 | 0.152x | 4.489x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.2 | 681.2 | 690.1 | 2.9 | 1.000x | 29.500x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 12.3 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.8 | 0.1 | 0.020x | 1.047x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.7 | 145.1 | 150.6 | 2.1 | 0.229x | 11.982x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.0 | 146.8 | 149.3 | 0.9 | 0.234x | 12.252x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.6 | 633.0 | 642.3 | 3.2 | 1.000x | 52.338x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.4 | 630.9 | 663.8 | 12.7 | 1.001x | 52.407x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.1 | 27.6 | 0.2 | 0.012x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 27.2 | 27.0 | 27.3 | 0.1 | 0.012x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.3 | 203.3 | 204.7 | 0.5 | 0.091x | 7.507x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,386.8 | 1,358.3 | 1,492.8 | 48.5 | 0.620x | 51.204x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,395.9 | 1,291.6 | 1,466.5 | 60.6 | 0.624x | 51.538x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,235.9 | 2,223.6 | 2,246.5 | 7.9 | 1.000x | 82.553x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.2 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.5 | 0.2 | 0.035x | 1.075x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 142.0 | 140.9 | 168.0 | 10.6 | 0.166x | 5.059x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 143.6 | 142.5 | 144.1 | 0.6 | 0.168x | 5.119x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853.5 | 845.8 | 870.3 | 9.2 | 1.000x | 30.416x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 865.2 | 846.2 | 884.5 | 13.0 | 1.014x | 30.834x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 48.5 | 48.4 | 49.6 | 0.5 | 0.057x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.9 | 51.8 | 52.1 | 0.1 | 0.061x | 1.070x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 144.5 | 144.1 | 145.0 | 0.3 | 0.170x | 2.979x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.8 | 147.4 | 148.8 | 0.5 | 0.174x | 3.046x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 148.9 | 148.6 | 149.4 | 0.3 | 0.175x | 3.068x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 849.3 | 843.4 | 854.4 | 3.7 | 1.000x | 17.502x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.2 | 55.8 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.7 | 61.3 | 0.6 | 0.069x | 1.077x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 157.3 | 156.5 | 183.4 | 10.6 | 0.181x | 2.831x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.1 | 158.5 | 159.4 | 0.3 | 0.183x | 2.864x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.6 | 857.3 | 873.0 | 5.5 | 1.000x | 15.632x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.1 | 864.3 | 890.4 | 9.6 | 1.009x | 15.767x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 110.5 | 0.4 | 0.125x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 112.9 | 112.8 | 113.3 | 0.2 | 0.128x | 1.031x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 159.9 | 159.5 | 160.7 | 0.4 | 0.182x | 1.460x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 164.4 | 163.8 | 165.3 | 0.5 | 0.187x | 1.500x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.7 | 163.8 | 165.8 | 0.8 | 0.187x | 1.504x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.9 | 868.1 | 887.8 | 6.4 | 1.000x | 8.023x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.6 | 43.0 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.5 | 43.0 | 0.1 | 0.019x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 739.7 | 736.5 | 743.8 | 2.4 | 0.333x | 17.312x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,054.9 | 1,044.3 | 1,071.9 | 9.8 | 0.476x | 24.689x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,218.2 | 2,206.5 | 2,255.4 | 18.6 | 1.000x | 51.915x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,232.4 | 2,215.9 | 2,275.5 | 21.7 | 1.006x | 52.246x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.2 | 89.5 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 93.0 | 92.9 | 93.2 | 0.1 | 0.030x | 1.040x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.1 | 404.3 | 409.5 | 1.8 | 0.131x | 4.552x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 916.1 | 915.4 | 919.7 | 1.6 | 0.294x | 10.243x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,256.7 | 1,233.2 | 1,267.3 | 11.4 | 0.404x | 14.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,113.9 | 3,110.2 | 3,161.3 | 19.7 | 1.000x | 34.817x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.3 | 146.2 | 0.7 | 0.185x | 10.998x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.7 | 145.4 | 150.1 | 1.7 | 0.186x | 11.078x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.4 | 771.4 | 828.1 | 22.0 | 0.997x | 59.323x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.1 | 778.9 | 798.9 | 6.6 | 1.000x | 59.527x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.1 | 0.2 | 0.008x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.4 | 214.6 | 221.5 | 2.5 | 0.082x | 10.777x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 750.7 | 725.3 | 854.2 | 49.7 | 0.279x | 36.705x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 770.1 | 724.9 | 871.5 | 59.2 | 0.286x | 37.649x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,690.5 | 2,676.0 | 2,708.5 | 11.1 | 1.000x | 131.540x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.007x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 191.3 | 188.5 | 192.5 | 1.5 | 0.242x | 14.458x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194.6 | 189.5 | 197.0 | 2.8 | 0.247x | 14.711x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.2 | 770.6 | 814.9 | 16.0 | 0.995x | 59.345x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 789.2 | 782.2 | 798.4 | 5.9 | 1.000x | 59.648x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.7 | 26.6 | 26.9 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.7 | 0.3 | 0.010x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 231.5 | 226.5 | 238.2 | 3.8 | 0.087x | 8.671x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,167.9 | 1,099.5 | 1,229.4 | 54.1 | 0.438x | 43.745x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,180.5 | 1,166.8 | 1,292.4 | 51.3 | 0.442x | 44.218x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.1 | 2,648.7 | 2,691.8 | 13.7 | 1.000x | 99.975x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.031x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.1 | 35.8 | 0.5 | 0.033x | 1.074x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.5 | 176.5 | 176.5 | 0.0 | 0.170x | 5.466x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 177.2 | 176.8 | 177.5 | 0.2 | 0.171x | 5.488x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.7 | 1,021.5 | 1,039.9 | 6.7 | 1.000x | 32.109x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,046.2 | 1,036.9 | 1,062.5 | 8.3 | 1.009x | 32.404x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.8 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.0 | 62.9 | 0.4 | 0.061x | 1.075x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.9 | 109.0 | 0.9 | 0.104x | 1.850x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 174.1 | 174.1 | 174.3 | 0.1 | 0.168x | 2.983x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 175.8 | 175.7 | 177.3 | 0.7 | 0.170x | 3.011x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.4 | 1,021.5 | 1,048.5 | 8.7 | 1.000x | 17.756x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.031x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 34.7 | 0.1 | 0.033x | 1.070x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.5 | 176.4 | 176.6 | 0.1 | 0.171x | 5.472x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 177.0 | 176.9 | 179.0 | 0.8 | 0.171x | 5.487x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,034.7 | 1,018.8 | 1,040.0 | 7.5 | 1.000x | 32.074x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,049.6 | 1,042.0 | 1,060.1 | 6.3 | 1.014x | 32.536x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.2 | 58.1 | 58.4 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 63.0 | 0.3 | 0.060x | 1.072x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.7 | 106.4 | 111.5 | 1.9 | 0.104x | 1.850x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 174.2 | 174.1 | 174.4 | 0.1 | 0.169x | 2.992x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 175.7 | 175.6 | 175.8 | 0.1 | 0.170x | 3.017x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,018.0 | 1,043.8 | 8.3 | 1.000x | 17.717x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.0 | 0.028x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 34.4 | 36.3 | 0.8 | 0.032x | 1.115x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.9 | 168.5 | 170.9 | 0.9 | 0.148x | 5.225x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.1 | 169.1 | 169.4 | 0.1 | 0.148x | 5.232x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.7 | 1,128.7 | 1,158.3 | 10.1 | 1.000x | 35.354x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,155.2 | 1,138.4 | 1,173.7 | 11.2 | 1.011x | 35.740x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 63.4 | 0.5 | 0.055x | 1.068x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.3 | 107.3 | 111.9 | 1.6 | 0.095x | 1.859x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 170.1 | 170.0 | 170.2 | 0.1 | 0.149x | 2.919x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 171.5 | 171.5 | 171.7 | 0.1 | 0.151x | 2.943x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,139.6 | 1,128.3 | 1,142.1 | 4.9 | 1.000x | 19.555x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 35.0 | 0.2 | 0.032x | 1.069x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.6 | 158.8 | 161.7 | 1.2 | 0.148x | 4.947x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.6 | 159.3 | 160.8 | 0.6 | 0.148x | 4.947x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.5 | 1,071.5 | 1,091.5 | 6.7 | 1.000x | 33.400x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,092.1 | 1,084.8 | 1,106.2 | 8.6 | 1.014x | 33.852x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.2 | 58.1 | 58.6 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.1 | 62.5 | 0.2 | 0.058x | 1.069x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.2 | 115.8 | 3.3 | 0.100x | 1.846x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 161.1 | 160.8 | 161.3 | 0.1 | 0.150x | 2.770x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 162.7 | 162.5 | 162.9 | 0.1 | 0.151x | 2.797x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.1 | 1,069.2 | 1,095.0 | 10.1 | 1.000x | 18.483x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.2 | 35.3 | 0.4 | 0.032x | 1.071x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.0 | 158.8 | 159.3 | 0.2 | 0.148x | 4.920x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.7 | 159.3 | 161.7 | 0.9 | 0.149x | 4.939x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.1 | 1,070.5 | 1,082.2 | 4.3 | 1.000x | 33.162x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,088.9 | 1,085.9 | 1,102.1 | 6.1 | 1.016x | 33.683x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.5 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.0 | 62.6 | 0.2 | 0.058x | 1.070x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 107.0 | 115.6 | 3.3 | 0.099x | 1.843x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 161.0 | 160.9 | 161.3 | 0.2 | 0.149x | 2.758x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 162.7 | 162.6 | 163.9 | 0.5 | 0.150x | 2.787x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,081.8 | 1,073.1 | 1,091.8 | 7.6 | 1.000x | 18.535x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.018x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 308.9 | 284.1 | 310.3 | 10.0 | 0.337x | 19.159x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 312.5 | 291.3 | 313.5 | 10.2 | 0.341x | 19.380x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 914.0 | 907.6 | 948.5 | 17.7 | 0.998x | 56.682x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 915.7 | 900.8 | 923.9 | 8.7 | 1.000x | 56.788x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.9 | 0.3 | 0.008x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 26.6 | 0.1 | 0.008x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 309.8 | 306.4 | 323.5 | 7.7 | 0.097x | 11.785x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,744.6 | 1,713.4 | 1,768.8 | 19.0 | 0.545x | 66.355x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,746.2 | 1,725.1 | 1,751.3 | 9.2 | 0.545x | 66.416x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,201.4 | 3,179.1 | 3,208.6 | 10.6 | 1.000x | 121.764x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.0 | 10.8 | 11.6 | 0.3 | 0.363x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 10.6 | 12.2 | 0.5 | 0.380x | 1.045x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 2.751x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 30.8 | 0.2 | 1.002x | 2.757x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.1 | 46.5 | 47.6 | 0.4 | 1.553x | 4.272x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.6 | 48.3 | 0.3 | 1.589x | 4.372x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.4 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.184x | 1.047x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 30.9 | 0.2 | 1.000x | 5.686x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 39.9 | 40.6 | 0.3 | 1.321x | 7.512x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 49.0 | 48.8 | 50.6 | 0.7 | 1.609x | 9.147x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 52.3 | 52.2 | 52.6 | 0.1 | 1.717x | 9.766x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.2 | 0.2 | 0.331x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.9 | 0.2 | 0.350x | 1.057x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 3.018x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 3.018x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.4 | 47.0 | 47.6 | 0.2 | 1.565x | 4.723x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.4 | 48.3 | 48.8 | 0.2 | 1.596x | 4.816x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 6.4 | 0.2 | 0.196x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 6.5 | 6.5 | 7.7 | 0.5 | 0.214x | 1.089x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 30.8 | 0.1 | 1.000x | 5.091x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 39.9 | 40.4 | 0.2 | 1.318x | 6.711x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 65.5 | 64.1 | 66.5 | 0.9 | 2.154x | 10.964x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 71.0 | 69.7 | 71.1 | 0.5 | 2.332x | 11.873x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.7 | 0.2 | 0.332x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.2 | 0.1 | 0.354x | 1.069x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.9 | 33.8 | 34.6 | 0.3 | 1.000x | 3.016x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 33.9 | 35.3 | 0.5 | 1.025x | 3.091x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 111.0 | 108.7 | 115.3 | 2.3 | 3.277x | 9.883x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 111.8 | 110.3 | 113.2 | 1.1 | 3.299x | 9.951x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.4 | 37.3 | 0.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.3 | 46.4 | 0.0 | 1.276x | 1.276x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.2 | 72.6 | 73.2 | 0.2 | 2.015x | 2.015x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 73.6 | 73.1 | 74.2 | 0.3 | 2.028x | 2.028x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 2,859.9 | 2,830.6 | 3,036.6 | 75.1 | 78.759x | 78.759x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 2,868.2 | 2,864.7 | 2,934.3 | 26.8 | 78.988x | 78.988x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.2 | 0.0 | 0.580x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 0.583x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 34.7 | 0.8 | 1.000x | 1.724x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 35.2 | 0.3 | 1.043x | 1.798x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.0 | 162.5 | 166.7 | 1.6 | 4.969x | 8.567x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 166.3 | 163.4 | 170.3 | 2.3 | 5.037x | 8.683x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 16.1 | 16.1 | 16.5 | 0.2 | 0.473x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 16.7 | 0.1 | 0.481x | 1.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 34.0 | 35.1 | 0.4 | 1.000x | 2.116x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.3 | 44.4 | 0.1 | 1.299x | 2.749x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 790.4 | 768.5 | 824.2 | 21.0 | 23.178x | 49.042x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 810.9 | 768.7 | 866.8 | 31.7 | 23.777x | 50.310x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,581,417.1 | 3,579,713.5 | 3,585,395.3 | 2,084.5 | 0.069x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,586,692.1 | 3,581,227.7 | 3,590,651.5 | 3,558.7 | 0.069x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,031,195.0 | 6,979,358.0 | 7,057,785.3 | 28,652.1 | 0.136x | 1.963x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 11,639,288.0 | 11,107,086.0 | 12,408,393.0 | 461,188.9 | 0.225x | 3.250x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12,204,220.0 | 11,456,745.0 | 12,883,584.0 | 460,305.1 | 0.236x | 3.408x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,615,885.8 | 51,304,264.0 | 52,022,538.5 | 284,120.8 | 1.000x | 14.412x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,798.8 | 18,672.9 | 18,972.7 | 113.2 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,875,347.2 | 1,874,675.9 | 1,878,002.9 | 1,336.5 | 99.759x | 99.759x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,881,379.0 | 1,877,943.1 | 1,890,945.6 | 4,695.8 | 100.080x | 100.080x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,589,931.3 | 17,552,497.7 | 17,676,695.0 | 42,309.9 | 935.693x | 935.693x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 84,163,304.0 | 83,289,168.0 | 90,624,651.0 | 2,981,935.3 | 4477.052x | 4477.052x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 84,428,288.0 | 83,695,475.0 | 89,394,618.0 | 2,336,118.2 | 4491.148x | 4491.148x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,761.9 | 18,621.4 | 18,785.8 | 71.3 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,875,174.1 | 1,874,561.6 | 1,889,879.8 | 5,897.2 | 99.946x | 99.946x | 5 | 100% |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,877,090.2 | 1,875,636.1 | 1,891,546.8 | 6,013.5 | 100.048x | 100.048x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,149,477.5 | 3,131,450.4 | 3,160,155.8 | 11,463.0 | 0.007x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,192,965.9 | 3,172,183.3 | 3,218,576.7 | 15,379.2 | 0.007x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42,743,471.0 | 42,677,077.0 | 43,235,138.3 | 205,178.3 | 0.096x | 13.572x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 101,043,491.0 | 99,738,183.0 | 118,828,272.0 | 8,417,120.6 | 0.226x | 32.083x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 116,495,339.0 | 106,043,167.0 | 121,751,489.0 | 5,198,372.7 | 0.260x | 36.989x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 447,267,822.4 | 446,157,442.5 | 452,012,100.1 | 2,246,381.8 | 1.000x | 142.013x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,846.0 | 18,750.9 | 19,031.6 | 94.9 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,092,666.6 | 3,082,447.1 | 3,098,093.6 | 5,314.4 | 164.102x | 164.102x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,152,957.6 | 3,125,188.6 | 3,209,869.2 | 29,061.8 | 167.301x | 167.301x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,545,364.0 | 22,516,477.0 | 23,129,297.3 | 250,645.8 | 1196.294x | 1196.294x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 99,774,883.0 | 97,301,189.0 | 117,139,853.0 | 7,493,961.0 | 5294.221x | 5294.221x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 112,022,042.0 | 98,318,421.0 | 115,256,721.0 | 5,938,688.2 | 5944.075x | 5944.075x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.200x | 1.143x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.353x | 2.015x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.0 | 0.355x | 2.030x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.3 | 1.000x | 5.712x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.003x | 5.728x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 14.0 | 0.4 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.132x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 17.9 | 20.3 | 0.9 | 0.181x | 1.406x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.1 | 20.9 | 0.9 | 0.187x | 1.451x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.435x | 3.377x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 68.6 | 69.6 | 0.4 | 0.685x | 5.316x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 99.7 | 105.6 | 2.1 | 1.000x | 7.762x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.5 | 0.2 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.196x | 1.129x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 0.352x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.0 | 0.356x | 2.051x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.5 | 0.7 | 0.994x | 5.727x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.7 | 0.4 | 1.000x | 5.763x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.136x | 1.019x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.179x | 1.343x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.180x | 1.351x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.5 | 0.3 | 0.439x | 3.291x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.1 | 0.2 | 0.688x | 5.150x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.7 | 101.4 | 1.0 | 1.000x | 7.491x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.200x | 1.146x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.354x | 2.034x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.357x | 2.051x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.726x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 5.745x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.1 | 12.1 | 12.7 | 0.2 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.073x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 0.180x | 1.477x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.181x | 1.491x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.6 | 0.4 | 0.440x | 3.618x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.9 | 67.3 | 69.4 | 0.8 | 0.682x | 5.607x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 99.1 | 101.4 | 0.8 | 1.000x | 8.221x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.356x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.2 | 1.000x | 5.689x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.007x | 5.729x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.9 | 0.3 | 0.150x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.4 | 15.3 | 15.5 | 0.1 | 0.152x | 1.011x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.177x | 1.176x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.179x | 1.191x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.433x | 2.880x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.5 | 70.0 | 0.7 | 0.682x | 4.533x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 96.0 | 101.4 | 2.3 | 1.000x | 6.646x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.356x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 32.2 | 1.4 | 1.000x | 5.704x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 1.003x | 5.719x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.183x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 18.0 | 18.8 | 0.3 | 0.187x | 1.026x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 19.7 | 19.6 | 19.8 | 0.1 | 0.198x | 1.084x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 20.6 | 20.6 | 20.8 | 0.1 | 0.207x | 1.135x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 44.5 | 45.4 | 0.3 | 0.450x | 2.466x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 71.8 | 71.5 | 72.1 | 0.2 | 0.720x | 3.944x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.9 | 101.6 | 1.2 | 1.000x | 5.475x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.198x | 1.125x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.691x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.1 | 29.1 | 0.3 | 1.008x | 5.740x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.2 | 12.1 | 12.2 | 0.1 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.067x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.179x | 1.470x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.4 | 0.3 | 0.440x | 3.607x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.1 | 66.6 | 67.6 | 0.4 | 0.672x | 5.513x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.3 | 101.0 | 1.3 | 1.000x | 8.199x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.202x | 1.154x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.045x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.699x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.718x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.1 | 12.1 | 12.2 | 0.0 | 0.122x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.073x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 0.180x | 1.477x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.496x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.8 | 0.4 | 0.440x | 3.610x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.7 | 67.2 | 70.7 | 1.3 | 0.681x | 5.590x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 101.4 | 1.4 | 1.000x | 8.211x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.356x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.359x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.0 | 1.000x | 5.711x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.002x | 5.723x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 15.2 | 15.1 | 15.3 | 0.0 | 0.153x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.4 | 15.4 | 15.4 | 0.0 | 0.155x | 1.014x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 0.180x | 1.178x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.1 | 0.1 | 0.182x | 1.190x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 47.8 | 1.5 | 0.443x | 2.901x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.3 | 69.4 | 0.4 | 0.692x | 4.537x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.2 | 1.2 | 1.000x | 6.556x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.197x | 1.128x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.354x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.050x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 5.719x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.722x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.1 | 0.1 | 0.180x | 1.379x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 45.5 | 0.7 | 0.440x | 3.372x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.6 | 70.4 | 0.7 | 0.692x | 5.299x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 100.2 | 1.0 | 1.000x | 7.662x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.031x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.694x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 28.8 | 0.2 | 1.007x | 5.732x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.026x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 0.180x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.392x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.4 | 0.2 | 0.442x | 3.377x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.0 | 69.4 | 70.2 | 0.3 | 0.704x | 5.384x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.6 | 1.0 | 1.000x | 7.648x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.6 | 0.2 | 0.356x | 2.031x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.701x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.006x | 5.733x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.133x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.179x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.437x | 3.362x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.1 | 96.6 | 10.8 | 0.697x | 5.369x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 101.2 | 1.2 | 1.000x | 7.699x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.2 | 0.356x | 2.030x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.044x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 28.8 | 0.1 | 1.000x | 5.706x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.1 | 1.002x | 5.716x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 14.8 | 14.8 | 15.3 | 0.2 | 0.148x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.1 | 15.1 | 15.1 | 0.0 | 0.151x | 1.020x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.211x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.222x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.439x | 2.959x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.4 | 0.3 | 0.693x | 4.668x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.7 | 1.0 | 1.000x | 6.737x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.0 | 0.356x | 2.033x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.705x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.5 | 0.7 | 1.007x | 5.748x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 14.0 | 0.0 | 0.140x | 1.021x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.181x | 1.315x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.0 | 0.182x | 1.327x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.5 | 0.4 | 0.441x | 3.216x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 81.7 | 5.2 | 0.694x | 5.054x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.0 | 98.1 | 101.0 | 1.1 | 1.000x | 7.285x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 2.033x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.360x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.694x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.7 | 0.4 | 1.006x | 5.729x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.021x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.314x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.182x | 1.329x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.440x | 3.215x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.1 | 68.9 | 0.3 | 0.689x | 5.035x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 98.0 | 100.9 | 1.1 | 1.000x | 7.306x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.356x | 2.033x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.705x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.009x | 5.754x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 12.5 | 0.0 | 0.124x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.047x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.179x | 1.444x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.180x | 1.452x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 45.9 | 0.8 | 0.441x | 3.549x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.9 | 67.9 | 69.3 | 0.5 | 0.680x | 5.475x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.7 | 101.0 | 1.2 | 1.000x | 8.047x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 2.024x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.042x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 30.3 | 0.7 | 1.000x | 5.709x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.725x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.1 | 0.137x | 1.026x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.179x | 1.343x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.363x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.9 | 0.8 | 0.442x | 3.317x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.5 | 68.4 | 75.4 | 2.5 | 0.697x | 5.228x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.3 | 101.4 | 1.1 | 1.000x | 7.501x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.355x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.713x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.001x | 5.718x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.136x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 0.180x | 1.349x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.355x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 46.0 | 1.0 | 0.441x | 3.312x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.4 | 69.1 | 0.3 | 0.691x | 5.184x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.3 | 101.0 | 1.3 | 1.000x | 7.506x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.1 | 0.2 | 0.196x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.026x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.710x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.004x | 5.733x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 14.0 | 13.9 | 14.3 | 0.2 | 0.141x | 1.029x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 0.180x | 1.317x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.326x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.4 | 0.6 | 0.441x | 3.227x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.5 | 73.8 | 2.0 | 0.692x | 5.066x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 7.320x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 2.047x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.050x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 0.999x | 5.725x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 1.000x | 5.732x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.5 | 0.1 | 0.134x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.8 | 0.1 | 0.137x | 1.025x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.180x | 1.345x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.358x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.1 | 0.6 | 0.440x | 3.293x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.4 | 69.1 | 0.3 | 0.692x | 5.177x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 7.479x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.2 | 0.2 | 0.196x | 1.117x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.204x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.023x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.039x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 5.704x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.002x | 5.715x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 14.0 | 13.9 | 14.7 | 0.3 | 0.142x | 1.034x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.180x | 1.316x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.182x | 1.327x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.4 | 0.6 | 0.445x | 3.251x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.2 | 69.3 | 0.4 | 0.691x | 5.043x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 101.0 | 1.3 | 1.000x | 7.302x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.029x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.691x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.7 | 0.0 | 1.005x | 5.718x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 14.3 | 0.0 | 0.142x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 14.5 | 14.5 | 14.5 | 0.0 | 0.145x | 1.020x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.261x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.270x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.9 | 0.5 | 0.441x | 3.095x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.1 | 69.1 | 0.4 | 0.693x | 4.866x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.3 | 100.6 | 1.1 | 1.000x | 7.026x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.355x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.358x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.000x | 5.713x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.003x | 5.728x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.7 | 0.3 | 0.180x | 1.373x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.8 | 49.5 | 2.2 | 0.445x | 3.402x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 68.9 | 71.6 | 0.9 | 0.703x | 5.375x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.6 | 101.0 | 1.2 | 1.000x | 7.645x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.042x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.723x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.741x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.5 | 0.3 | 0.443x | 3.381x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.7 | 69.1 | 0.1 | 0.695x | 5.307x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 99.9 | 0.6 | 1.000x | 7.636x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.198x | 1.125x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.2 | 0.0 | 0.212x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.030x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.358x | 2.041x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.693x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 29.7 | 0.5 | 1.005x | 5.722x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 18.2 | 0.1 | 0.180x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.181x | 1.385x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.3 | 0.3 | 0.440x | 3.366x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.1 | 69.8 | 0.6 | 0.694x | 5.303x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.7 | 99.9 | 0.9 | 1.000x | 7.645x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.0 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.029x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.5 | 0.1 | 0.356x | 2.031x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 28.7 | 0.1 | 1.000x | 5.712x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.0 | 0.5 | 1.003x | 5.732x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.3 | 0.134x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.5 | 0.3 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.9 | 44.6 | 0.3 | 0.447x | 3.421x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.0 | 69.7 | 71.1 | 0.6 | 0.704x | 5.387x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 101.1 | 0.9 | 1.000x | 7.657x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.198x | 1.124x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.357x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.361x | 2.052x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.689x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.008x | 5.735x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.1 | 13.3 | 0.1 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.394x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.3 | 0.3 | 0.441x | 3.375x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.2 | 69.2 | 0.4 | 0.694x | 5.314x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.9 | 1.1 | 1.000x | 7.661x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.125x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.038x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.700x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.0 | 1.005x | 5.729x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.132x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.178x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.1 | 0.1 | 0.179x | 1.385x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.3 | 0.6 | 0.437x | 3.372x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.2 | 69.2 | 0.4 | 0.683x | 5.273x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 97.4 | 103.1 | 1.8 | 1.000x | 7.723x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.202x | 1.153x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.356x | 2.033x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 31.6 | 1.2 | 1.000x | 5.713x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 1.004x | 5.734x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.181x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.182x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 47.4 | 1.5 | 0.443x | 3.368x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.6 | 69.3 | 0.2 | 0.696x | 5.299x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 104.3 | 2.4 | 1.000x | 7.608x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 2.037x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.1 | 1.000x | 5.705x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.8 | 0.1 | 1.004x | 5.729x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 0.182x | 1.378x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.5 | 0.2 | 0.183x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 44.8 | 0.4 | 0.446x | 3.388x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.8 | 68.8 | 70.1 | 0.5 | 0.708x | 5.374x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.6 | 97.3 | 104.5 | 2.6 | 1.000x | 7.594x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.698x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.005x | 5.728x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.5 | 0.2 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.021x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.182x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.442x | 3.366x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.5 | 69.2 | 0.3 | 0.694x | 5.287x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 97.7 | 104.6 | 2.4 | 1.000x | 7.622x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.7 | 0.0 | 0.197x | 1.126x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.709x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.006x | 5.740x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.1 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.2 | 0.1 | 0.179x | 1.379x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.1 | 0.0 | 0.181x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.438x | 3.375x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.2 | 69.4 | 71.0 | 0.5 | 0.701x | 5.398x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 104.7 | 2.4 | 1.000x | 7.699x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.357x | 2.029x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.039x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.689x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.737x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.180x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.1 | 0.181x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.6 | 45.1 | 0.6 | 0.445x | 3.402x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.4 | 69.2 | 0.3 | 0.690x | 5.278x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.3 | 104.8 | 2.6 | 1.000x | 7.644x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.043x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.1 | 0.2 | 1.000x | 5.688x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.007x | 5.727x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.5 | 0.2 | 0.181x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.183x | 1.387x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.4 | 0.3 | 0.444x | 3.372x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 68.2 | 69.7 | 0.6 | 0.701x | 5.323x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.7 | 97.3 | 104.9 | 2.8 | 1.000x | 7.599x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.034x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.1 | 0.358x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.712x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.002x | 5.725x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.4 | 0.2 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.135x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.3 | 0.2 | 0.181x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.183x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.3 | 0.450x | 3.414x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.3 | 70.7 | 0.8 | 0.699x | 5.296x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.5 | 97.6 | 104.1 | 2.4 | 1.000x | 7.580x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.173x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.0 | 0.1 | 0.194x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.352x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 2.041x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 0.990x | 5.725x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 29.4 | 0.3 | 1.000x | 5.781x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.2 | 0.134x | 1.025x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 0.180x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.383x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.442x | 3.373x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.8 | 69.2 | 70.3 | 0.4 | 0.703x | 5.368x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 104.4 | 2.4 | 1.000x | 7.633x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.033x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 2.044x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.4 | 0.3 | 1.000x | 5.722x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.723x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 14.0 | 0.3 | 0.134x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.6 | 0.3 | 0.179x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.181x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.4 | 0.3 | 0.442x | 3.385x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.5 | 70.5 | 0.8 | 0.693x | 5.308x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.6 | 102.1 | 1.5 | 1.000x | 7.664x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.125x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.031x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.047x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.713x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.745x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.4 | 0.2 | 0.180x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.182x | 1.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.441x | 3.367x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.4 | 113.4 | 17.9 | 0.691x | 5.279x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.2 | 99.9 | 1.0 | 1.000x | 7.642x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.353x | 2.026x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 2.049x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 0.997x | 5.731x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.000x | 5.746x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.180x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.181x | 1.385x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.6 | 0.4 | 0.441x | 3.368x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 72.8 | 1.3 | 0.702x | 5.358x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 100.7 | 1.2 | 1.000x | 7.636x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.040x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 5.729x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 5.729x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.2 | 0.135x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.181x | 1.379x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.2 | 0.1 | 0.183x | 1.394x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.444x | 3.373x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.2 | 0.2 | 0.695x | 5.287x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 100.7 | 1.2 | 1.000x | 7.605x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.355x | 2.023x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 2.040x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 1.000x | 5.693x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.005x | 5.722x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.0 | 0.136x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.179x | 1.346x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.1 | 0.0 | 0.180x | 1.355x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.6 | 47.9 | 1.6 | 0.441x | 3.319x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.3 | 69.0 | 0.3 | 0.684x | 5.146x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.2 | 100.5 | 1.2 | 1.000x | 7.526x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.173x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.124x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.209x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 2.036x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.355x | 2.052x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 0.996x | 5.748x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.1 | 0.2 | 1.000x | 5.774x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 9.0 | 0.2 | 0.265x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 9.0 | 8.6 | 9.1 | 0.2 | 0.278x | 1.050x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.4 | 13.3 | 14.0 | 0.3 | 0.413x | 1.561x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.4 | 13.1 | 14.6 | 0.5 | 0.414x | 1.564x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.7 | 0.3 | 0.552x | 2.086x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 35.0 | 1.0 | 1.000x | 3.781x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 36.3 | 40.1 | 1.3 | 1.151x | 4.353x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.065x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.065x | 1.003x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.070x | 1.079x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 11.0 | 0.2 | 0.123x | 1.897x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.8 | 0.1 | 0.123x | 1.910x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 86.8 | 86.4 | 88.4 | 0.7 | 1.000x | 15.478x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.7 | 86.5 | 90.1 | 1.1 | 1.021x | 15.807x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 11.0 | 10.9 | 11.5 | 0.2 | 0.110x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.183x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 17.3 | 17.2 | 17.4 | 0.1 | 0.173x | 1.570x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.3 | 17.2 | 21.3 | 1.6 | 0.173x | 1.574x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 52.2 | 3.2 | 0.443x | 4.026x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 66.9 | 66.5 | 67.9 | 0.6 | 0.671x | 6.090x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.1 | 101.2 | 1.2 | 1.000x | 9.082x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.2 | 0.2 | 0.195x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.352x | 2.024x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.355x | 2.042x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 0.996x | 5.734x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.2 | 1.000x | 5.757x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.1 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.5 | 17.5 | 17.7 | 0.1 | 0.177x | 1.347x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 17.5 | 18.3 | 0.3 | 0.183x | 1.396x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.1 | 0.8 | 0.449x | 3.416x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.1 | 71.1 | 0.7 | 0.705x | 5.366x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 98.0 | 101.8 | 1.5 | 1.000x | 7.613x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.039x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.720x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 1.001x | 5.725x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 14.8 | 14.8 | 15.0 | 0.1 | 0.149x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.1 | 15.1 | 15.1 | 0.0 | 0.151x | 1.015x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 19.3 | 0.6 | 0.179x | 1.203x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.8 | 18.0 | 18.9 | 0.4 | 0.189x | 1.267x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.4 | 0.6 | 0.446x | 2.991x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 68.2 | 69.7 | 0.6 | 0.697x | 4.676x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 101.0 | 1.2 | 1.000x | 6.707x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.124x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.044x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.697x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.1 | 1.006x | 5.732x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.8 | 0.2 | 0.134x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.6 | 0.0 | 0.137x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.346x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.4 | 0.181x | 1.359x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 44.1 | 45.8 | 0.6 | 0.450x | 3.371x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.2 | 68.9 | 0.3 | 0.688x | 5.151x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.0 | 101.6 | 1.6 | 1.000x | 7.486x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.194x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.209x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.356x | 2.049x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 0.996x | 5.737x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.0 | 0.2 | 1.000x | 5.762x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.1 | 0.136x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.179x | 1.346x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.0 | 18.9 | 0.3 | 0.182x | 1.368x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.1 | 0.5 | 0.448x | 3.363x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.4 | 69.9 | 0.6 | 0.691x | 5.192x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.3 | 101.0 | 1.1 | 1.000x | 7.510x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.024x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.359x | 2.041x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.693x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.728x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.6 | 0.1 | 0.135x | 1.026x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.181x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.9 | 0.3 | 0.183x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.4 | 0.6 | 0.449x | 3.416x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.0 | 70.4 | 0.5 | 0.704x | 5.360x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 100.7 | 1.2 | 1.000x | 7.614x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.353x | 2.019x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.358x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.714x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 28.9 | 0.1 | 1.008x | 5.760x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.6 | 0.1 | 0.134x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.8 | 17.9 | 0.0 | 0.179x | 1.374x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.1 | 1.2 | 0.448x | 3.434x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 70.2 | 0.3 | 0.699x | 5.358x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.5 | 100.8 | 1.2 | 1.000x | 7.666x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 2.025x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.047x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.709x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.003x | 5.729x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.026x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.183x | 1.394x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.0 | 0.8 | 0.449x | 3.430x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 68.7 | 69.9 | 0.4 | 0.699x | 5.343x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 101.0 | 1.3 | 1.000x | 7.638x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.198x | 1.132x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.4 | 0.1 | 0.354x | 2.022x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 2.042x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.714x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.003x | 5.729x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 14.5 | 14.5 | 14.5 | 0.0 | 0.146x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 14.8 | 14.8 | 14.8 | 0.0 | 0.149x | 1.020x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.235x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.182x | 1.248x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.6 | 45.2 | 0.5 | 0.449x | 3.076x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.5 | 69.1 | 0.2 | 0.695x | 4.762x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.5 | 101.8 | 1.5 | 1.000x | 6.853x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.197x | 1.127x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.356x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.044x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.710x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.002x | 5.724x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.1 | 0.134x | 1.026x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.180x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.181x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.1 | 1.2 | 0.448x | 3.422x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.4 | 69.4 | 0.4 | 0.693x | 5.292x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.6 | 101.7 | 1.4 | 1.000x | 7.636x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.204x | 1.161x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.357x | 2.035x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.359x | 2.045x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.695x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.2 | 28.9 | 0.2 | 1.005x | 5.726x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 14.5 | 14.5 | 14.7 | 0.1 | 0.145x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 14.8 | 14.8 | 14.8 | 0.0 | 0.148x | 1.020x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.5 | 0.3 | 0.179x | 1.236x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.9 | 0.4 | 0.181x | 1.245x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.6 | 1.4 | 0.447x | 3.077x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.0 | 70.6 | 0.9 | 0.690x | 4.755x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 100.9 | 1.1 | 1.000x | 6.889x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.196x | 1.128x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.5 | 0.2 | 0.352x | 2.019x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.039x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.996x | 5.722x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.000x | 5.743x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.021x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 0.180x | 1.379x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.384x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.3 | 1.3 | 0.448x | 3.429x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.2 | 70.1 | 0.4 | 0.701x | 5.358x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 100.4 | 0.8 | 1.000x | 7.647x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 0.354x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.035x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 0.999x | 5.721x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.2 | 1.000x | 5.726x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.181x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.9 | 0.4 | 0.182x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 47.2 | 1.3 | 0.448x | 3.410x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 69.1 | 69.8 | 0.2 | 0.701x | 5.343x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 101.0 | 1.1 | 1.000x | 7.617x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.212x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.355x | 2.020x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.358x | 2.035x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.683x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.728x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.182x | 1.388x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.3 | 0.5 | 0.447x | 3.410x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.3 | 69.0 | 70.0 | 0.4 | 0.699x | 5.334x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.8 | 100.6 | 0.9 | 1.000x | 7.634x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.027x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 2.039x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.0 | 0.2 | 1.000x | 5.688x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.005x | 5.718x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.3 | 0.2 | 0.179x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.9 | 0.3 | 0.181x | 1.391x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.9 | 0.8 | 0.446x | 3.418x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 69.6 | 0.1 | 0.698x | 5.355x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 101.5 | 1.2 | 1.000x | 7.671x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.197x | 1.126x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.037x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 0.358x | 2.045x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.999x | 5.703x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.3 | 28.7 | 0.1 | 1.000x | 5.706x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.378x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 51.8 | 3.0 | 0.451x | 3.444x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.1 | 72.5 | 1.2 | 0.703x | 5.370x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 100.1 | 1.1 | 1.000x | 7.638x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.2 | 0.1 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 2.023x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.040x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.999x | 5.732x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 1.000x | 5.738x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.209x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.357x | 2.045x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 2.047x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.715x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.5 | 0.3 | 1.000x | 5.733x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.197x | 1.126x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.1 | 0.2 | 1.000x | 5.712x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.002x | 5.723x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.1 | 0.196x | 1.123x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.716x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.001x | 5.720x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.120x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.0 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.355x | 2.031x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.358x | 2.045x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.1 | 1.000x | 5.715x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.005x | 5.741x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.7 | 0.0 | 0.197x | 1.125x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.355x | 2.024x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.710x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.002x | 5.721x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 2.028x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.047x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.720x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.739x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.1 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.033x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.717x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 32.0 | 1.3 | 1.003x | 5.732x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.2 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.033x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.718x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 28.8 | 0.3 | 1.002x | 5.728x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.179x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.181x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.0 | 45.4 | 0.6 | 0.448x | 3.439x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.1 | 0.3 | 0.689x | 5.288x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.5 | 100.6 | 1.2 | 1.000x | 7.680x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.198x | 1.128x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 2.036x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.361x | 2.053x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 1.000x | 5.686x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.9 | 0.5 | 1.005x | 5.714x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.4 | 13.3 | 13.6 | 0.1 | 0.135x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 14.1 | 0.2 | 0.137x | 1.017x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.332x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.346x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.1 | 0.5 | 0.448x | 3.326x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 69.8 | 0.5 | 0.690x | 5.119x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.9 | 100.8 | 1.0 | 1.000x | 7.421x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.356x | 2.025x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.8 | 0.3 | 0.361x | 2.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.9 | 0.2 | 1.000x | 5.683x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 29.0 | 0.2 | 1.009x | 5.736x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 19.0 | 0.4 | 0.182x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.8 | 47.5 | 1.3 | 0.454x | 3.471x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.1 | 68.5 | 69.8 | 0.4 | 0.695x | 5.318x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.4 | 100.5 | 0.9 | 1.000x | 7.649x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.122x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.040x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.044x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.710x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.002x | 5.721x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.1 | 12.1 | 12.1 | 0.0 | 0.121x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.073x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.1 | 0.179x | 1.475x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.181x | 1.491x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.8 | 45.7 | 0.6 | 0.449x | 3.706x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.6 | 67.2 | 68.8 | 0.5 | 0.677x | 5.585x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.9 | 101.2 | 1.2 | 1.000x | 8.255x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.356x | 2.034x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.717x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.002x | 5.726x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.0 | 0.179x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.180x | 1.385x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.0 | 1.2 | 0.447x | 3.432x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.3 | 69.3 | 0.3 | 0.690x | 5.299x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.6 | 101.3 | 1.2 | 1.000x | 7.677x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 2.041x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.699x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.006x | 5.731x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12.1 | 12.1 | 12.2 | 0.0 | 0.121x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 0.130x | 1.072x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.1 | 0.1 | 0.180x | 1.478x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.489x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.6 | 45.0 | 0.5 | 0.450x | 3.703x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.2 | 67.0 | 69.0 | 0.7 | 0.674x | 5.549x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.4 | 101.1 | 1.3 | 1.000x | 8.232x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.118x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.358x | 2.043x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.709x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.002x | 5.718x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.8 | 0.3 | 0.181x | 1.007x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 18.8 | 18.5 | 19.1 | 0.2 | 0.188x | 1.047x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.199x | 1.106x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.8 | 44.6 | 52.4 | 2.8 | 0.460x | 2.559x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.5 | 70.1 | 0.2 | 0.701x | 3.901x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.1 | 101.8 | 1.6 | 1.000x | 5.560x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.354x | 2.032x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.358x | 2.051x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.996x | 5.715x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 5.736x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 15.7 | 15.7 | 15.9 | 0.1 | 0.158x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.9 | 15.9 | 16.0 | 0.0 | 0.160x | 1.017x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 17.9 | 0.0 | 0.180x | 1.140x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.8 | 0.3 | 0.182x | 1.154x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.4 | 0.6 | 0.450x | 2.854x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 67.8 | 69.1 | 0.5 | 0.688x | 4.362x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.8 | 1.5 | 1.000x | 6.344x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.6 | 5.9 | 0.1 | 0.204x | 1.166x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 2.034x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.359x | 2.054x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.998x | 5.712x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.722x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.5 | 0.2 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.4 | 13.3 | 14.2 | 0.3 | 0.134x | 1.029x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.6 | 0.3 | 0.180x | 1.380x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.8 | 0.3 | 0.182x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.1 | 45.1 | 0.3 | 0.449x | 3.438x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.6 | 70.8 | 0.4 | 0.703x | 5.380x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.2 | 101.2 | 1.2 | 1.000x | 7.655x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.353x | 2.021x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.052x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.999x | 5.725x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 5.729x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.7 | 0.2 | 0.134x | 1.024x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.183x | 1.396x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 49.5 | 2.1 | 0.449x | 3.427x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.3 | 70.0 | 0.6 | 0.694x | 5.302x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 102.6 | 1.6 | 1.000x | 7.637x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.119x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.356x | 2.024x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.0 | 1.000x | 5.690x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.006x | 5.726x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.9 | 45.6 | 0.6 | 0.447x | 3.424x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.1 | 69.6 | 0.6 | 0.694x | 5.314x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.7 | 2.4 | 1.000x | 7.657x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.118x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.205x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.029x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.5 | 0.1 | 1.000x | 5.683x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.007x | 5.723x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.130x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.8 | 0.3 | 0.181x | 1.389x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.7 | 0.7 | 0.450x | 3.451x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 69.1 | 0.3 | 0.691x | 5.293x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.6 | 2.5 | 1.000x | 7.663x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.200x | 1.136x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.4 | 0.1 | 0.357x | 2.031x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.690x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.5 | 0.3 | 1.006x | 5.726x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.0 | 0.0 | 0.180x | 1.375x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.9 | 0.3 | 0.182x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 44.8 | 0.4 | 0.449x | 3.440x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 67.8 | 69.0 | 0.4 | 0.691x | 5.288x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 102.5 | 1.8 | 1.000x | 7.657x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.176x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 6.0 | 0.1 | 0.199x | 1.132x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.212x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.359x | 2.046x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.360x | 2.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.694x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.009x | 5.744x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.131x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 17.9 | 0.0 | 0.180x | 1.377x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.4 | 0.1 | 0.182x | 1.390x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.7 | 46.2 | 1.0 | 0.453x | 3.459x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.1 | 0.2 | 0.693x | 5.300x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.5 | 100.6 | 1.1 | 1.000x | 7.644x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.0 | 0.0 | 0.175x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.121x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.0 | 6.1 | 0.0 | 0.211x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.6 | 0.2 | 0.355x | 2.030x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 2.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.724x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.001x | 5.729x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.132x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.134x | 1.022x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.9 | 18.0 | 0.1 | 0.181x | 1.376x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.2 | 0.1 | 0.182x | 1.386x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 46.7 | 1.0 | 0.457x | 3.473x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.3 | 68.9 | 0.3 | 0.694x | 5.272x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.5 | 100.6 | 1.2 | 1.000x | 7.601x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.0 | 5.0 | 5.1 | 0.0 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.201x | 1.155x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.210x | 1.206x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.353x | 2.029x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.356x | 2.046x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 0.998x | 5.727x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 5.740x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.132x | 1.023x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.0 | 17.9 | 18.4 | 0.2 | 0.179x | 1.385x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.0 | 18.2 | 0.1 | 0.180x | 1.394x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.3 | 0.6 | 0.445x | 3.441x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.2 | 68.9 | 0.3 | 0.684x | 5.284x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.7 | 100.8 | 1.3 | 1.000x | 7.731x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.3 | 5.3 | 5.3 | 0.0 | 0.187x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.198x | 1.057x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.8 | 5.8 | 0.0 | 0.203x | 1.083x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.8 | 0.1 | 0.372x | 1.986x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.6 | 10.8 | 0.1 | 0.373x | 1.996x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 28.7 | 0.2 | 1.000x | 5.344x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.6 | 0.0 | 1.004x | 5.367x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 6.9 | 0.5 | 0.174x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.175x | 1.004x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 5.9 | 0.0 | 0.184x | 1.054x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.9 | 0.1 | 0.208x | 1.194x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 7.1 | 7.1 | 7.1 | 0.0 | 0.220x | 1.262x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.2 | 32.2 | 34.9 | 1.1 | 1.000x | 5.735x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.0 | 37.1 | 39.2 | 0.7 | 1.210x | 6.940x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 8.1 | 8.0 | 8.6 | 0.2 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.0 | 0.5 | 0.091x | 1.090x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.127x | 1.526x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.127x | 1.527x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.6 | 96.6 | 99.3 | 0.9 | 1.000x | 12.013x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 96.9 | 100.2 | 1.1 | 1.008x | 12.105x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 116.1 | 115.8 | 116.1 | 0.1 | 1.189x | 14.289x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 11.0 | 10.9 | 11.5 | 0.2 | 0.109x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 0.129x | 1.185x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.1 | 0.169x | 1.549x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17.1 | 17.0 | 17.2 | 0.1 | 0.170x | 1.557x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.7 | 0.7 | 0.444x | 4.065x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 66.5 | 66.4 | 67.5 | 0.4 | 0.662x | 6.064x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.7 | 101.5 | 1.4 | 1.000x | 9.164x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.0 | 5.6 | 0.2 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.004x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.079x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.826x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.826x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.126x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.001x | 5.130x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 9.8 | 9.4 | 9.9 | 0.2 | 0.290x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 10.6 | 10.5 | 10.6 | 0.1 | 0.314x | 1.084x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.2 | 17.2 | 17.3 | 0.0 | 0.509x | 1.754x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.4 | 0.7 | 0.853x | 2.942x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.8 | 33.7 | 34.9 | 0.5 | 1.000x | 3.449x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 34.4 | 28.9 | 34.8 | 2.2 | 1.018x | 3.511x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.1 | 38.5 | 44.6 | 2.3 | 1.156x | 3.985x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.0 | 5.6 | 0.3 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6.1 | 6.1 | 6.1 | 0.0 | 0.211x | 1.079x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.815x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 1.826x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.105x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.3 | 2.2 | 1.005x | 5.132x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 9.2 | 8.6 | 9.4 | 0.3 | 0.281x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 9.2 | 8.6 | 9.3 | 0.3 | 0.281x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 10.8 | 10.8 | 10.9 | 0.0 | 0.332x | 1.180x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 10.9 | 10.9 | 10.9 | 0.0 | 0.335x | 1.193x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 16.5 | 16.3 | 16.9 | 0.2 | 0.507x | 1.805x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 35.0 | 1.0 | 1.000x | 3.560x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.8 | 36.3 | 41.3 | 2.1 | 1.160x | 4.130x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 581,707.3 | 576,544.6 | 596,660.3 | 8,174.8 | 0.162x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 627,246.0 | 626,914.5 | 1,062,268.9 | 173,551.6 | 0.175x | 1.078x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 628,059.0 | 627,640.4 | 629,819.7 | 964.3 | 0.175x | 1.080x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 658,242.3 | 648,348.3 | 710,633.7 | 25,446.9 | 0.184x | 1.132x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 761,325.9 | 760,775.6 | 762,127.3 | 573.2 | 0.212x | 1.309x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,728,929.7 | 1,671,641.0 | 1,736,029.1 | 27,268.7 | 0.482x | 2.972x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,585,463.7 | 3,561,821.5 | 3,642,459.6 | 36,446.1 | 1.000x | 6.164x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 17,662.8 | 17,643.8 | 17,854.8 | 77.7 | 0.997x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,667.6 | 17,660.5 | 17,692.6 | 13.4 | 0.997x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,720.1 | 17,679.0 | 17,806.5 | 42.2 | 1.000x | 1.003x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17,933.5 | 17,881.8 | 17,998.2 | 42.2 | 1.012x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,676.1 | 39,138.6 | 39,809.0 | 239.0 | 2.239x | 2.246x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 310,113.4 | 310,042.7 | 311,418.4 | 525.4 | 17.501x | 17.557x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 310,324.2 | 310,168.3 | 319,607.6 | 3,718.1 | 17.513x | 17.569x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 17,621.4 | 17,597.3 | 17,997.0 | 150.9 | 0.993x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,649.3 | 17,628.2 | 17,659.4 | 11.7 | 0.994x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,749.3 | 17,679.5 | 17,781.5 | 38.4 | 1.000x | 1.007x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18,076.5 | 17,887.1 | 18,123.6 | 85.0 | 1.018x | 1.026x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,337.4 | 39,223.7 | 40,015.7 | 287.4 | 2.216x | 2.232x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 310,117.0 | 309,910.7 | 310,479.5 | 183.7 | 17.472x | 17.599x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 310,392.8 | 310,137.1 | 319,688.7 | 3,742.7 | 17.488x | 17.615x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 30,896.9 | 30,746.9 | 30,951.7 | 70.7 | 0.438x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 30,949.2 | 30,783.9 | 32,747.8 | 745.7 | 0.438x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 34,679.3 | 34,666.8 | 35,416.4 | 288.4 | 0.491x | 1.122x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,317.0 | 68,798.6 | 69,580.9 | 260.6 | 0.982x | 2.243x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,617.0 | 70,422.3 | 70,889.1 | 166.8 | 1.000x | 2.286x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 320,961.8 | 320,429.3 | 323,151.1 | 952.5 | 4.545x | 10.388x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 322,506.7 | 322,072.3 | 325,096.1 | 1,112.4 | 4.567x | 10.438x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 17,645.2 | 17,634.8 | 17,673.2 | 14.3 | 0.994x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 17,671.8 | 17,651.3 | 18,368.4 | 281.8 | 0.996x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,747.4 | 17,718.3 | 17,791.3 | 24.5 | 1.000x | 1.006x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18,053.0 | 17,864.5 | 18,150.3 | 100.8 | 1.017x | 1.023x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,612.0 | 39,513.1 | 40,068.9 | 198.9 | 2.232x | 2.245x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 310,051.9 | 309,924.5 | 310,227.2 | 106.8 | 17.470x | 17.571x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 310,488.9 | 310,268.5 | 310,797.5 | 215.1 | 17.495x | 17.596x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.6 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.3 | 32.8 | 0.1 | 0.059x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.5 | 44.3 | 44.7 | 0.2 | 0.080x | 1.372x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.1 | 46.7 | 47.3 | 0.2 | 0.085x | 1.450x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.5 | 170.0 | 171.5 | 0.5 | 0.308x | 5.252x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 545.3 | 540.1 | 551.4 | 4.2 | 0.985x | 16.795x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.4 | 545.4 | 558.0 | 4.5 | 1.000x | 17.043x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 53.3 | 53.3 | 53.7 | 0.2 | 0.097x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.3 | 58.8 | 0.2 | 0.107x | 1.099x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.7 | 58.4 | 59.4 | 0.3 | 0.107x | 1.101x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 73.4 | 73.0 | 75.5 | 0.9 | 0.134x | 1.377x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.3 | 77.2 | 80.5 | 1.3 | 0.141x | 1.450x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 248.2 | 247.0 | 267.0 | 7.6 | 0.453x | 4.656x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.5 | 539.0 | 553.7 | 5.4 | 1.000x | 10.271x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.7 | 41.4 | 0.6 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.8 | 40.1 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 84.9 | 84.4 | 85.4 | 0.3 | 0.111x | 2.124x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 90.3 | 92.0 | 0.6 | 0.120x | 2.289x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 186.5 | 186.3 | 186.8 | 0.2 | 0.244x | 4.668x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 764.0 | 759.3 | 782.6 | 8.8 | 1.000x | 19.123x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 768.1 | 746.8 | 771.8 | 9.3 | 1.005x | 19.226x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 77.8 | 77.6 | 78.0 | 0.1 | 0.101x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 77.8 | 77.6 | 78.2 | 0.2 | 0.101x | 1.000x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 88.8 | 88.7 | 90.0 | 0.5 | 0.116x | 1.142x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 90.4 | 90.2 | 90.6 | 0.1 | 0.118x | 1.163x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.9 | 90.6 | 95.8 | 1.8 | 0.122x | 1.208x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 318.1 | 315.5 | 341.5 | 9.8 | 0.414x | 4.090x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.8 | 761.8 | 780.8 | 6.9 | 1.000x | 9.873x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 0.038x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.0 | 30.4 | 0.1 | 0.062x | 1.661x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 33.1 | 33.3 | 0.1 | 0.068x | 1.820x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 133.7 | 133.4 | 135.4 | 0.8 | 0.275x | 7.337x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 483.8 | 473.4 | 487.4 | 4.8 | 0.997x | 26.540x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 485.4 | 478.3 | 503.1 | 8.8 | 1.000x | 26.631x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 26.5 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.1 | 0.0 | 0.054x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 37.9 | 37.5 | 38.4 | 0.3 | 0.079x | 1.458x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 54.7 | 54.6 | 68.5 | 5.6 | 0.113x | 2.100x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.6 | 64.2 | 68.5 | 1.7 | 0.134x | 2.482x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 192.6 | 191.4 | 193.9 | 0.9 | 0.400x | 7.399x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 481.8 | 472.6 | 490.3 | 6.4 | 1.000x | 18.514x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.5 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 43.2 | 43.6 | 0.1 | 0.056x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 59.1 | 57.6 | 61.7 | 1.3 | 0.076x | 1.365x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.0 | 59.3 | 61.2 | 0.7 | 0.077x | 1.384x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 194.8 | 194.6 | 196.2 | 0.6 | 0.251x | 4.496x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 771.2 | 760.1 | 781.3 | 8.3 | 0.992x | 17.803x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.4 | 767.8 | 785.7 | 6.7 | 1.000x | 17.946x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 66.2 | 65.2 | 69.2 | 1.4 | 0.086x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 84.9 | 84.2 | 93.5 | 3.5 | 0.110x | 1.283x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 86.3 | 85.9 | 86.8 | 0.3 | 0.112x | 1.304x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 86.8 | 86.5 | 86.9 | 0.2 | 0.112x | 1.312x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.6 | 92.8 | 94.2 | 0.5 | 0.121x | 1.415x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 314.7 | 313.6 | 340.8 | 10.5 | 0.408x | 4.757x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.5 | 770.3 | 782.3 | 4.5 | 1.000x | 11.662x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.5 | 57.1 | 58.8 | 0.6 | 0.101x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.6 | 60.9 | 0.1 | 0.107x | 1.056x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.0 | 60.9 | 61.1 | 0.1 | 0.108x | 1.061x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.8 | 61.4 | 0.2 | 0.108x | 1.062x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 229.0 | 228.3 | 231.9 | 1.3 | 0.404x | 3.983x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 567.1 | 561.7 | 570.8 | 3.1 | 1.000x | 9.862x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.0 | 554.8 | 575.2 | 7.6 | 1.009x | 9.947x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 65.8 | 64.6 | 65.9 | 0.5 | 0.116x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 88.7 | 88.3 | 88.9 | 0.2 | 0.157x | 1.349x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.7 | 91.1 | 94.1 | 1.1 | 0.164x | 1.409x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 120.1 | 120.5 | 0.1 | 0.212x | 1.826x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 120.4 | 119.4 | 120.8 | 0.4 | 0.212x | 1.830x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 420.4 | 418.0 | 429.1 | 3.9 | 0.742x | 6.391x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.7 | 561.3 | 573.1 | 4.3 | 1.000x | 8.615x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.2 | 0.0 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.037x | 1.000x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.2 | 30.4 | 0.1 | 0.061x | 1.666x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.2 | 33.8 | 0.2 | 0.067x | 1.828x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 133.7 | 133.0 | 134.9 | 0.6 | 0.270x | 7.340x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 481.8 | 471.6 | 494.3 | 7.8 | 0.971x | 26.447x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 496.2 | 473.9 | 530.0 | 18.9 | 1.000x | 27.233x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.1 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 0.054x | 1.000x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 38.1 | 37.4 | 38.5 | 0.4 | 0.079x | 1.460x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 54.6 | 54.6 | 55.1 | 0.2 | 0.114x | 2.096x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.2 | 63.9 | 69.5 | 2.1 | 0.136x | 2.501x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 193.5 | 192.1 | 195.9 | 1.4 | 0.403x | 7.422x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 480.6 | 473.6 | 483.7 | 3.5 | 1.000x | 18.432x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.1 | 0.038x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.2 | 95.0 | 96.5 | 0.6 | 0.118x | 3.079x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 96.7 | 96.5 | 98.1 | 0.6 | 0.120x | 3.128x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 167.0 | 166.6 | 168.6 | 0.7 | 0.208x | 5.399x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 771.8 | 800.2 | 10.8 | 0.969x | 25.191x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.9 | 775.8 | 843.0 | 24.7 | 1.000x | 25.997x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 55.7 | 55.5 | 56.0 | 0.2 | 0.070x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 56.1 | 55.7 | 59.1 | 1.3 | 0.071x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 84.0 | 91.2 | 3.2 | 0.108x | 1.530x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 129.0 | 127.2 | 130.0 | 0.9 | 0.163x | 2.316x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 138.2 | 135.6 | 144.5 | 3.1 | 0.174x | 2.479x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 281.4 | 280.8 | 284.5 | 1.3 | 0.355x | 5.050x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 792.6 | 778.7 | 794.9 | 5.9 | 1.000x | 14.223x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.7 | 46.6 | 47.0 | 0.2 | 0.074x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.0 | 0.1 | 0.075x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 52.5 | 52.3 | 53.3 | 0.4 | 0.084x | 1.124x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.6 | 55.9 | 0.1 | 0.089x | 1.194x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 199.0 | 201.0 | 0.7 | 0.319x | 4.282x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.2 | 603.0 | 623.1 | 7.0 | 0.986x | 13.245x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 627.3 | 613.0 | 635.7 | 9.0 | 1.000x | 13.439x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 62.0 | 61.0 | 68.2 | 2.6 | 0.100x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 78.0 | 77.5 | 89.6 | 4.7 | 0.125x | 1.258x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.8 | 85.6 | 96.3 | 4.1 | 0.147x | 1.481x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 91.8 | 92.6 | 0.3 | 0.148x | 1.484x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 92.0 | 91.8 | 92.3 | 0.2 | 0.148x | 1.484x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 324.7 | 321.0 | 353.5 | 11.9 | 0.522x | 5.240x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 622.3 | 612.9 | 629.0 | 5.5 | 1.000x | 10.044x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.6 | 36.7 | 0.1 | 0.067x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 45.9 | 46.6 | 0.3 | 0.085x | 1.265x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.8 | 48.5 | 49.0 | 0.2 | 0.089x | 1.332x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 179.5 | 179.0 | 180.5 | 0.5 | 0.328x | 4.903x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.1 | 534.1 | 544.5 | 3.6 | 0.990x | 14.805x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.4 | 542.6 | 556.1 | 4.4 | 1.000x | 14.948x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 55.3 | 54.6 | 55.8 | 0.4 | 0.102x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 69.8 | 0.1 | 0.128x | 1.259x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 69.7 | 69.6 | 70.3 | 0.3 | 0.128x | 1.260x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 75.2 | 75.0 | 92.1 | 6.8 | 0.138x | 1.360x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.3 | 78.7 | 87.4 | 3.2 | 0.146x | 1.434x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 264.6 | 262.6 | 276.1 | 4.9 | 0.487x | 4.786x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.7 | 538.4 | 551.3 | 4.8 | 1.000x | 9.833x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.054x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.054x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.6 | 42.4 | 43.7 | 0.5 | 0.078x | 1.442x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.9 | 44.8 | 45.2 | 0.1 | 0.082x | 1.519x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.4 | 162.0 | 162.7 | 0.3 | 0.298x | 5.494x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535.2 | 532.1 | 542.0 | 3.4 | 0.982x | 18.107x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 544.9 | 537.2 | 549.6 | 4.4 | 1.000x | 18.435x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 50.6 | 50.0 | 54.6 | 1.6 | 0.093x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 52.8 | 0.6 | 0.095x | 1.016x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.2 | 51.5 | 0.1 | 0.095x | 1.016x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 71.0 | 70.8 | 75.5 | 1.8 | 0.131x | 1.403x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.4 | 74.6 | 83.2 | 3.2 | 0.139x | 1.490x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 236.5 | 235.0 | 271.2 | 14.0 | 0.435x | 4.673x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.3 | 536.2 | 544.0 | 2.9 | 1.000x | 10.735x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.7 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.067x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.4 | 30.8 | 32.5 | 0.6 | 0.071x | 1.062x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 32.8 | 35.0 | 0.7 | 0.075x | 1.131x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.1 | 162.0 | 163.2 | 0.5 | 0.366x | 5.492x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.6 | 433.4 | 443.8 | 3.9 | 0.987x | 14.827x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 443.4 | 439.3 | 445.4 | 2.2 | 1.000x | 15.022x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 36.3 | 35.8 | 36.9 | 0.4 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 37.6 | 36.6 | 37.7 | 0.4 | 0.086x | 1.038x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.6 | 0.1 | 0.118x | 1.417x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.0 | 0.2 | 0.119x | 1.425x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.4 | 67.3 | 75.8 | 2.9 | 0.159x | 1.913x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.3 | 231.0 | 239.5 | 3.2 | 0.531x | 6.378x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 435.5 | 431.9 | 444.6 | 5.4 | 1.000x | 12.009x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.8 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.7 | 13.8 | 0.4 | 0.036x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.083x | 2.302x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 31.0 | 32.2 | 0.5 | 0.089x | 2.465x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 61.1 | 10.9 | 0.096x | 2.657x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 346.0 | 338.3 | 350.5 | 4.0 | 0.987x | 27.239x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.6 | 341.0 | 365.6 | 8.5 | 1.000x | 27.604x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.7 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.8 | 0.1 | 0.020x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 59.7 | 58.9 | 70.7 | 4.5 | 0.034x | 1.721x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.9 | 140.3 | 146.1 | 2.6 | 0.081x | 4.090x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 319.0 | 314.8 | 323.3 | 3.0 | 0.183x | 9.196x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 319.6 | 316.1 | 320.6 | 1.6 | 0.183x | 9.212x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.6 | 1,732.2 | 1,776.7 | 14.9 | 1.000x | 50.322x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.4 | 35.6 | 0.1 | 0.052x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 72.5 | 72.2 | 74.1 | 0.7 | 0.106x | 2.056x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.6 | 73.5 | 73.8 | 0.1 | 0.108x | 2.087x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.8 | 176.2 | 177.6 | 0.5 | 0.259x | 5.015x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.1 | 665.2 | 686.4 | 8.0 | 0.983x | 19.002x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.9 | 670.9 | 694.9 | 7.9 | 1.000x | 19.338x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 65.2 | 64.6 | 65.3 | 0.2 | 0.097x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 65.7 | 0.1 | 0.097x | 1.006x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 66.8 | 0.5 | 0.097x | 1.009x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 82.3 | 81.7 | 82.8 | 0.4 | 0.122x | 1.263x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.4 | 82.3 | 89.7 | 2.8 | 0.122x | 1.265x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 255.2 | 254.2 | 266.2 | 4.6 | 0.378x | 3.916x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.9 | 664.4 | 691.4 | 9.9 | 1.000x | 10.358x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.052x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 72.6 | 72.5 | 74.8 | 0.9 | 0.107x | 2.060x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.6 | 73.4 | 73.7 | 0.1 | 0.108x | 2.087x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.3 | 175.9 | 176.7 | 0.3 | 0.259x | 5.002x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.1 | 663.7 | 683.5 | 8.5 | 0.981x | 18.952x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.2 | 670.4 | 697.5 | 9.0 | 1.000x | 19.326x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 64.3 | 64.2 | 64.9 | 0.3 | 0.095x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.5 | 65.3 | 65.8 | 0.2 | 0.097x | 1.019x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 65.8 | 0.2 | 0.097x | 1.020x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.5 | 81.9 | 87.1 | 1.9 | 0.122x | 1.282x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 82.5 | 81.5 | 83.1 | 0.5 | 0.122x | 1.283x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 258.5 | 255.3 | 303.7 | 18.6 | 0.382x | 4.018x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.5 | 666.1 | 691.6 | 8.5 | 1.000x | 10.517x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.055x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.055x | 1.000x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.6 | 47.7 | 50.8 | 1.1 | 0.090x | 1.644x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.1 | 50.4 | 0.1 | 0.093x | 1.701x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.0 | 161.6 | 163.2 | 0.6 | 0.299x | 5.481x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.2 | 522.8 | 542.2 | 6.7 | 0.992x | 18.171x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.4 | 537.1 | 546.1 | 3.4 | 1.000x | 18.314x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.2 | 52.4 | 0.4 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.3 | 51.7 | 0.2 | 0.097x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 54.6 | 54.1 | 55.1 | 0.4 | 0.102x | 1.062x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 72.7 | 72.4 | 73.3 | 0.3 | 0.136x | 1.413x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.0 | 76.7 | 84.8 | 3.1 | 0.144x | 1.499x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 236.6 | 235.8 | 245.8 | 3.9 | 0.443x | 4.602x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 534.4 | 529.4 | 549.7 | 7.2 | 1.000x | 10.394x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.7 | 33.9 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 33.9 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 66.8 | 66.6 | 66.9 | 0.1 | 0.102x | 1.980x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.9 | 67.7 | 68.0 | 0.1 | 0.104x | 2.012x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.6 | 170.9 | 172.1 | 0.4 | 0.262x | 5.089x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 650.4 | 645.3 | 663.3 | 6.9 | 0.994x | 19.281x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 654.3 | 652.0 | 665.4 | 5.0 | 1.000x | 19.397x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 61.7 | 61.1 | 62.7 | 0.5 | 0.094x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.4 | 63.4 | 0.3 | 0.096x | 1.015x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.7 | 62.6 | 63.1 | 0.2 | 0.096x | 1.016x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 80.7 | 80.0 | 80.9 | 0.3 | 0.123x | 1.308x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.0 | 80.7 | 88.9 | 3.2 | 0.124x | 1.313x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.9 | 249.6 | 288.7 | 15.2 | 0.384x | 4.065x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.8 | 640.4 | 671.3 | 10.0 | 1.000x | 10.592x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.5 | 11.8 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.7 | 12.0 | 0.1 | 0.062x | 1.020x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 24.7 | 24.3 | 24.9 | 0.2 | 0.130x | 2.128x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.4 | 25.0 | 26.4 | 0.5 | 0.134x | 2.193x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.137x | 2.233x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 187.0 | 185.2 | 187.3 | 0.8 | 0.987x | 16.135x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 189.5 | 185.1 | 203.3 | 6.2 | 1.000x | 16.350x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 0.024x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.9 | 0.3 | 0.024x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.7 | 50.4 | 51.2 | 0.3 | 0.047x | 1.938x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.4 | 108.4 | 115.8 | 3.1 | 0.102x | 4.181x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 227.1 | 225.5 | 233.6 | 2.8 | 0.211x | 8.677x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 228.6 | 226.5 | 342.9 | 45.8 | 0.212x | 8.734x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.7 | 1,063.5 | 1,091.4 | 9.9 | 1.000x | 41.136x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.4 | 0.0 | 0.052x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 72.5 | 72.4 | 73.1 | 0.2 | 0.107x | 2.057x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.7 | 73.6 | 74.0 | 0.1 | 0.109x | 2.090x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 175.9 | 175.6 | 176.3 | 0.2 | 0.260x | 4.988x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.7 | 662.3 | 676.7 | 5.4 | 0.987x | 18.960x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.7 | 669.4 | 685.4 | 5.1 | 1.000x | 19.217x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 64.9 | 64.4 | 66.9 | 0.9 | 0.096x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.098x | 1.013x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.4 | 66.4 | 0.3 | 0.098x | 1.015x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 82.2 | 81.8 | 88.7 | 2.7 | 0.122x | 1.267x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.8 | 81.1 | 148.5 | 25.8 | 0.125x | 1.293x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 256.7 | 255.2 | 326.6 | 28.0 | 0.382x | 3.958x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.4 | 662.1 | 689.5 | 9.6 | 1.000x | 10.368x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.8 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.8 | 0.0 | 0.052x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 66.7 | 66.5 | 68.0 | 0.5 | 0.102x | 1.976x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.9 | 67.3 | 68.7 | 0.5 | 0.104x | 2.011x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 172.1 | 171.3 | 172.7 | 0.5 | 0.264x | 5.094x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 651.7 | 645.3 | 665.8 | 7.3 | 1.000x | 19.294x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.1 | 645.7 | 663.0 | 5.9 | 1.005x | 19.395x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 61.8 | 61.4 | 63.1 | 0.6 | 0.095x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 62.8 | 0.2 | 0.096x | 1.011x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.0 | 0.2 | 0.096x | 1.014x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 80.1 | 79.8 | 87.6 | 3.0 | 0.123x | 1.295x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.7 | 80.5 | 141.0 | 23.2 | 0.127x | 1.338x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 251.7 | 250.0 | 268.8 | 7.2 | 0.387x | 4.071x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 650.4 | 648.0 | 670.7 | 8.2 | 1.000x | 10.522x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.1 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.2 | 0.1 | 0.062x | 1.011x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 26.0 | 0.2 | 0.130x | 2.143x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.2 | 26.7 | 0.6 | 0.130x | 2.144x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.5 | 26.4 | 26.7 | 0.1 | 0.136x | 2.227x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 192.5 | 192.0 | 195.2 | 1.3 | 0.983x | 16.154x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 195.8 | 188.5 | 199.8 | 4.1 | 1.000x | 16.429x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.6 | 27.7 | 0.1 | 0.025x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 27.9 | 0.2 | 0.025x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 52.6 | 52.5 | 62.0 | 3.8 | 0.048x | 1.908x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 111.0 | 109.4 | 119.3 | 4.4 | 0.102x | 4.022x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 237.9 | 237.6 | 521.0 | 113.0 | 0.219x | 8.621x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 239.2 | 236.6 | 243.8 | 2.6 | 0.220x | 8.669x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,088.1 | 1,080.5 | 1,101.5 | 7.7 | 1.000x | 39.437x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 39.0 | 0.3 | 0.056x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.8 | 0.2 | 0.056x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.1 | 63.0 | 63.8 | 0.3 | 0.092x | 1.646x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 65.8 | 65.7 | 66.6 | 0.3 | 0.096x | 1.716x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 183.9 | 183.7 | 184.3 | 0.2 | 0.269x | 4.793x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.8 | 675.2 | 692.2 | 5.7 | 0.998x | 17.772x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.3 | 682.5 | 696.6 | 5.3 | 1.000x | 17.810x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 70.0 | 69.2 | 70.2 | 0.5 | 0.103x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 72.9 | 72.6 | 72.9 | 0.1 | 0.107x | 1.041x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.7 | 73.3 | 0.2 | 0.107x | 1.041x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.3 | 84.9 | 158.3 | 28.5 | 0.127x | 1.233x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 87.5 | 86.7 | 88.0 | 0.5 | 0.128x | 1.249x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 274.5 | 273.3 | 289.8 | 6.3 | 0.402x | 3.921x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 679.3 | 697.0 | 6.5 | 1.000x | 9.743x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 0.042x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 74.9 | 74.7 | 76.6 | 0.7 | 0.106x | 2.533x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.1 | 83.8 | 86.1 | 0.8 | 0.120x | 2.881x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.4 | 161.8 | 163.6 | 0.6 | 0.229x | 5.494x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 703.4 | 700.4 | 712.0 | 4.1 | 0.994x | 23.799x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.8 | 703.1 | 739.1 | 13.7 | 1.000x | 23.949x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 51.6 | 0.2 | 0.073x | 1.002x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 62.7 | 61.4 | 70.0 | 3.1 | 0.089x | 1.221x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 64.4 | 61.0 | 69.8 | 3.2 | 0.091x | 1.254x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 89.9 | 97.0 | 2.8 | 0.128x | 1.754x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 233.9 | 230.8 | 253.2 | 8.3 | 0.331x | 4.554x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 705.9 | 696.9 | 709.2 | 4.9 | 1.000x | 13.741x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 35.7 | 36.4 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.2 | 38.5 | 0.1 | 0.085x | 1.060x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.6 | 41.6 | 0.0 | 0.092x | 1.151x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.8 | 0.1 | 0.092x | 1.152x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.6 | 190.2 | 191.7 | 0.5 | 0.423x | 5.272x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 445.6 | 444.5 | 451.6 | 2.8 | 0.989x | 12.329x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.7 | 449.8 | 465.6 | 6.0 | 1.000x | 12.468x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 40.9 | 40.2 | 46.4 | 2.4 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 41.9 | 41.0 | 41.9 | 0.4 | 0.093x | 1.024x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.4 | 70.0 | 76.4 | 2.3 | 0.158x | 1.748x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 79.9 | 80.6 | 0.2 | 0.179x | 1.970x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.7 | 80.3 | 80.9 | 0.2 | 0.179x | 1.974x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.1 | 278.7 | 289.8 | 4.0 | 0.621x | 6.854x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.8 | 443.3 | 454.7 | 4.0 | 1.000x | 11.033x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.053x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.053x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.4 | 77.2 | 0.3 | 0.114x | 2.171x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.7 | 84.3 | 86.1 | 0.7 | 0.126x | 2.400x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.7 | 175.4 | 185.8 | 3.8 | 0.263x | 5.008x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.2 | 665.6 | 674.6 | 2.9 | 0.997x | 18.992x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.0 | 670.1 | 688.4 | 7.8 | 1.000x | 19.044x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.6 | 65.6 | 65.7 | 0.1 | 0.098x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.3 | 0.2 | 0.099x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 67.5 | 62.8 | 70.8 | 2.7 | 0.101x | 1.028x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 72.1 | 62.4 | 72.8 | 4.9 | 0.108x | 1.100x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.5 | 82.8 | 90.7 | 3.0 | 0.125x | 1.273x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 253.6 | 252.5 | 259.3 | 2.5 | 0.380x | 3.865x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.2 | 661.9 | 675.6 | 4.7 | 1.000x | 10.169x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.041x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 77.2 | 76.9 | 79.9 | 1.1 | 0.107x | 2.613x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.0 | 84.6 | 89.1 | 1.8 | 0.122x | 2.976x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.2 | 161.7 | 188.9 | 10.8 | 0.225x | 5.484x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 707.6 | 701.3 | 713.3 | 4.4 | 0.981x | 23.932x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.4 | 714.7 | 742.4 | 9.8 | 1.000x | 24.398x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 52.5 | 0.4 | 0.073x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 51.8 | 51.3 | 52.3 | 0.3 | 0.073x | 1.007x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 66.3 | 65.7 | 68.7 | 1.1 | 0.094x | 1.289x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 87.5 | 86.8 | 89.1 | 0.8 | 0.124x | 1.700x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 89.1 | 96.3 | 2.8 | 0.127x | 1.744x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.6 | 231.1 | 232.8 | 0.7 | 0.327x | 4.500x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.0 | 703.5 | 720.2 | 5.7 | 1.000x | 13.756x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.047x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 36.6 | 0.5 | 0.047x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.3 | 79.0 | 0.3 | 0.106x | 2.233x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.3 | 86.2 | 86.3 | 0.1 | 0.116x | 2.444x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.0 | 175.7 | 177.2 | 0.6 | 0.237x | 4.988x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.6 | 722.5 | 733.9 | 4.3 | 0.974x | 20.533x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 743.6 | 727.3 | 750.5 | 7.9 | 1.000x | 21.071x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 65.7 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.5 | 0.3 | 0.090x | 1.002x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 66.4 | 66.3 | 66.7 | 0.1 | 0.091x | 1.012x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.1 | 83.9 | 100.7 | 6.6 | 0.115x | 1.281x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 87.9 | 83.9 | 88.9 | 2.0 | 0.120x | 1.339x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 255.3 | 253.6 | 255.8 | 0.8 | 0.350x | 3.888x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 730.1 | 725.0 | 734.2 | 2.9 | 1.000x | 11.118x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.7 | 36.1 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.2 | 39.5 | 0.5 | 0.085x | 1.063x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.8 | 0.1 | 0.092x | 1.156x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.8 | 0.1 | 0.092x | 1.158x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 190.3 | 191.5 | 0.5 | 0.422x | 5.286x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.8 | 442.5 | 453.2 | 3.7 | 0.989x | 12.403x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.7 | 445.1 | 464.8 | 7.0 | 1.000x | 12.537x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 40.5 | 40.4 | 46.4 | 2.4 | 0.091x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 41.7 | 41.0 | 42.0 | 0.4 | 0.093x | 1.028x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 69.9 | 77.1 | 2.7 | 0.159x | 1.757x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.4 | 80.7 | 0.1 | 0.180x | 1.986x |
| 5 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.8 | 80.3 | 81.5 | 0.4 | 0.181x | 1.993x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.8 | 278.9 | 288.5 | 3.5 | 0.628x | 6.928x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 446.9 | 443.5 | 455.2 | 3.9 | 1.000x | 11.028x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 42.2 | 0.3 | 0.065x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.5 | 41.9 | 0.1 | 0.065x | 1.000x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 71.7 | 74.1 | 0.9 | 0.114x | 1.759x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 87.1 | 84.5 | 88.1 | 1.4 | 0.136x | 2.095x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 190.0 | 196.9 | 2.6 | 0.297x | 4.577x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 628.6 | 623.0 | 637.1 | 4.7 | 0.981x | 15.113x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.5 | 626.2 | 654.9 | 10.7 | 1.000x | 15.400x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 62.0 | 61.8 | 66.6 | 1.9 | 0.098x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 63.3 | 63.1 | 63.4 | 0.1 | 0.100x | 1.021x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.3 | 80.7 | 0.2 | 0.127x | 1.297x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 81.2 | 0.2 | 0.127x | 1.300x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.3 | 90.8 | 3.7 | 0.128x | 1.313x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.4 | 278.5 | 285.4 | 2.5 | 0.442x | 4.518x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.9 | 625.9 | 639.5 | 4.6 | 1.000x | 10.217x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.1 | 0.4 | 0.044x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 32.1 | 0.5 | 0.102x | 2.349x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.9 | 34.7 | 35.2 | 0.2 | 0.115x | 2.644x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 33.6 | 36.8 | 1.1 | 0.116x | 2.664x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.7 | 292.9 | 302.4 | 3.4 | 0.977x | 22.424x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 302.6 | 295.3 | 322.3 | 9.6 | 1.000x | 22.948x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.2 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 22.3 | 22.2 | 22.5 | 0.1 | 0.021x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 45.7 | 45.6 | 46.4 | 0.3 | 0.043x | 2.065x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.0 | 67.5 | 76.8 | 3.3 | 0.064x | 3.113x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 252.6 | 249.4 | 258.3 | 3.2 | 0.235x | 11.403x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 258.4 | 254.8 | 259.0 | 1.5 | 0.241x | 11.667x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.1 | 1,066.8 | 1,085.8 | 7.1 | 1.000x | 48.453x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.8 | 0.6 | 0.044x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.7 | 0.2 | 0.045x | 1.016x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 31.1 | 0.1 | 0.103x | 2.343x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 32.9 | 36.0 | 1.1 | 0.112x | 2.553x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.0 | 0.1 | 0.116x | 2.646x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.8 | 299.7 | 1.8 | 0.980x | 22.380x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.8 | 296.3 | 316.5 | 7.4 | 1.000x | 22.835x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 45.3 | 45.3 | 46.3 | 0.4 | 0.042x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.4 | 45.7 | 0.1 | 0.043x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 69.1 | 73.7 | 1.8 | 0.065x | 1.527x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.9 | 70.2 | 77.6 | 2.6 | 0.067x | 1.587x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 530.2 | 528.4 | 538.3 | 3.5 | 0.497x | 11.700x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 535.6 | 529.5 | 537.5 | 3.5 | 0.502x | 11.818x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.4 | 1,062.8 | 1,089.0 | 9.6 | 1.000x | 23.533x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.2 | 0.4 | 0.044x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.2 | 0.1 | 0.103x | 2.322x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 33.5 | 35.4 | 0.6 | 0.115x | 2.601x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.6 | 34.8 | 0.1 | 0.115x | 2.612x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.5 | 294.8 | 299.4 | 1.8 | 0.992x | 22.435x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.9 | 295.8 | 317.0 | 7.5 | 1.000x | 22.621x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 23.1 | 0.4 | 0.021x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 22.5 | 22.0 | 22.9 | 0.3 | 0.021x | 1.010x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46.2 | 45.8 | 46.4 | 0.3 | 0.043x | 2.073x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 76.6 | 3.1 | 0.064x | 3.086x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 257.5 | 249.8 | 259.2 | 3.7 | 0.241x | 11.570x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 257.8 | 254.3 | 267.9 | 5.3 | 0.241x | 11.583x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.9 | 1,057.0 | 1,090.1 | 12.0 | 1.000x | 48.066x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 14.1 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.044x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.4 | 0.2 | 0.103x | 2.329x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 32.9 | 33.9 | 0.5 | 0.112x | 2.532x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.7 | 35.9 | 0.4 | 0.116x | 2.626x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.6 | 294.0 | 298.7 | 1.7 | 0.981x | 22.193x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.2 | 297.0 | 314.7 | 6.4 | 1.000x | 22.615x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 29.5 | 30.3 | 0.3 | 0.028x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.3 | 0.2 | 0.028x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 54.3 | 54.1 | 63.6 | 3.8 | 0.051x | 1.811x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.2 | 70.4 | 77.9 | 2.5 | 0.068x | 2.412x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 332.3 | 330.6 | 334.2 | 1.5 | 0.313x | 11.092x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 332.6 | 326.3 | 432.4 | 40.6 | 0.313x | 11.104x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.0 | 1,057.5 | 1,080.6 | 8.0 | 1.000x | 35.451x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 0.045x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.097x | 2.151x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.4 | 45.3 | 47.3 | 0.7 | 0.129x | 2.869x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.4 | 53.1 | 57.6 | 1.8 | 0.160x | 3.547x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.8 | 352.4 | 361.4 | 2.9 | 0.993x | 22.056x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 359.4 | 349.7 | 380.0 | 10.1 | 1.000x | 22.215x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.4 | 26.9 | 0.2 | 0.021x | 1.012x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.4 | 48.2 | 48.6 | 0.1 | 0.037x | 1.838x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.6 | 71.1 | 79.1 | 3.0 | 0.055x | 2.719x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 381.1 | 377.0 | 381.3 | 1.6 | 0.293x | 14.462x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 383.8 | 382.6 | 388.3 | 2.1 | 0.295x | 14.565x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,299.4 | 1,294.6 | 1,301.5 | 2.4 | 1.000x | 49.313x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.4 | 0.2 | 0.051x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.110x | 2.161x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 41.6 | 47.3 | 2.1 | 0.137x | 2.692x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.9 | 48.8 | 53.1 | 1.7 | 0.164x | 3.226x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 312.6 | 307.9 | 318.2 | 3.9 | 0.984x | 19.414x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.6 | 312.5 | 334.9 | 8.1 | 1.000x | 19.721x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 26.4 | 0.2 | 0.023x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.023x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 52.9 | 1.8 | 0.043x | 1.842x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.0 | 70.7 | 78.7 | 3.1 | 0.063x | 2.704x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 357.5 | 355.7 | 363.2 | 2.9 | 0.316x | 13.619x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 359.1 | 353.5 | 364.7 | 3.9 | 0.317x | 13.680x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,133.0 | 1,129.5 | 1,140.8 | 3.7 | 1.000x | 43.162x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 21.2 | 0.4 | 0.035x | 1.004x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.6 | 26.0 | 0.2 | 0.044x | 1.270x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.9 | 26.2 | 0.1 | 0.044x | 1.291x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.0 | 0.1 | 0.068x | 1.970x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 570.5 | 565.7 | 587.3 | 7.9 | 0.970x | 28.197x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 588.2 | 573.0 | 598.6 | 8.8 | 1.000x | 29.069x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.5 | 0.2 | 0.009x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.4 | 0.1 | 0.009x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.5 | 41.2 | 42.1 | 0.3 | 0.019x | 2.176x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.1 | 97.4 | 101.1 | 1.4 | 0.045x | 5.144x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 176.1 | 174.4 | 181.1 | 2.3 | 0.081x | 9.235x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 179.5 | 178.8 | 183.2 | 1.7 | 0.083x | 9.417x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,170.6 | 2,151.6 | 2,185.1 | 10.7 | 1.000x | 113.856x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.1 | 0.0 | 0.029x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.6 | 44.8 | 0.4 | 0.055x | 1.899x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 127.1 | 123.5 | 127.6 | 1.5 | 0.159x | 5.509x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 128.4 | 115.5 | 132.9 | 6.4 | 0.161x | 5.563x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 791.9 | 790.9 | 794.5 | 1.3 | 0.992x | 34.313x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 798.4 | 786.8 | 815.9 | 10.2 | 1.000x | 34.597x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.2 | 25.5 | 0.1 | 0.008x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 52.8 | 1.8 | 0.016x | 1.910x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 133.0 | 134.5 | 0.6 | 0.044x | 5.247x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 703.6 | 686.3 | 705.6 | 7.2 | 0.234x | 27.725x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 714.5 | 710.8 | 722.1 | 3.7 | 0.238x | 28.156x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,007.1 | 2,991.5 | 3,018.2 | 9.6 | 1.000x | 118.501x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.7 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 13.0 | 0.2 | 0.060x | 1.006x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.6 | 0.2 | 0.125x | 2.090x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 25.1 | 27.4 | 0.9 | 0.126x | 2.110x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.141x | 2.346x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.7 | 204.6 | 216.4 | 4.4 | 0.990x | 16.532x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.7 | 206.1 | 221.5 | 6.0 | 1.000x | 16.693x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 27.1 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.2 | 0.1 | 0.037x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.1 | 50.8 | 0.2 | 0.069x | 1.885x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 65.7 | 72.5 | 2.7 | 0.094x | 2.578x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 240.9 | 238.9 | 241.2 | 1.1 | 0.328x | 8.975x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 242.2 | 238.3 | 246.8 | 3.3 | 0.330x | 9.021x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.5 | 721.7 | 738.0 | 6.6 | 1.000x | 27.325x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.2 | 0.043x | 1.007x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.9 | 0.2 | 0.094x | 2.222x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.7 | 40.2 | 41.2 | 0.4 | 0.118x | 2.783x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.9 | 39.7 | 42.5 | 1.0 | 0.121x | 2.865x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 337.5 | 336.0 | 339.8 | 1.4 | 0.975x | 23.090x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 346.1 | 334.1 | 360.6 | 9.4 | 1.000x | 23.679x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 21.1 | 20.9 | 21.4 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 20.7 | 21.5 | 0.3 | 0.017x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 44.2 | 43.9 | 53.0 | 3.6 | 0.036x | 2.095x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.8 | 66.2 | 76.2 | 3.5 | 0.056x | 3.212x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 294.2 | 290.4 | 298.7 | 2.7 | 0.242x | 13.943x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 310.4 | 306.0 | 313.7 | 2.7 | 0.255x | 14.709x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,215.0 | 1,204.7 | 1,222.0 | 6.7 | 1.000x | 57.582x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.3 | 0.1 | 0.047x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.047x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 44.1 | 43.6 | 44.2 | 0.2 | 0.089x | 1.917x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.7 | 71.4 | 71.8 | 0.1 | 0.145x | 3.111x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.1 | 74.0 | 74.7 | 0.3 | 0.150x | 3.215x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 485.4 | 484.5 | 502.3 | 6.8 | 0.983x | 21.075x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 494.0 | 486.1 | 495.4 | 3.6 | 1.000x | 21.448x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.7 | 27.1 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.1 | 0.015x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.5 | 50.8 | 0.1 | 0.028x | 1.891x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.7 | 90.3 | 98.6 | 2.9 | 0.053x | 3.580x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 577.9 | 574.0 | 586.2 | 4.6 | 0.319x | 21.608x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 611.8 | 584.3 | 613.4 | 10.9 | 0.337x | 22.876x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,813.6 | 1,799.7 | 1,818.1 | 6.8 | 1.000x | 67.816x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 0.059x | 1.006x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 27.8 | 0.7 | 0.128x | 2.195x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.8 | 0.3 | 0.129x | 2.203x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.2 | 27.2 | 0.4 | 0.129x | 2.218x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 204.2 | 198.6 | 211.9 | 4.5 | 1.000x | 17.142x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.0 | 202.1 | 207.7 | 1.8 | 1.004x | 17.213x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.8 | 0.3 | 0.063x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 59.2 | 59.0 | 59.4 | 0.1 | 0.063x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 99.7 | 98.9 | 100.6 | 0.6 | 0.106x | 1.689x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 105.7 | 112.6 | 2.5 | 0.115x | 1.820x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 113.1 | 112.4 | 114.0 | 0.5 | 0.121x | 1.916x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 244.5 | 243.3 | 278.8 | 13.8 | 0.261x | 4.140x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 937.3 | 927.6 | 939.4 | 4.5 | 1.000x | 15.876x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.2 | 0.1 | 0.660x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.4 | 0.1 | 0.725x | 1.098x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.0 | 0.746x | 1.132x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.747x | 1.132x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.1 | 33.6 | 35.0 | 0.5 | 0.977x | 1.482x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.2 | 38.8 | 2.0 | 1.000x | 1.516x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 48.4 | 47.1 | 48.7 | 0.6 | 1.387x | 2.102x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.9 | 23.7 | 24.0 | 0.1 | 0.659x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 23.9 | 23.8 | 25.0 | 0.5 | 0.659x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.0 | 39.0 | 1.4 | 1.000x | 1.518x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.2 | 47.6 | 4.5 | 1.005x | 1.525x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 47.8 | 47.6 | 48.5 | 0.4 | 1.317x | 1.998x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 197.2 | 194.8 | 199.7 | 1.8 | 5.430x | 8.240x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 198.0 | 196.4 | 200.4 | 1.4 | 5.450x | 8.271x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.2 | 0.3 | 0.350x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 11.3 | 0.3 | 0.355x | 1.014x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.1 | 15.0 | 15.6 | 0.2 | 0.500x | 1.428x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.4 | 0.0 | 0.543x | 1.551x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 22.9 | 23.1 | 0.1 | 0.766x | 2.188x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 29.6 | 0.3 | 0.972x | 2.776x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 28.9 | 30.4 | 0.5 | 1.000x | 2.856x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.8 | 19.4 | 0.2 | 0.507x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.5 | 19.3 | 0.3 | 0.511x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.2 | 36.3 | 40.7 | 1.6 | 1.000x | 1.972x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 37.1 | 47.8 | 4.2 | 1.007x | 1.985x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.3 | 41.3 | 41.5 | 0.1 | 1.113x | 2.194x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 142.8 | 142.6 | 147.4 | 1.9 | 3.842x | 7.575x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 143.9 | 142.7 | 144.4 | 0.7 | 3.871x | 7.633x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.8 | 13.3 | 14.3 | 0.4 | 0.066x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.9 | 13.6 | 14.7 | 0.4 | 0.066x | 1.006x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.5 | 16.9 | 17.7 | 0.3 | 0.083x | 1.264x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.9 | 0.1 | 0.090x | 1.358x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.3 | 29.0 | 29.5 | 0.2 | 0.140x | 2.117x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 208.5 | 205.9 | 217.9 | 4.2 | 0.994x | 15.076x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 209.7 | 208.1 | 212.7 | 1.7 | 1.000x | 15.163x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 13.2 | 0.5 | 0.056x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 12.1 | 11.9 | 13.1 | 0.5 | 0.056x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.5 | 0.3 | 0.133x | 2.393x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 53.2 | 51.3 | 58.2 | 2.4 | 0.245x | 4.400x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 61.5 | 61.1 | 63.0 | 0.6 | 0.283x | 5.093x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 67.8 | 67.2 | 68.8 | 0.6 | 0.312x | 5.610x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.4 | 214.8 | 218.1 | 1.1 | 1.000x | 17.986x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.6 | 13.0 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.0 | 0.1 | 0.084x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.3 | 25.3 | 0.8 | 0.155x | 1.845x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.4 | 23.9 | 0.2 | 0.155x | 1.847x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.192x | 2.285x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 152.4 | 150.8 | 158.2 | 2.6 | 1.000x | 11.919x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.6 | 148.5 | 155.1 | 2.3 | 1.008x | 12.015x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 71.1 | 71.0 | 71.2 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 71.1 | 71.8 | 0.3 | 0.067x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 100.4 | 98.9 | 107.0 | 3.1 | 0.094x | 1.411x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 147.8 | 147.0 | 149.0 | 0.8 | 0.138x | 2.079x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 160.5 | 160.0 | 162.3 | 0.8 | 0.150x | 2.258x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 268.3 | 267.3 | 302.6 | 13.6 | 0.251x | 3.774x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.4 | 1,060.9 | 1,071.8 | 4.1 | 1.000x | 15.054x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.2 | 0.3 | 0.344x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.6 | 0.1 | 0.348x | 1.012x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.0 | 14.9 | 15.9 | 0.4 | 0.499x | 1.450x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.542x | 1.575x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 22.9 | 22.8 | 23.1 | 0.1 | 0.761x | 2.209x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.5 | 0.1 | 0.978x | 2.840x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 29.2 | 30.8 | 0.5 | 1.000x | 2.904x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.1 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 61.9 | 0.1 | 0.115x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 71.4 | 70.0 | 87.0 | 6.3 | 0.133x | 1.156x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 77.2 | 87.3 | 3.8 | 0.144x | 1.259x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 87.8 | 87.0 | 100.0 | 5.0 | 0.163x | 1.421x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.9 | 250.5 | 253.9 | 1.3 | 0.466x | 4.062x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.8 | 538.2 | 546.0 | 3.5 | 1.000x | 8.723x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.6 | 12.8 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.084x | 1.007x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.6 | 23.8 | 0.1 | 0.156x | 1.871x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 24.0 | 23.3 | 24.7 | 0.5 | 0.158x | 1.898x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.1 | 29.1 | 29.2 | 0.0 | 0.192x | 2.305x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 151.6 | 150.0 | 157.9 | 2.9 | 1.000x | 12.002x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 152.5 | 147.8 | 155.3 | 2.4 | 1.006x | 12.074x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 26.2 | 0.2 | 0.052x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.5 | 50.1 | 61.4 | 4.4 | 0.101x | 1.951x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 65.5 | 73.0 | 2.5 | 0.137x | 2.633x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 223.7 | 222.8 | 232.0 | 3.5 | 0.448x | 8.647x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 227.7 | 224.9 | 255.7 | 11.6 | 0.456x | 8.802x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 499.0 | 497.7 | 510.5 | 4.8 | 1.000x | 19.288x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.8 | 22.7 | 0.4 | 0.046x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 22.0 | 0.1 | 0.046x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.1 | 41.9 | 0.3 | 0.087x | 1.895x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 49.8 | 54.7 | 1.8 | 0.107x | 2.321x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.6 | 51.9 | 53.5 | 0.5 | 0.111x | 2.416x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 467.4 | 464.4 | 472.3 | 2.8 | 0.987x | 21.460x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.7 | 468.1 | 486.2 | 7.6 | 1.000x | 21.749x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 18.9 | 18.8 | 19.4 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.9 | 19.3 | 0.1 | 0.011x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.5 | 41.4 | 41.7 | 0.1 | 0.024x | 2.200x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.5 | 85.0 | 93.1 | 3.1 | 0.049x | 4.534x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 350.0 | 347.4 | 350.5 | 1.1 | 0.200x | 18.558x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 360.9 | 356.5 | 366.6 | 3.3 | 0.207x | 19.135x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.8 | 1,737.9 | 1,758.3 | 7.0 | 1.000x | 92.568x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.029x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.033x | 1.136x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.7 | 26.1 | 27.1 | 0.4 | 0.034x | 1.158x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.5 | 44.3 | 0.3 | 0.055x | 1.900x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.7 | 780.8 | 800.2 | 7.6 | 0.989x | 34.084x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 794.5 | 783.2 | 807.3 | 9.0 | 1.000x | 34.467x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.4 | 20.3 | 20.5 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 20.7 | 20.5 | 20.7 | 0.1 | 0.007x | 1.014x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 43.7 | 43.4 | 44.1 | 0.3 | 0.014x | 2.143x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.3 | 116.7 | 119.8 | 1.0 | 0.039x | 5.805x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 187.2 | 184.1 | 192.1 | 3.0 | 0.062x | 9.187x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 188.5 | 185.6 | 189.2 | 1.6 | 0.062x | 9.251x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,034.5 | 3,008.6 | 3,060.5 | 19.5 | 1.000x | 148.885x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.044x | 1.006x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 17.0 | 17.8 | 0.3 | 0.057x | 1.311x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 18.8 | 0.0 | 0.062x | 1.423x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.9 | 31.1 | 32.2 | 0.4 | 0.106x | 2.423x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.5 | 290.4 | 299.5 | 3.1 | 0.987x | 22.584x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.4 | 293.1 | 317.7 | 8.7 | 1.000x | 22.879x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 12.9 | 0.2 | 0.016x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 13.3 | 0.3 | 0.016x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 33.6 | 32.9 | 34.0 | 0.4 | 0.042x | 2.652x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.6 | 60.0 | 68.7 | 3.1 | 0.077x | 4.867x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 88.6 | 86.0 | 92.4 | 2.1 | 0.110x | 7.003x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 90.6 | 88.5 | 92.7 | 1.5 | 0.113x | 7.156x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.6 | 801.4 | 812.2 | 3.7 | 1.000x | 63.503x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.4 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.3 | 12.5 | 0.1 | 0.086x | 1.015x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.0 | 21.0 | 21.5 | 0.2 | 0.146x | 1.724x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.0 | 0.155x | 1.835x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 27.6 | 27.4 | 27.9 | 0.2 | 0.192x | 2.268x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.8 | 142.0 | 145.1 | 1.3 | 1.000x | 11.826x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 143.8 | 142.6 | 148.1 | 2.0 | 1.000x | 11.826x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.5 | 68.4 | 68.7 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.2 | 0.3 | 0.067x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.6 | 97.2 | 105.6 | 3.1 | 0.096x | 1.439x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 127.8 | 126.7 | 128.9 | 0.7 | 0.124x | 1.864x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 140.2 | 139.4 | 185.1 | 17.9 | 0.136x | 2.045x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 264.8 | 263.7 | 293.0 | 11.4 | 0.257x | 3.863x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,019.9 | 1,039.8 | 7.3 | 1.000x | 15.047x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 15.0 | 0.2 | 0.048x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.7 | 14.7 | 0.0 | 0.048x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.7 | 0.1 | 0.108x | 2.233x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.1 | 43.8 | 1.0 | 0.138x | 2.860x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.2 | 40.4 | 44.5 | 1.3 | 0.139x | 2.887x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.0 | 298.6 | 301.4 | 1.1 | 0.990x | 20.550x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 303.1 | 296.8 | 309.7 | 4.4 | 1.000x | 20.765x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 53.7 | 53.4 | 53.8 | 0.2 | 0.033x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 53.7 | 53.7 | 54.3 | 0.2 | 0.033x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 103.9 | 102.5 | 112.1 | 3.5 | 0.064x | 1.936x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 233.3 | 232.5 | 244.9 | 4.6 | 0.143x | 4.348x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 297.8 | 290.7 | 302.6 | 4.4 | 0.182x | 5.549x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 299.2 | 297.8 | 302.5 | 1.9 | 0.183x | 5.575x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,632.5 | 1,617.5 | 1,637.8 | 7.4 | 1.000x | 30.423x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.4 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.3 | 12.8 | 0.2 | 0.086x | 1.023x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.0 | 22.3 | 0.4 | 0.150x | 1.786x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 22.5 | 0.1 | 0.155x | 1.839x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 27.4 | 27.3 | 27.9 | 0.2 | 0.189x | 2.255x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.2 | 138.7 | 145.1 | 2.1 | 0.984x | 11.711x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 144.6 | 143.7 | 148.0 | 1.5 | 1.000x | 11.906x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.9 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.0 | 0.2 | 0.068x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 106.7 | 3.4 | 0.097x | 1.439x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 127.6 | 126.9 | 128.1 | 0.5 | 0.126x | 1.859x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 139.4 | 138.8 | 139.9 | 0.4 | 0.137x | 2.031x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 265.1 | 263.0 | 292.5 | 11.3 | 0.261x | 3.863x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.0 | 1,006.3 | 1,023.0 | 6.1 | 1.000x | 14.773x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.7 | 0.2 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.949x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.9 | 0.4 | 0.088x | 1.955x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.2 | 0.1 | 0.104x | 2.311x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.2 | 302.0 | 2.9 | 0.996x | 22.060x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.2 | 293.1 | 316.4 | 8.3 | 1.000x | 22.160x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 19.8 | 19.5 | 19.9 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.1 | 19.7 | 20.1 | 0.2 | 0.019x | 1.014x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.4 | 41.3 | 42.4 | 0.4 | 0.039x | 2.090x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.8 | 68.2 | 81.1 | 5.0 | 0.064x | 3.473x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 176.3 | 175.4 | 178.9 | 1.2 | 0.165x | 8.906x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 180.9 | 180.5 | 184.9 | 1.7 | 0.169x | 9.134x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,071.8 | 1,066.7 | 1,085.4 | 6.5 | 1.000x | 54.134x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.088x | 1.959x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.8 | 0.4 | 0.088x | 1.960x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 34.0 | 1.2 | 0.105x | 2.320x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.9 | 294.2 | 316.3 | 8.3 | 1.000x | 22.165x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.0 | 292.8 | 300.2 | 2.8 | 1.000x | 22.171x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 15.3 | 0.3 | 0.014x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.4 | 15.4 | 0.4 | 0.014x | 1.016x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.1 | 37.9 | 38.3 | 0.1 | 0.036x | 2.617x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 67.2 | 74.9 | 2.9 | 0.063x | 4.632x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 167.5 | 165.8 | 171.3 | 2.1 | 0.157x | 11.499x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 168.0 | 166.6 | 182.8 | 6.1 | 0.157x | 11.531x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,056.4 | 1,080.2 | 7.8 | 1.000x | 73.292x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.8 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.4 | 13.5 | 0.1 | 0.045x | 1.008x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.9 | 26.2 | 0.1 | 0.088x | 1.962x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.7 | 26.9 | 0.4 | 0.088x | 1.962x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 33.1 | 0.9 | 0.104x | 2.321x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.5 | 291.6 | 302.0 | 3.5 | 0.994x | 22.193x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.3 | 294.9 | 315.0 | 7.5 | 1.000x | 22.321x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.5 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.3 | 15.8 | 0.5 | 0.014x | 1.009x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.2 | 38.0 | 38.3 | 0.1 | 0.036x | 2.644x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.3 | 67.1 | 75.4 | 3.3 | 0.063x | 4.667x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 168.2 | 165.8 | 169.5 | 1.3 | 0.157x | 11.655x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 169.3 | 164.5 | 170.0 | 2.1 | 0.158x | 11.732x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.4 | 1,057.2 | 1,078.9 | 7.5 | 1.000x | 74.041x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.2 | 13.5 | 0.1 | 0.045x | 1.011x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.958x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.9 | 0.4 | 0.088x | 1.969x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.6 | 31.2 | 0.2 | 0.104x | 2.327x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.6 | 292.6 | 297.2 | 1.8 | 0.993x | 22.134x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.6 | 295.2 | 315.8 | 7.8 | 1.000x | 22.285x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 14.3 | 14.2 | 14.5 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 15.5 | 0.4 | 0.014x | 1.020x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 37.9 | 37.9 | 38.1 | 0.1 | 0.036x | 2.652x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 66.9 | 77.0 | 3.9 | 0.063x | 4.717x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 167.4 | 166.0 | 170.5 | 1.5 | 0.157x | 11.702x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 169.9 | 166.4 | 171.1 | 1.8 | 0.159x | 11.872x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,048.7 | 1,075.0 | 10.3 | 1.000x | 74.635x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 0.045x | 1.007x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.970x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.7 | 26.8 | 0.4 | 0.088x | 1.977x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 31.2 | 0.2 | 0.104x | 2.337x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 293.6 | 302.6 | 3.4 | 0.985x | 22.176x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 294.7 | 310.8 | 5.8 | 1.000x | 22.511x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 16.4 | 16.1 | 16.9 | 0.2 | 0.015x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 17.1 | 0.3 | 0.015x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.1 | 38.1 | 38.3 | 0.1 | 0.036x | 2.324x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.4 | 67.2 | 77.1 | 3.8 | 0.063x | 4.114x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 158.5 | 156.6 | 159.9 | 1.1 | 0.149x | 9.671x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 159.9 | 159.0 | 162.8 | 1.5 | 0.150x | 9.752x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.0 | 1,056.1 | 1,075.7 | 6.7 | 1.000x | 64.910x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,668.3 | 7,662.7 | 7,670.7 | 2.9 | 0.778x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,668.9 | 7,665.5 | 7,673.1 | 2.7 | 0.778x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,807.6 | 9,803.5 | 9,928.5 | 48.1 | 0.995x | 1.279x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,855.2 | 9,806.5 | 12,656.5 | 1,195.4 | 1.000x | 1.285x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,068.7 | 19,066.2 | 19,079.4 | 4.8 | 1.935x | 2.487x |
| 6 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,079.8 | 19,077.0 | 19,143.2 | 25.7 | 1.936x | 2.488x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 36,469.8 | 36,450.4 | 36,525.9 | 27.0 | 3.701x | 4.756x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,888.7 | 5,860.8 | 5,899.5 | 13.0 | 0.081x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,269.8 | 6,209.5 | 6,282.4 | 26.0 | 0.086x | 1.065x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,460.4 | 7,458.6 | 7,505.9 | 18.6 | 0.103x | 1.267x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,464.5 | 7,464.1 | 7,483.6 | 7.6 | 0.103x | 1.268x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 14,333.4 | 14,326.6 | 14,342.3 | 6.1 | 0.197x | 2.434x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,378.4 | 72,269.0 | 74,027.3 | 754.0 | 0.996x | 12.291x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,689.9 | 72,672.9 | 73,928.7 | 484.2 | 1.000x | 12.344x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,548.8 | 9,546.9 | 9,559.4 | 4.6 | 0.060x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,554.9 | 9,554.3 | 9,574.7 | 7.9 | 0.060x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,701.6 | 13,698.1 | 13,730.8 | 12.2 | 0.086x | 1.435x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,706.2 | 13,693.4 | 13,720.6 | 8.9 | 0.086x | 1.435x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 18,308.2 | 18,303.8 | 18,315.8 | 4.4 | 0.115x | 1.917x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 158,736.5 | 158,161.5 | 159,418.1 | 434.7 | 1.000x | 16.624x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,127.1 | 157,791.5 | 162,247.5 | 1,654.8 | 1.002x | 16.665x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,633.0 | 7,631.9 | 7,639.4 | 3.1 | 0.810x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,637.4 | 7,632.5 | 7,659.4 | 10.0 | 0.811x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,415.1 | 9,403.1 | 9,437.9 | 11.6 | 1.000x | 1.233x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,419.3 | 9,412.3 | 9,426.6 | 4.7 | 1.000x | 1.234x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 18,172.2 | 18,164.9 | 18,198.1 | 11.7 | 1.929x | 2.381x |
| 6 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,044.4 | 19,039.5 | 19,053.2 | 5.3 | 2.022x | 2.495x |
| 7 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,055.3 | 19,053.8 | 19,057.1 | 1.3 | 2.023x | 2.496x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,736.4 | 3,733.8 | 3,741.9 | 2.7 | 0.084x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,737.9 | 3,737.4 | 3,740.2 | 1.0 | 0.084x | 1.000x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,132.8 | 6,130.4 | 6,134.4 | 1.5 | 0.138x | 1.641x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,590.8 | 6,537.0 | 6,909.6 | 136.0 | 0.148x | 1.764x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 7,234.0 | 7,227.8 | 7,261.0 | 12.0 | 0.163x | 1.936x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,486.7 | 44,477.2 | 45,695.2 | 497.0 | 1.000x | 11.906x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,565.1 | 44,446.3 | 44,670.6 | 90.2 | 1.002x | 11.927x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.049x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.3 | 0.0 | 0.050x | 1.010x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 35.6 | 34.8 | 36.3 | 0.6 | 0.109x | 2.212x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.0 | 45.5 | 0.8 | 0.135x | 2.725x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.9 | 48.8 | 53.2 | 1.6 | 0.154x | 3.104x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.3 | 320.1 | 328.3 | 2.9 | 0.989x | 19.977x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 325.0 | 317.0 | 333.0 | 5.1 | 1.000x | 20.204x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 4,577.9 | 4,575.3 | 4,607.8 | 12.4 | 0.042x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,787.6 | 4,787.1 | 4,790.1 | 1.1 | 0.043x | 1.046x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,788.9 | 4,788.0 | 4,790.6 | 1.0 | 0.043x | 1.046x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,847.9 | 6,844.0 | 6,852.5 | 3.2 | 0.062x | 1.496x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,847.9 | 6,846.3 | 6,856.6 | 4.7 | 0.062x | 1.496x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109,919.6 | 108,684.5 | 110,183.5 | 547.2 | 0.997x | 24.011x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,242.2 | 109,781.6 | 110,939.9 | 446.6 | 1.000x | 24.082x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,643.7 | 7,642.9 | 7,646.9 | 1.5 | 0.080x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,650.2 | 7,648.0 | 7,651.8 | 1.4 | 0.080x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,575.4 | 10,571.2 | 10,615.4 | 16.8 | 0.111x | 1.384x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,582.4 | 10,573.2 | 10,663.4 | 39.3 | 0.111x | 1.384x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 14,686.5 | 14,675.7 | 14,918.9 | 94.4 | 0.154x | 1.921x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94,708.6 | 94,592.0 | 95,802.6 | 542.7 | 0.994x | 12.390x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,310.1 | 94,721.9 | 95,982.9 | 470.3 | 1.000x | 12.469x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.9 | 0.2 | 0.357x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.9 | 0.2 | 0.359x | 1.005x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.5 | 15.1 | 16.1 | 0.4 | 0.528x | 1.478x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.557x | 1.559x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 23.3 | 22.9 | 23.9 | 0.3 | 0.794x | 2.221x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 29.0 | 29.8 | 0.4 | 0.991x | 2.771x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.7 | 0.2 | 1.000x | 2.798x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.2 | 21.8 | 0.2 | 0.038x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 21.4 | 21.1 | 22.4 | 0.4 | 0.038x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.3 | 48.2 | 48.5 | 0.1 | 0.086x | 2.254x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.0 | 61.4 | 71.4 | 3.8 | 0.110x | 2.896x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 227.3 | 224.8 | 229.1 | 1.6 | 0.404x | 10.614x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 228.8 | 224.8 | 231.0 | 2.1 | 0.407x | 10.683x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.1 | 553.4 | 580.2 | 8.8 | 1.000x | 26.247x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 35.0 | 0.5 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.8 | 0.0 | 0.052x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 66.7 | 66.6 | 67.0 | 0.2 | 0.102x | 1.981x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.8 | 67.5 | 68.2 | 0.3 | 0.104x | 2.015x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.9 | 171.2 | 172.6 | 0.5 | 0.263x | 5.106x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.3 | 647.6 | 667.6 | 7.8 | 1.000x | 19.409x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 659.4 | 653.3 | 669.0 | 5.5 | 1.009x | 19.591x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 61.4 | 61.1 | 62.1 | 0.3 | 0.092x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 62.3 | 62.3 | 62.4 | 0.1 | 0.094x | 1.014x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.4 | 63.2 | 0.3 | 0.094x | 1.019x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 80.5 | 80.3 | 80.8 | 0.2 | 0.121x | 1.310x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 79.1 | 88.9 | 3.5 | 0.125x | 1.357x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.4 | 249.3 | 258.2 | 3.3 | 0.377x | 4.075x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 664.9 | 659.9 | 667.4 | 2.5 | 1.000x | 10.824x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.051x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.5 | 0.1 | 0.051x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.5 | 70.9 | 74.0 | 1.2 | 0.112x | 2.213x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 81.7 | 81.0 | 82.3 | 0.6 | 0.128x | 2.529x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.8 | 170.5 | 0.3 | 0.266x | 5.261x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.8 | 635.0 | 644.5 | 3.2 | 0.999x | 19.748x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638.2 | 630.8 | 645.8 | 6.5 | 1.000x | 19.760x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.2 | 58.2 | 60.3 | 0.8 | 0.090x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.090x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.8 | 79.9 | 88.9 | 4.1 | 0.125x | 1.388x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 88.0 | 88.0 | 88.1 | 0.0 | 0.136x | 1.511x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 90.1 | 91.4 | 0.5 | 0.140x | 1.550x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 276.4 | 273.6 | 295.1 | 7.9 | 0.429x | 4.747x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 644.7 | 635.0 | 647.7 | 5.2 | 1.000x | 11.070x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.0 | 0.040x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 17.0 | 0.1 | 0.041x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.0 | 18.8 | 0.3 | 0.044x | 1.083x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.7 | 20.9 | 0.1 | 0.050x | 1.238x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 129.3 | 128.8 | 129.8 | 0.3 | 0.312x | 7.707x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.2 | 410.3 | 424.4 | 4.9 | 1.000x | 24.698x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 418.6 | 412.3 | 422.2 | 3.2 | 1.011x | 24.958x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.1 | 23.3 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 25.6 | 0.9 | 0.057x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.7 | 23.8 | 0.1 | 0.058x | 1.021x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.1 | 0.0 | 0.063x | 1.121x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 59.0 | 56.3 | 67.5 | 3.9 | 0.144x | 2.544x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 179.0 | 178.7 | 188.0 | 3.6 | 0.436x | 7.715x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 410.9 | 406.6 | 415.6 | 3.2 | 1.000x | 17.711x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 14.0 | 0.6 | 0.060x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.9 | 12.5 | 14.7 | 0.8 | 0.061x | 1.023x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.0 | 0.124x | 2.074x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 27.8 | 25.1 | 28.4 | 1.2 | 0.132x | 2.206x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.4 | 0.1 | 0.139x | 2.313x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 210.6 | 205.8 | 212.6 | 2.4 | 1.000x | 16.696x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212.7 | 206.5 | 223.5 | 6.0 | 1.010x | 16.863x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 27.2 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 28.6 | 0.6 | 0.038x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.3 | 50.8 | 0.2 | 0.070x | 1.865x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.5 | 68.3 | 73.8 | 2.0 | 0.096x | 2.561x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 243.2 | 243.2 | 245.4 | 0.9 | 0.336x | 8.968x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 246.7 | 241.9 | 252.7 | 3.7 | 0.341x | 9.097x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.0 | 711.0 | 737.7 | 9.4 | 1.000x | 26.655x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.9 | 27.9 | 28.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.2 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.3 | 42.0 | 42.7 | 0.3 | 0.078x | 1.514x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.4 | 44.1 | 44.7 | 0.2 | 0.082x | 1.591x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 158.2 | 157.9 | 158.5 | 0.2 | 0.292x | 5.668x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 540.6 | 533.2 | 545.8 | 4.6 | 0.999x | 19.367x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.0 | 537.4 | 547.8 | 3.8 | 1.000x | 19.381x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 48.7 | 0.1 | 0.089x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.2 | 48.4 | 0.1 | 0.089x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 50.2 | 49.2 | 50.5 | 0.5 | 0.092x | 1.037x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 70.5 | 70.2 | 71.2 | 0.3 | 0.130x | 1.458x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 74.6 | 86.1 | 4.2 | 0.143x | 1.606x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 228.3 | 227.1 | 252.8 | 9.9 | 0.421x | 4.720x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.4 | 538.1 | 543.6 | 2.1 | 1.000x | 11.212x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.5 | 55.6 | 0.0 | 0.100x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.2 | 56.4 | 0.4 | 0.100x | 1.004x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.8 | 55.4 | 57.3 | 0.7 | 0.100x | 1.005x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.2 | 58.7 | 0.5 | 0.104x | 1.044x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 217.5 | 216.8 | 221.4 | 1.6 | 0.390x | 3.917x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 557.3 | 555.8 | 565.7 | 3.6 | 1.000x | 10.037x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.5 | 550.1 | 568.4 | 7.0 | 1.008x | 10.113x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 64.1 | 64.0 | 64.9 | 0.3 | 0.115x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 90.1 | 89.7 | 90.5 | 0.3 | 0.161x | 1.404x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.4 | 88.4 | 97.4 | 3.1 | 0.162x | 1.410x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.5 | 110.2 | 0.2 | 0.197x | 1.710x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 109.7 | 109.6 | 109.9 | 0.1 | 0.197x | 1.710x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 375.3 | 374.1 | 384.1 | 3.7 | 0.673x | 5.852x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 558.0 | 554.1 | 566.5 | 4.2 | 1.000x | 8.699x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.7 | 43.4 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.6 | 43.4 | 0.3 | 0.035x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 65.1 | 64.7 | 65.3 | 0.2 | 0.054x | 1.523x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 65.1 | 64.7 | 65.6 | 0.3 | 0.054x | 1.524x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.0 | 67.0 | 67.2 | 0.1 | 0.055x | 1.567x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,212.7 | 1,178.7 | 1,220.6 | 17.0 | 1.000x | 28.375x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,224.0 | 1,180.2 | 1,271.5 | 29.8 | 1.009x | 28.638x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 89.3 | 89.3 | 89.5 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 88.9 | 90.3 | 0.5 | 0.052x | 1.005x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 139.2 | 134.3 | 143.8 | 3.5 | 0.080x | 1.558x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 149.3 | 149.0 | 149.6 | 0.2 | 0.086x | 1.672x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.8 | 169.2 | 178.6 | 3.2 | 0.099x | 1.923x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 327.8 | 323.8 | 346.0 | 7.9 | 0.189x | 3.669x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,731.7 | 1,725.9 | 1,740.8 | 5.6 | 1.000x | 19.381x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.004x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.088x | 1.978x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 25.5 | 28.6 | 1.0 | 0.090x | 2.018x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 31.0 | 0.1 | 0.104x | 2.328x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.9 | 296.5 | 305.7 | 3.5 | 1.000x | 22.400x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 301.0 | 296.9 | 305.1 | 2.9 | 1.014x | 22.706x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.4 | 21.4 | 0.4 | 0.019x | 1.006x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 44.0 | 43.4 | 44.1 | 0.3 | 0.041x | 2.147x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 68.0 | 76.6 | 3.2 | 0.064x | 3.349x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 191.7 | 187.6 | 194.3 | 2.3 | 0.178x | 9.354x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 193.4 | 188.6 | 195.4 | 2.3 | 0.179x | 9.434x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.6 | 1,068.6 | 1,092.8 | 8.3 | 1.000x | 52.620x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 31.2 | 0.2 | 0.104x | 2.322x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.1 | 0.1 | 0.118x | 2.627x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.6 | 35.1 | 36.4 | 0.5 | 0.119x | 2.670x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.9 | 295.6 | 302.4 | 2.5 | 1.000x | 22.358x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.1 | 296.0 | 304.2 | 3.4 | 1.014x | 22.672x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.7 | 0.4 | 0.025x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.2 | 0.1 | 0.025x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.5 | 50.4 | 50.7 | 0.1 | 0.047x | 1.883x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.2 | 70.7 | 77.7 | 2.5 | 0.068x | 2.730x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 305.0 | 300.8 | 308.3 | 2.7 | 0.283x | 11.369x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 306.8 | 301.1 | 317.8 | 5.8 | 0.285x | 11.435x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.1 | 1,055.2 | 1,080.5 | 9.1 | 1.000x | 40.147x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.2 | 33.6 | 0.5 | 0.051x | 1.000x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.4 | 86.2 | 86.6 | 0.2 | 0.136x | 2.671x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 88.8 | 88.8 | 88.9 | 0.0 | 0.140x | 2.747x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 169.1 | 180.1 | 4.1 | 0.267x | 5.258x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 631.8 | 625.6 | 638.4 | 4.4 | 0.993x | 19.532x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.4 | 628.8 | 639.5 | 3.8 | 1.000x | 19.676x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.8 | 0.2 | 0.091x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 59.5 | 58.4 | 59.9 | 0.7 | 0.092x | 1.020x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 68.4 | 68.1 | 74.3 | 2.4 | 0.106x | 1.172x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 97.4 | 4.0 | 0.136x | 1.499x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 90.5 | 90.4 | 90.6 | 0.1 | 0.141x | 1.552x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.9 | 231.5 | 240.6 | 3.4 | 0.360x | 3.977x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 643.9 | 636.7 | 657.9 | 7.5 | 1.000x | 11.043x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 33.0 | 0.3 | 0.051x | 1.001x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.3 | 86.2 | 86.8 | 0.2 | 0.136x | 2.673x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 88.9 | 88.8 | 89.0 | 0.1 | 0.140x | 2.753x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 170.0 | 179.2 | 3.6 | 0.267x | 5.265x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.6 | 624.8 | 641.1 | 5.9 | 0.996x | 19.616x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.2 | 625.6 | 638.0 | 4.4 | 1.000x | 19.695x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.1 | 58.5 | 0.1 | 0.091x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.1 | 60.4 | 0.9 | 0.091x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 68.4 | 67.9 | 75.3 | 2.8 | 0.107x | 1.173x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 93.4 | 2.4 | 0.136x | 1.498x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 90.6 | 90.4 | 90.9 | 0.2 | 0.141x | 1.553x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.9 | 230.9 | 239.6 | 3.5 | 0.361x | 3.977x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 641.6 | 634.3 | 653.9 | 6.7 | 1.000x | 11.001x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.7 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.5 | 0.1 | 0.046x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 75.1 | 74.7 | 75.3 | 0.2 | 0.108x | 2.319x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.5 | 84.5 | 86.6 | 0.7 | 0.123x | 2.641x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.1 | 169.7 | 180.1 | 4.8 | 0.245x | 5.284x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 696.2 | 690.0 | 707.4 | 6.4 | 0.998x | 21.506x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 697.7 | 690.4 | 704.1 | 4.9 | 1.000x | 21.554x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 60.3 | 0.8 | 0.083x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 58.8 | 0.2 | 0.084x | 1.002x |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 62.2 | 61.5 | 64.2 | 1.0 | 0.089x | 1.064x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 65.5 | 60.7 | 70.7 | 3.2 | 0.094x | 1.122x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.8 | 88.3 | 93.5 | 2.0 | 0.127x | 1.520x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 232.2 | 231.0 | 240.9 | 3.6 | 0.332x | 3.976x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 699.8 | 695.3 | 711.8 | 7.1 | 1.000x | 11.983x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.045x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 56.0 | 53.7 | 66.2 | 4.4 | 0.077x | 1.734x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72.4 | 72.3 | 72.6 | 0.1 | 0.100x | 2.243x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 169.3 | 179.3 | 3.8 | 0.235x | 5.262x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 721.4 | 714.8 | 732.3 | 5.8 | 0.996x | 22.355x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.1 | 711.0 | 728.9 | 6.6 | 1.000x | 22.436x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.5 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.6 | 0.2 | 0.080x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 65.6 | 58.2 | 74.7 | 5.7 | 0.090x | 1.127x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 69.7 | 66.7 | 74.5 | 2.5 | 0.096x | 1.196x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 82.9 | 93.3 | 4.9 | 0.115x | 1.432x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 232.0 | 230.9 | 240.5 | 3.6 | 0.320x | 3.982x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 725.5 | 723.7 | 726.3 | 1.0 | 1.000x | 12.453x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.3 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.0 | 0.3 | 0.045x | 1.003x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.8 | 53.7 | 55.2 | 0.6 | 0.074x | 1.666x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72.4 | 72.3 | 73.4 | 0.4 | 0.100x | 2.242x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.0 | 169.6 | 178.7 | 3.5 | 0.235x | 5.264x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 723.2 | 715.7 | 729.5 | 5.0 | 0.999x | 22.398x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.0 | 714.6 | 730.6 | 5.8 | 1.000x | 22.422x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.7 | 0.2 | 0.081x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.3 | 0.0 | 0.081x | 1.001x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 66.6 | 66.4 | 70.0 | 1.4 | 0.092x | 1.143x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 67.9 | 59.4 | 69.8 | 3.8 | 0.094x | 1.166x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 94.3 | 4.6 | 0.115x | 1.429x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.6 | 230.0 | 240.8 | 4.0 | 0.320x | 3.977x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.4 | 721.7 | 726.2 | 1.7 | 1.000x | 12.418x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 17.3 | 0.5 | 0.046x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.2 | 0.099x | 2.149x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.0 | 45.7 | 48.6 | 1.1 | 0.134x | 2.917x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.9 | 55.3 | 57.1 | 0.8 | 0.159x | 3.468x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.8 | 345.6 | 364.4 | 6.6 | 1.000x | 21.753x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 352.6 | 349.8 | 358.5 | 3.0 | 1.005x | 21.866x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.8 | 0.3 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.6 | 0.2 | 0.021x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.3 | 48.3 | 48.4 | 0.0 | 0.038x | 1.840x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.7 | 70.9 | 79.0 | 3.0 | 0.056x | 2.729x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 377.8 | 375.7 | 399.7 | 8.9 | 0.295x | 14.381x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 381.8 | 377.8 | 385.6 | 3.0 | 0.298x | 14.532x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,280.1 | 1,263.2 | 1,288.8 | 8.8 | 1.000x | 48.729x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.193x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.4 | 0.1 | 0.384x | 1.993x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.0 | 12.1 | 0.4 | 0.392x | 2.036x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.8 | 0.0 | 0.468x | 2.429x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.6 | 15.7 | 0.1 | 0.534x | 2.774x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 29.1 | 0.1 | 0.991x | 5.141x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.3 | 0.0 | 1.000x | 5.191x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.7 | 0.1 | 0.184x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.185x | 1.004x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 5.7 | 5.2 | 6.2 | 0.3 | 0.188x | 1.019x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 15.1 | 14.9 | 15.2 | 0.1 | 0.496x | 2.691x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.6 | 0.1 | 0.569x | 3.086x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.2 | 31.0 | 0.4 | 1.000x | 5.425x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.5 | 34.9 | 48.5 | 4.8 | 1.230x | 6.675x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.188x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.0 | 0.3 | 0.346x | 1.841x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.7 | 0.5 | 0.351x | 1.869x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.8 | 14.9 | 17.0 | 0.7 | 0.525x | 2.798x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.4 | 0.0 | 0.544x | 2.900x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 28.9 | 29.8 | 0.3 | 0.987x | 5.256x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.0 | 29.6 | 30.2 | 0.2 | 1.000x | 5.327x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 7.1 | 0.5 | 0.194x | 1.066x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 6.5 | 5.9 | 7.2 | 0.4 | 0.209x | 1.153x |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 24.9 | 0.5 | 0.763x | 4.202x |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 24.3 | 24.0 | 26.9 | 1.1 | 0.783x | 4.311x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 35.1 | 1.6 | 1.000x | 5.509x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.8 | 36.4 | 49.7 | 4.9 | 1.250x | 6.887x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.9 | 13.2 | 0.5 | 0.308x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.8 | 0.4 | 0.310x | 1.008x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 21.1 | 22.5 | 0.5 | 0.556x | 1.805x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.5 | 21.7 | 0.1 | 0.559x | 1.816x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.3 | 26.9 | 0.6 | 0.674x | 2.189x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.3 | 35.2 | 40.6 | 1.9 | 0.939x | 3.051x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 38.6 | 35.7 | 41.6 | 2.4 | 1.000x | 3.248x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.0 | 36.6 | 40.7 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.4 | 37.0 | 50.0 | 5.1 | 1.038x | 1.038x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.0 | 73.8 | 0.3 | 1.985x | 1.985x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 73.6 | 73.3 | 73.7 | 0.1 | 1.990x | 1.990x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 97.3 | 96.7 | 97.6 | 0.4 | 2.631x | 2.631x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 624.1 | 614.6 | 638.4 | 8.6 | 16.885x | 16.885x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 626.6 | 616.0 | 633.7 | 6.0 | 16.953x | 16.953x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 0.507x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.3 | 0.1 | 0.508x | 1.002x |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.4 | 21.0 | 0.2 | 0.551x | 1.088x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.8 | 23.1 | 0.1 | 0.608x | 1.200x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.1 | 35.2 | 0.4 | 0.915x | 1.807x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.8 | 35.2 | 40.1 | 1.8 | 1.000x | 1.974x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 38.2 | 38.2 | 39.0 | 0.3 | 1.010x | 1.993x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 18.4 | 0.8 | 0.450x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.1 | 17.6 | 0.5 | 0.454x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.7 | 40.3 | 1.7 | 1.000x | 2.224x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.1 | 49.7 | 5.2 | 1.006x | 2.238x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.2 | 38.2 | 38.5 | 0.1 | 1.053x | 2.343x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 123.3 | 120.6 | 124.6 | 1.4 | 3.399x | 7.561x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 126.4 | 125.6 | 127.6 | 0.7 | 3.484x | 7.751x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,578,393.8 | 3,576,939.1 | 3,579,998.5 | 1,246.8 | 0.125x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,584,125.0 | 3,575,522.4 | 3,586,988.7 | 4,723.2 | 0.125x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,700,507.0 | 3,619,299.0 | 3,704,156.4 | 32,418.7 | 0.129x | 1.034x |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 5,069,643.3 | 4,986,086.0 | 5,514,422.7 | 194,215.8 | 0.177x | 1.417x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 5,186,766.7 | 5,166,419.7 | 5,215,883.3 | 17,324.0 | 0.181x | 1.449x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 6,366,900.5 | 6,355,186.0 | 6,407,762.0 | 20,748.8 | 0.222x | 1.779x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,638,016.7 | 28,601,379.1 | 29,677,306.8 | 409,825.4 | 1.000x | 8.003x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,983.0 | 17,950.2 | 18,048.6 | 35.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,865,231.4 | 1,861,637.8 | 1,865,867.4 | 1,625.3 | 103.722x | 103.722x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,885,944.5 | 1,884,012.8 | 1,890,252.9 | 2,131.6 | 104.874x | 104.874x |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,888,192.1 | 1,884,753.9 | 1,905,477.8 | 7,414.1 | 104.999x | 104.999x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,559,712.1 | 2,540,969.5 | 2,565,705.2 | 11,254.9 | 142.340x | 142.340x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 15,989,261.3 | 15,918,127.7 | 16,089,628.7 | 66,429.2 | 889.130x | 889.130x |
| 7 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 16,108,472.3 | 15,958,645.0 | 16,485,861.3 | 192,675.5 | 895.759x | 895.759x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,933.2 | 17,893.8 | 18,022.1 | 43.7 | 1.000x | 1.000x | 5 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,868,705.8 | 1,868,221.4 | 1,869,819.8 | 555.3 | 104.204x | 104.204x | 5 | 100% |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,874,971.6 | 1,874,566.2 | 1,890,593.4 | 6,177.8 | 104.553x | 104.553x | 5 | 100% |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,875,429.5 | 1,874,090.8 | 1,890,585.2 | 6,248.7 | 104.579x | 104.579x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,818,428.0 | 2,816,233.6 | 2,822,301.8 | 2,573.3 | 157.163x | 157.163x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,942,459.5 | 1,939,161.1 | 1,946,073.1 | 2,539.5 | 0.021x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,137,544.3 | 3,124,093.6 | 3,148,941.8 | 8,618.0 | 0.033x | 1.615x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,154,491.2 | 3,123,908.6 | 3,189,887.4 | 23,889.3 | 0.034x | 1.624x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,966,791.7 | 5,961,199.2 | 6,000,178.1 | 14,414.3 | 0.064x | 3.072x |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 17,162,935.3 | 16,945,837.3 | 17,607,011.0 | 256,161.1 | 0.183x | 8.836x |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 17,416,373.0 | 16,639,741.7 | 17,620,677.7 | 354,885.3 | 0.185x | 8.966x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 93,901,018.6 | 93,759,164.2 | 99,292,858.2 | 2,164,943.1 | 1.000x | 48.341x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,971.3 | 17,957.5 | 17,984.6 | 10.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,869,164.2 | 1,866,891.0 | 1,876,262.2 | 3,331.0 | 104.008x | 104.008x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,094,784.0 | 3,079,311.4 | 3,116,634.8 | 13,242.1 | 172.207x | 172.207x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,095,320.2 | 3,087,598.5 | 3,100,842.1 | 4,652.3 | 172.237x | 172.237x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,159,050.0 | 3,155,013.8 | 3,180,387.1 | 9,183.7 | 175.783x | 175.783x |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 17,610,014.7 | 17,112,101.7 | 17,692,555.0 | 233,472.4 | 979.895x | 979.895x |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 17,636,524.3 | 16,556,841.3 | 17,675,714.3 | 441,749.5 | 981.370x | 981.370x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 151,621,570.0 | 150,070,112.0 | 160,325,170.0 | 3,773,314.3 | 5 | 47,440 | 82,131 | 13,433 | 0.025 | compiled=5 | 10,169,728.0 | 140,530,217.0 | 114,060.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,328,764.0 | 154,959,980.0 | 186,417,630.0 | 10,113,724.8 | 5 | 47,584 | 94,342 | 15,349 | 0.059 (max is trial 1) | compiled=5 | 12,979,624.0 | 158,353,199.0 | 192,941.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 557,601,392.0 | 549,327,714.0 | 569,843,521.0 | 7,315,769.4 | 5 | 39,248 | 58,359 | 56,805 | 0.013 | compiled=5 | 2,524,514.0 | 554,883,877.0 | 193,001.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 565,207,216.0 | 558,228,695.0 | 571,057,819.0 | 4,268,779.8 | 5 | 39,248 | 58,475 | 56,921 | 0.008 | compiled=5 | 2,169,652.0 | 561,344,614.0 | 200,541.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 557,938,347.0 | 546,318,699.0 | 563,311,338.0 | 6,106,183.7 | 5 | 39,248 | 58,359 | 56,805 | 0.011 | compiled=5 | 2,326,253.0 | 555,627,603.0 | 108,241.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 561,136,606.0 | 549,125,744.0 | 565,607,772.0 | 5,693,701.3 | 5 | 39,248 | 58,475 | 56,921 | 0.010 | compiled=5 | 2,209,483.0 | 558,601,840.0 | 106,210.0 |
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 164,584,146.0 | 163,200,287.0 | 172,326,812.0 | 3,438,404.2 | 5 | 48,128 | 82,455 | 13,761 | 0.021 | compiled=5 | 9,866,191.0 | 154,496,783.0 | 194,071.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 183,590,851.0 | 175,932,235.0 | 194,146,927.0 | 6,021,076.8 | 5 | 48,264 | 94,666 | 15,677 | 0.033 | compiled=5 | 12,225,066.0 | 171,279,445.0 | 198,781.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 139,949,224.0 | 130,838,550.0 | 142,838,561.0 | 4,676,626.4 | 5 | 22,832 | 17,965 | 12,968 | 0.033 | compiled=5 | 1,653,409.0 | 136,240,052.0 | 109,170.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 148,273,931.0 | 141,076,649.0 | 152,803,577.0 | 4,745,842.6 | 5 | 22,968 | 20,308 | 14,985 | 0.032 | compiled=5 | 1,822,371.0 | 146,451,511.0 | 183,361.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 128,967,530.0 | 124,322,624.0 | 137,012,847.0 | 4,823,380.7 | 5 | 22,376 | 17,258 | 17,258 | 0.037 | compiled=5 | 1,429,138.0 | 127,548,612.0 | 182,731.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 137,382,550.0 | 121,509,347.0 | 142,162,417.0 | 7,505,540.6 | 5 | 22,376 | 17,369 | 17,369 | 0.055 | compiled=5 | 1,457,899.0 | 135,826,510.0 | 98,900.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 136,759,498.0 | 133,740,580.0 | 137,964,826.0 | 1,824,242.0 | 5 | 22,376 | 17,258 | 17,258 | 0.013 | compiled=5 | 1,467,469.0 | 135,122,328.0 | 196,311.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 136,344,905.0 | 128,201,518.0 | 141,820,418.0 | 5,034,770.1 | 5 | 22,376 | 17,369 | 17,369 | 0.037 | compiled=5 | 1,755,101.0 | 133,278,078.0 | 190,831.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 146,925,846.0 | 134,069,456.0 | 156,562,775.0 | 7,227,152.4 | 5 | 27,608 | 18,106 | 13,109 | 0.049 | compiled=5 | 1,805,321.0 | 144,978,534.0 | 192,931.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 158,953,769.0 | 153,090,875.0 | 161,812,987.0 | 3,417,763.5 | 5 | 27,752 | 20,449 | 15,126 | 0.022 | compiled=5 | 1,819,561.0 | 155,299,577.0 | 213,442.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 155,645,893.0 | 148,604,192.0 | 161,597,979.0 | 5,318,300.2 | 5 | 43,304 | 81,907 | 13,380 | 0.034 | compiled=5 | 9,623,285.0 | 139,588,191.0 | 112,860.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,558,255.0 | 168,392,047.0 | 174,796,025.0 | 2,301,945.8 | 5 | 47,544 | 94,118 | 15,296 | 0.013 | compiled=5 | 11,420,075.0 | 157,236,173.0 | 193,971.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 432,550,604.0 | 423,790,122.0 | 432,981,428.0 | 3,557,204.4 | 5 | 30,976 | 47,188 | 45,801 | 0.008 | compiled=5 | 1,953,732.0 | 430,495,102.0 | 115,240.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 432,168,521.0 | 409,864,175.0 | 439,547,864.0 | 11,267,008.2 | 5 | 30,976 | 47,306 | 45,919 | 0.026 | compiled=5 | 1,929,061.0 | 430,050,959.0 | 192,691.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 437,531,255.0 | 432,370,325.0 | 447,960,387.0 | 5,531,367.4 | 5 | 30,976 | 47,188 | 45,801 | 0.013 | compiled=5 | 2,042,772.0 | 433,210,960.0 | 188,701.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 429,579,968.0 | 421,616,232.0 | 432,505,467.0 | 3,830,835.1 | 5 | 30,976 | 47,306 | 45,919 | 0.009 | compiled=5 | 2,052,033.0 | 427,185,674.0 | 197,772.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 166,883,659.0 | 162,455,282.0 | 173,020,587.0 | 4,309,592.0 | 5 | 48,088 | 82,048 | 13,521 | 0.026 | compiled=5 | 9,496,359.0 | 154,801,744.0 | 195,231.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 178,790,732.0 | 164,688,805.0 | 180,042,050.0 | 5,996,848.9 | 5 | 48,224 | 94,259 | 15,437 | 0.034 (max is trial 1) | compiled=5 | 11,568,361.0 | 159,379,703.0 | 108,781.0 |

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

