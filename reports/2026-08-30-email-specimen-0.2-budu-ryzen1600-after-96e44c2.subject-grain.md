# pcrec-bench report

reporter: v9 (2026-08-30)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-08-30T11:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 6
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-caps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-nocaps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-in-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z.jsonl) — agreement: n/a (v1.3)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 6 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.4 | 32.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.040x | 1.072x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.2 | 146.5 | 149.6 | 1.2 | 0.167x | 4.537x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 147.3 | 148.6 | 0.5 | 0.169x | 4.566x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 879.1 | 863.5 | 882.7 | 6.9 | 1.000x | 27.093x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 879.3 | 869.9 | 892.4 | 8.3 | 1.000x | 27.097x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.5 | 59.3 | 0.3 | 0.068x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.2 | 64.5 | 0.8 | 0.073x | 1.063x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 148.2 | 147.6 | 148.6 | 0.4 | 0.172x | 2.512x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 148.4 | 147.8 | 151.5 | 1.3 | 0.172x | 2.515x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.8 | 154.3 | 155.1 | 0.3 | 0.179x | 2.624x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 864.2 | 858.9 | 873.7 | 5.3 | 1.000x | 14.646x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 40.0 | 40.4 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.0 | 42.8 | 43.8 | 0.4 | 0.035x | 1.073x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.6 | 199.3 | 229.9 | 11.8 | 0.161x | 4.983x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.3 | 199.2 | 202.4 | 1.1 | 0.162x | 5.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,230.4 | 1,226.0 | 1,252.8 | 9.7 | 0.993x | 30.724x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,239.2 | 1,205.9 | 1,269.7 | 23.3 | 1.000x | 30.944x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 77.8 | 77.7 | 82.5 | 1.9 | 0.064x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 80.7 | 80.0 | 81.1 | 0.4 | 0.066x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.6 | 172.8 | 176.0 | 1.2 | 0.144x | 2.258x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 207.1 | 206.6 | 209.4 | 1.0 | 0.169x | 2.662x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 211.9 | 211.8 | 214.7 | 1.1 | 0.173x | 2.724x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,222.2 | 1,212.9 | 1,230.2 | 5.6 | 1.000x | 15.711x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.024x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.6 | 20.9 | 0.1 | 0.027x | 1.131x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.5 | 105.7 | 0.5 | 0.139x | 5.745x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.4 | 105.1 | 117.1 | 4.6 | 0.139x | 5.775x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 754.2 | 750.5 | 759.9 | 3.3 | 0.998x | 41.338x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 755.5 | 754.0 | 785.4 | 12.1 | 1.000x | 41.411x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 0.038x | 1.085x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 105.5 | 105.5 | 106.3 | 0.3 | 0.141x | 3.994x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 106.9 | 105.2 | 107.7 | 1.0 | 0.142x | 4.044x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.2 | 119.2 | 124.3 | 2.0 | 0.163x | 4.624x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.8 | 745.6 | 752.4 | 2.4 | 1.000x | 28.414x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 43.3 | 43.4 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.6 | 46.2 | 47.3 | 0.4 | 0.035x | 1.075x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 210.3 | 209.4 | 210.9 | 0.5 | 0.157x | 4.850x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 212.4 | 211.9 | 214.5 | 0.9 | 0.159x | 4.901x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,331.8 | 1,319.0 | 1,351.9 | 12.2 | 0.995x | 30.722x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,338.8 | 1,325.2 | 1,393.6 | 23.7 | 1.000x | 30.883x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 86.5 | 86.4 | 87.1 | 0.3 | 0.065x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 87.6 | 87.0 | 88.6 | 0.5 | 0.066x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.0 | 182.3 | 187.0 | 1.6 | 0.140x | 2.139x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 221.4 | 220.9 | 222.5 | 0.5 | 0.167x | 2.559x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 224.4 | 221.4 | 226.0 | 1.5 | 0.170x | 2.595x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,323.6 | 1,314.5 | 1,353.0 | 14.0 | 1.000x | 15.304x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.3 | 61.1 | 61.6 | 0.2 | 0.070x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.0 | 64.8 | 65.4 | 0.2 | 0.074x | 1.060x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 162.1 | 161.7 | 162.7 | 0.4 | 0.184x | 2.643x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 163.0 | 162.7 | 163.4 | 0.3 | 0.185x | 2.658x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.5 | 879.3 | 910.1 | 11.9 | 1.000x | 14.355x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 887.5 | 879.5 | 894.4 | 5.6 | 1.008x | 14.469x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 120.7 | 120.1 | 121.0 | 0.3 | 0.137x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 123.8 | 123.4 | 126.5 | 1.1 | 0.141x | 1.026x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.2 | 166.6 | 169.1 | 1.0 | 0.190x | 1.386x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 167.6 | 167.4 | 168.1 | 0.3 | 0.191x | 1.389x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 167.7 | 166.8 | 168.4 | 0.5 | 0.191x | 1.390x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.8 | 869.5 | 890.5 | 7.7 | 1.000x | 7.283x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.4 | 20.9 | 0.1 | 0.027x | 1.134x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.5 | 104.5 | 105.1 | 0.3 | 0.139x | 5.742x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.3 | 105.1 | 106.7 | 0.6 | 0.140x | 5.786x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 753.6 | 747.8 | 782.8 | 13.5 | 1.000x | 41.393x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 754.3 | 750.2 | 756.7 | 2.1 | 1.001x | 41.433x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 27.4 | 0.5 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 28.7 | 28.2 | 28.7 | 0.2 | 0.038x | 1.095x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 105.5 | 105.4 | 108.2 | 1.1 | 0.141x | 4.030x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 106.9 | 104.9 | 109.0 | 1.4 | 0.143x | 4.083x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.1 | 120.7 | 124.1 | 1.1 | 0.163x | 4.663x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 749.5 | 739.5 | 766.7 | 8.9 | 1.000x | 28.626x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.0 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.8 | 33.4 | 0.2 | 0.024x | 1.068x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 228.5 | 228.0 | 228.6 | 0.2 | 0.168x | 7.387x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 231.4 | 230.9 | 231.4 | 0.3 | 0.170x | 7.482x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,346.0 | 1,327.3 | 1,387.0 | 21.5 | 0.989x | 43.520x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,361.2 | 1,340.0 | 1,370.3 | 10.7 | 1.000x | 44.011x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 55.9 | 55.5 | 56.4 | 0.3 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 59.3 | 59.3 | 60.2 | 0.3 | 0.044x | 1.061x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.7 | 164.9 | 166.5 | 0.6 | 0.123x | 2.962x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 229.2 | 227.8 | 230.7 | 1.0 | 0.170x | 4.098x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 229.9 | 228.3 | 232.4 | 1.3 | 0.171x | 4.110x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,344.7 | 1,335.1 | 1,349.1 | 4.8 | 1.000x | 24.041x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.5 | 47.2 | 0.2 | 0.048x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.3 | 50.7 | 0.2 | 0.051x | 1.077x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.3 | 167.1 | 167.6 | 0.2 | 0.171x | 3.578x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 167.8 | 166.8 | 176.5 | 3.6 | 0.171x | 3.589x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 974.4 | 966.0 | 1,011.8 | 16.2 | 0.994x | 20.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 979.8 | 957.5 | 996.1 | 14.8 | 1.000x | 20.954x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 92.2 | 91.9 | 93.0 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 94.5 | 94.2 | 95.3 | 0.4 | 0.098x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.3 | 168.7 | 174.1 | 1.7 | 0.177x | 1.859x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 173.5 | 172.9 | 177.4 | 1.8 | 0.180x | 1.882x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 173.9 | 173.3 | 175.2 | 0.6 | 0.180x | 1.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 966.0 | 964.9 | 983.4 | 7.1 | 1.000x | 10.480x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.6 | 36.7 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.5 | 0.1 | 0.046x | 1.073x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.7 | 151.9 | 153.2 | 0.4 | 0.177x | 4.168x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 153.6 | 153.3 | 154.4 | 0.4 | 0.178x | 4.191x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 863.4 | 852.1 | 900.5 | 17.5 | 1.000x | 23.562x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 863.8 | 849.6 | 885.6 | 14.4 | 1.000x | 23.573x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 69.8 | 69.7 | 70.6 | 0.4 | 0.082x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 73.6 | 73.4 | 73.6 | 0.1 | 0.086x | 1.055x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 150.1 | 150.0 | 150.7 | 0.2 | 0.175x | 2.152x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 150.5 | 150.2 | 151.4 | 0.4 | 0.176x | 2.158x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.0 | 157.6 | 158.8 | 0.4 | 0.185x | 2.264x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 855.8 | 851.4 | 865.4 | 4.8 | 1.000x | 12.268x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.2 | 0.037x | 1.066x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 144.1 | 144.0 | 144.6 | 0.2 | 0.168x | 4.865x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 145.0 | 146.6 | 0.6 | 0.170x | 4.912x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 858.0 | 840.1 | 869.8 | 11.0 | 1.000x | 28.976x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 864.9 | 848.3 | 898.6 | 17.1 | 1.008x | 29.209x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.5 | 51.9 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.6 | 55.8 | 0.1 | 0.065x | 1.081x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 146.9 | 146.1 | 148.0 | 0.6 | 0.170x | 2.846x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 147.0 | 146.4 | 147.2 | 0.3 | 0.170x | 2.848x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.6 | 147.1 | 148.2 | 0.3 | 0.171x | 2.859x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.5 | 856.9 | 867.2 | 3.6 | 1.000x | 16.708x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.9 | 0.1 | 0.041x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.9 | 0.1 | 0.044x | 1.069x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 106.3 | 106.3 | 106.7 | 0.2 | 0.148x | 3.585x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.9 | 107.8 | 108.1 | 0.1 | 0.150x | 3.636x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 707.8 | 702.6 | 719.3 | 5.6 | 0.983x | 23.864x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 720.1 | 708.6 | 727.7 | 7.0 | 1.000x | 24.278x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 51.8 | 0.2 | 0.073x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 56.0 | 0.3 | 0.078x | 1.075x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 103.8 | 103.5 | 104.3 | 0.3 | 0.146x | 2.011x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 106.0 | 105.8 | 106.3 | 0.2 | 0.149x | 2.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.9 | 118.5 | 119.2 | 0.2 | 0.167x | 2.303x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 710.8 | 703.0 | 724.1 | 7.5 | 1.000x | 13.773x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.7 | 0.3 | 0.020x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.4 | 0.1 | 0.020x | 1.015x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 213.4 | 210.8 | 215.7 | 1.6 | 0.347x | 17.671x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 214.3 | 212.2 | 220.9 | 3.1 | 0.348x | 17.738x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 614.9 | 612.8 | 619.3 | 2.4 | 1.000x | 50.909x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 617.7 | 611.2 | 631.6 | 7.1 | 1.004x | 51.137x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 35.6 | 0.5 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 34.9 | 34.7 | 35.2 | 0.2 | 0.007x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.8 | 433.0 | 440.1 | 2.4 | 0.093x | 12.656x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,010.1 | 1,958.3 | 2,108.6 | 54.0 | 0.427x | 58.110x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,032.4 | 1,989.9 | 2,103.7 | 40.3 | 0.432x | 58.755x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,705.3 | 4,687.9 | 4,718.1 | 10.3 | 1.000x | 136.024x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 37.5 | 37.9 | 0.1 | 0.034x | 1.066x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.4 | 196.8 | 200.5 | 1.2 | 0.180x | 5.614x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 198.4 | 198.2 | 199.0 | 0.3 | 0.180x | 5.615x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,099.7 | 1,082.5 | 1,114.8 | 11.8 | 1.000x | 31.113x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,112.5 | 1,082.0 | 1,157.5 | 25.1 | 1.012x | 31.475x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 66.1 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.6 | 0.3 | 0.063x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.5 | 170.2 | 172.5 | 0.9 | 0.156x | 2.594x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.6 | 198.0 | 199.2 | 0.4 | 0.181x | 3.021x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 203.3 | 202.4 | 203.8 | 0.5 | 0.185x | 3.092x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,096.4 | 1,079.2 | 1,101.4 | 7.6 | 1.000x | 16.677x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 37.3 | 37.8 | 0.2 | 0.034x | 1.066x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.8 | 197.5 | 198.2 | 0.3 | 0.180x | 5.596x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.8 | 197.7 | 200.9 | 1.4 | 0.180x | 5.624x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,101.2 | 1,082.7 | 1,107.0 | 9.6 | 1.000x | 31.161x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,105.7 | 1,072.0 | 1,127.8 | 19.4 | 1.004x | 31.287x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.8 | 66.2 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.4 | 0.2 | 0.063x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.3 | 170.1 | 171.1 | 0.4 | 0.156x | 2.584x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.6 | 198.4 | 199.9 | 0.6 | 0.182x | 3.013x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 203.1 | 202.5 | 206.3 | 1.3 | 0.186x | 3.081x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.3 | 1,076.7 | 1,109.4 | 11.0 | 1.000x | 16.585x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 31.4 | 0.7 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.2 | 0.2 | 0.036x | 1.070x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 151.7 | 151.2 | 159.0 | 3.0 | 0.173x | 5.117x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 154.2 | 153.3 | 154.5 | 0.4 | 0.176x | 5.199x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 875.0 | 861.1 | 885.6 | 8.9 | 1.000x | 29.509x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.4 | 865.1 | 893.5 | 9.5 | 1.002x | 29.555x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 51.7 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.4 | 55.7 | 0.1 | 0.064x | 1.079x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.4 | 153.6 | 155.2 | 0.6 | 0.178x | 2.995x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 157.5 | 157.3 | 178.9 | 8.6 | 0.182x | 3.055x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 164.1 | 163.8 | 164.4 | 0.2 | 0.189x | 3.182x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 865.9 | 859.2 | 872.6 | 4.7 | 1.000x | 16.794x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.8 | 36.1 | 0.1 | 0.034x | 1.064x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.3 | 196.0 | 198.4 | 0.9 | 0.186x | 5.841x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.5 | 198.0 | 200.5 | 0.9 | 0.187x | 5.877x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,059.9 | 1,037.7 | 1,067.2 | 10.0 | 1.000x | 31.376x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,066.2 | 1,042.8 | 1,068.2 | 11.3 | 1.006x | 31.561x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 63.2 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.2 | 0.1 | 0.062x | 1.053x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.5 | 172.3 | 175.3 | 1.0 | 0.164x | 2.770x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.2 | 198.0 | 201.2 | 1.2 | 0.188x | 3.165x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 203.0 | 202.5 | 206.7 | 1.6 | 0.192x | 3.241x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.7 | 1,051.6 | 1,059.6 | 3.0 | 1.000x | 16.853x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.1 | 0.3 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 10.8 | 11.7 | 0.3 | 0.031x | 1.084x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.6 | 102.0 | 104.9 | 1.1 | 0.287x | 9.978x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 106.4 | 108.2 | 0.7 | 0.294x | 10.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 360.1 | 359.0 | 370.6 | 4.3 | 0.987x | 34.338x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 364.8 | 358.7 | 378.0 | 6.4 | 1.000x | 34.789x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.5 | 0.1 | 0.011x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 258.9 | 258.4 | 262.9 | 1.7 | 0.109x | 9.935x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,419.8 | 1,392.5 | 1,525.4 | 52.6 | 0.596x | 54.471x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,472.1 | 1,366.4 | 1,536.5 | 56.1 | 0.618x | 56.475x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,382.4 | 2,372.0 | 2,408.9 | 13.2 | 1.000x | 91.402x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 38.4 | 1.2 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 37.9 | 0.2 | 0.034x | 1.058x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.7 | 197.4 | 199.2 | 0.6 | 0.182x | 5.588x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.1 | 197.3 | 199.9 | 1.0 | 0.182x | 5.598x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,086.2 | 1,075.4 | 1,104.9 | 9.6 | 1.000x | 30.698x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,094.8 | 1,086.0 | 1,115.1 | 10.3 | 1.008x | 30.940x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.7 | 66.6 | 0.4 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.063x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.3 | 170.1 | 170.7 | 0.2 | 0.156x | 2.584x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.8 | 198.2 | 199.3 | 0.4 | 0.182x | 3.016x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 203.6 | 202.5 | 205.6 | 1.1 | 0.187x | 3.090x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.8 | 1,083.5 | 1,097.5 | 4.8 | 1.000x | 16.565x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.8 | 36.8 | 1.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.7 | 36.1 | 0.1 | 0.034x | 1.057x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.2 | 196.4 | 197.9 | 0.5 | 0.186x | 5.801x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.4 | 197.5 | 208.5 | 4.2 | 0.188x | 5.837x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.6 | 1,036.5 | 1,067.0 | 10.6 | 1.000x | 31.110x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,060.7 | 1,055.9 | 1,076.6 | 7.3 | 1.003x | 31.199x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.7 | 62.4 | 62.9 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 66.4 | 65.9 | 69.6 | 1.4 | 0.063x | 1.060x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.9 | 172.6 | 174.9 | 0.8 | 0.165x | 2.758x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.3 | 197.2 | 200.9 | 1.3 | 0.189x | 3.162x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 204.3 | 203.3 | 206.6 | 1.1 | 0.195x | 3.258x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,049.3 | 1,047.6 | 1,059.6 | 4.4 | 1.000x | 16.737x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.9 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 10.9 | 11.8 | 0.3 | 0.029x | 1.043x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 106.4 | 105.4 | 132.7 | 10.7 | 0.273x | 9.831x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 109.4 | 108.2 | 111.0 | 1.0 | 0.280x | 10.114x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 385.8 | 384.9 | 398.3 | 5.0 | 0.989x | 35.653x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 390.2 | 386.3 | 401.5 | 5.9 | 1.000x | 36.060x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 27.9 | 27.6 | 28.0 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.9 | 28.2 | 0.1 | 0.011x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 264.8 | 263.9 | 265.6 | 0.5 | 0.104x | 9.490x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,497.7 | 1,477.4 | 1,507.1 | 11.8 | 0.589x | 53.682x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,507.6 | 1,497.6 | 1,522.2 | 9.9 | 0.593x | 54.033x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,542.1 | 2,538.0 | 2,566.7 | 10.8 | 1.000x | 91.114x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.5 | 38.3 | 42.3 | 1.5 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 40.9 | 41.6 | 0.2 | 0.037x | 1.071x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 220.6 | 219.4 | 222.0 | 0.8 | 0.197x | 5.729x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 222.9 | 220.5 | 226.3 | 1.9 | 0.199x | 5.788x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,109.3 | 1,102.0 | 1,122.3 | 7.7 | 0.993x | 28.811x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,117.3 | 1,103.0 | 1,118.5 | 5.8 | 1.000x | 29.018x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 73.1 | 73.0 | 73.2 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 77.0 | 76.8 | 78.0 | 0.5 | 0.070x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.3 | 174.8 | 175.4 | 0.2 | 0.159x | 2.399x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 204.7 | 203.8 | 212.2 | 3.2 | 0.185x | 2.803x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 209.2 | 208.4 | 211.4 | 1.0 | 0.189x | 2.863x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,105.6 | 1,102.8 | 1,121.5 | 7.0 | 1.000x | 15.134x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 32.5 | 1.2 | 0.026x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.4 | 31.8 | 0.1 | 0.028x | 1.070x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.7 | 164.9 | 178.1 | 5.0 | 0.144x | 5.593x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 165.8 | 164.5 | 166.1 | 0.7 | 0.144x | 5.599x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,146.0 | 1,137.4 | 1,153.7 | 6.3 | 0.996x | 38.687x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,150.6 | 1,132.4 | 1,159.9 | 9.9 | 1.000x | 38.844x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.6 | 55.4 | 1.5 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 55.7 | 55.4 | 55.8 | 0.2 | 0.048x | 1.077x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.8 | 108.5 | 111.5 | 0.9 | 0.095x | 2.122x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 167.5 | 167.4 | 168.0 | 0.2 | 0.145x | 3.239x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 168.1 | 167.4 | 178.7 | 4.3 | 0.146x | 3.251x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,151.8 | 1,139.5 | 1,156.6 | 5.8 | 1.000x | 22.268x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.7 | 47.8 | 2.4 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.3 | 0.2 | 0.064x | 1.070x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 137.5 | 137.0 | 138.4 | 0.5 | 0.198x | 3.286x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 137.5 | 137.3 | 139.8 | 1.0 | 0.198x | 3.286x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.2 | 678.4 | 684.8 | 2.1 | 0.977x | 16.255x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 696.0 | 676.5 | 701.6 | 9.2 | 1.000x | 16.633x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.4 | 81.9 | 0.5 | 0.118x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 83.8 | 83.1 | 84.1 | 0.3 | 0.123x | 1.039x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.4 | 98.2 | 99.1 | 0.3 | 0.144x | 1.220x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 139.8 | 139.7 | 150.8 | 4.4 | 0.205x | 1.734x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 141.3 | 141.2 | 143.6 | 0.9 | 0.207x | 1.752x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.3 | 678.6 | 695.7 | 6.3 | 1.000x | 8.461x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.2 | 37.2 | 37.4 | 0.1 | 0.033x | 1.054x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.8 | 165.1 | 167.0 | 0.8 | 0.148x | 4.720x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.1 | 165.7 | 168.3 | 1.0 | 0.148x | 4.729x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,126.8 | 1,112.0 | 1,149.6 | 12.5 | 1.000x | 31.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,128.0 | 1,122.2 | 1,149.4 | 9.4 | 1.001x | 31.919x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.5 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.3 | 0.1 | 0.061x | 1.045x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.3 | 107.6 | 0.4 | 0.094x | 1.623x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 168.4 | 168.3 | 168.6 | 0.1 | 0.148x | 2.552x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 168.4 | 168.4 | 169.1 | 0.3 | 0.148x | 2.553x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,135.7 | 1,122.6 | 1,142.1 | 7.7 | 1.000x | 17.213x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 31.5 | 0.7 | 0.026x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.0 | 0.1 | 0.027x | 1.068x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 170.3 | 170.1 | 176.4 | 2.5 | 0.148x | 5.742x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.3 | 170.0 | 170.3 | 0.1 | 0.148x | 5.742x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,152.1 | 1,133.3 | 1,174.1 | 13.5 | 1.000x | 38.851x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,152.5 | 1,149.1 | 1,159.1 | 3.5 | 1.000x | 38.864x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.4 | 51.5 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.4 | 56.3 | 0.3 | 0.048x | 1.084x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.2 | 108.5 | 110.3 | 0.6 | 0.095x | 2.122x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 171.4 | 171.2 | 174.4 | 1.2 | 0.149x | 3.331x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 171.4 | 171.2 | 171.7 | 0.2 | 0.149x | 3.332x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,151.9 | 1,139.6 | 1,163.1 | 8.3 | 1.000x | 22.389x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 38.5 | 1.3 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 37.2 | 37.7 | 0.2 | 0.033x | 1.062x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 172.8 | 172.7 | 173.0 | 0.1 | 0.152x | 4.899x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.2 | 182.4 | 3.6 | 0.153x | 4.914x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,136.6 | 1,118.6 | 1,151.2 | 10.6 | 1.000x | 32.212x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,139.7 | 1,126.3 | 1,172.8 | 16.7 | 1.003x | 32.298x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.8 | 66.9 | 0.4 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.3 | 0.1 | 0.061x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.6 | 106.5 | 107.2 | 0.2 | 0.094x | 1.617x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 173.8 | 173.6 | 173.9 | 0.1 | 0.153x | 2.636x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 174.0 | 173.8 | 174.2 | 0.1 | 0.153x | 2.639x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,137.2 | 1,130.3 | 1,154.8 | 8.9 | 1.000x | 17.249x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.4 | 45.8 | 1.7 | 0.061x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.6 | 44.7 | 0.1 | 0.065x | 1.069x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 137.2 | 137.0 | 139.1 | 0.8 | 0.201x | 3.287x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 137.6 | 137.5 | 138.6 | 0.4 | 0.202x | 3.296x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 676.7 | 671.6 | 697.7 | 9.1 | 0.993x | 16.205x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.5 | 672.7 | 684.3 | 4.0 | 1.000x | 16.321x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 81.1 | 0.3 | 0.119x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 83.7 | 83.4 | 83.9 | 0.2 | 0.124x | 1.039x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.4 | 98.3 | 99.0 | 0.3 | 0.146x | 1.222x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 139.8 | 139.1 | 140.2 | 0.4 | 0.207x | 1.736x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 141.4 | 141.3 | 141.4 | 0.0 | 0.210x | 1.755x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.5 | 673.3 | 686.0 | 5.2 | 1.000x | 8.373x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 45.7 | 1.6 | 0.039x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.8 | 44.6 | 44.9 | 0.1 | 0.042x | 1.075x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.7 | 166.2 | 174.7 | 3.2 | 0.155x | 4.000x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.4 | 167.9 | 177.5 | 3.7 | 0.156x | 4.042x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.9 | 1,069.1 | 1,096.8 | 10.1 | 0.998x | 25.770x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.6 | 1,058.1 | 1,082.6 | 8.6 | 1.000x | 25.834x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.2 | 80.7 | 0.1 | 0.074x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 83.7 | 83.3 | 86.1 | 1.0 | 0.077x | 1.041x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.2 | 103.9 | 104.4 | 0.2 | 0.096x | 1.295x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 169.1 | 168.9 | 169.4 | 0.2 | 0.156x | 2.102x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 169.1 | 168.9 | 172.4 | 1.3 | 0.156x | 2.102x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.1 | 1,064.0 | 1,098.9 | 12.7 | 1.000x | 13.452x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.017x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.9 | 178.7 | 194.5 | 5.5 | 0.245x | 14.354x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194.4 | 191.7 | 196.4 | 1.5 | 0.250x | 14.619x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.1 | 776.7 | 845.7 | 26.6 | 1.000x | 58.580x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.3 | 778.1 | 791.5 | 4.9 | 1.005x | 58.895x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 22.7 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 22.4 | 22.2 | 22.8 | 0.2 | 0.008x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.1 | 215.9 | 222.6 | 2.4 | 0.083x | 9.866x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 897.0 | 818.6 | 927.7 | 36.2 | 0.337x | 40.216x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 942.8 | 907.5 | 1,030.8 | 46.6 | 0.354x | 42.269x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,664.0 | 2,658.0 | 2,679.9 | 8.6 | 1.000x | 119.438x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 192.9 | 191.4 | 194.4 | 1.3 | 0.245x | 14.534x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194.1 | 192.5 | 197.9 | 1.8 | 0.246x | 14.627x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.5 | 774.7 | 794.0 | 6.9 | 0.988x | 58.660x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.0 | 781.9 | 933.2 | 58.9 | 1.000x | 59.374x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 45.4 | 45.3 | 45.7 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 45.6 | 45.4 | 45.6 | 0.1 | 0.017x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 232.7 | 226.6 | 235.2 | 2.9 | 0.087x | 5.120x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.8 | 2,658.8 | 2,679.5 | 7.0 | 1.000x | 58.713x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 3,229.2 | 3,184.6 | 3,374.6 | 68.3 | 1.210x | 71.069x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 3,232.3 | 3,194.5 | 3,308.4 | 39.5 | 1.212x | 71.136x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.3 | 0.8 | 0.017x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.2 | 179.0 | 193.1 | 4.9 | 0.243x | 14.332x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.1 | 190.0 | 207.8 | 6.4 | 0.247x | 14.555x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.3 | 774.3 | 792.0 | 6.9 | 0.995x | 58.655x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.1 | 771.6 | 830.2 | 21.0 | 1.000x | 58.939x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.3 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 23.3 | 0.4 | 0.008x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.1 | 218.2 | 221.7 | 1.4 | 0.083x | 9.941x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 873.6 | 817.6 | 977.9 | 54.3 | 0.328x | 39.462x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 874.8 | 786.8 | 952.0 | 59.6 | 0.328x | 39.513x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,664.7 | 2,661.3 | 2,676.8 | 5.9 | 1.000x | 120.362x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 16.5 | 1.3 | 0.017x | 1.012x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.2 | 185.6 | 192.5 | 2.6 | 0.243x | 14.393x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 192.8 | 190.5 | 195.2 | 1.8 | 0.247x | 14.585x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 776.0 | 773.3 | 786.5 | 4.7 | 0.993x | 58.721x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.7 | 773.6 | 826.1 | 18.8 | 1.000x | 59.151x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.0 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 29.9 | 29.6 | 30.2 | 0.2 | 0.011x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 230.1 | 228.8 | 234.1 | 1.8 | 0.086x | 7.748x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,389.1 | 1,327.0 | 1,476.4 | 51.5 | 0.522x | 46.785x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,439.5 | 1,388.2 | 1,501.6 | 44.2 | 0.541x | 48.484x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,661.8 | 2,657.9 | 2,705.8 | 18.0 | 1.000x | 89.649x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 15.9 | 19.3 | 1.3 | 0.018x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.0 | 269.2 | 319.3 | 16.4 | 0.318x | 18.095x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 294.4 | 245.1 | 306.0 | 22.4 | 0.321x | 18.242x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 917.8 | 917.4 | 986.3 | 26.7 | 1.000x | 56.867x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 920.0 | 913.8 | 944.6 | 10.9 | 1.002x | 57.002x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.8 | 0.3 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.2 | 0.008x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 319.1 | 313.6 | 327.2 | 4.4 | 0.098x | 12.160x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,731.4 | 1,713.5 | 1,778.1 | 21.8 | 0.530x | 65.974x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,736.6 | 1,721.7 | 1,751.0 | 9.7 | 0.531x | 66.171x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,268.2 | 3,247.1 | 3,278.6 | 13.1 | 1.000x | 124.528x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.1 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.005x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 289.9 | 275.7 | 301.7 | 9.5 | 0.331x | 18.065x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 296.8 | 288.8 | 312.9 | 8.1 | 0.338x | 18.494x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 868.6 | 865.7 | 887.3 | 7.9 | 0.990x | 54.123x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 877.2 | 868.1 | 913.7 | 16.3 | 1.000x | 54.656x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.7 | 0.4 | 0.009x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.1 | 0.009x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 332.8 | 305.0 | 338.1 | 12.0 | 0.110x | 12.757x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,725.6 | 1,721.1 | 1,728.8 | 2.9 | 0.568x | 66.150x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,732.4 | 1,710.8 | 1,744.8 | 11.1 | 0.571x | 66.411x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,036.1 | 3,031.9 | 3,053.3 | 7.5 | 1.000x | 116.388x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 23.2 | 1.3 | 0.016x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.1 | 0.016x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.3 | 145.2 | 163.6 | 7.0 | 0.116x | 7.228x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 148.3 | 150.4 | 0.7 | 0.119x | 7.355x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,253.2 | 1,249.7 | 1,261.0 | 4.2 | 0.998x | 61.916x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,256.0 | 1,253.5 | 1,299.7 | 17.7 | 1.000x | 62.053x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.1 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.1 | 19.3 | 0.0 | 0.004x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.8 | 383.2 | 389.7 | 2.6 | 0.084x | 20.384x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 635.3 | 625.5 | 721.0 | 35.7 | 0.137x | 33.390x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 700.2 | 614.1 | 713.6 | 36.9 | 0.151x | 36.800x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,623.7 | 4,614.8 | 4,638.3 | 7.8 | 1.000x | 243.017x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 25.8 | 1.1 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.5 | 0.2 | 0.015x | 1.002x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 475.2 | 462.3 | 478.4 | 6.0 | 0.301x | 20.603x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 480.3 | 385.1 | 485.9 | 38.5 | 0.304x | 20.826x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,578.0 | 1,570.2 | 1,584.8 | 5.2 | 0.999x | 68.418x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,579.0 | 1,573.7 | 1,656.9 | 31.5 | 1.000x | 68.464x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.5 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 25.5 | 25.3 | 25.5 | 0.1 | 0.004x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 483.3 | 475.8 | 490.6 | 4.9 | 0.082x | 19.137x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,764.7 | 1,763.8 | 1,785.6 | 8.9 | 0.299x | 69.879x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,765.3 | 1,758.2 | 1,768.7 | 3.6 | 0.299x | 69.903x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,910.5 | 5,896.0 | 5,937.1 | 16.9 | 1.000x | 234.046x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.4 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.3 | 0.1 | 0.019x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.0 | 144.9 | 151.3 | 2.1 | 0.233x | 12.068x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 148.0 | 151.2 | 1.2 | 0.236x | 12.259x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 631.5 | 629.9 | 659.9 | 11.4 | 1.000x | 51.853x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 632.4 | 626.7 | 634.0 | 3.0 | 1.001x | 51.926x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.5 | 0.3 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.1 | 0.1 | 0.013x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 194.9 | 193.8 | 195.0 | 0.5 | 0.094x | 7.253x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,489.3 | 1,444.0 | 1,500.3 | 22.1 | 0.716x | 55.438x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,553.6 | 1,432.6 | 1,574.1 | 55.1 | 0.747x | 57.831x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,079.5 | 2,078.0 | 2,084.7 | 2.5 | 1.000x | 77.407x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 0.017x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 210.8 | 208.1 | 212.1 | 1.4 | 0.251x | 14.421x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 219.0 | 215.3 | 222.3 | 2.6 | 0.260x | 14.980x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 841.3 | 834.7 | 844.5 | 3.4 | 1.000x | 57.552x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 841.5 | 837.5 | 877.0 | 14.9 | 1.000x | 57.567x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 20.7 | 20.7 | 21.1 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 21.0 | 20.8 | 21.0 | 0.1 | 0.007x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 286.6 | 284.2 | 295.9 | 4.8 | 0.098x | 13.821x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,303.0 | 1,301.4 | 1,322.6 | 7.8 | 0.446x | 62.831x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,319.7 | 1,313.3 | 1,328.3 | 5.2 | 0.452x | 63.639x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,920.8 | 2,910.7 | 2,927.8 | 5.6 | 1.000x | 140.842x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.0 | 23.4 | 0.1 | 0.023x | 1.002x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 471.2 | 468.6 | 504.6 | 15.1 | 0.467x | 20.366x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.9 | 434.4 | 494.1 | 21.6 | 0.481x | 21.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,002.2 | 998.6 | 1,025.2 | 9.5 | 0.993x | 43.316x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,009.4 | 996.0 | 1,031.0 | 11.4 | 1.000x | 43.628x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.0 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.2 | 0.1 | 0.007x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 567.9 | 566.7 | 570.1 | 1.2 | 0.157x | 21.170x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,866.9 | 2,846.3 | 2,909.4 | 21.7 | 0.794x | 106.876x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,867.8 | 2,862.2 | 2,871.8 | 3.8 | 0.794x | 106.910x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,610.2 | 3,574.7 | 3,645.1 | 22.8 | 1.000x | 134.586x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.0 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.1 | 0.1 | 0.029x | 1.019x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.0 | 104.1 | 106.2 | 0.8 | 0.275x | 9.606x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.3 | 104.6 | 106.3 | 0.7 | 0.279x | 9.727x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 381.0 | 376.4 | 397.9 | 7.9 | 0.999x | 34.868x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 381.3 | 377.9 | 382.7 | 1.9 | 1.000x | 34.889x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 59.3 | 58.9 | 59.4 | 0.2 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 62.4 | 0.1 | 0.040x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 211.3 | 210.0 | 212.4 | 0.8 | 0.137x | 3.565x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 299.9 | 298.0 | 301.0 | 1.1 | 0.195x | 5.060x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 301.4 | 299.1 | 302.5 | 1.2 | 0.195x | 5.085x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,541.7 | 1,533.6 | 1,563.7 | 10.3 | 1.000x | 26.013x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.1 | 0.1 | 0.749x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.749x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.8 | 32.7 | 35.4 | 1.0 | 1.000x | 1.335x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.1 | 34.1 | 36.1 | 0.6 | 1.010x | 1.348x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.6 | 255.9 | 257.8 | 0.7 | 7.380x | 9.854x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 257.0 | 256.5 | 266.7 | 4.0 | 7.391x | 9.869x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 23.7 | 23.5 | 24.5 | 0.3 | 0.690x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 23.8 | 0.1 | 0.691x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.4 | 33.9 | 34.5 | 0.2 | 1.000x | 1.449x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.4 | 44.5 | 0.1 | 1.291x | 1.870x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,788.3 | 1,768.3 | 1,865.0 | 36.7 | 52.015x | 75.367x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,842.8 | 1,672.6 | 1,856.8 | 68.2 | 53.600x | 77.663x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.6 | 9.5 | 12.3 | 1.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.1 | 0.1 | 0.061x | 1.036x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.8 | 50.2 | 0.9 | 0.294x | 4.992x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 49.1 | 49.6 | 0.1 | 0.301x | 5.124x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.4 | 159.7 | 164.2 | 1.8 | 0.985x | 16.749x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 163.8 | 161.4 | 168.4 | 2.7 | 1.000x | 17.005x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 18.6 | 18.9 | 0.1 | 0.103x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.5 | 18.8 | 0.1 | 0.104x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 54.8 | 0.0 | 0.304x | 2.945x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 179.9 | 176.8 | 182.5 | 1.9 | 1.000x | 9.679x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 940.5 | 925.1 | 1,019.4 | 39.2 | 5.229x | 50.611x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,054.4 | 1,010.2 | 1,075.3 | 26.1 | 5.862x | 56.740x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.022x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.7 | 13.6 | 14.1 | 0.2 | 0.022x | 1.027x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 98.3 | 78.2 | 98.8 | 8.0 | 0.160x | 7.392x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99.2 | 98.6 | 110.6 | 4.6 | 0.161x | 7.456x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 613.5 | 611.7 | 619.4 | 2.7 | 0.995x | 46.115x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 616.4 | 603.9 | 617.5 | 5.6 | 1.000x | 46.334x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 11.0 | 10.9 | 11.0 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 12.0 | 11.4 | 12.9 | 0.6 | 0.019x | 1.089x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.9 | 83.6 | 92.1 | 3.3 | 0.137x | 7.727x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 169.3 | 167.5 | 172.8 | 2.3 | 0.272x | 15.408x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 173.4 | 172.6 | 195.6 | 8.9 | 0.279x | 15.785x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 621.9 | 618.5 | 625.9 | 2.4 | 1.000x | 56.599x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.2 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.2 | 14.8 | 1.0 | 0.021x | 1.021x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.1 | 144.6 | 147.4 | 1.1 | 0.251x | 11.942x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.0 | 147.8 | 156.0 | 2.9 | 0.258x | 12.262x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 576.6 | 566.3 | 583.4 | 5.9 | 0.998x | 47.454x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.7 | 575.5 | 592.0 | 6.0 | 1.000x | 47.544x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 71.3 | 71.2 | 71.7 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 73.8 | 73.6 | 74.0 | 0.1 | 0.026x | 1.035x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 288.4 | 285.4 | 289.9 | 1.6 | 0.103x | 4.044x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 714.5 | 684.3 | 743.7 | 19.7 | 0.255x | 10.019x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 720.1 | 715.5 | 780.3 | 25.5 | 0.257x | 10.097x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,796.8 | 2,792.3 | 2,801.9 | 4.0 | 1.000x | 39.216x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.5 | 11.1 | 0.6 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.1 | 0.1 | 0.060x | 1.019x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.9 | 47.7 | 49.0 | 0.5 | 0.289x | 4.924x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.6 | 48.8 | 49.9 | 0.4 | 0.300x | 5.099x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.7 | 160.1 | 165.6 | 2.4 | 0.977x | 16.610x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 165.6 | 161.5 | 168.1 | 2.5 | 1.000x | 17.009x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.7 | 0.4 | 0.061x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 64.3 | 64.2 | 64.8 | 0.2 | 0.064x | 1.040x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.8 | 158.5 | 161.5 | 1.0 | 0.159x | 2.585x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 166.3 | 165.6 | 169.9 | 1.5 | 0.165x | 2.690x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 168.9 | 168.6 | 169.9 | 0.4 | 0.168x | 2.732x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,005.6 | 999.8 | 1,029.8 | 10.9 | 1.000x | 16.262x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.9 | 0.3 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.022x | 1.021x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.4 | 147.1 | 1.1 | 0.252x | 11.951x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.1 | 148.0 | 154.9 | 2.5 | 0.258x | 12.242x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.4 | 572.7 | 577.7 | 1.6 | 0.997x | 47.233x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 576.9 | 564.4 | 580.0 | 6.0 | 1.000x | 47.358x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 30.7 | 2.0 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 25.8 | 0.1 | 0.013x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 198.9 | 196.8 | 201.6 | 1.8 | 0.099x | 7.752x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,423.1 | 1,385.3 | 1,470.6 | 30.9 | 0.712x | 55.476x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,469.3 | 1,428.3 | 1,496.8 | 24.7 | 0.735x | 57.279x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,999.1 | 1,970.6 | 2,019.8 | 16.4 | 1.000x | 77.931x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.8 | 0.0 | 0.022x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 21.9 | 0.1 | 0.022x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 389.7 | 362.0 | 396.2 | 15.1 | 0.391x | 17.916x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 394.7 | 371.1 | 433.0 | 20.4 | 0.396x | 18.146x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 996.2 | 987.8 | 1,007.9 | 6.6 | 1.000x | 45.803x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 996.2 | 990.1 | 1,015.2 | 9.6 | 1.000x | 45.803x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.9 | 19.9 | 0.4 | 0.005x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.0 | 19.9 | 20.1 | 0.0 | 0.006x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534.0 | 532.8 | 567.7 | 13.3 | 0.153x | 28.173x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,725.2 | 1,717.7 | 1,822.6 | 39.2 | 0.493x | 91.020x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,725.7 | 1,708.4 | 1,737.7 | 11.1 | 0.493x | 91.046x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,500.3 | 3,496.6 | 3,537.9 | 15.6 | 1.000x | 184.668x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.5 | 0.2 | 0.014x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.7 | 0.2 | 0.014x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 144.8 | 147.4 | 1.0 | 0.090x | 6.321x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 147.2 | 151.1 | 1.4 | 0.092x | 6.452x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,614.8 | 1,608.6 | 1,637.9 | 10.1 | 0.994x | 69.966x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,625.0 | 1,617.5 | 1,724.0 | 39.6 | 1.000x | 70.406x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 21.4 | 0.4 | 0.003x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.1 | 0.003x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 468.9 | 467.2 | 487.1 | 7.3 | 0.078x | 22.856x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 769.7 | 710.2 | 818.4 | 37.4 | 0.127x | 37.514x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 789.4 | 726.9 | 917.5 | 69.5 | 0.131x | 38.473x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,036.9 | 6,017.0 | 6,083.4 | 23.1 | 1.000x | 294.234x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.5 | 105.4 | 106.3 | 0.3 | 0.136x | 7.973x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.2 | 106.7 | 110.1 | 1.3 | 0.139x | 8.180x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 777.3 | 775.6 | 795.0 | 7.3 | 1.000x | 58.742x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.5 | 774.7 | 799.2 | 9.8 | 1.000x | 58.756x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 12.0 | 12.0 | 12.1 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 12.3 | 12.0 | 12.6 | 0.2 | 0.006x | 1.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.7 | 181.3 | 187.0 | 2.1 | 0.091x | 15.469x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 327.9 | 309.0 | 345.5 | 12.3 | 0.161x | 27.310x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 339.2 | 306.6 | 382.6 | 29.6 | 0.167x | 28.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,030.7 | 2,012.1 | 2,043.2 | 12.0 | 1.000x | 169.128x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.3 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.5 | 12.3 | 0.3 | 0.021x | 1.029x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.9 | 128.0 | 131.7 | 1.4 | 0.234x | 11.486x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 131.7 | 131.5 | 135.1 | 1.4 | 0.239x | 11.740x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.6 | 539.0 | 556.1 | 5.6 | 0.996x | 48.894x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.8 | 544.8 | 568.6 | 8.3 | 1.000x | 49.087x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 68.8 | 68.7 | 69.7 | 0.4 | 0.027x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 71.9 | 72.7 | 0.3 | 0.028x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 272.0 | 271.6 | 275.2 | 1.3 | 0.106x | 3.952x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 591.5 | 576.3 | 594.4 | 6.4 | 0.230x | 8.594x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 598.2 | 589.4 | 622.2 | 13.1 | 0.233x | 8.691x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.1 | 2,552.5 | 2,804.0 | 96.8 | 1.000x | 37.314x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.0 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 0.019x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 206.6 | 282.6 | 27.5 | 0.318x | 16.716x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 244.9 | 234.0 | 283.6 | 21.6 | 0.319x | 16.771x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 764.8 | 759.1 | 776.8 | 6.0 | 0.997x | 52.380x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.4 | 762.6 | 771.8 | 3.2 | 1.000x | 52.560x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 54.0 | 53.9 | 54.4 | 0.2 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 56.8 | 56.8 | 57.0 | 0.1 | 0.016x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 380.6 | 373.4 | 386.8 | 5.6 | 0.108x | 7.048x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,012.3 | 986.4 | 1,034.4 | 16.1 | 0.288x | 18.745x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,022.1 | 1,020.0 | 1,041.8 | 9.3 | 0.291x | 18.926x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,512.8 | 3,509.1 | 3,543.5 | 12.9 | 1.000x | 65.046x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.6 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.6 | 0.0 | 0.021x | 1.026x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.6 | 127.9 | 129.1 | 0.5 | 0.235x | 11.459x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 129.5 | 133.0 | 1.2 | 0.238x | 11.598x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 546.1 | 543.5 | 552.6 | 3.1 | 0.998x | 48.663x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.1 | 542.0 | 552.8 | 3.6 | 1.000x | 48.750x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.6 | 69.3 | 0.3 | 0.027x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 72.1 | 72.0 | 72.3 | 0.1 | 0.028x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 272.2 | 270.7 | 274.7 | 1.5 | 0.106x | 3.967x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 577.2 | 554.4 | 594.7 | 17.1 | 0.225x | 8.412x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 585.5 | 564.9 | 589.0 | 8.9 | 0.228x | 8.532x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,562.6 | 2,557.0 | 2,581.7 | 9.7 | 1.000x | 37.345x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.017x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.3 | 144.4 | 148.1 | 1.3 | 0.186x | 10.943x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.1 | 147.6 | 150.8 | 1.2 | 0.190x | 11.157x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 775.5 | 791.2 | 5.5 | 0.999x | 58.671x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.9 | 772.8 | 816.9 | 15.8 | 1.000x | 58.744x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.5 | 19.5 | 19.7 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 20.0 | 0.1 | 0.007x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 214.3 | 212.3 | 222.9 | 4.0 | 0.080x | 10.968x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 691.5 | 628.7 | 744.6 | 42.1 | 0.258x | 35.391x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 711.0 | 640.2 | 728.4 | 31.7 | 0.265x | 36.390x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,682.0 | 2,659.8 | 2,692.5 | 10.9 | 1.000x | 137.259x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.017x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.0 | 148.5 | 1.5 | 0.187x | 10.955x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.4 | 147.2 | 151.5 | 1.7 | 0.192x | 11.237x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 776.6 | 772.9 | 798.9 | 9.5 | 0.997x | 58.412x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.0 | 774.7 | 788.3 | 4.5 | 1.000x | 58.597x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.1 | 14.1 | 14.5 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.6 | 0.1 | 0.005x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.0 | 217.1 | 221.4 | 1.6 | 0.082x | 15.554x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 623.0 | 554.0 | 634.8 | 31.0 | 0.234x | 44.046x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 652.7 | 606.4 | 662.0 | 21.6 | 0.245x | 46.145x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.0 | 2,658.2 | 2,673.2 | 5.3 | 1.000x | 188.555x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.006x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.0 | 145.0 | 147.6 | 0.9 | 0.188x | 11.044x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.0 | 146.6 | 151.4 | 1.8 | 0.191x | 11.269x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.6 | 774.9 | 788.0 | 5.6 | 1.000x | 58.893x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.1 | 774.1 | 797.1 | 9.1 | 1.003x | 59.087x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.1 | 14.1 | 14.2 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.6 | 0.1 | 0.005x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.0 | 213.9 | 220.9 | 2.6 | 0.082x | 15.475x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 577.5 | 530.0 | 615.2 | 32.3 | 0.216x | 40.813x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 622.3 | 573.2 | 661.5 | 28.1 | 0.233x | 43.982x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,670.4 | 2,661.7 | 2,675.4 | 5.0 | 1.000x | 188.730x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 145.2 | 146.6 | 0.5 | 0.187x | 10.976x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.7 | 148.5 | 149.6 | 0.4 | 0.191x | 11.217x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 776.2 | 771.7 | 787.3 | 5.6 | 0.998x | 58.572x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.1 | 773.5 | 786.6 | 5.0 | 1.000x | 58.715x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.1 | 14.1 | 14.2 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.7 | 0.1 | 0.005x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.2 | 217.7 | 223.1 | 1.9 | 0.083x | 15.684x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 610.6 | 535.8 | 645.3 | 37.5 | 0.229x | 43.302x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 636.6 | 534.8 | 649.0 | 52.0 | 0.238x | 45.149x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.5 | 2,661.4 | 2,725.8 | 23.2 | 1.000x | 189.311x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.9 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.9 | 144.2 | 145.5 | 0.5 | 0.186x | 10.906x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 147.2 | 149.2 | 0.8 | 0.191x | 11.169x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.4 | 775.4 | 790.8 | 5.6 | 1.000x | 58.530x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.2 | 772.0 | 785.1 | 4.2 | 1.001x | 58.589x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.1 | 16.3 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.4 | 16.5 | 0.0 | 0.006x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.5 | 215.6 | 222.3 | 2.3 | 0.083x | 13.563x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 597.3 | 562.5 | 667.6 | 38.8 | 0.224x | 36.738x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 632.9 | 567.5 | 654.3 | 34.2 | 0.238x | 38.926x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,664.7 | 2,655.3 | 2,685.1 | 10.2 | 1.000x | 163.892x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,754.2 | 7,748.1 | 7,756.9 | 3.7 | 0.764x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,755.2 | 7,747.4 | 8,225.1 | 186.2 | 0.764x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,146.2 | 10,116.0 | 10,408.8 | 108.6 | 1.000x | 1.308x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,148.0 | 10,134.5 | 10,239.4 | 37.8 | 1.000x | 1.309x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,097.9 | 19,091.5 | 19,103.6 | 4.4 | 1.882x | 2.463x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,106.5 | 19,095.9 | 19,123.9 | 9.2 | 1.883x | 2.464x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,469.7 | 7,467.1 | 7,492.0 | 9.4 | 0.041x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,475.4 | 7,472.5 | 7,483.9 | 4.0 | 0.041x | 1.001x | 5 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,195.9 | 29,068.1 | 29,320.5 | 83.5 | 0.160x | 3.909x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 181,932.8 | 180,779.3 | 183,975.7 | 1,083.9 | 1.000x | 24.356x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,759.8 | 181,499.4 | 184,367.5 | 1,008.5 | 1.005x | 24.467x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,561.5 | 9,557.7 | 9,577.0 | 6.7 | 0.033x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,567.2 | 9,562.1 | 9,570.2 | 3.0 | 0.033x | 1.001x | 5 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,293.3 | 71,975.5 | 73,170.3 | 411.2 | 0.249x | 7.561x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 289,976.9 | 288,737.9 | 290,980.9 | 826.3 | 1.000x | 30.327x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290,970.5 | 289,656.8 | 293,039.7 | 1,099.9 | 1.003x | 30.431x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,077.7 | 19,065.4 | 19,097.5 | 11.0 | 0.022x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,078.7 | 19,067.8 | 19,085.9 | 6.1 | 0.022x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194,217.0 | 194,021.8 | 200,044.0 | 2,357.1 | 0.229x | 10.180x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,376.3 | 194,239.7 | 194,632.2 | 134.1 | 0.229x | 10.189x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 846,863.5 | 843,027.5 | 869,794.0 | 10,392.2 | 0.998x | 44.390x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 848,685.3 | 846,007.6 | 871,213.1 | 9,455.3 | 1.000x | 44.486x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,740.8 | 3,738.4 | 3,742.7 | 1.6 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,746.5 | 3,745.4 | 3,748.3 | 1.3 | 0.052x | 1.002x | 5 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 11,027.1 | 10,975.9 | 11,107.6 | 45.7 | 0.152x | 2.948x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,456.1 | 72,246.4 | 73,419.8 | 444.1 | 1.000x | 19.369x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,651.1 | 72,168.5 | 73,304.9 | 361.8 | 1.003x | 19.421x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.9 | 0.3 | 0.018x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.2 | 283.6 | 311.9 | 10.5 | 0.341x | 18.457x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 302.4 | 265.3 | 315.9 | 18.5 | 0.346x | 18.717x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 874.6 | 870.2 | 895.1 | 8.9 | 1.000x | 54.134x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 888.3 | 867.6 | 894.5 | 10.0 | 1.016x | 54.984x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,794.5 | 4,792.5 | 4,804.9 | 4.6 | 0.023x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,797.0 | 4,793.3 | 4,798.3 | 2.0 | 0.023x | 1.001x | 5 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99,792.2 | 98,079.8 | 101,283.0 | 1,035.8 | 0.473x | 20.814x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211,082.5 | 210,299.9 | 213,912.5 | 1,494.7 | 1.000x | 44.026x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,503.0 | 212,236.1 | 214,326.9 | 779.0 | 1.007x | 44.322x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,660.7 | 7,657.2 | 7,669.9 | 4.7 | 0.051x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,665.8 | 7,652.6 | 7,708.3 | 25.3 | 0.051x | 1.001x | 5 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,949.2 | 32,703.1 | 33,055.4 | 125.3 | 0.220x | 4.301x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,830.8 | 148,295.5 | 150,167.7 | 738.8 | 0.995x | 19.428x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 149,614.1 | 148,643.7 | 151,095.3 | 844.7 | 1.000x | 19.530x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.0 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 9.5 | 11.6 | 1.0 | 0.070x | 1.146x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.0 | 47.5 | 48.4 | 0.3 | 0.294x | 4.811x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.2 | 48.9 | 49.5 | 0.2 | 0.302x | 4.938x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 163.0 | 162.7 | 169.9 | 3.1 | 1.000x | 16.348x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.4 | 160.9 | 169.7 | 3.5 | 1.009x | 16.489x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 21.1 | 21.1 | 21.2 | 0.0 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.1 | 21.3 | 0.1 | 0.013x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.6 | 141.1 | 142.1 | 0.3 | 0.088x | 6.704x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,172.1 | 1,116.7 | 1,255.1 | 55.8 | 0.725x | 55.475x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,192.6 | 1,188.2 | 1,251.2 | 25.6 | 0.737x | 56.447x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,617.1 | 1,608.8 | 1,630.2 | 8.1 | 1.000x | 76.538x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 33.8 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.2 | 35.9 | 36.5 | 0.2 | 0.034x | 1.072x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.3 | 196.8 | 197.6 | 0.3 | 0.185x | 5.845x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 198.1 | 198.0 | 199.1 | 0.4 | 0.186x | 5.869x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.5 | 1,061.7 | 1,083.5 | 7.9 | 1.000x | 31.623x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,070.2 | 1,059.5 | 1,079.3 | 6.9 | 1.003x | 31.705x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.7 | 62.6 | 63.1 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.3 | 0.1 | 0.062x | 1.053x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.0 | 172.3 | 174.6 | 0.8 | 0.162x | 2.758x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 198.4 | 197.7 | 201.0 | 1.4 | 0.185x | 3.164x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 203.4 | 203.1 | 205.8 | 1.0 | 0.190x | 3.244x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.8 | 1,055.2 | 1,079.5 | 7.9 | 1.000x | 17.060x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.3 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.5 | 36.0 | 0.5 | 0.035x | 1.079x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 171.0 | 170.7 | 173.4 | 1.0 | 0.170x | 5.294x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.4 | 171.5 | 173.7 | 0.8 | 0.171x | 5.338x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,005.4 | 996.4 | 1,031.0 | 11.8 | 1.000x | 31.132x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,011.6 | 1,003.4 | 1,044.7 | 14.7 | 1.006x | 31.325x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.5 | 61.2 | 1.1 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.4 | 0.1 | 0.062x | 1.064x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.6 | 159.8 | 161.6 | 0.6 | 0.159x | 2.744x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 169.6 | 167.4 | 171.7 | 1.5 | 0.168x | 2.898x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 175.8 | 176.5 | 0.3 | 0.175x | 3.012x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,009.0 | 999.0 | 1,023.1 | 8.9 | 1.000x | 17.245x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.9 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.2 | 0.1 | 0.028x | 1.142x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 86.5 | 86.5 | 86.7 | 0.1 | 0.125x | 5.160x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.9 | 86.8 | 87.6 | 0.3 | 0.126x | 5.183x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 690.7 | 685.3 | 699.8 | 5.2 | 1.000x | 41.197x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 692.8 | 687.4 | 699.9 | 4.4 | 1.003x | 41.321x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 23.3 | 23.2 | 24.0 | 0.3 | 0.034x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.4 | 26.0 | 0.2 | 0.038x | 1.109x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 87.8 | 87.8 | 88.3 | 0.2 | 0.128x | 3.770x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 89.7 | 89.6 | 89.8 | 0.1 | 0.131x | 3.850x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.0 | 103.8 | 104.2 | 0.2 | 0.152x | 4.465x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.5 | 680.7 | 691.0 | 3.7 | 1.000x | 29.337x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 11.8 | 12.5 | 0.3 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.2 | 13.8 | 0.6 | 0.021x | 1.104x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 143.8 | 148.3 | 1.5 | 0.228x | 11.859x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.3 | 146.6 | 151.1 | 1.5 | 0.232x | 12.079x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636.7 | 633.2 | 641.1 | 2.6 | 0.998x | 51.868x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 637.9 | 634.0 | 657.2 | 8.7 | 1.000x | 51.971x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 27.2 | 27.1 | 27.3 | 0.1 | 0.012x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 27.2 | 27.1 | 27.3 | 0.1 | 0.012x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.1 | 200.2 | 204.0 | 1.5 | 0.091x | 7.468x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,420.6 | 1,398.9 | 1,460.1 | 23.1 | 0.635x | 52.238x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,448.3 | 1,374.6 | 1,503.5 | 43.6 | 0.647x | 53.255x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,237.5 | 2,229.3 | 2,444.9 | 82.5 | 1.000x | 82.274x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 30.5 | 1.0 | 0.032x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.4 | 0.1 | 0.035x | 1.079x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 139.1 | 138.8 | 142.0 | 1.2 | 0.161x | 4.967x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 140.8 | 140.3 | 141.2 | 0.3 | 0.163x | 5.027x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 862.2 | 851.6 | 897.5 | 16.2 | 0.997x | 30.785x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 864.7 | 847.2 | 908.7 | 22.4 | 1.000x | 30.876x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 48.7 | 0.2 | 0.057x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 52.0 | 51.4 | 52.1 | 0.2 | 0.061x | 1.071x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 145.4 | 145.2 | 145.6 | 0.1 | 0.170x | 2.995x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 145.4 | 144.8 | 147.9 | 1.1 | 0.170x | 2.995x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 149.3 | 147.7 | 150.9 | 1.2 | 0.175x | 3.076x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 854.0 | 848.9 | 868.0 | 6.7 | 1.000x | 17.590x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.3 | 56.0 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 60.1 | 59.4 | 61.8 | 0.8 | 0.069x | 1.080x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 154.8 | 154.2 | 155.1 | 0.3 | 0.178x | 2.781x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 156.6 | 155.6 | 157.6 | 0.7 | 0.180x | 2.812x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.0 | 857.3 | 889.6 | 10.3 | 1.000x | 15.644x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 892.4 | 872.6 | 928.8 | 20.4 | 1.025x | 16.028x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 109.9 | 109.6 | 110.6 | 0.4 | 0.125x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 113.3 | 112.8 | 113.9 | 0.4 | 0.129x | 1.031x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 160.6 | 160.4 | 160.9 | 0.2 | 0.182x | 1.461x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 161.0 | 160.8 | 161.8 | 0.4 | 0.183x | 1.465x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.4 | 164.0 | 166.9 | 1.1 | 0.187x | 1.496x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.7 | 874.7 | 883.1 | 2.9 | 1.000x | 8.014x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 44.6 | 0.8 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 42.8 | 0.0 | 0.019x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 738.2 | 735.9 | 789.7 | 20.7 | 0.324x | 17.267x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,055.5 | 1,048.3 | 1,100.5 | 19.3 | 0.464x | 24.690x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,240.6 | 2,224.4 | 2,328.2 | 41.3 | 0.984x | 52.408x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,275.9 | 2,215.3 | 2,313.6 | 36.6 | 1.000x | 53.234x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 89.6 | 89.2 | 90.3 | 0.4 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 93.2 | 93.0 | 93.4 | 0.1 | 0.030x | 1.040x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.1 | 404.2 | 410.4 | 2.2 | 0.131x | 4.545x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 912.8 | 909.9 | 915.4 | 2.1 | 0.294x | 10.190x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,257.8 | 1,248.5 | 1,272.0 | 8.3 | 0.405x | 14.042x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,105.2 | 3,101.1 | 3,122.1 | 7.3 | 1.000x | 34.666x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.0 | 0.3 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.009x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.4 | 144.5 | 148.5 | 1.4 | 0.185x | 11.000x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 148.1 | 151.0 | 1.2 | 0.189x | 11.207x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.5 | 778.1 | 801.3 | 8.1 | 0.996x | 59.191x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.9 | 774.2 | 811.4 | 14.8 | 1.000x | 59.451x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.6 | 0.0 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 20.8 | 0.1 | 0.008x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.0 | 216.4 | 220.0 | 1.3 | 0.082x | 10.683x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 833.0 | 780.9 | 917.9 | 53.3 | 0.312x | 40.633x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 837.6 | 731.6 | 890.2 | 66.5 | 0.314x | 40.858x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,671.2 | 2,666.5 | 2,686.7 | 7.8 | 1.000x | 130.297x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 14.0 | 0.3 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 191.8 | 182.5 | 197.4 | 4.9 | 0.245x | 14.451x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 193.7 | 189.5 | 196.0 | 2.2 | 0.248x | 14.592x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.9 | 777.2 | 811.5 | 13.3 | 1.000x | 58.903x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.7 | 780.1 | 799.3 | 7.0 | 1.002x | 59.036x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.6 | 26.9 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 26.9 | 0.1 | 0.010x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 231.5 | 228.6 | 234.2 | 2.2 | 0.087x | 8.634x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,122.3 | 1,103.9 | 1,178.1 | 30.2 | 0.421x | 41.847x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,177.7 | 1,117.6 | 1,211.4 | 30.5 | 0.442x | 43.916x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.8 | 2,660.3 | 2,673.2 | 5.0 | 1.000x | 99.330x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.4 | 34.9 | 0.1 | 0.033x | 1.071x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.3 | 173.5 | 0.1 | 0.168x | 5.369x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.8 | 174.1 | 176.7 | 0.9 | 0.169x | 5.412x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,033.2 | 1,020.7 | 1,053.2 | 12.5 | 1.000x | 31.993x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,041.4 | 1,037.9 | 1,059.3 | 7.8 | 1.008x | 32.249x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.8 | 0.2 | 0.057x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.2 | 62.6 | 0.1 | 0.060x | 1.067x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.9 | 106.4 | 107.5 | 0.4 | 0.104x | 1.830x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 174.0 | 173.9 | 174.8 | 0.3 | 0.169x | 2.978x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 176.0 | 178.7 | 1.0 | 0.171x | 3.017x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.1 | 1,023.8 | 1,045.6 | 7.3 | 1.000x | 17.665x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.9 | 0.2 | 0.031x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 34.8 | 0.1 | 0.033x | 1.071x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 173.7 | 173.3 | 179.6 | 2.4 | 0.166x | 5.366x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.9 | 174.1 | 175.1 | 0.4 | 0.167x | 5.403x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,044.7 | 1,038.0 | 1,097.3 | 22.1 | 0.996x | 32.285x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,049.1 | 1,031.6 | 1,069.8 | 13.6 | 1.000x | 32.418x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.2 | 58.2 | 58.7 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 63.1 | 0.3 | 0.060x | 1.070x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.3 | 106.4 | 108.8 | 0.8 | 0.104x | 1.842x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 174.0 | 173.6 | 174.2 | 0.2 | 0.168x | 2.987x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 176.2 | 176.7 | 0.2 | 0.170x | 3.026x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,035.2 | 1,027.4 | 1,037.1 | 3.6 | 1.000x | 17.773x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.2 | 32.5 | 0.1 | 0.028x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.3 | 35.0 | 0.3 | 0.030x | 1.063x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.2 | 164.4 | 166.6 | 0.8 | 0.145x | 5.135x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 166.5 | 165.4 | 166.9 | 0.5 | 0.145x | 5.143x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,144.9 | 1,139.7 | 1,169.9 | 12.2 | 1.000x | 35.369x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,146.5 | 1,138.3 | 1,178.2 | 13.8 | 1.001x | 35.419x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.1 | 58.8 | 0.2 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.5 | 0.2 | 0.055x | 1.066x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 107.5 | 108.3 | 0.3 | 0.095x | 1.842x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 168.4 | 168.2 | 170.2 | 0.7 | 0.148x | 2.883x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 168.4 | 168.2 | 168.7 | 0.2 | 0.148x | 2.884x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,136.8 | 1,131.4 | 1,154.7 | 9.9 | 1.000x | 19.464x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 36.4 | 0.8 | 0.031x | 1.066x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 160.9 | 160.9 | 161.4 | 0.2 | 0.146x | 4.972x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 161.6 | 161.3 | 162.2 | 0.3 | 0.147x | 4.995x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,086.7 | 1,072.3 | 1,108.0 | 13.8 | 0.988x | 33.580x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,099.8 | 1,075.1 | 1,332.7 | 97.8 | 1.000x | 33.986x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 61.3 | 1.1 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.1 | 62.4 | 0.1 | 0.058x | 1.065x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.3 | 106.8 | 114.2 | 2.8 | 0.100x | 1.836x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 162.9 | 162.7 | 164.5 | 0.6 | 0.152x | 2.787x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 163.4 | 162.9 | 165.8 | 1.0 | 0.152x | 2.796x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.7 | 1,061.0 | 1,077.0 | 5.7 | 1.000x | 18.384x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 33.0 | 0.3 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.3 | 34.8 | 0.2 | 0.031x | 1.067x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 161.0 | 160.9 | 161.5 | 0.2 | 0.146x | 4.973x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 162.1 | 161.1 | 163.1 | 0.7 | 0.147x | 5.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,080.4 | 1,077.0 | 1,103.8 | 10.8 | 0.978x | 33.375x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,105.2 | 1,071.1 | 1,137.1 | 22.6 | 1.000x | 34.142x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 59.0 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 62.5 | 0.1 | 0.058x | 1.068x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.5 | 107.0 | 112.1 | 1.9 | 0.101x | 1.875x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 163.0 | 162.8 | 163.5 | 0.3 | 0.151x | 2.790x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 163.2 | 163.1 | 163.4 | 0.1 | 0.151x | 2.794x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,079.5 | 1,067.8 | 1,079.9 | 4.7 | 1.000x | 18.485x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.3 | 0.1 | 0.018x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 295.5 | 283.4 | 316.0 | 13.6 | 0.323x | 18.352x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 307.0 | 278.3 | 319.7 | 13.8 | 0.336x | 19.063x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 898.2 | 884.1 | 929.6 | 15.7 | 0.982x | 55.770x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 915.0 | 897.1 | 948.0 | 17.9 | 1.000x | 56.814x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.6 | 0.2 | 0.008x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 323.5 | 304.7 | 339.0 | 12.4 | 0.102x | 12.346x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 1,721.9 | 1,711.3 | 1,732.4 | 7.3 | 0.542x | 65.716x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 1,726.8 | 1,721.8 | 1,749.0 | 9.8 | 0.544x | 65.903x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,174.4 | 3,123.4 | 3,203.6 | 26.8 | 1.000x | 121.153x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.1 | 0.1 | 0.350x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.0 | 12.5 | 0.6 | 0.355x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.2 | 30.3 | 31.7 | 0.5 | 1.000x | 2.858x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 31.9 | 31.1 | 32.0 | 0.4 | 1.024x | 2.926x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.1 | 46.8 | 47.3 | 0.2 | 1.511x | 4.318x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.2 | 47.9 | 49.3 | 0.5 | 1.547x | 4.421x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 4.4 | 4.4 | 5.5 | 0.4 | 0.145x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 4.8 | 4.7 | 5.3 | 0.2 | 0.156x | 1.075x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.6 | 30.4 | 33.8 | 1.3 | 1.000x | 6.882x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 40.2 | 42.5 | 1.1 | 1.317x | 9.064x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 49.8 | 49.2 | 50.1 | 0.3 | 1.627x | 11.198x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 50.2 | 49.5 | 50.4 | 0.3 | 1.641x | 11.296x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.5 | 9.7 | 0.1 | 0.314x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.323x | 1.029x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 30.3 | 31.1 | 0.4 | 1.000x | 3.181x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 31.0 | 30.9 | 31.8 | 0.3 | 1.002x | 3.187x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.6 | 47.2 | 47.8 | 0.2 | 1.537x | 4.890x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.6 | 48.4 | 49.5 | 0.4 | 1.568x | 4.989x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 5.3 | 5.0 | 5.4 | 0.1 | 0.173x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.7 | 0.1 | 0.178x | 1.025x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.7 | 30.5 | 33.5 | 1.2 | 1.000x | 5.775x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.5 | 40.4 | 45.7 | 2.0 | 1.320x | 7.623x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 66.7 | 66.4 | 68.4 | 0.8 | 2.174x | 12.552x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 68.7 | 67.8 | 70.7 | 1.0 | 2.239x | 12.929x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.0 | 0.0 | 0.310x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.1 | 12.7 | 0.6 | 0.318x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 34.3 | 35.7 | 0.6 | 0.985x | 3.173x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.2 | 33.8 | 35.9 | 0.8 | 1.000x | 3.221x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 110.3 | 109.5 | 113.3 | 1.4 | 3.135x | 10.096x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 112.3 | 111.1 | 113.8 | 1.0 | 3.193x | 10.283x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.6 | 36.2 | 0.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.2 | 46.2 | 46.6 | 0.2 | 1.323x | 1.323x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 72.7 | 72.4 | 72.8 | 0.2 | 2.082x | 2.082x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 73.6 | 73.5 | 74.5 | 0.4 | 2.109x | 2.109x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,839.2 | 2,836.3 | 2,900.3 | 24.6 | 81.355x | 81.355x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,877.6 | 2,869.2 | 2,914.7 | 18.4 | 82.454x | 82.454x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.2 | 0.1 | 0.573x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.3 | 0.1 | 0.574x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.4 | 32.7 | 35.3 | 0.9 | 1.000x | 1.744x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.9 | 34.6 | 35.6 | 0.4 | 1.047x | 1.826x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.2 | 162.2 | 165.6 | 1.2 | 4.923x | 8.588x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.7 | 166.1 | 168.0 | 0.7 | 5.028x | 8.770x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 16.2 | 16.1 | 17.0 | 0.3 | 0.472x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.4 | 0.1 | 0.476x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.3 | 34.0 | 35.9 | 0.7 | 1.000x | 2.120x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 44.4 | 45.4 | 0.4 | 1.298x | 2.751x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 816.7 | 781.9 | 821.3 | 14.6 | 23.842x | 50.546x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 837.8 | 821.2 | 856.9 | 14.0 | 24.460x | 51.856x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,581,485.2 | 3,575,620.5 | 3,714,875.4 | 53,552.4 | 0.069x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,588,937.2 | 3,586,878.6 | 3,598,651.7 | 4,198.3 | 0.069x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,048,954.7 | 7,008,591.0 | 7,235,819.0 | 81,864.3 | 0.136x | 1.968x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 11,068,535.0 | 10,733,163.0 | 13,251,238.0 | 914,437.3 | 0.214x | 3.090x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 11,887,350.0 | 11,405,027.0 | 13,862,231.0 | 849,554.5 | 0.230x | 3.319x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,692,993.8 | 51,614,176.2 | 53,263,735.5 | 630,378.3 | 1.000x | 14.433x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,417.0 | 19,187.3 | 19,694.2 | 174.8 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,877,627.3 | 1,876,565.4 | 1,886,670.4 | 3,759.9 | 96.700x | 96.700x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,891,541.7 | 1,889,089.9 | 1,896,202.9 | 2,429.5 | 97.417x | 97.417x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,626,675.3 | 17,564,725.0 | 17,863,835.0 | 102,614.4 | 907.795x | 907.795x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 84,673,810.0 | 83,837,085.0 | 85,471,734.0 | 622,370.8 | 4360.802x | 4360.802x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 84,810,791.0 | 83,147,550.0 | 86,117,238.0 | 963,194.5 | 4367.857x | 4367.857x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,842.9 | 18,616.5 | 18,943.4 | 111.5 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,876,184.2 | 1,875,029.7 | 1,883,934.8 | 3,543.8 | 99.570x | 99.570x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,878,044.0 | 1,876,100.5 | 1,898,775.9 | 8,532.0 | 99.668x | 99.668x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,137,206.7 | 3,121,378.4 | 3,158,632.2 | 13,287.6 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,198,130.0 | 3,181,344.2 | 3,221,693.9 | 13,692.0 | 0.007x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42,806,561.0 | 42,721,640.3 | 42,870,086.0 | 51,621.3 | 0.096x | 13.645x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 105,545,892.0 | 99,130,185.0 | 116,018,334.0 | 6,447,326.9 | 0.235x | 33.643x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 109,997,738.0 | 105,797,194.0 | 116,888,179.0 | 3,862,132.4 | 0.245x | 35.062x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448,191,962.3 | 446,693,951.6 | 474,088,375.7 | 10,441,740.8 | 1.000x | 142.863x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,569.1 | 19,202.7 | 20,192.9 | 355.2 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,099,418.9 | 3,089,559.4 | 3,113,057.2 | 8,833.6 | 158.383x | 158.383x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,166,592.9 | 3,147,195.3 | 3,177,016.8 | 9,675.8 | 161.816x | 161.816x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,577,782.7 | 22,528,058.7 | 22,596,558.3 | 24,463.0 | 1153.748x | 1153.748x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 98,751,873.0 | 97,612,716.0 | 116,217,796.0 | 7,943,807.3 | 5046.322x | 5046.322x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 100,302,832.0 | 98,512,922.0 | 102,903,057.0 | 1,503,431.5 | 5125.578x | 5125.578x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.151x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.3 | 0.2 | 0.338x | 1.225x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.0 | 0.339x | 1.230x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.8 | 2.4 | 0.996x | 3.613x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 29.5 | 0.3 | 1.000x | 3.628x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.5 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 17.7 | 18.6 | 0.3 | 0.181x | 1.015x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.259x | 1.455x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.4 | 0.2 | 0.260x | 1.458x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 43.9 | 50.7 | 2.6 | 0.463x | 2.597x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.7 | 100.1 | 106.1 | 2.3 | 1.000x | 5.612x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.147x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.336x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.341x | 1.232x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 1.000x | 3.616x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 28.9 | 0.1 | 1.000x | 3.617x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 0.283x | 1.611x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.285x | 1.625x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 51.0 | 2.8 | 0.461x | 2.624x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 98.8 | 102.6 | 1.3 | 1.000x | 5.696x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.342x | 1.233x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.000x | 3.601x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.5 | 2.3 | 1.006x | 3.622x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.0 | 0.1 | 0.168x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 18.0 | 0.2 | 0.174x | 1.035x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 0.176x | 1.051x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.176x | 1.051x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 51.1 | 2.7 | 0.462x | 2.754x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 99.0 | 101.8 | 1.1 | 1.000x | 5.959x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.338x | 1.224x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.338x | 1.227x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 34.5 | 2.3 | 0.995x | 3.606x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.5 | 0.4 | 1.000x | 3.626x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.2 | 0.2 | 0.182x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.8 | 50.9 | 2.7 | 0.477x | 2.628x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 53.0 | 52.9 | 53.1 | 0.1 | 0.543x | 2.993x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 53.3 | 53.2 | 53.7 | 0.2 | 0.547x | 3.013x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.6 | 96.6 | 101.6 | 1.9 | 1.000x | 5.512x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.338x | 1.225x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.339x | 1.227x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 34.5 | 2.3 | 1.000x | 3.619x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.3 | 0.2 | 1.000x | 3.620x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.1 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 47.0 | 44.6 | 58.3 | 5.1 | 0.466x | 2.574x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 80.7 | 80.6 | 81.0 | 0.1 | 0.800x | 4.421x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 80.7 | 80.4 | 81.9 | 0.5 | 0.800x | 4.421x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 99.2 | 102.8 | 1.3 | 1.000x | 5.525x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.2 | 0.319x | 1.148x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.218x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.339x | 1.221x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.3 | 0.3 | 1.000x | 3.599x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.002x | 3.607x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 17.1 | 0.1 | 0.168x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 0.174x | 1.035x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.048x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.177x | 1.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.7 | 51.1 | 2.8 | 0.464x | 2.762x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 99.7 | 103.4 | 1.5 | 1.000x | 5.957x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.336x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.337x | 1.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.0 | 0.1 | 1.000x | 3.619x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.4 | 34.5 | 2.3 | 1.002x | 3.628x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.166x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.4 | 0.0 | 0.172x | 1.036x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.174x | 1.051x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.174x | 1.052x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.7 | 43.7 | 51.2 | 2.9 | 0.460x | 2.773x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 99.4 | 103.0 | 1.3 | 1.000x | 6.034x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.153x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.217x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.336x | 1.221x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 34.5 | 2.4 | 0.993x | 3.603x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.2 | 0.2 | 1.000x | 3.630x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.175x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.6 | 51.1 | 2.7 | 0.458x | 2.628x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 53.0 | 52.9 | 53.8 | 0.4 | 0.523x | 2.998x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 53.5 | 53.2 | 54.5 | 0.5 | 0.528x | 3.025x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 99.6 | 101.8 | 0.8 | 1.000x | 5.733x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.335x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.336x | 1.217x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 35.3 | 2.6 | 0.998x | 3.613x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.2 | 0.2 | 1.000x | 3.618x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.178x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 27.2 | 0.6 | 0.260x | 1.467x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 25.9 | 26.5 | 0.2 | 0.265x | 1.497x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.7 | 51.2 | 2.8 | 0.466x | 2.630x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.0 | 102.9 | 1.7 | 1.000x | 5.642x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 34.6 | 2.4 | 0.998x | 3.600x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 3.607x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.175x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.0 | 0.1 | 0.257x | 1.465x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.9 | 0.3 | 0.258x | 1.475x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 44.1 | 51.4 | 2.8 | 0.459x | 2.620x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 99.3 | 103.6 | 1.4 | 1.000x | 5.709x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.2 | 1.000x | 3.597x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 36.5 | 3.1 | 1.003x | 3.608x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.6 | 0.3 | 0.260x | 1.471x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.1 | 0.2 | 0.260x | 1.472x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 51.1 | 2.8 | 0.464x | 2.625x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 99.1 | 101.7 | 1.1 | 1.000x | 5.661x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.219x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 30.4 | 0.7 | 1.000x | 3.602x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 37.6 | 3.5 | 1.004x | 3.615x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 19.5 | 0.7 | 0.175x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 43.7 | 51.1 | 2.8 | 0.457x | 2.612x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 50.2 | 50.2 | 50.3 | 0.1 | 0.496x | 2.834x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 50.4 | 50.1 | 50.7 | 0.2 | 0.497x | 2.842x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 98.5 | 102.0 | 1.3 | 1.000x | 5.714x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.336x | 1.215x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.9 | 2.5 | 0.998x | 3.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 3.613x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 31.2 | 0.1 | 0.308x | 1.747x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 31.5 | 31.3 | 32.1 | 0.3 | 0.313x | 1.775x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 51.3 | 2.9 | 0.462x | 2.617x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 99.5 | 102.7 | 1.2 | 1.000x | 5.668x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.317x | 1.147x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.211x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.338x | 1.222x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.616x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 34.7 | 2.4 | 1.000x | 3.617x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.1 | 0.2 | 0.175x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 31.0 | 30.9 | 31.4 | 0.2 | 0.307x | 1.753x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 31.5 | 31.2 | 31.6 | 0.2 | 0.312x | 1.781x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.8 | 51.1 | 2.9 | 0.460x | 2.625x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 99.0 | 102.4 | 1.2 | 1.000x | 5.702x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.336x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.337x | 1.221x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.7 | 2.3 | 0.996x | 3.606x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.1 | 1.000x | 3.619x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.175x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 19.5 | 19.5 | 20.7 | 0.5 | 0.193x | 1.103x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 19.8 | 19.8 | 21.0 | 0.5 | 0.196x | 1.121x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 43.6 | 51.4 | 2.9 | 0.462x | 2.634x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 99.2 | 106.3 | 2.5 | 1.000x | 5.704x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.337x | 1.222x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.337x | 1.222x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.997x | 3.615x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.0 | 0.1 | 1.000x | 3.624x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.1 | 0.177x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 0.284x | 1.617x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 28.9 | 0.0 | 0.287x | 1.634x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 43.7 | 51.3 | 3.0 | 0.461x | 2.622x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 99.0 | 101.7 | 1.1 | 1.000x | 5.684x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.147x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.6 | 9.6 | 9.8 | 0.1 | 0.335x | 1.207x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.216x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 28.9 | 0.2 | 1.000x | 3.606x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 34.6 | 2.3 | 1.001x | 3.608x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.178x | 1.012x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 29.1 | 0.3 | 0.284x | 1.613x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.288x | 1.633x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.9 | 54.4 | 3.9 | 0.463x | 2.626x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 97.9 | 101.8 | 1.4 | 1.000x | 5.670x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.316x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.7 | 0.0 | 0.334x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.335x | 1.221x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 34.6 | 2.3 | 0.991x | 3.608x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.6 | 29.5 | 0.3 | 1.000x | 3.641x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 30.9 | 30.9 | 31.0 | 0.0 | 0.307x | 1.746x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 31.4 | 31.2 | 31.6 | 0.2 | 0.311x | 1.770x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 43.8 | 54.6 | 3.9 | 0.459x | 2.613x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 98.6 | 103.5 | 1.6 | 1.000x | 5.692x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.1 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.335x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.338x | 1.223x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.3 | 0.2 | 1.000x | 3.622x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 1.001x | 3.625x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 18.0 | 0.2 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 0.177x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.6 | 0.1 | 0.286x | 1.617x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.289x | 1.636x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.7 | 43.7 | 54.5 | 4.0 | 0.469x | 2.649x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.5 | 101.7 | 1.1 | 1.000x | 5.655x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.216x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 34.6 | 2.4 | 0.991x | 3.595x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.4 | 0.2 | 1.000x | 3.628x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 30.9 | 30.8 | 31.0 | 0.1 | 0.308x | 1.749x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 31.2 | 31.2 | 31.6 | 0.2 | 0.312x | 1.767x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.7 | 54.1 | 3.9 | 0.464x | 2.632x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 99.2 | 103.8 | 1.8 | 1.000x | 5.671x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.5 | 0.2 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.337x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.000x | 3.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.5 | 0.3 | 1.000x | 3.610x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.176x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 43.7 | 54.1 | 3.8 | 0.462x | 2.621x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 47.2 | 45.3 | 48.3 | 1.2 | 0.471x | 2.671x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 47.4 | 46.6 | 49.1 | 0.9 | 0.473x | 2.681x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.2 | 102.3 | 1.5 | 1.000x | 5.674x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.6 | 0.2 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.0 | 0.1 | 0.336x | 1.213x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.213x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.0 | 0.1 | 1.000x | 3.615x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 1.002x | 3.620x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 20.0 | 0.9 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.4 | 0.2 | 0.259x | 1.469x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.9 | 0.4 | 0.261x | 1.483x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 43.7 | 54.1 | 3.8 | 0.461x | 2.617x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 98.3 | 103.0 | 1.5 | 1.000x | 5.679x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.336x | 1.214x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.337x | 1.218x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 31.2 | 1.0 | 1.000x | 3.612x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.000x | 3.614x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.176x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.6 | 0.2 | 0.259x | 1.474x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.260x | 1.477x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 43.6 | 54.1 | 3.9 | 0.463x | 2.636x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 98.8 | 102.2 | 1.2 | 1.000x | 5.689x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.151x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.335x | 1.218x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.222x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.995x | 3.614x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.2 | 0.2 | 1.000x | 3.632x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.177x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 0.262x | 1.481x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 25.9 | 26.7 | 0.4 | 0.265x | 1.501x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.8 | 43.7 | 54.3 | 3.9 | 0.468x | 2.648x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.2 | 101.7 | 1.2 | 1.000x | 5.656x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.335x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.337x | 1.223x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.4 | 0.3 | 1.000x | 3.626x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 1.000x | 3.627x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.4 | 0.2 | 0.259x | 1.477x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 26.9 | 0.4 | 0.260x | 1.484x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 54.4 | 3.9 | 0.460x | 2.619x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 98.6 | 102.6 | 1.3 | 1.000x | 5.700x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.2 | 0.2 | 0.338x | 1.224x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 0.999x | 3.619x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.4 | 29.3 | 0.3 | 1.000x | 3.621x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 20.9 | 1.3 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.6 | 0.3 | 0.260x | 1.475x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.8 | 0.3 | 0.260x | 1.475x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.8 | 54.1 | 3.8 | 0.463x | 2.625x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 98.6 | 103.4 | 1.6 | 1.000x | 5.672x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.337x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.999x | 3.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.1 | 0.2 | 1.000x | 3.613x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.177x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.6 | 26.4 | 0.3 | 0.260x | 1.473x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.261x | 1.478x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.7 | 54.1 | 3.8 | 0.464x | 2.629x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.5 | 101.5 | 1.1 | 1.000x | 5.664x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.319x | 1.159x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.334x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.0 | 0.1 | 0.338x | 1.227x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 34.6 | 2.4 | 0.990x | 3.598x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.4 | 29.4 | 0.4 | 1.000x | 3.635x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.9 | 26.2 | 0.1 | 0.258x | 1.466x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.5 | 0.3 | 0.259x | 1.476x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 44.3 | 53.8 | 3.6 | 0.460x | 2.615x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.7 | 99.0 | 101.8 | 1.0 | 1.000x | 5.691x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.341x | 1.231x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.000x | 3.612x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 34.6 | 2.3 | 1.001x | 3.616x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.177x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.259x | 1.465x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 27.3 | 0.6 | 0.263x | 1.483x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.7 | 43.8 | 61.1 | 6.4 | 0.468x | 2.641x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.5 | 101.6 | 1.2 | 1.000x | 5.648x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.334x | 1.211x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.338x | 1.223x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.2 | 34.6 | 2.4 | 0.998x | 3.616x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.0 | 0.1 | 1.000x | 3.622x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.175x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.256x | 1.469x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.4 | 0.2 | 0.259x | 1.485x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 43.7 | 54.7 | 3.9 | 0.456x | 2.616x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 99.0 | 102.2 | 1.3 | 1.000x | 5.731x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.336x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 34.6 | 2.3 | 0.991x | 3.600x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.4 | 0.3 | 1.000x | 3.631x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.177x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.2 | 0.2 | 0.259x | 1.466x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.2 | 0.260x | 1.475x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.8 | 54.8 | 4.0 | 0.465x | 2.637x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 98.9 | 103.0 | 1.5 | 1.000x | 5.671x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.337x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.340x | 1.230x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 34.6 | 2.4 | 0.994x | 3.594x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.615x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.175x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.5 | 0.2 | 0.260x | 1.484x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.7 | 26.5 | 0.3 | 0.260x | 1.485x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.6 | 54.4 | 3.9 | 0.460x | 2.627x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 99.1 | 101.5 | 0.8 | 1.000x | 5.705x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.315x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.334x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.338x | 1.230x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 34.6 | 2.3 | 0.999x | 3.637x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.1 | 28.6 | 29.7 | 0.4 | 1.000x | 3.641x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 0.173x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.174x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 26.6 | 0.3 | 0.256x | 1.475x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.5 | 0.2 | 0.257x | 1.480x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.1 | 44.4 | 54.9 | 4.0 | 0.482x | 2.781x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.8 | 98.0 | 103.4 | 2.0 | 1.000x | 5.766x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.4 | 0.2 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.6 | 9.6 | 9.8 | 0.1 | 0.337x | 1.209x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.1 | 0.1 | 0.341x | 1.223x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.000x | 3.591x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 34.6 | 2.4 | 1.005x | 3.607x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.9 | 0.4 | 0.258x | 1.459x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.5 | 0.3 | 0.259x | 1.464x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 44.6 | 54.3 | 3.6 | 0.463x | 2.617x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 99.6 | 101.7 | 0.9 | 1.000x | 5.651x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.151x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.336x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.338x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.0 | 0.5 | 1.000x | 3.618x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 34.6 | 2.3 | 1.005x | 3.638x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 26.3 | 0.3 | 0.257x | 1.463x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.8 | 0.4 | 0.257x | 1.466x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 44.1 | 54.7 | 3.8 | 0.461x | 2.626x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 98.7 | 103.0 | 1.4 | 1.000x | 5.701x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.220x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.221x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 3.609x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.7 | 2.3 | 1.001x | 3.612x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.4 | 0.2 | 0.260x | 1.473x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 26.7 | 0.3 | 0.263x | 1.487x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 44.2 | 54.8 | 3.8 | 0.466x | 2.634x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 99.1 | 101.7 | 1.0 | 1.000x | 5.655x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.336x | 1.216x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.2 | 0.2 | 1.000x | 3.622x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.7 | 2.3 | 1.001x | 3.625x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.3 | 0.2 | 0.259x | 1.467x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 27.4 | 0.7 | 0.260x | 1.473x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 44.2 | 57.1 | 4.6 | 0.461x | 2.614x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 98.8 | 101.9 | 1.1 | 1.000x | 5.672x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.316x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.337x | 1.226x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 34.6 | 2.3 | 0.992x | 3.602x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 29.4 | 0.3 | 1.000x | 3.633x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 25.9 | 0.1 | 0.257x | 1.461x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 27.1 | 0.5 | 0.258x | 1.466x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.1 | 44.1 | 57.0 | 4.6 | 0.459x | 2.606x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 98.8 | 105.3 | 2.3 | 1.000x | 5.675x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 12.6 | 1.4 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.337x | 1.220x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.338x | 1.225x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.7 | 2.4 | 1.000x | 3.621x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.622x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.6 | 0.3 | 0.178x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 26.7 | 0.4 | 0.258x | 1.452x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 27.5 | 0.5 | 0.264x | 1.489x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 43.9 | 57.0 | 4.8 | 0.465x | 2.621x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.2 | 102.8 | 1.6 | 1.000x | 5.637x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.220x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.0 | 0.1 | 0.339x | 1.226x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.5 | 0.3 | 1.000x | 3.619x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 1.001x | 3.623x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.7 | 0.4 | 0.176x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.7 | 0.1 | 0.282x | 1.611x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.285x | 1.625x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.5 | 44.2 | 57.0 | 4.7 | 0.461x | 2.631x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 99.4 | 102.2 | 1.1 | 1.000x | 5.708x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.340x | 1.221x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.4 | 0.3 | 1.000x | 3.592x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 34.6 | 2.3 | 1.003x | 3.602x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.263x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.9 | 0.1 | 0.263x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 39.1 | 2.6 | 1.000x | 3.807x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 41.5 | 35.9 | 49.2 | 4.9 | 1.271x | 4.839x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 59.9 | 59.0 | 60.7 | 0.6 | 1.837x | 6.992x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 60.4 | 59.4 | 65.0 | 2.2 | 1.850x | 7.044x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.103x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 11.7 | 0.7 | 0.113x | 1.091x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.8 | 10.3 | 0.1 | 0.114x | 1.098x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 9.9 | 11.3 | 0.5 | 0.118x | 1.144x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.7 | 87.1 | 89.0 | 0.7 | 0.990x | 9.564x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 88.7 | 88.2 | 89.0 | 0.3 | 1.000x | 9.663x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 14.2 | 0.0 | 0.143x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.0 | 0.166x | 1.167x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.4 | 0.0 | 0.174x | 1.223x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.4 | 17.3 | 27.0 | 3.8 | 0.175x | 1.224x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 44.5 | 56.6 | 4.4 | 0.467x | 3.276x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.6 | 102.6 | 1.5 | 1.000x | 7.012x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.5 | 9.9 | 0.1 | 0.338x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.2 | 0.2 | 1.000x | 3.608x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 34.6 | 2.3 | 1.006x | 3.628x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.5 | 17.5 | 17.6 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.6 | 17.5 | 20.1 | 1.0 | 0.174x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.7 | 25.7 | 28.2 | 1.0 | 0.264x | 1.522x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.7 | 26.1 | 27.4 | 0.5 | 0.264x | 1.523x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 44.2 | 57.3 | 4.7 | 0.461x | 2.657x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 98.5 | 101.6 | 1.1 | 1.000x | 5.762x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.151x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.339x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.341x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 3.592x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 1.009x | 3.626x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.7 | 18.0 | 0.1 | 0.178x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 44.1 | 57.2 | 4.7 | 0.460x | 2.587x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 50.2 | 50.0 | 50.5 | 0.2 | 0.499x | 2.805x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 50.4 | 50.2 | 52.0 | 0.6 | 0.500x | 2.812x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.7 | 98.7 | 102.4 | 1.4 | 1.000x | 5.621x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.335x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.339x | 1.229x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.996x | 3.611x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.2 | 0.2 | 1.000x | 3.625x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 21.5 | 1.5 | 0.175x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 0.284x | 1.622x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.8 | 28.2 | 29.0 | 0.3 | 0.284x | 1.626x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 46.5 | 57.2 | 3.6 | 0.488x | 2.791x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 98.5 | 102.0 | 1.3 | 1.000x | 5.719x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.337x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.341x | 1.227x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 3.599x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 34.6 | 2.3 | 1.005x | 3.618x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.8 | 0.1 | 0.174x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.174x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 29.0 | 0.2 | 0.281x | 1.614x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 0.282x | 1.621x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.1 | 44.1 | 57.4 | 5.9 | 0.484x | 2.783x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 99.6 | 103.5 | 1.4 | 1.000x | 5.753x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.336x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.0 | 0.1 | 0.338x | 1.221x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.000x | 3.610x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 3.612x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.1 | 0.1 | 0.261x | 1.473x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.262x | 1.483x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.5 | 44.4 | 57.3 | 4.8 | 0.495x | 2.801x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.9 | 102.0 | 1.2 | 1.000x | 5.654x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.152x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.221x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.339x | 1.222x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.000x | 3.609x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 1.004x | 3.622x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.176x | 1.005x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.259x | 1.479x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.7 | 26.6 | 0.4 | 0.260x | 1.485x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.2 | 57.4 | 4.9 | 0.489x | 2.792x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 98.9 | 101.7 | 1.1 | 1.000x | 5.712x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.151x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.338x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.340x | 1.222x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.000x | 3.593x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 34.6 | 2.3 | 1.011x | 3.632x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.177x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.2 | 0.2 | 0.260x | 1.473x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.3 | 0.260x | 1.476x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.5 | 44.2 | 57.5 | 4.8 | 0.493x | 2.797x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.7 | 102.5 | 1.3 | 1.000x | 5.671x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.274x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.315x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.333x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.334x | 1.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.7 | 2.4 | 0.988x | 3.602x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.1 | 28.8 | 29.2 | 0.2 | 1.000x | 3.647x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.1 | 0.177x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 47.5 | 47.2 | 47.6 | 0.1 | 0.472x | 2.684x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 47.8 | 0.1 | 0.473x | 2.689x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.5 | 44.1 | 57.5 | 4.9 | 0.493x | 2.799x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 98.8 | 101.6 | 1.0 | 1.000x | 5.681x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.219x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.338x | 1.225x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.7 | 2.4 | 0.995x | 3.608x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.3 | 0.2 | 1.000x | 3.625x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.2 | 0.2 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.8 | 0.3 | 0.259x | 1.469x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.3 | 0.1 | 0.259x | 1.470x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.2 | 57.2 | 4.8 | 0.492x | 2.790x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 99.3 | 102.0 | 1.1 | 1.000x | 5.669x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.334x | 1.211x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 34.7 | 2.4 | 0.997x | 3.614x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.3 | 0.2 | 1.000x | 3.627x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.2 | 0.2 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 47.5 | 47.5 | 47.7 | 0.1 | 0.473x | 2.685x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 47.6 | 47.5 | 48.2 | 0.3 | 0.473x | 2.688x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.7 | 57.1 | 4.5 | 0.491x | 2.789x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 98.8 | 102.2 | 1.4 | 1.000x | 5.680x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.338x | 1.226x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.1 | 1.000x | 3.623x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.2 | 28.4 | 34.6 | 2.3 | 1.012x | 3.665x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.176x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.8 | 25.5 | 26.1 | 0.2 | 0.256x | 1.457x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.258x | 1.463x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.1 | 57.2 | 4.8 | 0.491x | 2.789x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.7 | 98.6 | 105.1 | 2.2 | 1.000x | 5.681x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.336x | 1.210x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.217x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.000x | 3.605x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 34.6 | 2.3 | 1.006x | 3.626x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.5 | 26.1 | 0.2 | 0.258x | 1.460x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.5 | 0.2 | 0.260x | 1.473x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.5 | 44.3 | 57.3 | 4.8 | 0.494x | 2.793x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 98.7 | 102.1 | 1.3 | 1.000x | 5.657x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.217x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.217x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 3.599x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 1.003x | 3.610x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.2 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.175x | 1.002x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.3 | 0.1 | 0.257x | 1.469x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.4 | 26.5 | 0.3 | 0.258x | 1.473x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.2 | 44.1 | 57.3 | 4.8 | 0.487x | 2.780x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 98.4 | 102.8 | 1.6 | 1.000x | 5.708x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.220x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.337x | 1.222x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 34.6 | 2.3 | 0.999x | 3.623x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.628x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.8 | 25.6 | 26.4 | 0.3 | 0.256x | 1.458x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 26.2 | 0.2 | 0.258x | 1.468x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.1 | 57.2 | 4.8 | 0.490x | 2.785x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 98.7 | 103.8 | 1.8 | 1.000x | 5.685x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.337x | 1.217x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.219x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.000x | 3.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.1 | 0.5 | 1.000x | 3.609x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.178x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.6 | 26.2 | 0.2 | 0.260x | 1.468x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.3 | 0.2 | 0.261x | 1.469x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.6 | 45.2 | 57.3 | 4.5 | 0.496x | 2.797x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.8 | 101.9 | 1.0 | 1.000x | 5.637x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.336x | 1.217x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.219x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.2 | 0.2 | 1.000x | 3.623x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.2 | 1.000x | 3.625x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.336x | 1.220x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.337x | 1.223x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.997x | 3.617x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.5 | 0.3 | 1.000x | 3.629x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.341x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.1 | 0.3 | 1.000x | 3.592x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 1.006x | 3.616x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.316x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 10.1 | 0.1 | 0.336x | 1.221x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.337x | 1.225x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.993x | 3.611x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 29.3 | 0.1 | 1.000x | 3.636x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.335x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.7 | 2.4 | 0.996x | 3.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.621x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.221x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.338x | 1.222x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 3.616x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.7 | 2.3 | 1.000x | 3.618x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.335x | 1.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 34.6 | 2.4 | 0.991x | 3.604x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.2 | 0.2 | 1.000x | 3.637x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.151x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.338x | 1.219x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.339x | 1.225x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.999x | 3.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.4 | 0.3 | 1.000x | 3.612x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.336x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.1 | 0.338x | 1.226x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 34.8 | 2.4 | 0.995x | 3.603x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.4 | 0.3 | 1.000x | 3.621x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.0 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.176x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.2 | 0.1 | 0.258x | 1.469x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.258x | 1.472x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.6 | 57.0 | 4.6 | 0.489x | 2.785x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 98.2 | 102.7 | 1.5 | 1.000x | 5.696x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.339x | 1.218x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.0 | 0.1 | 0.340x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.5 | 0.4 | 1.000x | 3.596x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 34.6 | 2.4 | 1.003x | 3.608x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.0 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.5 | 0.3 | 0.176x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 28.3 | 28.2 | 28.4 | 0.1 | 0.280x | 1.594x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.283x | 1.612x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.2 | 57.2 | 4.7 | 0.489x | 2.782x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 98.8 | 102.9 | 1.4 | 1.000x | 5.685x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.150x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.339x | 1.219x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.1 | 0.2 | 0.340x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.4 | 0.3 | 1.000x | 3.599x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 1.008x | 3.626x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.6 | 18.5 | 0.3 | 0.177x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.2 | 0.1 | 0.257x | 1.462x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.1 | 0.1 | 0.257x | 1.463x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.2 | 44.3 | 57.3 | 4.7 | 0.489x | 2.778x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 99.7 | 102.6 | 1.1 | 1.000x | 5.684x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.318x | 1.150x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.217x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.9 | 0.1 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 34.6 | 2.4 | 0.998x | 3.608x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 31.6 | 1.1 | 1.000x | 3.614x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 17.1 | 0.1 | 0.167x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.8 | 0.2 | 0.174x | 1.037x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.176x | 1.052x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.2 | 57.1 | 4.8 | 0.491x | 2.932x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 99.5 | 102.4 | 1.1 | 1.000x | 5.972x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.151x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.337x | 1.214x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 34.6 | 2.4 | 0.998x | 3.599x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 28.9 | 0.2 | 1.000x | 3.607x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 0.177x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.5 | 26.1 | 0.2 | 0.259x | 1.462x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.4 | 0.2 | 0.259x | 1.462x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.4 | 44.3 | 57.2 | 4.7 | 0.493x | 2.788x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 99.5 | 103.2 | 1.4 | 1.000x | 5.653x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.336x | 1.219x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.337x | 1.220x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 34.6 | 2.3 | 0.999x | 3.621x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.6 | 0.3 | 1.000x | 3.625x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.166x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 0.172x | 1.034x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.175x | 1.052x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 18.1 | 0.1 | 0.176x | 1.054x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.2 | 56.5 | 4.6 | 0.487x | 2.926x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 98.3 | 102.8 | 1.5 | 1.000x | 6.006x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.335x | 1.218x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.221x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 0.996x | 3.618x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.5 | 0.3 | 1.000x | 3.632x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 0.177x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.9 | 55.5 | 4.0 | 0.490x | 2.779x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 72.5 | 72.4 | 72.5 | 0.1 | 0.722x | 4.091x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 72.7 | 72.6 | 73.4 | 0.3 | 0.723x | 4.100x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 99.0 | 101.8 | 1.0 | 1.000x | 5.669x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.0 | 0.335x | 1.212x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.337x | 1.219x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.2 | 0.1 | 1.000x | 3.616x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 34.6 | 2.3 | 1.000x | 3.618x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.9 | 0.5 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 17.9 | 0.1 | 0.177x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.3 | 56.0 | 4.5 | 0.492x | 2.789x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 59.0 | 0.2 | 0.583x | 3.310x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.589x | 3.339x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.2 | 102.7 | 1.5 | 1.000x | 5.672x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.148x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.8 | 0.1 | 0.339x | 1.225x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 12.7 | 1.2 | 0.339x | 1.226x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.3 | 1.000x | 3.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 28.9 | 0.2 | 1.000x | 3.610x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.8 | 17.6 | 18.4 | 0.3 | 0.177x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 26.2 | 0.2 | 0.259x | 1.461x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.1 | 0.260x | 1.468x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.1 | 44.2 | 55.9 | 4.0 | 0.491x | 2.772x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 99.0 | 102.0 | 1.2 | 1.000x | 5.647x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.150x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.217x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.0 | 0.336x | 1.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 34.6 | 2.3 | 0.999x | 3.621x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.3 | 0.3 | 1.000x | 3.625x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 21.2 | 1.4 | 0.177x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.4 | 0.2 | 0.259x | 1.470x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 26.4 | 0.2 | 0.261x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.2 | 44.2 | 55.9 | 4.4 | 0.491x | 2.783x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.9 | 101.8 | 1.0 | 1.000x | 5.674x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.148x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.1 | 0.337x | 1.214x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.8 | 0.0 | 0.339x | 1.222x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 29.4 | 0.3 | 1.000x | 3.604x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.4 | 1.000x | 3.605x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.174x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 0.175x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.3 | 0.2 | 0.257x | 1.471x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 26.5 | 0.2 | 0.258x | 1.478x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 45.8 | 56.0 | 3.6 | 0.486x | 2.786x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 99.2 | 103.6 | 1.6 | 1.000x | 5.735x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.277x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.149x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.7 | 0.1 | 0.337x | 1.214x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.218x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.000x | 3.605x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.7 | 2.4 | 1.002x | 3.611x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 17.7 | 18.6 | 0.3 | 0.177x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.2 | 0.1 | 0.256x | 1.462x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 27.4 | 0.6 | 0.257x | 1.468x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.4 | 56.5 | 4.6 | 0.487x | 2.780x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 98.5 | 101.6 | 1.1 | 1.000x | 5.707x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.275x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.9 | 0.1 | 0.333x | 1.213x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.7 | 0.0 | 0.335x | 1.219x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.991x | 3.608x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.1 | 28.9 | 29.3 | 0.2 | 1.000x | 3.642x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 0.176x | 1.002x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 25.7 | 27.1 | 0.4 | 0.261x | 1.488x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.6 | 26.5 | 0.3 | 0.261x | 1.488x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.9 | 56.5 | 4.3 | 0.489x | 2.787x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 99.6 | 101.5 | 0.7 | 1.000x | 5.704x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.146x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.338x | 1.216x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.218x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.2 | 1.000x | 3.595x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.6 | 2.4 | 1.001x | 3.598x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 0.175x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 0.175x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.4 | 0.3 | 0.255x | 1.460x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 27.3 | 0.5 | 0.259x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.1 | 58.0 | 5.1 | 0.486x | 2.780x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 99.0 | 101.7 | 1.1 | 1.000x | 5.720x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.1 | 0.0 | 0.279x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.320x | 1.148x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.339x | 1.219x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.341x | 1.223x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 3.590x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.7 | 2.4 | 1.003x | 3.602x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 0.177x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.3 | 0.2 | 0.260x | 1.467x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.261x | 1.472x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52.4 | 44.4 | 58.2 | 5.4 | 0.525x | 2.965x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 99.3 | 105.5 | 2.3 | 1.000x | 5.647x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.149x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 0.336x | 1.219x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.337x | 1.223x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 34.6 | 2.3 | 0.996x | 3.612x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.0 | 0.1 | 1.000x | 3.626x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.0 | 0.1 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 21.1 | 1.3 | 0.176x | 1.004x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.5 | 0.2 | 0.258x | 1.469x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.4 | 0.2 | 0.259x | 1.477x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.6 | 59.2 | 5.5 | 0.488x | 2.780x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 98.4 | 101.8 | 1.2 | 1.000x | 5.696x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.6 | 8.6 | 8.6 | 0.0 | 0.301x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 0.312x | 1.034x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.9 | 0.1 | 0.377x | 1.253x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.6 | 10.9 | 0.1 | 0.381x | 1.266x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 1.000x | 3.321x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 34.6 | 2.4 | 1.005x | 3.336x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 5.0 | 5.0 | 5.0 | 0.0 | 0.156x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 5.3 | 0.1 | 0.157x | 1.006x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 9.2 | 9.2 | 9.4 | 0.1 | 0.284x | 1.823x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 10.2 | 10.2 | 10.3 | 0.0 | 0.317x | 2.032x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.2 | 32.2 | 32.3 | 0.0 | 1.000x | 6.412x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.8 | 39.8 | 48.0 | 3.6 | 1.265x | 8.112x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.2 | 0.1 | 0.111x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.7 | 0.1 | 0.118x | 1.062x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.1 | 0.128x | 1.150x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.4 | 12.6 | 0.1 | 0.128x | 1.157x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.9 | 95.7 | 99.6 | 1.7 | 0.980x | 8.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.8 | 95.7 | 98.7 | 1.2 | 1.000x | 9.016x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 14.2 | 0.0 | 0.142x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 16.6 | 16.5 | 16.8 | 0.1 | 0.166x | 1.168x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.0 | 0.170x | 1.198x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17.1 | 16.9 | 17.2 | 0.1 | 0.171x | 1.204x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 49.3 | 44.2 | 56.5 | 4.2 | 0.493x | 3.478x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.8 | 102.2 | 1.3 | 1.000x | 7.052x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.5 | 0.2 | 0.278x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.147x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.338x | 1.216x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 10.4 | 0.3 | 0.339x | 1.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.000x | 3.596x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 34.6 | 2.3 | 1.002x | 3.604x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 9.3 | 9.2 | 9.9 | 0.3 | 0.281x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 9.6 | 9.4 | 10.2 | 0.3 | 0.290x | 1.035x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.1 | 33.1 | 34.0 | 0.4 | 1.000x | 3.565x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.9 | 37.3 | 51.1 | 5.5 | 1.235x | 4.402x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 137.4 | 133.4 | 144.1 | 3.5 | 4.153x | 14.804x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 137.8 | 135.7 | 139.7 | 1.5 | 4.163x | 14.843x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.276x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.148x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.6 | 9.8 | 0.1 | 0.336x | 1.215x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.6 | 9.9 | 0.1 | 0.338x | 1.226x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 34.7 | 2.3 | 0.996x | 3.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.4 | 28.9 | 0.2 | 1.000x | 3.622x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.263x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.264x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 32.6 | 0.1 | 1.000x | 3.802x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.4 | 42.4 | 48.8 | 2.3 | 1.333x | 5.068x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 45.2 | 45.2 | 46.3 | 0.4 | 1.388x | 5.278x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 45.8 | 45.5 | 45.9 | 0.2 | 1.406x | 5.346x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 628,684.2 | 627,967.1 | 635,823.3 | 2,884.7 | 0.176x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 628,731.1 | 627,718.5 | 630,599.7 | 1,044.9 | 0.176x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,825,442.7 | 1,692,620.8 | 1,902,078.7 | 78,326.2 | 0.512x | 2.904x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,563,281.1 | 3,550,716.9 | 3,602,989.6 | 20,584.4 | 1.000x | 5.668x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 3,923,994.5 | 3,914,908.5 | 3,954,707.3 | 14,707.0 | 1.101x | 6.242x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 4,012,120.3 | 4,009,847.7 | 4,058,000.5 | 22,964.0 | 1.126x | 6.382x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17,669.7 | 17,659.5 | 17,766.6 | 40.8 | 0.992x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17,732.9 | 17,674.9 | 17,758.6 | 27.6 | 0.996x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,809.6 | 17,759.4 | 17,901.6 | 54.5 | 1.000x | 1.008x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,399.9 | 39,121.7 | 39,616.7 | 164.8 | 2.212x | 2.230x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 3,047,388.0 | 2,800,119.1 | 3,293,198.7 | 190,533.4 | 171.109x | 172.464x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 3,076,750.8 | 2,841,198.8 | 3,247,798.5 | 162,904.6 | 172.758x | 174.126x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17,697.9 | 17,667.5 | 17,855.7 | 73.4 | 0.994x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17,734.3 | 17,719.4 | 17,782.4 | 22.7 | 0.996x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,798.9 | 17,747.5 | 17,897.5 | 52.6 | 1.000x | 1.006x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,807.9 | 39,546.0 | 40,369.6 | 283.6 | 2.237x | 2.249x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,791,699.8 | 2,789,004.5 | 2,829,668.1 | 15,450.1 | 156.847x | 157.742x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,799,563.2 | 2,789,783.7 | 3,071,085.4 | 108,296.7 | 157.289x | 158.186x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 30,939.0 | 30,875.2 | 30,967.6 | 31.3 | 0.441x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 30,981.7 | 30,853.5 | 31,202.3 | 126.7 | 0.442x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,985.7 | 68,919.1 | 71,942.0 | 1,320.9 | 0.998x | 2.262x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,122.5 | 69,881.1 | 70,621.9 | 271.3 | 1.000x | 2.266x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 3,337,656.4 | 3,274,377.3 | 3,374,722.5 | 43,521.6 | 47.597x | 107.879x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 3,368,779.2 | 3,294,248.8 | 3,384,503.3 | 33,560.1 | 48.041x | 108.885x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 17,695.9 | 17,676.9 | 18,034.9 | 136.4 | 0.997x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 17,734.5 | 17,696.4 | 18,368.6 | 257.2 | 0.999x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,756.0 | 17,713.0 | 17,797.8 | 29.6 | 1.000x | 1.003x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,399.3 | 39,747.2 | 40,616.9 | 292.7 | 2.275x | 2.283x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,941,908.1 | 2,900,648.5 | 3,407,472.8 | 190,740.9 | 165.685x | 166.248x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 3,407,572.1 | 2,910,537.8 | 3,410,830.8 | 218,862.0 | 191.911x | 192.563x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 0.059x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.4 | 45.8 | 0.5 | 0.081x | 1.377x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.1 | 47.0 | 49.2 | 0.8 | 0.086x | 1.453x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 549.0 | 540.1 | 551.8 | 4.4 | 0.997x | 16.925x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.5 | 544.0 | 558.2 | 5.0 | 1.000x | 16.970x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 54.2 | 53.9 | 64.1 | 4.0 | 0.099x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 55.1 | 54.4 | 55.7 | 0.4 | 0.100x | 1.017x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 71.4 | 5.1 | 0.106x | 1.079x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.8 | 58.4 | 67.4 | 3.5 | 0.107x | 1.084x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.0 | 76.3 | 78.3 | 0.7 | 0.140x | 1.421x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 549.1 | 543.0 | 562.2 | 6.8 | 1.000x | 10.134x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.7 | 40.1 | 0.1 | 0.053x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.8 | 40.4 | 0.2 | 0.053x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 86.2 | 85.0 | 86.2 | 0.5 | 0.113x | 2.156x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.7 | 88.1 | 89.9 | 0.7 | 0.117x | 2.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 760.4 | 748.6 | 769.1 | 6.5 | 1.000x | 19.025x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 765.7 | 754.6 | 788.2 | 11.0 | 1.007x | 19.159x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 77.9 | 77.8 | 82.4 | 1.8 | 0.103x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 77.9 | 77.7 | 83.5 | 2.2 | 0.103x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 91.2 | 90.7 | 92.6 | 0.7 | 0.120x | 1.171x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 92.8 | 92.5 | 92.9 | 0.1 | 0.122x | 1.191x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.3 | 91.5 | 95.8 | 1.9 | 0.126x | 1.223x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 758.5 | 755.0 | 781.1 | 11.0 | 1.000x | 9.738x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.3 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.2 | 18.9 | 0.3 | 0.038x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.5 | 30.3 | 30.9 | 0.2 | 0.064x | 1.667x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.1 | 36.3 | 1.3 | 0.070x | 1.820x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 478.4 | 471.0 | 481.8 | 3.8 | 1.000x | 26.187x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 480.5 | 472.3 | 486.5 | 5.2 | 1.005x | 26.305x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 33.6 | 3.0 | 0.054x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 38.0 | 37.9 | 39.2 | 0.5 | 0.079x | 1.457x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 38.7 | 0.1 | 0.080x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.2 | 62.0 | 80.2 | 6.8 | 0.133x | 2.459x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 483.6 | 475.6 | 494.2 | 6.0 | 1.000x | 18.526x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 43.3 | 43.5 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 43.2 | 43.5 | 0.1 | 0.057x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 59.2 | 58.5 | 60.0 | 0.6 | 0.078x | 1.364x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.2 | 60.4 | 0.4 | 0.078x | 1.380x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 763.7 | 754.4 | 768.5 | 5.7 | 1.000x | 17.604x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 772.8 | 760.9 | 1,064.6 | 116.9 | 1.012x | 17.814x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 66.4 | 66.0 | 71.0 | 1.9 | 0.087x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 67.5 | 66.5 | 68.2 | 0.6 | 0.088x | 1.015x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 86.9 | 86.3 | 91.1 | 1.7 | 0.114x | 1.307x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 87.1 | 86.8 | 87.5 | 0.2 | 0.114x | 1.310x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.6 | 93.4 | 97.9 | 1.6 | 0.125x | 1.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 764.4 | 757.2 | 785.6 | 10.1 | 1.000x | 11.506x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.3 | 58.3 | 0.3 | 0.103x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.4 | 62.5 | 0.8 | 0.108x | 1.046x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 61.0 | 61.2 | 0.1 | 0.109x | 1.053x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 61.0 | 61.5 | 0.2 | 0.109x | 1.054x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.2 | 557.0 | 577.8 | 7.3 | 1.000x | 9.693x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 562.8 | 553.1 | 569.1 | 5.2 | 1.001x | 9.704x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 66.8 | 65.8 | 67.3 | 0.5 | 0.118x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 67.8 | 67.8 | 68.8 | 0.4 | 0.120x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.7 | 91.4 | 94.9 | 1.2 | 0.164x | 1.388x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 120.4 | 120.4 | 120.5 | 0.1 | 0.213x | 1.803x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 120.4 | 119.9 | 130.3 | 4.0 | 0.213x | 1.803x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 564.5 | 559.7 | 580.6 | 7.6 | 1.000x | 8.455x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.3 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.1 | 0.038x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.3 | 30.5 | 0.1 | 0.063x | 1.665x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.3 | 34.6 | 0.5 | 0.070x | 1.832x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 478.7 | 475.8 | 485.2 | 3.4 | 1.000x | 26.259x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 481.9 | 473.0 | 486.5 | 4.5 | 1.007x | 26.433x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.7 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 33.2 | 2.8 | 0.054x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 38.0 | 37.8 | 39.3 | 0.5 | 0.079x | 1.455x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.4 | 38.8 | 0.1 | 0.080x | 1.479x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.7 | 62.7 | 66.2 | 1.2 | 0.133x | 2.436x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 480.5 | 474.9 | 498.4 | 8.4 | 1.000x | 18.374x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.8 | 31.1 | 0.1 | 0.040x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.1 | 30.9 | 31.6 | 0.2 | 0.040x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 96.3 | 94.7 | 98.9 | 1.4 | 0.124x | 3.115x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 96.7 | 95.4 | 98.2 | 1.1 | 0.124x | 3.129x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 775.1 | 767.9 | 787.4 | 6.5 | 0.996x | 25.071x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.2 | 769.6 | 789.7 | 6.6 | 1.000x | 25.174x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 55.9 | 55.9 | 56.1 | 0.1 | 0.071x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 56.0 | 55.7 | 62.8 | 2.8 | 0.071x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.4 | 83.4 | 91.0 | 2.8 | 0.107x | 1.510x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 132.4 | 132.1 | 133.5 | 0.5 | 0.168x | 2.369x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 139.5 | 134.6 | 142.9 | 2.9 | 0.177x | 2.497x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.2 | 773.8 | 820.0 | 15.3 | 1.000x | 14.109x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.5 | 47.3 | 0.3 | 0.076x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.7 | 47.5 | 0.3 | 0.076x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 52.7 | 53.9 | 0.4 | 0.087x | 1.142x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.4 | 56.5 | 0.4 | 0.090x | 1.185x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 613.7 | 609.1 | 622.8 | 4.5 | 1.000x | 13.099x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 614.6 | 610.2 | 636.5 | 9.3 | 1.001x | 13.119x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 62.4 | 61.8 | 62.7 | 0.3 | 0.101x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 64.3 | 63.9 | 65.1 | 0.4 | 0.103x | 1.029x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 92.3 | 91.9 | 92.5 | 0.2 | 0.149x | 1.478x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 92.5 | 91.8 | 102.3 | 4.0 | 0.149x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.1 | 90.2 | 97.1 | 2.6 | 0.150x | 1.490x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.9 | 604.4 | 638.8 | 11.0 | 1.000x | 9.945x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.6 | 37.1 | 0.2 | 0.068x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.5 | 37.8 | 0.5 | 0.068x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.6 | 46.3 | 46.8 | 0.2 | 0.086x | 1.270x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.7 | 48.6 | 51.0 | 1.1 | 0.090x | 1.328x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 539.8 | 537.9 | 544.8 | 2.4 | 0.997x | 14.725x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.3 | 535.4 | 546.1 | 3.9 | 1.000x | 14.766x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 55.1 | 54.5 | 55.6 | 0.4 | 0.102x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 56.9 | 56.7 | 57.3 | 0.2 | 0.105x | 1.032x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.5 | 81.5 | 4.8 | 0.128x | 1.263x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 69.7 | 69.5 | 69.9 | 0.1 | 0.129x | 1.265x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.1 | 79.3 | 81.7 | 0.9 | 0.148x | 1.453x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.2 | 539.6 | 561.9 | 8.5 | 1.000x | 9.834x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 31.2 | 0.7 | 0.055x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.8 | 0.1 | 0.055x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.6 | 42.9 | 0.1 | 0.080x | 1.442x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.5 | 45.1 | 47.2 | 0.9 | 0.085x | 1.538x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 533.5 | 529.9 | 538.5 | 3.1 | 0.995x | 18.026x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 536.0 | 533.0 | 544.3 | 4.2 | 1.000x | 18.111x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 50.7 | 50.4 | 50.8 | 0.1 | 0.094x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 63.5 | 4.8 | 0.095x | 1.015x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.2 | 0.2 | 0.096x | 1.020x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 52.7 | 52.4 | 53.0 | 0.2 | 0.098x | 1.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.3 | 74.2 | 76.5 | 0.8 | 0.140x | 1.486x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.9 | 530.5 | 563.1 | 11.2 | 1.000x | 10.629x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 0.068x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 0.068x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.9 | 31.4 | 33.2 | 0.6 | 0.074x | 1.077x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.4 | 34.6 | 0.4 | 0.079x | 1.148x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 432.9 | 431.4 | 439.6 | 3.2 | 1.000x | 14.611x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 434.2 | 431.8 | 445.6 | 5.0 | 1.003x | 14.655x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 36.4 | 36.2 | 36.4 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 37.1 | 36.8 | 37.4 | 0.2 | 0.086x | 1.020x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 63.6 | 4.9 | 0.119x | 1.415x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 51.8 | 0.1 | 0.119x | 1.418x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.9 | 68.5 | 71.3 | 1.1 | 0.159x | 1.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 433.7 | 433.6 | 452.0 | 7.1 | 1.000x | 11.909x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.4 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.7 | 0.2 | 0.037x | 1.010x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 30.9 | 31.5 | 0.2 | 0.092x | 2.544x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.7 | 36.0 | 0.9 | 0.100x | 2.758x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 339.2 | 338.7 | 352.3 | 5.3 | 1.000x | 27.549x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 343.5 | 341.6 | 344.5 | 1.1 | 1.013x | 27.902x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 41.9 | 2.9 | 0.020x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.9 | 0.1 | 0.020x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.0 | 137.6 | 143.6 | 2.0 | 0.080x | 4.041x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 322.1 | 320.7 | 328.2 | 2.6 | 0.184x | 9.301x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 324.5 | 324.0 | 341.3 | 6.7 | 0.186x | 9.371x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,746.1 | 1,736.7 | 1,833.4 | 35.9 | 1.000x | 50.422x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.5 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.7 | 0.2 | 0.052x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62.6 | 60.4 | 65.2 | 1.8 | 0.092x | 1.772x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.1 | 72.8 | 73.4 | 0.2 | 0.107x | 2.069x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 677.5 | 674.1 | 685.3 | 4.0 | 0.991x | 19.178x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.0 | 672.5 | 688.1 | 5.5 | 1.000x | 19.361x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 64.9 | 64.3 | 66.0 | 0.7 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 66.1 | 65.5 | 66.5 | 0.3 | 0.097x | 1.018x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 66.2 | 65.5 | 82.4 | 6.6 | 0.097x | 1.019x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 70.2 | 66.8 | 71.9 | 2.0 | 0.103x | 1.080x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.1 | 81.4 | 83.8 | 0.9 | 0.120x | 1.264x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.4 | 674.4 | 710.7 | 12.9 | 1.000x | 10.507x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.052x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.8 | 60.3 | 65.7 | 1.9 | 0.091x | 1.748x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 73.1 | 73.8 | 0.3 | 0.107x | 2.073x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 678.4 | 676.1 | 680.1 | 1.5 | 0.996x | 19.202x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.4 | 677.9 | 692.0 | 5.3 | 1.000x | 19.287x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 65.1 | 64.5 | 66.4 | 0.6 | 0.096x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.0 | 0.1 | 0.097x | 1.010x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.7 | 82.3 | 6.6 | 0.098x | 1.012x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 67.4 | 67.0 | 70.3 | 1.4 | 0.100x | 1.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.5 | 81.3 | 83.7 | 0.9 | 0.122x | 1.266x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 675.9 | 672.0 | 701.5 | 10.7 | 1.000x | 10.378x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 32.3 | 1.1 | 0.055x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.0 | 47.8 | 49.8 | 0.7 | 0.089x | 1.621x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.2 | 53.8 | 1.6 | 0.094x | 1.701x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 532.2 | 526.6 | 540.4 | 4.8 | 0.988x | 17.966x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.4 | 530.7 | 540.9 | 3.7 | 1.000x | 18.175x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 51.6 | 51.5 | 63.3 | 4.7 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 52.0 | 0.2 | 0.096x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 54.8 | 54.8 | 56.0 | 0.5 | 0.101x | 1.063x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 57.5 | 56.8 | 61.4 | 1.9 | 0.106x | 1.116x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.7 | 74.9 | 77.4 | 1.0 | 0.140x | 1.469x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 540.2 | 533.7 | 559.3 | 9.3 | 1.000x | 10.477x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 34.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 34.0 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.8 | 62.2 | 1.7 | 0.088x | 1.715x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 67.1 | 67.1 | 67.3 | 0.1 | 0.102x | 1.984x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 646.3 | 644.9 | 658.1 | 4.9 | 0.986x | 19.110x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.5 | 648.2 | 657.1 | 3.2 | 1.000x | 19.382x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 62.3 | 61.7 | 62.8 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.3 | 78.7 | 6.5 | 0.096x | 1.005x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.3 | 63.2 | 0.3 | 0.096x | 1.006x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 64.7 | 64.1 | 65.7 | 0.5 | 0.099x | 1.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.5 | 79.2 | 83.5 | 1.5 | 0.123x | 1.292x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 654.2 | 648.4 | 680.0 | 11.3 | 1.000x | 10.500x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.8 | 11.5 | 0.3 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.7 | 12.7 | 0.7 | 0.060x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.1 | 25.1 | 25.3 | 0.1 | 0.137x | 2.301x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 27.8 | 0.8 | 0.141x | 2.376x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 183.2 | 180.7 | 186.1 | 1.8 | 1.000x | 16.797x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 184.2 | 182.0 | 184.8 | 1.0 | 1.005x | 16.884x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.2 | 26.4 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 33.3 | 2.8 | 0.024x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.4 | 108.3 | 110.0 | 0.6 | 0.101x | 4.171x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 232.0 | 228.9 | 235.5 | 2.1 | 0.215x | 8.846x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 233.9 | 232.0 | 245.2 | 4.8 | 0.217x | 8.919x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.0 | 1,073.6 | 1,135.6 | 23.1 | 1.000x | 41.110x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.5 | 60.4 | 65.4 | 2.0 | 0.089x | 1.713x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.1 | 72.7 | 73.7 | 0.4 | 0.108x | 2.068x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 669.5 | 666.6 | 678.7 | 4.4 | 0.990x | 18.945x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.5 | 673.9 | 679.6 | 2.2 | 1.000x | 19.143x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 65.4 | 62.9 | 66.4 | 1.2 | 0.097x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 82.1 | 6.6 | 0.097x | 1.005x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.6 | 66.4 | 0.3 | 0.098x | 1.009x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 68.0 | 66.7 | 69.6 | 1.2 | 0.101x | 1.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.0 | 81.8 | 82.4 | 0.2 | 0.122x | 1.254x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.2 | 669.8 | 713.1 | 15.8 | 1.000x | 10.310x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.9 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.1 | 0.052x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.6 | 62.6 | 1.9 | 0.088x | 1.712x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 67.3 | 67.0 | 67.7 | 0.2 | 0.103x | 1.991x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 653.2 | 647.2 | 655.6 | 3.3 | 0.995x | 19.317x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 656.4 | 648.3 | 662.8 | 5.0 | 1.000x | 19.411x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 62.2 | 62.2 | 62.5 | 0.1 | 0.095x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 62.7 | 0.2 | 0.096x | 1.004x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.5 | 78.7 | 6.4 | 0.096x | 1.008x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 64.5 | 64.2 | 68.4 | 1.6 | 0.099x | 1.036x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.4 | 79.0 | 81.2 | 0.8 | 0.123x | 1.292x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.0 | 644.7 | 675.6 | 10.7 | 1.000x | 10.491x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.1 | 11.8 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.8 | 0.3 | 0.059x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.7 | 27.2 | 0.6 | 0.135x | 2.314x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.7 | 26.6 | 28.9 | 0.9 | 0.140x | 2.395x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 190.8 | 190.2 | 194.1 | 1.4 | 1.000x | 17.146x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 193.0 | 189.5 | 194.7 | 1.7 | 1.011x | 17.340x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 39.4 | 4.7 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 27.9 | 0.1 | 0.025x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 111.4 | 110.0 | 113.4 | 1.2 | 0.102x | 4.042x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 241.1 | 237.3 | 244.3 | 2.4 | 0.220x | 8.752x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 244.8 | 241.6 | 254.1 | 4.5 | 0.224x | 8.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,094.4 | 1,086.6 | 1,156.0 | 25.9 | 1.000x | 39.723x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.3 | 38.5 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 39.0 | 0.3 | 0.056x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.7 | 63.3 | 63.7 | 0.2 | 0.093x | 1.660x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 66.2 | 65.8 | 68.9 | 1.2 | 0.097x | 1.726x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 682.4 | 677.3 | 696.7 | 6.6 | 1.000x | 17.798x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.7 | 678.0 | 685.8 | 2.5 | 1.000x | 17.806x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 70.1 | 69.5 | 70.7 | 0.4 | 0.102x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 72.6 | 71.2 | 76.0 | 2.1 | 0.106x | 1.035x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 73.0 | 72.9 | 84.0 | 4.4 | 0.106x | 1.041x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 73.1 | 73.0 | 73.5 | 0.2 | 0.106x | 1.043x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 83.2 | 85.5 | 0.8 | 0.124x | 1.215x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 687.3 | 678.3 | 710.7 | 11.3 | 1.000x | 9.803x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.8 | 0.1 | 0.042x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.5 | 75.3 | 76.6 | 0.6 | 0.109x | 2.580x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.9 | 86.0 | 87.4 | 0.5 | 0.124x | 2.932x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 701.9 | 699.1 | 709.9 | 4.1 | 1.000x | 23.682x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 706.6 | 697.6 | 708.8 | 4.0 | 1.007x | 23.842x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 51.3 | 51.2 | 63.5 | 4.8 | 0.073x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.8 | 0.5 | 0.073x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 74.3 | 74.2 | 76.1 | 0.7 | 0.105x | 1.447x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 89.9 | 91.6 | 0.6 | 0.127x | 1.756x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 93.6 | 92.5 | 94.9 | 0.9 | 0.132x | 1.823x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.6 | 698.1 | 737.7 | 14.6 | 1.000x | 13.782x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.4 | 37.8 | 0.5 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.0 | 37.8 | 38.1 | 0.1 | 0.085x | 1.038x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.4 | 41.9 | 0.2 | 0.093x | 1.137x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 43.5 | 0.7 | 0.093x | 1.138x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449.6 | 443.7 | 451.5 | 2.8 | 1.000x | 12.279x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 449.6 | 445.7 | 453.1 | 2.8 | 1.000x | 12.280x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 40.4 | 40.3 | 46.4 | 2.4 | 0.089x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 42.2 | 41.9 | 42.2 | 0.1 | 0.093x | 1.044x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.3 | 70.8 | 71.6 | 0.3 | 0.157x | 1.763x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.5 | 0.1 | 0.178x | 1.989x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.2 | 91.5 | 4.4 | 0.178x | 1.993x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 452.5 | 446.9 | 475.2 | 9.9 | 1.000x | 11.197x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.3 | 36.0 | 0.3 | 0.053x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.8 | 0.2 | 0.053x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 77.3 | 76.7 | 84.3 | 2.9 | 0.116x | 2.180x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.9 | 84.3 | 85.1 | 0.3 | 0.127x | 2.392x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 666.9 | 664.4 | 675.2 | 3.8 | 1.000x | 18.798x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 667.2 | 666.6 | 669.6 | 1.2 | 1.000x | 18.808x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 78.1 | 4.9 | 0.099x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.7 | 66.3 | 0.2 | 0.099x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 74.8 | 74.5 | 75.3 | 0.3 | 0.112x | 1.137x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.9 | 82.8 | 83.5 | 0.2 | 0.124x | 1.260x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 94.4 | 92.7 | 94.8 | 0.7 | 0.142x | 1.436x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.0 | 664.3 | 706.6 | 15.9 | 1.000x | 10.140x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.041x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 79.1 | 78.2 | 80.1 | 0.6 | 0.110x | 2.673x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.4 | 88.0 | 89.5 | 0.6 | 0.123x | 2.986x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 716.7 | 710.4 | 719.9 | 3.3 | 0.998x | 24.216x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 717.9 | 705.0 | 728.3 | 8.9 | 1.000x | 24.256x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.4 | 63.8 | 4.9 | 0.072x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 51.8 | 51.5 | 51.9 | 0.2 | 0.073x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.4 | 89.1 | 94.1 | 2.3 | 0.126x | 1.738x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 90.1 | 89.4 | 93.1 | 1.3 | 0.127x | 1.752x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 97.1 | 96.4 | 97.4 | 0.4 | 0.136x | 1.888x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.9 | 700.3 | 741.0 | 14.5 | 1.000x | 13.841x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.3 | 0.0 | 0.049x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.5 | 0.1 | 0.049x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 79.7 | 79.4 | 80.1 | 0.2 | 0.110x | 2.259x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 91.6 | 91.0 | 92.7 | 0.6 | 0.126x | 2.594x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 727.4 | 726.0 | 731.6 | 1.9 | 1.000x | 20.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.7 | 725.5 | 732.9 | 2.6 | 1.000x | 20.614x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 66.1 | 65.9 | 66.5 | 0.2 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 66.4 | 65.8 | 77.5 | 4.5 | 0.091x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.7 | 84.7 | 0.4 | 0.116x | 1.273x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 91.0 | 90.4 | 93.2 | 1.1 | 0.125x | 1.377x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 96.1 | 95.6 | 96.5 | 0.3 | 0.132x | 1.454x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 726.7 | 721.7 | 762.0 | 14.7 | 1.000x | 10.992x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 37.1 | 36.6 | 37.3 | 0.3 | 0.083x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 37.8 | 37.6 | 38.1 | 0.2 | 0.085x | 1.017x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.4 | 42.1 | 0.2 | 0.093x | 1.122x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.8 | 0.1 | 0.093x | 1.123x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 446.7 | 441.6 | 452.6 | 3.5 | 1.000x | 12.040x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.8 | 445.5 | 449.1 | 1.2 | 1.000x | 12.043x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 41.3 | 39.5 | 46.3 | 2.4 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 42.3 | 42.1 | 43.0 | 0.3 | 0.093x | 1.024x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.9 | 70.5 | 73.1 | 1.0 | 0.156x | 1.716x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.6 | 0.1 | 0.177x | 1.947x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 80.3 | 91.6 | 4.4 | 0.178x | 1.949x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 453.3 | 446.0 | 478.8 | 11.8 | 1.000x | 10.976x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.3 | 41.8 | 0.2 | 0.066x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.8 | 0.1 | 0.066x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.7 | 72.6 | 74.6 | 0.7 | 0.117x | 1.768x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.1 | 85.0 | 85.3 | 0.1 | 0.135x | 2.040x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.3 | 626.1 | 630.5 | 1.6 | 1.000x | 15.066x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.0 | 624.9 | 644.5 | 6.7 | 1.008x | 15.179x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 74.1 | 73.1 | 75.7 | 0.8 | 0.118x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 80.7 | 80.4 | 81.1 | 0.2 | 0.128x | 1.089x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 80.8 | 80.4 | 91.9 | 4.5 | 0.128x | 1.090x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 81.4 | 82.3 | 0.4 | 0.130x | 1.102x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 89.0 | 88.8 | 89.3 | 0.2 | 0.141x | 1.201x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 629.9 | 627.5 | 659.9 | 12.3 | 1.000x | 8.500x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.046x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 33.9 | 35.0 | 0.4 | 0.117x | 2.576x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.0 | 0.1 | 0.118x | 2.609x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.4 | 293.7 | 295.7 | 0.7 | 1.000x | 22.060x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.9 | 291.8 | 304.8 | 5.0 | 1.002x | 22.099x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.2 | 25.0 | 1.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 30.6 | 3.3 | 0.021x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.9 | 68.2 | 71.7 | 1.2 | 0.064x | 3.103x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 260.4 | 253.5 | 265.1 | 4.1 | 0.242x | 11.729x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 260.5 | 258.8 | 262.9 | 1.4 | 0.242x | 11.733x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.4 | 1,066.1 | 1,088.7 | 7.4 | 1.000x | 48.480x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.1 | 35.7 | 1.0 | 0.114x | 2.521x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.1 | 0.1 | 0.119x | 2.628x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.3 | 293.6 | 297.2 | 1.5 | 1.000x | 22.131x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.0 | 293.9 | 300.2 | 2.4 | 1.009x | 22.334x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 45.4 | 45.3 | 45.5 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 45.4 | 45.2 | 54.9 | 3.8 | 0.042x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.0 | 69.4 | 76.0 | 2.5 | 0.065x | 1.542x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 532.9 | 528.8 | 538.4 | 3.3 | 0.498x | 11.743x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 537.7 | 536.0 | 539.2 | 1.0 | 0.502x | 11.849x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.1 | 1,064.1 | 1,089.4 | 9.1 | 1.000x | 23.580x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.3 | 0.4 | 0.046x | 1.016x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.7 | 34.9 | 0.5 | 0.116x | 2.573x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.6 | 0.4 | 0.119x | 2.633x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 293.4 | 292.6 | 308.3 | 6.0 | 1.000x | 22.216x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.0 | 293.9 | 311.6 | 6.5 | 1.009x | 22.416x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 23.1 | 0.3 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.1 | 31.4 | 3.6 | 0.021x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 67.5 | 69.7 | 0.8 | 0.064x | 3.076x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 266.0 | 254.3 | 271.0 | 5.5 | 0.248x | 11.931x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 267.0 | 258.7 | 271.2 | 4.6 | 0.249x | 11.976x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.9 | 1,056.1 | 1,088.9 | 11.3 | 1.000x | 48.030x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.6 | 35.7 | 0.8 | 0.115x | 2.545x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.0 | 0.0 | 0.118x | 2.626x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 293.7 | 303.4 | 3.8 | 0.998x | 22.116x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.9 | 294.1 | 296.3 | 0.9 | 1.000x | 22.165x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 29.8 | 29.4 | 40.4 | 4.3 | 0.028x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 29.9 | 29.3 | 30.5 | 0.4 | 0.028x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.7 | 68.6 | 71.0 | 0.8 | 0.065x | 2.342x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 334.5 | 330.7 | 336.4 | 2.1 | 0.310x | 11.241x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 336.1 | 327.0 | 342.9 | 5.5 | 0.312x | 11.295x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.8 | 1,056.2 | 1,081.5 | 9.0 | 1.000x | 36.216x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 54.6 | 54.2 | 57.4 | 1.2 | 0.153x | 3.392x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.5 | 58.2 | 60.3 | 0.8 | 0.164x | 3.637x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 356.6 | 353.8 | 358.3 | 1.5 | 1.000x | 22.164x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 357.3 | 352.4 | 360.8 | 2.8 | 1.002x | 22.204x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.7 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.6 | 26.1 | 35.2 | 3.5 | 0.020x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.8 | 70.4 | 73.0 | 0.9 | 0.055x | 2.723x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 395.6 | 394.8 | 398.7 | 1.4 | 0.303x | 14.997x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 399.1 | 394.8 | 404.8 | 3.2 | 0.306x | 15.128x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,304.2 | 1,291.3 | 1,330.4 | 13.4 | 1.000x | 49.440x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.1 | 0.0 | 0.052x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 48.0 | 52.0 | 1.3 | 0.162x | 3.121x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.3 | 54.8 | 55.6 | 0.3 | 0.178x | 3.441x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 310.8 | 307.2 | 321.1 | 4.8 | 1.000x | 19.320x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 312.1 | 310.7 | 316.6 | 2.2 | 1.004x | 19.403x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.7 | 0.3 | 0.023x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.5 | 26.0 | 34.9 | 3.3 | 0.023x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.7 | 69.8 | 71.4 | 0.5 | 0.062x | 2.709x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 360.8 | 360.0 | 364.2 | 1.6 | 0.319x | 13.824x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 368.4 | 366.9 | 372.9 | 2.1 | 0.325x | 14.115x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,132.8 | 1,125.2 | 1,158.4 | 12.3 | 1.000x | 43.400x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.035x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.035x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.6 | 25.5 | 26.4 | 0.4 | 0.044x | 1.268x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.8 | 0.3 | 0.045x | 1.293x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 574.9 | 572.6 | 587.4 | 5.2 | 0.988x | 28.440x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 581.8 | 566.3 | 589.9 | 7.9 | 1.000x | 28.780x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.1 | 0.0 | 0.009x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 26.6 | 3.0 | 0.009x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.6 | 97.2 | 98.5 | 0.5 | 0.045x | 5.124x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 182.3 | 170.5 | 185.0 | 5.2 | 0.083x | 9.572x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 184.7 | 174.6 | 188.6 | 4.8 | 0.084x | 9.699x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,188.0 | 2,174.7 | 2,253.6 | 29.2 | 1.000x | 114.881x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.0 | 0.029x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 129.6 | 129.0 | 130.0 | 0.3 | 0.164x | 5.618x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 135.3 | 135.0 | 136.5 | 0.5 | 0.171x | 5.864x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 789.9 | 786.9 | 799.2 | 4.3 | 1.000x | 34.234x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 794.8 | 783.0 | 804.8 | 7.6 | 1.006x | 34.449x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 25.2 | 25.2 | 25.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 37.3 | 4.8 | 0.008x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 133.0 | 133.8 | 0.3 | 0.044x | 5.277x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 693.7 | 685.7 | 698.8 | 5.0 | 0.228x | 27.491x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 702.9 | 697.4 | 704.3 | 2.8 | 0.231x | 27.854x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,038.2 | 3,018.2 | 3,134.0 | 41.2 | 1.000x | 120.401x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.8 | 12.5 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.060x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.7 | 0.2 | 0.123x | 2.066x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 27.0 | 0.4 | 0.127x | 2.128x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 205.9 | 205.4 | 206.5 | 0.4 | 1.000x | 16.809x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.5 | 205.2 | 208.8 | 1.3 | 1.008x | 16.938x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.0 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 32.9 | 2.4 | 0.037x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.1 | 64.7 | 67.0 | 0.9 | 0.089x | 2.427x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 239.7 | 239.4 | 247.0 | 3.1 | 0.328x | 8.940x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 248.2 | 243.6 | 250.7 | 2.3 | 0.340x | 9.256x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 730.3 | 721.6 | 742.0 | 8.2 | 1.000x | 27.237x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 0.043x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.5 | 14.8 | 0.1 | 0.044x | 1.006x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 39.4 | 41.2 | 0.6 | 0.120x | 2.753x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 40.9 | 42.7 | 0.7 | 0.123x | 2.822x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 337.7 | 335.4 | 338.5 | 1.1 | 1.000x | 23.024x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 339.4 | 333.8 | 342.3 | 3.6 | 1.005x | 23.143x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.9 | 20.7 | 29.7 | 3.5 | 0.017x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.9 | 21.2 | 0.1 | 0.017x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.9 | 66.7 | 70.5 | 1.3 | 0.057x | 3.294x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 303.0 | 302.3 | 305.3 | 1.2 | 0.251x | 14.476x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 307.0 | 302.3 | 310.6 | 2.7 | 0.254x | 14.669x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,208.5 | 1,199.0 | 1,257.9 | 20.8 | 1.000x | 57.742x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.047x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.7 | 0.3 | 0.047x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 72.0 | 71.6 | 72.5 | 0.3 | 0.146x | 3.127x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.3 | 74.1 | 82.8 | 3.3 | 0.151x | 3.228x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 489.0 | 483.3 | 495.0 | 4.4 | 0.993x | 21.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 492.5 | 483.1 | 493.1 | 3.7 | 1.000x | 21.403x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.6 | 38.5 | 4.7 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.5 | 0.3 | 0.015x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.0 | 90.9 | 94.4 | 1.2 | 0.052x | 3.466x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 598.2 | 594.8 | 607.9 | 4.7 | 0.333x | 22.303x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 600.5 | 592.7 | 610.5 | 6.4 | 0.334x | 22.388x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,798.1 | 1,793.7 | 1,874.2 | 34.6 | 1.000x | 67.042x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.5 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.3 | 0.1 | 0.054x | 1.006x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.1 | 27.9 | 0.6 | 0.129x | 2.392x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 27.2 | 26.3 | 28.8 | 1.0 | 0.133x | 2.462x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 202.9 | 200.9 | 207.3 | 2.5 | 0.991x | 18.354x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 204.8 | 202.1 | 209.5 | 2.5 | 1.000x | 18.525x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.9 | 58.9 | 64.1 | 2.1 | 0.062x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 76.7 | 7.1 | 0.062x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 100.7 | 99.1 | 102.7 | 1.2 | 0.105x | 1.708x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 102.2 | 101.3 | 116.4 | 5.7 | 0.107x | 1.735x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.0 | 105.5 | 107.7 | 0.8 | 0.111x | 1.799x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 955.6 | 939.8 | 981.9 | 14.5 | 1.000x | 16.211x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.2 | 23.8 | 0.2 | 0.678x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.4 | 0.1 | 0.732x | 1.080x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.753x | 1.111x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 27.8 | 0.7 | 0.755x | 1.114x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 33.8 | 33.6 | 52.2 | 7.3 | 0.976x | 1.440x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.6 | 34.3 | 35.6 | 0.5 | 1.000x | 1.475x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 23.6 | 23.6 | 30.4 | 2.7 | 0.670x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 24.2 | 0.2 | 0.674x | 1.006x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.3 | 35.0 | 37.0 | 0.7 | 1.000x | 1.492x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.0 | 36.3 | 41.5 | 1.9 | 1.078x | 1.609x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 194.8 | 194.4 | 198.5 | 1.8 | 5.524x | 8.240x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 199.8 | 198.1 | 200.8 | 0.9 | 5.665x | 8.451x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.1 | 0.344x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 9.8 | 10.7 | 0.3 | 0.355x | 1.032x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.4 | 15.1 | 16.2 | 0.4 | 0.529x | 1.537x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 16.5 | 0.1 | 0.560x | 1.627x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.0 | 29.4 | 0.2 | 1.000x | 2.906x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 33.0 | 1.4 | 1.008x | 2.928x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 18.5 | 18.3 | 18.9 | 0.2 | 0.508x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.4 | 25.4 | 2.7 | 0.513x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.5 | 36.2 | 36.9 | 0.3 | 1.000x | 1.968x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42.0 | 37.5 | 42.6 | 1.9 | 1.151x | 2.266x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 143.0 | 142.2 | 143.3 | 0.4 | 3.917x | 7.708x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 149.1 | 147.0 | 150.1 | 1.2 | 4.084x | 8.039x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.6 | 13.8 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.8 | 0.1 | 0.067x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.1 | 0.1 | 0.083x | 1.251x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 18.9 | 0.1 | 0.091x | 1.373x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 205.8 | 204.6 | 210.6 | 2.1 | 1.000x | 15.107x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 208.1 | 206.1 | 209.4 | 1.2 | 1.011x | 15.269x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 11.6 | 11.4 | 13.0 | 0.7 | 0.053x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 12.3 | 11.4 | 12.9 | 0.5 | 0.056x | 1.055x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52.6 | 52.1 | 54.3 | 0.9 | 0.242x | 4.528x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 62.9 | 0.3 | 0.287x | 5.369x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 67.7 | 67.0 | 68.1 | 0.4 | 0.311x | 5.827x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.7 | 213.7 | 219.1 | 2.4 | 1.000x | 18.722x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.5 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.080x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.3 | 24.7 | 0.5 | 0.154x | 1.924x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.8 | 23.6 | 25.5 | 0.7 | 0.155x | 1.937x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 151.7 | 148.4 | 154.5 | 2.4 | 0.990x | 12.352x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 153.2 | 150.7 | 154.5 | 1.3 | 1.000x | 12.475x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 71.1 | 82.3 | 4.5 | 0.066x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 71.3 | 71.2 | 71.5 | 0.1 | 0.066x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 101.1 | 99.2 | 104.2 | 1.8 | 0.094x | 1.420x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 148.1 | 147.6 | 149.9 | 0.8 | 0.138x | 2.080x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 149.3 | 148.4 | 153.5 | 1.9 | 0.139x | 2.096x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.2 | 1,068.8 | 1,109.2 | 15.1 | 1.000x | 15.072x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.5 | 0.3 | 0.337x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.1 | 0.1 | 0.341x | 1.011x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.5 | 15.3 | 16.2 | 0.3 | 0.528x | 1.565x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.5 | 0.1 | 0.556x | 1.649x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.4 | 29.2 | 30.5 | 0.5 | 1.000x | 2.965x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.4 | 32.6 | 1.3 | 1.003x | 2.974x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.8 | 62.3 | 0.2 | 0.114x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.0 | 61.8 | 74.1 | 4.8 | 0.114x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 71.5 | 68.3 | 72.8 | 1.6 | 0.132x | 1.154x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 72.2 | 71.0 | 73.8 | 1.0 | 0.133x | 1.166x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.1 | 77.5 | 85.2 | 2.7 | 0.146x | 1.277x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.7 | 535.0 | 561.5 | 9.8 | 1.000x | 8.762x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.6 | 0.2 | 0.082x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.082x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.5 | 23.6 | 0.0 | 0.157x | 1.917x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.9 | 23.8 | 26.6 | 1.1 | 0.159x | 1.942x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 150.4 | 149.5 | 152.5 | 1.3 | 1.000x | 12.232x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 151.7 | 149.4 | 152.1 | 1.1 | 1.009x | 12.343x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 25.8 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.2 | 31.5 | 2.3 | 0.052x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.3 | 63.0 | 70.9 | 2.6 | 0.131x | 2.539x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 225.0 | 224.7 | 232.7 | 3.1 | 0.452x | 8.747x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 225.5 | 223.5 | 227.2 | 1.4 | 0.452x | 8.765x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498.3 | 497.5 | 527.8 | 11.7 | 1.000x | 19.371x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 24.2 | 1.0 | 0.046x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 0.046x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.9 | 50.5 | 52.4 | 0.7 | 0.108x | 2.337x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.1 | 52.0 | 54.9 | 1.1 | 0.111x | 2.392x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 468.8 | 463.3 | 473.9 | 3.4 | 0.996x | 21.519x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 470.8 | 466.5 | 481.7 | 5.5 | 1.000x | 21.613x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 18.8 | 26.6 | 3.0 | 0.011x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.1 | 18.8 | 19.8 | 0.4 | 0.011x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.1 | 84.7 | 90.4 | 2.1 | 0.050x | 4.587x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 348.2 | 346.6 | 350.1 | 1.4 | 0.200x | 18.344x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 351.5 | 349.4 | 352.4 | 1.2 | 0.202x | 18.518x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,738.2 | 1,732.9 | 1,798.3 | 24.7 | 1.000x | 91.564x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 0.029x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.5 | 26.6 | 0.4 | 0.032x | 1.115x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.1 | 28.1 | 0.8 | 0.033x | 1.140x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 786.4 | 782.4 | 792.3 | 3.2 | 0.992x | 34.081x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 793.1 | 784.4 | 796.6 | 4.6 | 1.000x | 34.373x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.3 | 20.8 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.4 | 20.2 | 28.6 | 3.3 | 0.007x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.4 | 118.6 | 120.6 | 0.7 | 0.039x | 5.858x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 186.3 | 185.5 | 192.1 | 2.9 | 0.061x | 9.142x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 190.9 | 187.6 | 193.4 | 2.2 | 0.062x | 9.367x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,058.0 | 3,038.5 | 3,160.5 | 44.4 | 1.000x | 150.082x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.3 | 0.4 | 0.045x | 1.017x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.3 | 0.1 | 0.057x | 1.286x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.8 | 0.1 | 0.063x | 1.421x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.7 | 292.9 | 297.6 | 1.6 | 1.000x | 22.384x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.6 | 292.9 | 298.0 | 1.9 | 1.003x | 22.452x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 12.1 | 12.0 | 12.3 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 12.8 | 12.4 | 18.4 | 2.3 | 0.016x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.7 | 61.2 | 68.0 | 2.5 | 0.077x | 5.115x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 88.5 | 86.2 | 92.0 | 2.1 | 0.110x | 7.331x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 93.6 | 92.6 | 95.0 | 0.9 | 0.116x | 7.752x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 807.0 | 804.9 | 820.4 | 5.8 | 1.000x | 66.860x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 12.4 | 0.4 | 0.079x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.5 | 11.6 | 0.0 | 0.079x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.4 | 21.3 | 22.4 | 0.4 | 0.147x | 1.857x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.0 | 0.153x | 1.935x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.3 | 141.8 | 144.7 | 1.3 | 0.992x | 12.519x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 145.5 | 141.6 | 146.7 | 1.8 | 1.000x | 12.617x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.8 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 68.9 | 68.3 | 80.5 | 4.7 | 0.067x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.0 | 97.7 | 100.0 | 0.8 | 0.096x | 1.444x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 127.7 | 127.4 | 128.8 | 0.5 | 0.124x | 1.862x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 128.9 | 128.7 | 134.9 | 2.4 | 0.125x | 1.880x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.3 | 1,017.8 | 1,062.1 | 14.9 | 1.000x | 15.054x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 0.049x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.9 | 0.1 | 0.049x | 1.008x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.2 | 42.1 | 0.3 | 0.138x | 2.835x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 41.6 | 43.4 | 0.6 | 0.143x | 2.931x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.8 | 298.5 | 305.8 | 2.6 | 1.000x | 20.511x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.3 | 298.5 | 302.8 | 1.8 | 1.002x | 20.548x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 67.5 | 5.4 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 53.9 | 53.7 | 54.5 | 0.3 | 0.033x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.8 | 103.9 | 108.6 | 1.9 | 0.064x | 1.947x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 299.8 | 298.7 | 305.0 | 2.2 | 0.183x | 5.567x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 302.6 | 300.4 | 316.5 | 6.0 | 0.185x | 5.620x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,634.6 | 1,628.5 | 1,676.7 | 17.6 | 1.000x | 30.356x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.5 | 0.0 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.4 | 11.9 | 0.1 | 0.081x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.4 | 22.3 | 0.3 | 0.153x | 1.882x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 22.4 | 0.1 | 0.157x | 1.937x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.9 | 140.1 | 144.3 | 1.7 | 0.995x | 12.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 141.5 | 140.2 | 143.9 | 1.4 | 1.000x | 12.306x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.6 | 68.8 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 68.8 | 68.6 | 80.5 | 4.7 | 0.068x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 106.7 | 3.5 | 0.097x | 1.440x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 128.2 | 127.8 | 128.6 | 0.3 | 0.126x | 1.868x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 129.1 | 127.7 | 136.4 | 3.2 | 0.127x | 1.881x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,015.4 | 1,012.0 | 1,054.0 | 16.0 | 1.000x | 14.796x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.7 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.8 | 0.2 | 0.046x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 26.4 | 0.4 | 0.087x | 1.912x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.090x | 1.966x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 292.6 | 292.1 | 296.7 | 1.7 | 1.000x | 21.967x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.4 | 294.4 | 298.8 | 1.5 | 1.010x | 22.177x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 19.7 | 27.7 | 3.2 | 0.018x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 19.7 | 19.7 | 20.1 | 0.1 | 0.018x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.9 | 67.4 | 79.0 | 4.3 | 0.064x | 3.498x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 179.7 | 177.9 | 187.6 | 3.5 | 0.168x | 9.128x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 184.6 | 181.0 | 187.3 | 2.1 | 0.172x | 9.375x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.7 | 1,066.6 | 1,098.8 | 11.3 | 1.000x | 54.475x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.046x | 1.007x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.6 | 0.1 | 0.087x | 1.911x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.3 | 0.1 | 0.089x | 1.957x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.1 | 294.0 | 297.2 | 1.3 | 1.000x | 22.068x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.1 | 294.8 | 300.5 | 2.1 | 1.010x | 22.293x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.2 | 14.1 | 20.1 | 2.3 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 22.2 | 3.1 | 0.013x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.6 | 66.3 | 68.7 | 1.0 | 0.063x | 4.752x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 167.2 | 164.4 | 171.3 | 2.3 | 0.156x | 11.753x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 167.4 | 165.0 | 171.1 | 2.1 | 0.156x | 11.765x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.4 | 1,058.1 | 1,087.0 | 9.9 | 1.000x | 75.501x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.7 | 0.1 | 0.086x | 1.910x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.1 | 28.7 | 1.0 | 0.089x | 1.978x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.1 | 291.6 | 296.8 | 1.7 | 1.000x | 22.107x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.2 | 293.7 | 298.4 | 1.6 | 1.004x | 22.189x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.2 | 14.0 | 16.8 | 1.1 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.3 | 14.0 | 21.4 | 2.9 | 0.013x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.8 | 65.6 | 68.9 | 1.2 | 0.064x | 4.790x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 166.8 | 163.9 | 167.9 | 1.5 | 0.157x | 11.785x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 167.3 | 163.5 | 169.0 | 2.0 | 0.157x | 11.822x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.3 | 1,061.0 | 1,071.6 | 4.0 | 1.000x | 75.069x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.5 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 25.7 | 0.1 | 0.086x | 1.908x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.1 | 27.1 | 0.3 | 0.089x | 1.971x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.2 | 293.4 | 298.9 | 1.9 | 0.996x | 22.118x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.3 | 292.6 | 301.3 | 3.1 | 1.000x | 22.201x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 14.1 | 14.0 | 21.3 | 2.9 | 0.013x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 14.2 | 14.1 | 18.0 | 1.5 | 0.013x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.4 | 65.4 | 69.0 | 1.3 | 0.063x | 4.780x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 166.7 | 166.0 | 170.8 | 1.7 | 0.156x | 11.815x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 166.7 | 163.1 | 168.0 | 1.7 | 0.156x | 11.817x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.0 | 1,058.5 | 1,074.6 | 6.3 | 1.000x | 75.567x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 0.046x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.4 | 25.4 | 25.7 | 0.1 | 0.087x | 1.919x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.0 | 26.4 | 0.1 | 0.090x | 1.981x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 292.6 | 290.1 | 294.7 | 1.8 | 1.000x | 22.072x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.8 | 292.2 | 297.0 | 1.8 | 1.014x | 22.389x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.4 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 24.8 | 3.4 | 0.015x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.7 | 66.3 | 68.4 | 0.8 | 0.063x | 4.153x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 160.1 | 157.3 | 162.1 | 1.6 | 0.150x | 9.828x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 161.7 | 157.9 | 162.1 | 1.5 | 0.152x | 9.928x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.8 | 1,055.9 | 1,080.3 | 8.8 | 1.000x | 65.491x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,685.9 | 7,683.7 | 7,703.4 | 7.5 | 0.782x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,697.9 | 7,678.5 | 7,711.6 | 13.9 | 0.783x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,831.0 | 9,828.9 | 9,851.6 | 10.3 | 1.000x | 1.279x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,852.0 | 9,817.2 | 10,036.6 | 80.2 | 1.002x | 1.282x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,092.5 | 19,090.6 | 19,107.2 | 6.1 | 1.942x | 2.484x |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,105.8 | 19,087.6 | 19,152.9 | 23.1 | 1.943x | 2.486x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,917.4 | 5,896.0 | 5,953.2 | 19.3 | 0.082x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,291.7 | 6,228.6 | 6,309.8 | 28.2 | 0.087x | 1.063x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,470.8 | 7,465.7 | 7,474.2 | 3.5 | 0.103x | 1.263x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,472.3 | 7,470.6 | 7,479.3 | 3.1 | 0.103x | 1.263x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,471.1 | 72,213.1 | 72,950.0 | 268.3 | 1.000x | 12.247x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,581.6 | 72,389.4 | 72,971.7 | 201.7 | 1.002x | 12.266x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,559.1 | 9,552.7 | 9,593.2 | 14.6 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,564.1 | 9,554.2 | 9,650.2 | 35.7 | 0.060x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,728.3 | 13,720.0 | 13,755.6 | 14.4 | 0.086x | 1.436x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,729.4 | 13,711.3 | 14,365.3 | 254.4 | 0.086x | 1.436x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158,718.0 | 158,450.4 | 159,056.2 | 227.1 | 1.000x | 16.604x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 158,786.5 | 158,762.0 | 159,442.8 | 260.3 | 1.000x | 16.611x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,657.4 | 7,653.2 | 7,675.6 | 8.2 | 0.812x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,661.4 | 7,645.7 | 7,675.7 | 10.4 | 0.813x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,426.8 | 9,408.4 | 9,441.0 | 13.6 | 1.000x | 1.231x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,433.0 | 9,429.3 | 9,500.3 | 31.9 | 1.001x | 1.232x |
| 5 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,072.0 | 19,066.0 | 19,145.5 | 29.7 | 2.023x | 2.491x |
| 6 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,073.6 | 19,064.1 | 19,094.2 | 10.8 | 2.023x | 2.491x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,742.0 | 3,739.6 | 3,797.5 | 22.3 | 0.084x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,742.5 | 3,739.6 | 3,746.0 | 2.4 | 0.084x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,147.5 | 6,143.5 | 6,215.0 | 27.7 | 0.138x | 1.643x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,561.0 | 6,548.9 | 6,574.1 | 8.8 | 0.147x | 1.753x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,481.6 | 44,468.2 | 44,544.1 | 31.4 | 0.998x | 11.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,550.0 | 44,445.4 | 44,597.5 | 51.3 | 1.000x | 11.905x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 17.6 | 0.6 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.6 | 0.2 | 0.051x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 48.5 | 54.1 | 2.1 | 0.169x | 3.325x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.9 | 54.6 | 57.1 | 0.9 | 0.174x | 3.422x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 315.7 | 313.0 | 316.3 | 1.2 | 0.997x | 19.659x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 316.4 | 314.2 | 336.1 | 8.0 | 1.000x | 19.708x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,792.7 | 4,790.0 | 4,810.0 | 7.3 | 0.044x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,793.1 | 4,792.0 | 4,852.8 | 23.8 | 0.044x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,866.0 | 6,861.1 | 6,876.9 | 5.6 | 0.062x | 1.433x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,870.6 | 6,858.9 | 7,162.9 | 117.0 | 0.063x | 1.434x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 109,890.6 | 109,563.4 | 110,226.9 | 220.9 | 1.000x | 22.929x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,184.2 | 109,639.3 | 110,909.8 | 405.5 | 1.003x | 22.990x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,654.1 | 7,651.0 | 7,659.8 | 3.0 | 0.081x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,654.7 | 7,652.1 | 7,659.3 | 2.5 | 0.081x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,595.0 | 10,583.7 | 10,924.6 | 133.3 | 0.111x | 1.384x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,660.1 | 10,596.2 | 10,682.8 | 36.6 | 0.112x | 1.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94,866.3 | 94,825.4 | 95,235.6 | 151.8 | 0.998x | 12.394x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,030.3 | 94,903.6 | 95,251.1 | 131.2 | 1.000x | 12.416x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.7 | 9.9 | 0.1 | 0.329x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.1 | 0.336x | 1.022x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.4 | 15.4 | 15.9 | 0.2 | 0.519x | 1.580x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.2 | 0.7 | 0.551x | 1.678x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.7 | 29.0 | 30.5 | 0.5 | 1.000x | 3.044x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.8 | 29.4 | 32.5 | 1.2 | 1.003x | 3.053x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.2 | 21.4 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 21.4 | 21.2 | 26.5 | 2.1 | 0.038x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.9 | 60.9 | 63.6 | 1.0 | 0.110x | 2.908x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 229.9 | 229.3 | 231.3 | 0.7 | 0.411x | 10.806x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 232.4 | 230.1 | 233.9 | 1.3 | 0.415x | 10.925x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 560.0 | 549.1 | 565.6 | 6.1 | 1.000x | 26.321x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.7 | 34.5 | 0.3 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.7 | 0.0 | 0.051x | 1.000x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.8 | 62.4 | 1.8 | 0.088x | 1.720x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 67.5 | 66.9 | 73.1 | 2.3 | 0.103x | 2.005x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.6 | 650.8 | 664.5 | 5.1 | 1.000x | 19.535x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 665.3 | 648.9 | 745.2 | 34.8 | 1.012x | 19.764x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 61.9 | 61.8 | 62.9 | 0.5 | 0.094x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.6 | 74.1 | 4.5 | 0.095x | 1.012x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 62.8 | 62.6 | 63.3 | 0.2 | 0.095x | 1.014x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 65.8 | 64.4 | 67.0 | 1.0 | 0.100x | 1.062x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 79.6 | 84.2 | 2.0 | 0.123x | 1.316x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 660.0 | 657.9 | 686.9 | 11.0 | 1.000x | 10.656x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.7 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.051x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.6 | 71.3 | 74.6 | 1.1 | 0.115x | 2.277x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 83.0 | 82.0 | 84.2 | 0.8 | 0.130x | 2.569x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.5 | 634.5 | 654.8 | 6.7 | 1.000x | 19.820x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 641.6 | 633.4 | 648.7 | 5.2 | 1.002x | 19.854x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.9 | 0.2 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.7 | 58.2 | 66.0 | 3.0 | 0.091x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 81.2 | 82.4 | 0.4 | 0.127x | 1.402x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 88.2 | 88.2 | 90.7 | 1.0 | 0.137x | 1.513x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 90.4 | 90.3 | 91.5 | 0.5 | 0.141x | 1.550x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.3 | 635.8 | 667.0 | 11.4 | 1.000x | 11.013x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.0 | 0.040x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.9 | 0.1 | 0.040x | 1.000x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.5 | 18.3 | 18.9 | 0.2 | 0.044x | 1.099x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.7 | 20.8 | 0.0 | 0.050x | 1.235x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 413.4 | 407.3 | 417.6 | 3.4 | 0.994x | 24.627x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 415.8 | 409.8 | 418.6 | 3.2 | 1.000x | 24.771x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 23.0 | 23.0 | 29.3 | 2.5 | 0.056x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 28.0 | 1.9 | 0.057x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 23.9 | 0.1 | 0.058x | 1.030x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.0 | 0.0 | 0.063x | 1.130x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 57.6 | 55.3 | 62.7 | 2.7 | 0.141x | 2.504x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 409.7 | 406.5 | 431.1 | 9.0 | 1.000x | 17.805x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 11.8 | 12.8 | 0.3 | 0.060x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.0 | 14.3 | 0.8 | 0.060x | 1.006x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.4 | 36.4 | 4.2 | 0.125x | 2.086x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.0 | 0.126x | 2.106x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.5 | 204.6 | 211.3 | 2.2 | 1.000x | 16.730x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.7 | 206.8 | 214.5 | 2.8 | 1.001x | 16.748x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 27.5 | 0.2 | 0.037x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 28.3 | 27.1 | 37.0 | 3.7 | 0.039x | 1.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.0 | 64.6 | 68.0 | 1.1 | 0.092x | 2.476x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 245.9 | 243.1 | 249.5 | 2.1 | 0.339x | 9.087x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 247.3 | 244.6 | 257.4 | 4.5 | 0.341x | 9.137x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.8 | 712.2 | 741.7 | 10.3 | 1.000x | 26.779x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.3 | 0.2 | 0.052x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 42.3 | 43.6 | 0.5 | 0.080x | 1.550x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.2 | 47.6 | 1.3 | 0.082x | 1.594x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.4 | 537.5 | 546.3 | 3.1 | 1.000x | 19.368x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 547.2 | 540.4 | 553.8 | 4.9 | 1.009x | 19.542x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 49.0 | 0.2 | 0.090x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 48.7 | 48.4 | 55.3 | 2.7 | 0.090x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 50.0 | 49.6 | 50.9 | 0.4 | 0.093x | 1.031x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 52.7 | 51.5 | 56.0 | 1.6 | 0.098x | 1.087x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 76.0 | 73.5 | 76.6 | 1.1 | 0.141x | 1.567x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.6 | 535.6 | 561.5 | 9.7 | 1.000x | 11.104x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.4 | 55.4 | 56.3 | 0.3 | 0.099x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.5 | 55.8 | 0.1 | 0.099x | 1.005x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.9 | 55.6 | 56.7 | 0.4 | 0.100x | 1.008x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.6 | 62.0 | 1.6 | 0.104x | 1.046x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 560.1 | 555.7 | 569.2 | 4.5 | 1.000x | 10.107x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.1 | 560.4 | 580.9 | 7.8 | 1.002x | 10.124x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 65.0 | 63.6 | 65.7 | 0.7 | 0.116x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 66.7 | 64.7 | 70.7 | 2.0 | 0.119x | 1.027x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.5 | 89.8 | 96.8 | 2.7 | 0.161x | 1.392x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 116.3 | 2.7 | 0.195x | 1.687x |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 110.0 | 109.6 | 110.3 | 0.3 | 0.196x | 1.693x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.1 | 554.2 | 581.4 | 9.1 | 1.000x | 8.651x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.6 | 43.8 | 0.4 | 0.036x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.0 | 42.8 | 44.5 | 0.6 | 0.036x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 66.0 | 65.9 | 66.3 | 0.1 | 0.056x | 1.543x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.1 | 67.0 | 72.5 | 2.1 | 0.057x | 1.567x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,181.1 | 1,173.9 | 1,195.1 | 7.3 | 1.000x | 27.588x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,185.5 | 1,177.6 | 1,221.3 | 16.7 | 1.004x | 27.690x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.3 | 90.0 | 0.3 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 89.6 | 89.4 | 101.6 | 4.8 | 0.052x | 1.003x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 135.9 | 133.4 | 142.0 | 3.6 | 0.078x | 1.521x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 136.1 | 133.9 | 140.3 | 2.6 | 0.078x | 1.523x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.3 | 166.9 | 178.1 | 3.8 | 0.098x | 1.905x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,737.5 | 1,724.6 | 1,864.9 | 51.7 | 1.000x | 19.444x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.045x | 1.002x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.4 | 26.7 | 0.5 | 0.087x | 1.937x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.088x | 1.956x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.0 | 294.2 | 297.5 | 1.2 | 0.995x | 22.116x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.5 | 293.1 | 299.9 | 2.2 | 1.000x | 22.234x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.3 | 20.5 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 27.9 | 2.9 | 0.019x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.4 | 67.5 | 74.0 | 2.3 | 0.064x | 3.391x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 190.0 | 187.6 | 193.5 | 2.4 | 0.177x | 9.290x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 190.2 | 189.4 | 192.5 | 1.2 | 0.177x | 9.299x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.2 | 1,062.1 | 1,089.7 | 10.0 | 1.000x | 52.611x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 15.7 | 1.0 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.9 | 34.9 | 35.6 | 0.3 | 0.118x | 2.623x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 33.9 | 36.3 | 1.0 | 0.119x | 2.630x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.6 | 294.2 | 297.2 | 1.2 | 0.999x | 22.125x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.8 | 292.9 | 300.3 | 2.5 | 1.000x | 22.140x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.1 | 0.025x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 36.8 | 4.0 | 0.025x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.8 | 69.4 | 71.2 | 0.8 | 0.066x | 2.639x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 311.3 | 306.1 | 313.2 | 2.4 | 0.291x | 11.597x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 311.6 | 303.6 | 312.8 | 3.5 | 0.292x | 11.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.1 | 1,065.5 | 1,079.9 | 6.0 | 1.000x | 39.795x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.051x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.1 | 89.8 | 0.3 | 0.141x | 2.760x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.9 | 92.6 | 0.7 | 0.144x | 2.814x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.2 | 632.5 | 643.7 | 4.4 | 1.000x | 19.583x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.6 | 632.0 | 638.9 | 2.5 | 1.002x | 19.627x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 70.9 | 5.0 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.4 | 67.4 | 3.5 | 0.092x | 1.009x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 68.5 | 67.7 | 74.2 | 2.4 | 0.107x | 1.173x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.8 | 87.3 | 88.5 | 0.4 | 0.137x | 1.503x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 102.0 | 102.0 | 102.5 | 0.2 | 0.159x | 1.746x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.7 | 631.8 | 675.8 | 15.7 | 1.000x | 10.998x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.3 | 32.7 | 0.2 | 0.052x | 1.009x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.0 | 89.4 | 0.1 | 0.141x | 2.762x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 90.9 | 90.9 | 91.1 | 0.1 | 0.144x | 2.814x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 631.9 | 630.3 | 642.0 | 4.2 | 1.000x | 19.558x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.1 | 629.4 | 644.5 | 5.0 | 1.003x | 19.626x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 71.0 | 5.1 | 0.091x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.7 | 0.2 | 0.092x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 68.6 | 68.1 | 74.7 | 2.4 | 0.108x | 1.178x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.0 | 87.8 | 88.1 | 0.1 | 0.138x | 1.510x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 102.0 | 101.9 | 103.2 | 0.5 | 0.160x | 1.751x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.8 | 632.1 | 678.2 | 17.0 | 1.000x | 10.929x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.046x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.5 | 75.5 | 77.4 | 0.7 | 0.108x | 2.368x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.8 | 85.1 | 94.0 | 3.4 | 0.122x | 2.657x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 700.3 | 691.2 | 702.9 | 4.0 | 0.994x | 21.685x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 704.9 | 697.8 | 710.5 | 4.3 | 1.000x | 21.826x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 70.9 | 5.0 | 0.083x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.4 | 59.2 | 0.3 | 0.083x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 74.7 | 74.6 | 77.0 | 0.9 | 0.106x | 1.279x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.8 | 85.5 | 91.0 | 1.8 | 0.126x | 1.521x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 94.0 | 92.8 | 94.7 | 0.6 | 0.134x | 1.611x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 702.4 | 697.7 | 747.5 | 18.4 | 1.000x | 12.032x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.4 | 0.0 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.0 | 54.0 | 56.5 | 0.9 | 0.076x | 1.702x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72.7 | 72.4 | 73.3 | 0.3 | 0.101x | 2.252x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 719.7 | 714.7 | 725.4 | 4.2 | 1.000x | 22.279x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 719.8 | 718.8 | 723.8 | 2.2 | 1.000x | 22.282x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 71.4 | 5.2 | 0.080x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.3 | 58.9 | 0.2 | 0.081x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 73.5 | 70.4 | 78.8 | 3.1 | 0.101x | 1.258x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.8 | 83.1 | 85.9 | 1.0 | 0.115x | 1.434x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 85.9 | 85.6 | 86.2 | 0.2 | 0.118x | 1.470x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 728.2 | 726.1 | 746.5 | 8.4 | 1.000x | 12.463x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.5 | 0.1 | 0.045x | 1.001x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 54.2 | 54.1 | 55.0 | 0.3 | 0.075x | 1.680x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72.7 | 72.6 | 74.3 | 0.6 | 0.101x | 2.252x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 720.4 | 719.3 | 730.5 | 4.1 | 1.000x | 22.317x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 722.3 | 717.5 | 731.4 | 4.7 | 1.003x | 22.374x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 58.2 | 58.1 | 70.8 | 5.1 | 0.079x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.6 | 0.1 | 0.080x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 75.7 | 72.9 | 79.4 | 2.7 | 0.103x | 1.300x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 83.1 | 85.3 | 0.8 | 0.114x | 1.433x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 85.6 | 85.2 | 86.1 | 0.3 | 0.117x | 1.470x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 734.1 | 723.6 | 747.5 | 8.1 | 1.000x | 12.617x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.5 | 0.1 | 0.046x | 1.004x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.0 | 52.8 | 58.3 | 2.0 | 0.164x | 3.540x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.2 | 57.8 | 60.5 | 1.0 | 0.167x | 3.615x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 347.9 | 344.4 | 351.0 | 2.2 | 1.000x | 21.605x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 350.2 | 348.3 | 354.8 | 2.7 | 1.007x | 21.749x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 26.3 | 35.3 | 3.5 | 0.021x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 70.5 | 72.0 | 0.6 | 0.056x | 2.711x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 383.8 | 380.4 | 386.4 | 2.5 | 0.300x | 14.619x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 396.9 | 393.8 | 399.2 | 2.0 | 0.310x | 15.116x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,279.1 | 1,264.8 | 1,303.8 | 13.6 | 1.000x | 48.713x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 12.0 | 0.4 | 0.378x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 10.9 | 11.4 | 0.2 | 0.385x | 1.019x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.2 | 14.1 | 14.6 | 0.2 | 0.480x | 1.272x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.6 | 15.6 | 0.0 | 0.527x | 1.395x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 32.5 | 1.4 | 0.978x | 2.591x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.6 | 29.2 | 30.2 | 0.3 | 1.000x | 2.648x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 4.5 | 4.4 | 4.6 | 0.1 | 0.147x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 4.6 | 4.5 | 4.7 | 0.1 | 0.151x | 1.026x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 14.9 | 14.9 | 15.1 | 0.1 | 0.490x | 3.323x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.4 | 0.0 | 0.569x | 3.860x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 30.6 | 0.1 | 1.000x | 6.780x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.8 | 37.0 | 38.8 | 0.7 | 1.241x | 8.417x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.1 | 0.1 | 0.337x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.344x | 1.020x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 15.2 | 17.5 | 0.9 | 0.554x | 1.644x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.7 | 0.1 | 0.561x | 1.664x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 29.2 | 0.1 | 1.000x | 2.966x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.3 | 32.5 | 1.2 | 1.010x | 2.995x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 5.9 | 0.4 | 0.163x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 5.3 | 5.0 | 5.4 | 0.2 | 0.171x | 1.049x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 22.4 | 22.4 | 22.5 | 0.0 | 0.720x | 4.431x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 24.6 | 24.5 | 25.0 | 0.2 | 0.789x | 4.852x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.2 | 31.1 | 33.7 | 1.0 | 1.000x | 6.152x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.9 | 36.8 | 39.5 | 1.0 | 1.248x | 7.677x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.8 | 0.3 | 0.308x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.0 | 11.2 | 0.1 | 0.311x | 1.008x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.3 | 21.0 | 23.8 | 1.0 | 0.589x | 1.910x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.597x | 1.937x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.5 | 34.3 | 37.0 | 0.9 | 0.983x | 3.186x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.1 | 35.2 | 36.7 | 0.5 | 1.000x | 3.242x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.6 | 35.5 | 36.7 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.5 | 38.5 | 42.6 | 1.4 | 1.139x | 1.139x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 73.3 | 72.4 | 79.8 | 2.7 | 2.060x | 2.060x |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 73.4 | 73.3 | 73.7 | 0.1 | 2.062x | 2.062x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 618.9 | 612.9 | 635.6 | 7.7 | 17.394x | 17.394x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 620.4 | 616.2 | 635.3 | 7.4 | 17.436x | 17.436x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.2 | 0.0 | 0.552x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.2 | 19.3 | 0.1 | 0.554x | 1.003x |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.1 | 21.0 | 21.6 | 0.2 | 0.610x | 1.105x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.8 | 0.3 | 0.665x | 1.204x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.3 | 35.4 | 0.4 | 0.999x | 1.809x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 36.3 | 0.7 | 1.000x | 1.811x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 16.1 | 16.0 | 20.2 | 1.6 | 0.461x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 16.2 | 16.0 | 16.9 | 0.3 | 0.464x | 1.008x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.0 | 34.9 | 36.1 | 0.4 | 1.000x | 2.172x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 36.6 | 48.2 | 4.1 | 1.147x | 2.490x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 122.8 | 121.7 | 123.9 | 0.7 | 3.509x | 7.620x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 125.5 | 125.1 | 126.1 | 0.3 | 3.584x | 7.783x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,583,848.6 | 3,574,796.0 | 3,610,612.4 | 12,224.7 | 0.124x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,587,388.5 | 3,581,768.5 | 3,621,958.1 | 14,392.7 | 0.124x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,696,994.6 | 3,663,976.9 | 3,717,467.8 | 20,693.8 | 0.128x | 1.032x |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 5,179,320.7 | 5,134,193.7 | 7,682,122.0 | 1,000,435.5 | 0.180x | 1.445x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 5,260,367.7 | 5,226,587.7 | 5,399,742.0 | 61,422.8 | 0.183x | 1.468x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,821,951.8 | 28,594,672.7 | 29,128,028.5 | 199,799.6 | 1.000x | 8.042x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,092.5 | 18,063.0 | 18,197.4 | 47.8 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,886,284.8 | 1,884,519.8 | 1,912,248.1 | 10,362.9 | 104.258x | 104.258x |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,887,163.0 | 1,885,469.8 | 1,921,983.8 | 13,910.1 | 104.306x | 104.306x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,546,837.8 | 2,522,818.8 | 2,594,883.6 | 24,643.3 | 140.767x | 140.767x |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 16,042,291.3 | 15,929,887.3 | 16,079,748.0 | 54,548.4 | 886.680x | 886.680x |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16,092,335.0 | 15,990,307.7 | 16,139,312.0 | 60,723.6 | 889.446x | 889.446x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,005.5 | 17,928.7 | 18,262.5 | 119.9 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,875,774.8 | 1,875,332.2 | 1,877,435.4 | 743.3 | 104.178x | 104.178x | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,876,250.4 | 1,873,584.1 | 1,918,973.8 | 17,329.2 | 104.204x | 104.204x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,820,671.8 | 2,818,849.3 | 2,827,148.1 | 3,234.1 | 156.656x | 156.656x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,135,589.7 | 3,132,307.1 | 3,145,628.4 | 4,981.3 | 0.033x | 1.000x |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,148,674.1 | 3,134,659.6 | 3,183,629.3 | 17,250.0 | 0.034x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,974,673.2 | 5,952,678.1 | 6,152,557.4 | 73,402.9 | 0.064x | 1.905x |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17,151,501.3 | 16,742,832.3 | 17,601,914.0 | 289,537.3 | 0.183x | 5.470x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 17,380,189.0 | 16,832,286.0 | 17,644,394.0 | 320,359.9 | 0.185x | 5.543x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 93,897,422.0 | 93,774,270.8 | 94,633,276.7 | 307,804.0 | 1.000x | 29.946x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,121.3 | 18,037.1 | 18,234.7 | 78.8 | 1.000x | 1.000x |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,095,070.0 | 3,090,272.4 | 3,104,000.7 | 5,153.8 | 170.797x | 170.797x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,097,595.6 | 3,091,457.5 | 3,110,152.6 | 6,472.4 | 170.937x | 170.937x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,166,813.3 | 3,157,057.6 | 3,368,320.8 | 81,571.9 | 174.756x | 174.756x |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16,977,360.3 | 16,679,475.0 | 17,742,841.3 | 393,864.9 | 936.874x | 936.874x |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 17,088,094.0 | 16,560,657.7 | 17,648,674.0 | 344,244.7 | 942.984x | 942.984x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced) -- the three tokens that share one `dfa overflowed` RX_ENGINE_WHY and differ in what survived -- OR a `lang=count-collapsed (size cap retry, ...)`: the size-cap rescue stamps sel=selected (measured at pcrec 96e44c2), so it is bucketed on its why prefix and marked `size-cap rescue` until pcrec's [LIM-1] gives it a token (inbox I-19 (3)).
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 161,367,376.0 | 160,364,191.0 | 168,045,206.0 | 2,768,245.7 | 5 | 43,224 | 82,080 | 13,386 | 0.017 | compiled=5 | 9,593,116.0 | 150,683,764.0 | 199,961.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 173,642,569.0 | 162,000,350.0 | 195,343,764.0 | 11,832,867.7 | 5 | 47,464 | 94,291 | 15,302 | 0.068 (max is trial 1) | compiled=5 | 17,795,364.0 | 160,135,889.0 | 196,911.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 156,332,757.0 | 146,742,271.0 | 169,572,655.0 | 8,313,785.5 | 5 | 43,224 | 81,897 | 13,199 | 0.053 | compiled=5 | 9,544,566.0 | 146,686,991.0 | 187,602.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 169,353,324.0 | 158,336,598.0 | 175,847,071.0 | 6,277,917.7 | 5 | 47,464 | 94,108 | 15,115 | 0.037 | compiled=5 | 11,953,990.0 | 157,465,023.0 | 179,471.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 560,952,030.0 | 552,401,499.0 | 574,504,699.0 | 7,800,620.7 | 5 | 39,128 | 58,254 | 56,700 | 0.014 | compiled=5 | 2,163,513.0 | 558,645,066.0 | 198,721.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 561,262,931.0 | 553,920,967.0 | 566,432,401.0 | 4,509,880.6 | 5 | 39,128 | 58,370 | 56,816 | 0.008 | compiled=5 | 2,579,045.0 | 557,399,298.0 | 90,240.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 549,464,481.0 | 548,090,774.0 | 552,673,581.0 | 1,655,066.8 | 5 | 39,128 | 58,254 | 56,700 | 0.003 (max is trial 1) | compiled=5 | 2,182,383.0 | 545,859,350.0 | 188,261.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 568,066,400.0 | 554,524,271.0 | 569,803,801.0 | 5,749,619.0 | 5 | 39,128 | 58,370 | 56,816 | 0.010 | compiled=5 | 2,302,993.0 | 565,593,376.0 | 100,111.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 133,986,396.0 | 129,174,899.0 | 142,126,773.0 | 4,614,847.4 | 5 | 22,712 | 17,731 | 12,734 | 0.034 | compiled=5 | 1,734,020.0 | 132,040,485.0 | 188,771.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 147,942,328.0 | 144,005,944.0 | 154,591,887.0 | 3,790,768.5 | 5 | 22,856 | 20,074 | 14,751 | 0.026 | compiled=5 | 1,672,159.0 | 145,940,916.0 | 99,891.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 131,184,190.0 | 124,625,080.0 | 138,781,244.0 | 5,533,696.7 | 5 | 22,712 | 17,731 | 12,734 | 0.042 | compiled=5 | 1,680,810.0 | 129,391,839.0 | 117,511.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 149,578,517.0 | 143,713,063.0 | 151,059,906.0 | 2,757,231.6 | 5 | 22,856 | 20,074 | 14,751 | 0.018 | compiled=5 | 1,678,290.0 | 147,514,265.0 | 102,211.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 144,984,105.0 | 140,000,455.0 | 155,450,617.0 | 5,526,755.8 | 5 | 22,344 | 17,660 | 17,660 | 0.038 | compiled=5 | 1,620,700.0 | 143,173,954.0 | 186,041.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 149,400,661.0 | 140,726,940.0 | 152,597,870.0 | 4,214,821.7 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 1,528,869.0 | 147,835,302.0 | 106,611.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 143,038,783.0 | 142,028,867.0 | 152,074,138.0 | 3,847,908.1 | 5 | 22,344 | 17,660 | 17,660 | 0.027 | compiled=5 | 1,451,489.0 | 140,558,609.0 | 190,721.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 149,887,504.0 | 141,599,525.0 | 152,215,158.0 | 4,185,187.6 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 2,899,487.0 | 146,859,346.0 | 187,241.0 |
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
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,970.0 | 63,740.0 | 158,851.0 | 35,898.1 | 5 | 951 | 0.513 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,320.0 | 4,940.0 | 55,180.0 | 19,635.4 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 61,501.0 | 54,730.0 | 185,332.0 | 49,645.3 | 5 | 1,609 | 0.807 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,880.0 | 12,990.0 | 43,700.0 | 11,712.6 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 370.0 | 310.0 | 15,581.0 | 6,081.7 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,400.0 | 12,240.0 | 56,820.0 | 17,389.8 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

