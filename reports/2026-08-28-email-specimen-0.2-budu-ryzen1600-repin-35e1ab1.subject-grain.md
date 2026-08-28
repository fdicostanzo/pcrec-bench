# pcrec-bench report

reporter: v6 (2026-08-28)

## Query

- filters: subbench=email-specimen, version=0.2
- record source: store/index.tsv (26 candidate file(s))
- records included: 6
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260828T145051Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260828T145051Z.jsonl)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260828T141718Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260828T141718Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-nocaps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-in-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z.jsonl)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.4 | 70.4 | 0.4 | 0.080x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 86.0 | 85.7 | 86.5 | 0.3 | 0.098x | 1.238x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 148.5 | 147.8 | 149.5 | 0.6 | 0.170x | 2.137x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.8 | 147.6 | 149.2 | 0.6 | 0.170x | 2.142x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 865.1 | 860.5 | 873.8 | 4.6 | 0.991x | 12.451x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 873.4 | 859.3 | 876.6 | 6.1 | 1.000x | 12.570x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.6 | 59.9 | 0.5 | 0.068x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.1 | 0.2 | 0.072x | 1.068x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 148.9 | 147.9 | 151.3 | 1.1 | 0.171x | 2.538x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 152.5 | 152.4 | 153.3 | 0.3 | 0.176x | 2.599x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.4 | 154.2 | 155.3 | 0.4 | 0.178x | 2.631x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.7 | 864.9 | 879.9 | 6.1 | 1.000x | 14.805x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.9 | 89.6 | 90.5 | 0.3 | 0.073x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.0 | 105.2 | 0.5 | 0.086x | 1.168x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.6 | 202.8 | 204.1 | 0.5 | 0.166x | 2.266x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 214.9 | 212.7 | 223.4 | 3.8 | 0.175x | 2.391x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,223.0 | 1,221.0 | 1,234.6 | 4.8 | 0.998x | 13.611x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,226.0 | 1,223.6 | 1,227.7 | 1.4 | 1.000x | 13.644x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 77.8 | 77.7 | 78.3 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 79.9 | 80.6 | 0.2 | 0.066x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.4 | 174.6 | 176.8 | 0.7 | 0.144x | 2.254x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 207.3 | 206.1 | 209.5 | 1.2 | 0.170x | 2.665x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 207.6 | 206.8 | 209.6 | 0.9 | 0.170x | 2.668x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,220.5 | 1,220.1 | 1,223.1 | 1.1 | 1.000x | 15.688x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.9 | 33.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 49.2 | 50.1 | 0.3 | 0.065x | 1.488x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.7 | 105.0 | 0.1 | 0.138x | 3.158x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 105.6 | 106.4 | 0.3 | 0.139x | 3.183x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 753.7 | 750.3 | 756.8 | 2.3 | 0.993x | 22.698x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 759.2 | 753.3 | 771.1 | 6.1 | 1.000x | 22.864x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.035x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 29.0 | 0.3 | 0.038x | 1.076x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103.6 | 103.3 | 103.9 | 0.2 | 0.139x | 3.921x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 107.4 | 107.0 | 109.1 | 0.9 | 0.144x | 4.063x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.2 | 119.9 | 123.8 | 1.4 | 0.163x | 4.625x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 747.6 | 744.6 | 765.1 | 7.6 | 1.000x | 28.289x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 97.3 | 97.6 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.9 | 111.6 | 0.3 | 0.084x | 1.141x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 216.7 | 216.2 | 217.4 | 0.4 | 0.163x | 2.225x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 220.2 | 220.1 | 227.4 | 3.1 | 0.166x | 2.261x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,321.6 | 1,308.9 | 1,336.6 | 8.8 | 0.996x | 13.569x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,327.6 | 1,310.5 | 1,332.4 | 7.6 | 1.000x | 13.630x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 86.5 | 86.3 | 87.3 | 0.4 | 0.066x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 87.7 | 87.4 | 88.3 | 0.3 | 0.067x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 183.7 | 182.5 | 186.9 | 1.8 | 0.139x | 2.124x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 220.9 | 219.9 | 222.6 | 1.0 | 0.168x | 2.555x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 228.2 | 227.1 | 230.1 | 1.0 | 0.173x | 2.639x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,317.7 | 1,311.6 | 1,326.5 | 5.7 | 1.000x | 15.238x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 131.8 | 131.4 | 132.2 | 0.3 | 0.148x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 147.1 | 146.5 | 148.2 | 0.5 | 0.165x | 1.116x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 162.0 | 161.1 | 163.0 | 0.6 | 0.182x | 1.229x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 162.9 | 162.6 | 163.8 | 0.4 | 0.183x | 1.236x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 890.6 | 872.0 | 896.2 | 9.3 | 0.999x | 6.756x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 891.1 | 879.6 | 899.7 | 6.8 | 1.000x | 6.760x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 120.3 | 120.9 | 0.2 | 0.138x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 123.6 | 123.4 | 123.8 | 0.1 | 0.141x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.7 | 166.8 | 168.5 | 0.6 | 0.192x | 1.391x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 168.0 | 167.8 | 168.0 | 0.1 | 0.192x | 1.394x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 171.4 | 171.1 | 172.3 | 0.4 | 0.196x | 1.423x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 874.5 | 868.7 | 883.9 | 6.0 | 1.000x | 7.256x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.7 | 33.2 | 0.2 | 0.043x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.3 | 49.1 | 49.6 | 0.2 | 0.065x | 1.494x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.5 | 105.0 | 0.2 | 0.137x | 3.174x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 105.2 | 105.9 | 0.3 | 0.139x | 3.203x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 749.2 | 744.6 | 756.5 | 4.1 | 0.983x | 22.696x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 762.5 | 746.5 | 789.5 | 14.0 | 1.000x | 23.096x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.6 | 26.1 | 27.2 | 0.4 | 0.036x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.0 | 28.3 | 29.9 | 0.6 | 0.039x | 1.092x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103.4 | 103.4 | 103.7 | 0.1 | 0.139x | 3.893x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 107.1 | 107.0 | 107.3 | 0.1 | 0.143x | 4.031x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.5 | 119.7 | 124.4 | 1.6 | 0.163x | 4.571x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 746.7 | 744.4 | 763.1 | 7.6 | 1.000x | 28.104x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 65.5 | 65.2 | 65.9 | 0.2 | 0.049x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 81.7 | 81.7 | 81.9 | 0.1 | 0.061x | 1.247x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 221.6 | 220.3 | 230.2 | 3.6 | 0.165x | 3.383x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 230.2 | 229.5 | 230.7 | 0.5 | 0.171x | 3.515x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,344.4 | 1,335.7 | 1,348.7 | 4.3 | 0.998x | 20.525x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,346.4 | 1,344.4 | 1,353.3 | 3.5 | 1.000x | 20.557x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 57.8 | 0.8 | 0.042x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 59.1 | 59.0 | 59.3 | 0.1 | 0.044x | 1.058x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.0 | 164.8 | 165.8 | 0.4 | 0.123x | 2.955x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 227.8 | 227.3 | 228.4 | 0.4 | 0.170x | 4.081x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 230.0 | 228.6 | 231.0 | 0.7 | 0.172x | 4.119x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,337.1 | 1,334.5 | 1,344.5 | 3.5 | 1.000x | 23.951x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 102.5 | 102.2 | 102.9 | 0.2 | 0.105x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.2 | 117.8 | 118.4 | 0.2 | 0.122x | 1.153x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.4 | 167.0 | 168.9 | 0.7 | 0.173x | 1.643x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 170.3 | 170.1 | 174.4 | 1.8 | 0.175x | 1.662x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.7 | 965.7 | 995.4 | 10.5 | 1.000x | 9.488x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 972.8 | 961.6 | 985.1 | 7.8 | 1.000x | 9.490x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 92.1 | 91.9 | 92.6 | 0.2 | 0.094x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 94.8 | 94.2 | 95.5 | 0.5 | 0.097x | 1.030x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.6 | 170.1 | 174.0 | 1.4 | 0.175x | 1.853x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.5 | 171.9 | 173.5 | 0.6 | 0.177x | 1.873x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 175.0 | 174.7 | 175.9 | 0.4 | 0.179x | 1.900x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 974.8 | 959.9 | 980.6 | 7.2 | 1.000x | 10.588x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 80.3 | 80.0 | 80.6 | 0.2 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.0 | 95.8 | 96.2 | 0.1 | 0.109x | 1.195x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 153.8 | 153.5 | 154.4 | 0.3 | 0.175x | 1.916x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 154.7 | 154.2 | 155.2 | 0.4 | 0.176x | 1.927x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.9 | 853.3 | 870.3 | 5.6 | 0.977x | 10.712x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.0 | 855.0 | 891.5 | 12.7 | 1.000x | 10.962x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.5 | 69.7 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.2 | 73.6 | 0.1 | 0.085x | 1.054x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 150.5 | 149.7 | 154.0 | 1.5 | 0.174x | 2.163x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 154.0 | 153.4 | 154.9 | 0.6 | 0.178x | 2.212x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.3 | 157.8 | 158.8 | 0.4 | 0.183x | 2.274x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 863.4 | 857.2 | 871.1 | 5.4 | 1.000x | 12.405x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.7 | 61.6 | 62.2 | 0.2 | 0.071x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.3 | 0.0 | 0.090x | 1.268x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.8 | 145.4 | 146.3 | 0.3 | 0.168x | 2.362x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.6 | 146.0 | 147.1 | 0.4 | 0.169x | 2.374x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.6 | 856.6 | 864.6 | 2.9 | 0.991x | 13.924x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 867.4 | 844.6 | 877.5 | 11.6 | 1.000x | 14.051x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 52.1 | 0.3 | 0.060x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.2 | 56.0 | 0.3 | 0.065x | 1.078x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 146.9 | 146.3 | 151.9 | 2.1 | 0.171x | 2.855x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.8 | 147.6 | 149.8 | 0.8 | 0.172x | 2.871x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 150.0 | 149.6 | 150.5 | 0.3 | 0.175x | 2.914x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 857.1 | 853.7 | 864.5 | 3.9 | 1.000x | 16.654x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.5 | 62.0 | 0.2 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.4 | 78.2 | 79.5 | 0.5 | 0.108x | 1.266x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.3 | 105.7 | 107.6 | 0.7 | 0.148x | 1.734x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 107.8 | 105.7 | 110.1 | 1.4 | 0.149x | 1.741x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 712.9 | 702.3 | 714.8 | 5.5 | 0.986x | 11.516x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.3 | 712.8 | 767.5 | 19.9 | 1.000x | 11.684x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.5 | 51.9 | 0.2 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.3 | 56.0 | 0.3 | 0.078x | 1.079x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 102.1 | 102.0 | 102.2 | 0.1 | 0.143x | 1.980x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 104.5 | 0.3 | 0.145x | 2.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.9 | 119.4 | 122.7 | 1.4 | 0.168x | 2.327x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 715.9 | 707.2 | 723.1 | 6.0 | 1.000x | 13.890x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.1 | 45.8 | 1.8 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.6 | 0.2 | 0.070x | 1.047x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 219.7 | 210.9 | 224.5 | 5.3 | 0.355x | 5.309x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.7 | 217.3 | 225.9 | 3.2 | 0.358x | 5.356x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.4 | 609.4 | 623.6 | 5.1 | 0.990x | 14.796x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.8 | 617.4 | 619.2 | 0.6 | 1.000x | 14.953x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.5 | 35.1 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.7 | 35.2 | 0.2 | 0.007x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 438.6 | 430.2 | 441.4 | 3.9 | 0.094x | 12.656x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,010.4 | 1,941.6 | 2,094.4 | 50.5 | 0.429x | 58.010x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,042.4 | 1,955.5 | 2,074.6 | 42.7 | 0.436x | 58.933x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,684.8 | 4,671.4 | 4,709.7 | 14.5 | 1.000x | 135.177x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.3 | 78.8 | 0.9 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.5 | 92.5 | 94.7 | 0.8 | 0.084x | 1.203x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.6 | 196.2 | 205.2 | 3.2 | 0.179x | 2.569x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.8 | 200.7 | 206.8 | 2.8 | 0.182x | 2.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,088.6 | 1,085.1 | 1,104.6 | 7.5 | 0.986x | 14.150x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,103.7 | 1,082.3 | 1,108.5 | 9.8 | 1.000x | 14.346x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.6 | 67.8 | 0.8 | 0.060x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.0 | 70.1 | 0.4 | 0.063x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.5 | 170.2 | 178.3 | 3.1 | 0.156x | 2.588x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.3 | 203.7 | 215.0 | 4.3 | 0.187x | 3.102x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 206.1 | 204.9 | 206.5 | 0.6 | 0.189x | 3.128x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,092.2 | 1,086.2 | 1,100.8 | 5.0 | 1.000x | 16.580x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.1 | 78.7 | 0.9 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.5 | 92.4 | 92.5 | 0.0 | 0.084x | 1.208x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.8 | 196.6 | 198.9 | 0.8 | 0.181x | 2.583x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.4 | 200.1 | 207.2 | 2.9 | 0.184x | 2.630x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,094.6 | 1,082.8 | 1,107.3 | 8.4 | 1.000x | 14.295x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,096.3 | 1,093.7 | 1,102.0 | 3.0 | 1.002x | 14.318x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.8 | 66.9 | 0.4 | 0.060x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.063x | 1.048x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.3 | 170.2 | 178.2 | 3.1 | 0.155x | 2.587x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.1 | 203.8 | 218.7 | 5.9 | 0.185x | 3.100x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.8 | 204.6 | 206.9 | 0.8 | 0.187x | 3.125x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,100.4 | 1,079.2 | 1,106.0 | 9.7 | 1.000x | 16.713x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.3 | 62.1 | 64.8 | 1.0 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.4 | 0.1 | 0.090x | 1.257x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 155.8 | 155.3 | 156.7 | 0.4 | 0.179x | 2.501x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 157.7 | 157.5 | 158.3 | 0.3 | 0.181x | 2.531x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 870.5 | 865.0 | 873.3 | 3.1 | 0.999x | 13.968x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.4 | 867.3 | 880.6 | 4.6 | 1.000x | 13.982x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 52.1 | 0.3 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 55.7 | 0.1 | 0.064x | 1.077x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.3 | 154.1 | 158.5 | 1.7 | 0.177x | 2.996x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 162.2 | 161.6 | 162.9 | 0.5 | 0.186x | 3.150x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 163.7 | 163.3 | 163.8 | 0.2 | 0.188x | 3.178x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 872.5 | 867.3 | 874.6 | 2.8 | 1.000x | 16.942x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.5 | 75.4 | 1.1 | 0.069x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.1 | 89.6 | 0.2 | 0.084x | 1.224x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.5 | 198.3 | 203.5 | 2.2 | 0.189x | 2.736x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.6 | 199.6 | 204.3 | 1.7 | 0.190x | 2.752x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.9 | 1,050.0 | 1,069.7 | 6.6 | 1.000x | 14.514x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,066.2 | 1,060.9 | 1,092.6 | 11.5 | 1.008x | 14.628x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.8 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.1 | 66.6 | 0.5 | 0.062x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.6 | 172.4 | 177.9 | 2.3 | 0.163x | 2.757x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 203.2 | 203.0 | 215.2 | 4.8 | 0.192x | 3.245x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.1 | 204.4 | 206.1 | 0.6 | 0.194x | 3.275x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,058.6 | 1,052.5 | 1,066.9 | 5.6 | 1.000x | 16.901x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.3 | 36.5 | 1.6 | 0.090x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.7 | 34.8 | 35.7 | 0.3 | 0.098x | 1.098x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.4 | 102.2 | 105.9 | 1.2 | 0.288x | 3.213x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.2 | 105.9 | 109.2 | 1.5 | 0.293x | 3.269x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 361.8 | 358.2 | 365.3 | 2.3 | 0.997x | 11.133x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 363.1 | 359.3 | 364.3 | 1.8 | 1.000x | 11.171x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.3 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.8 | 0.3 | 0.011x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259.5 | 257.8 | 263.2 | 2.0 | 0.109x | 9.944x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,495.0 | 1,423.4 | 1,531.2 | 45.1 | 0.626x | 57.281x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,522.3 | 1,402.8 | 1,561.0 | 56.0 | 0.638x | 58.329x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,386.4 | 2,363.3 | 2,390.7 | 9.7 | 1.000x | 91.438x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.5 | 78.1 | 0.6 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 93.3 | 92.3 | 94.1 | 0.7 | 0.085x | 1.215x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.9 | 197.8 | 198.8 | 0.4 | 0.181x | 2.579x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.9 | 200.7 | 207.2 | 2.8 | 0.183x | 2.617x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,094.7 | 1,088.3 | 1,112.3 | 8.0 | 1.000x | 14.261x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,100.4 | 1,089.5 | 1,103.4 | 5.0 | 1.005x | 14.335x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.5 | 0.2 | 0.063x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.5 | 170.3 | 178.7 | 3.2 | 0.155x | 2.594x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 205.0 | 204.2 | 218.5 | 5.5 | 0.186x | 3.120x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 206.9 | 204.8 | 208.1 | 1.1 | 0.188x | 3.148x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,102.8 | 1,091.2 | 1,106.1 | 5.9 | 1.000x | 16.785x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.7 | 72.1 | 73.0 | 0.3 | 0.069x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.6 | 89.4 | 92.4 | 1.1 | 0.085x | 1.232x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 198.0 | 197.5 | 206.2 | 3.3 | 0.187x | 2.722x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.5 | 199.8 | 204.7 | 1.9 | 0.189x | 2.757x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,059.3 | 1,051.4 | 1,066.8 | 5.4 | 1.000x | 14.562x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,064.4 | 1,055.0 | 1,067.7 | 4.6 | 1.005x | 14.632x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 63.1 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.7 | 0.3 | 0.062x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.1 | 172.3 | 177.3 | 2.0 | 0.163x | 2.764x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.1 | 203.1 | 214.9 | 4.5 | 0.192x | 3.258x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.4 | 203.8 | 205.9 | 0.8 | 0.194x | 3.280x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,060.6 | 1,050.1 | 1,069.2 | 7.2 | 1.000x | 16.933x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 34.1 | 34.7 | 0.2 | 0.088x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.2 | 38.9 | 0.9 | 0.095x | 1.073x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.5 | 106.8 | 0.8 | 0.270x | 3.056x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.6 | 106.0 | 110.0 | 1.5 | 0.275x | 3.109x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.7 | 387.2 | 390.1 | 1.1 | 0.999x | 11.308x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 388.0 | 385.7 | 394.0 | 2.8 | 1.000x | 11.317x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 28.0 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.8 | 28.2 | 0.1 | 0.011x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 266.3 | 263.5 | 271.7 | 3.1 | 0.105x | 9.620x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,527.8 | 1,485.2 | 1,579.5 | 31.3 | 0.602x | 55.199x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,554.3 | 1,463.9 | 1,578.7 | 41.3 | 0.612x | 56.156x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,539.6 | 2,532.8 | 2,564.0 | 11.1 | 1.000x | 91.757x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 83.5 | 83.4 | 84.2 | 0.3 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 100.2 | 100.0 | 101.1 | 0.4 | 0.090x | 1.199x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 220.9 | 220.8 | 222.4 | 0.6 | 0.199x | 2.644x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 225.5 | 222.4 | 230.8 | 2.9 | 0.203x | 2.699x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,112.0 | 1,108.2 | 1,133.7 | 9.5 | 1.000x | 13.310x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,115.5 | 1,110.3 | 1,119.5 | 4.1 | 1.003x | 13.351x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 73.0 | 72.8 | 74.0 | 0.5 | 0.066x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 76.9 | 76.8 | 77.3 | 0.2 | 0.069x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.0 | 174.8 | 179.9 | 2.0 | 0.158x | 2.397x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 210.2 | 208.9 | 224.4 | 5.9 | 0.189x | 2.879x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 211.3 | 210.0 | 216.5 | 2.3 | 0.190x | 2.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,110.3 | 1,105.6 | 1,117.4 | 4.2 | 1.000x | 15.212x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.8 | 62.1 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.4 | 0.1 | 0.068x | 1.264x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.9 | 164.8 | 177.8 | 5.2 | 0.143x | 2.663x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.9 | 168.5 | 174.4 | 2.1 | 0.148x | 2.760x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,144.8 | 1,137.9 | 1,153.6 | 5.6 | 0.994x | 18.489x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,151.2 | 1,146.1 | 1,180.7 | 12.8 | 1.000x | 18.592x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.3 | 52.7 | 0.5 | 0.045x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.3 | 56.3 | 0.4 | 0.049x | 1.074x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.8 | 110.5 | 113.1 | 1.0 | 0.097x | 2.145x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.2 | 170.1 | 170.3 | 0.1 | 0.149x | 3.295x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 171.5 | 171.2 | 172.6 | 0.5 | 0.150x | 3.321x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,139.6 | 1,133.0 | 1,159.3 | 9.0 | 1.000x | 22.066x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 91.7 | 0.2 | 0.134x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 106.9 | 107.3 | 0.1 | 0.156x | 1.171x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 137.4 | 137.3 | 145.8 | 3.3 | 0.201x | 1.503x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 137.7 | 137.6 | 141.0 | 1.4 | 0.201x | 1.507x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 679.8 | 675.9 | 683.4 | 2.9 | 0.993x | 7.437x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.7 | 677.9 | 701.9 | 9.3 | 1.000x | 7.490x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 79.4 | 80.9 | 0.5 | 0.119x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.1 | 83.0 | 83.9 | 0.4 | 0.123x | 1.034x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.7 | 98.5 | 100.9 | 1.0 | 0.146x | 1.227x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 140.0 | 139.8 | 141.3 | 0.5 | 0.207x | 1.741x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 141.2 | 141.2 | 142.0 | 0.3 | 0.209x | 1.756x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 675.9 | 670.7 | 682.7 | 4.0 | 1.000x | 8.407x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.9 | 77.1 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.7 | 92.5 | 93.0 | 0.2 | 0.081x | 1.205x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.1 | 165.8 | 178.3 | 4.9 | 0.145x | 2.159x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 169.6 | 172.9 | 1.2 | 0.149x | 2.211x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,129.4 | 1,123.1 | 1,134.3 | 3.6 | 0.988x | 14.680x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,143.1 | 1,127.4 | 1,164.5 | 11.8 | 1.000x | 14.857x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.5 | 65.9 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.1 | 0.1 | 0.061x | 1.051x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.9 | 106.4 | 108.5 | 0.8 | 0.095x | 1.625x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 171.1 | 170.9 | 171.2 | 0.1 | 0.152x | 2.602x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 172.2 | 172.1 | 172.7 | 0.2 | 0.153x | 2.618x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,128.0 | 1,120.4 | 1,132.8 | 4.0 | 1.000x | 17.153x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.7 | 62.6 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.1 | 78.6 | 0.1 | 0.068x | 1.260x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.9 | 168.6 | 173.5 | 1.8 | 0.147x | 2.720x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.6 | 172.5 | 174.4 | 0.7 | 0.150x | 2.780x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,151.2 | 1,144.5 | 1,189.5 | 16.4 | 1.000x | 18.540x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,152.1 | 1,144.8 | 1,155.0 | 3.4 | 1.001x | 18.554x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.4 | 51.8 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.3 | 55.7 | 0.2 | 0.048x | 1.074x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.4 | 109.6 | 112.8 | 1.3 | 0.096x | 2.136x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 174.3 | 174.2 | 174.4 | 0.1 | 0.152x | 3.373x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 175.2 | 175.1 | 175.4 | 0.1 | 0.153x | 3.391x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,146.9 | 1,139.3 | 1,160.5 | 7.1 | 1.000x | 22.192x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.5 | 76.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.4 | 92.4 | 92.7 | 0.1 | 0.081x | 1.207x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 171.3 | 171.3 | 176.1 | 1.9 | 0.150x | 2.238x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.7 | 175.3 | 176.3 | 0.3 | 0.153x | 2.294x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,130.6 | 1,125.2 | 1,148.7 | 9.0 | 0.987x | 14.767x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,146.0 | 1,129.8 | 1,185.8 | 20.0 | 1.000x | 14.967x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 65.9 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.061x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.7 | 106.5 | 108.9 | 1.0 | 0.095x | 1.638x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 176.7 | 176.4 | 179.6 | 1.2 | 0.156x | 2.686x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 177.9 | 177.4 | 178.2 | 0.2 | 0.157x | 2.705x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,135.8 | 1,133.7 | 1,141.3 | 2.7 | 1.000x | 17.271x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.3 | 91.7 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 107.0 | 107.3 | 0.1 | 0.156x | 1.171x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 137.3 | 141.3 | 1.8 | 0.201x | 1.511x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 136.9 | 145.2 | 3.1 | 0.201x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 679.7 | 675.5 | 681.0 | 2.2 | 0.991x | 7.435x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 686.2 | 674.1 | 699.6 | 8.8 | 1.000x | 7.506x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.2 | 81.4 | 0.4 | 0.119x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.7 | 83.2 | 84.2 | 0.4 | 0.124x | 1.041x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.6 | 98.4 | 101.0 | 1.0 | 0.148x | 1.238x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 140.1 | 139.9 | 140.5 | 0.2 | 0.208x | 1.742x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 141.2 | 141.0 | 141.6 | 0.2 | 0.210x | 1.756x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 673.6 | 673.3 | 682.5 | 3.5 | 1.000x | 8.377x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 91.5 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.3 | 107.1 | 107.4 | 0.1 | 0.099x | 1.174x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 167.3 | 166.8 | 188.1 | 8.7 | 0.155x | 1.831x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.0 | 170.7 | 174.4 | 1.4 | 0.161x | 1.904x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,072.2 | 1,059.4 | 1,076.9 | 5.8 | 0.992x | 11.734x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,080.5 | 1,067.9 | 1,110.8 | 14.4 | 1.000x | 11.825x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.1 | 80.8 | 0.2 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.6 | 83.1 | 84.8 | 0.6 | 0.078x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.0 | 103.7 | 106.5 | 1.1 | 0.098x | 1.303x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 171.7 | 171.6 | 172.0 | 0.1 | 0.160x | 2.131x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 173.2 | 173.0 | 173.5 | 0.2 | 0.161x | 2.150x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.3 | 1,059.4 | 1,088.4 | 9.3 | 1.000x | 13.320x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.8 | 27.7 | 0.4 | 0.034x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 31.9 | 34.0 | 0.7 | 0.043x | 1.245x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 180.4 | 179.0 | 203.8 | 9.9 | 0.230x | 6.717x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 185.8 | 181.2 | 197.1 | 6.7 | 0.236x | 6.918x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.7 | 775.4 | 791.5 | 6.2 | 1.000x | 29.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.9 | 778.2 | 817.2 | 13.7 | 1.000x | 29.259x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.1 | 22.3 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.3 | 0.1 | 0.008x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.6 | 218.4 | 223.2 | 2.0 | 0.083x | 9.969x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 950.6 | 867.0 | 1,019.5 | 51.5 | 0.356x | 42.957x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,077.8 | 917.6 | 1,230.1 | 124.7 | 0.404x | 48.704x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.9 | 2,663.0 | 2,682.9 | 6.8 | 1.000x | 120.608x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 51.1 | 50.7 | 51.6 | 0.3 | 0.065x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 53.4 | 53.7 | 0.1 | 0.068x | 1.046x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 181.4 | 177.8 | 193.7 | 6.5 | 0.231x | 3.549x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 184.3 | 182.3 | 198.3 | 6.7 | 0.235x | 3.605x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.8 | 771.5 | 790.8 | 7.0 | 0.996x | 15.273x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 784.2 | 773.6 | 818.1 | 15.8 | 1.000x | 15.340x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.1 | 45.6 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 45.6 | 45.4 | 45.7 | 0.1 | 0.017x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.6 | 231.2 | 239.7 | 2.9 | 0.088x | 5.138x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.4 | 2,665.2 | 2,673.8 | 3.2 | 1.000x | 58.717x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 3,198.1 | 3,148.9 | 3,471.1 | 122.4 | 1.198x | 70.347x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,299.0 | 3,230.5 | 3,365.9 | 50.6 | 1.236x | 72.568x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.7 | 27.1 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 31.6 | 34.6 | 1.3 | 0.041x | 1.203x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 182.2 | 181.5 | 198.0 | 6.5 | 0.234x | 6.805x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 192.6 | 179.5 | 197.0 | 7.4 | 0.247x | 7.192x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.0 | 776.4 | 817.8 | 15.5 | 1.000x | 29.130x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.7 | 773.6 | 790.5 | 6.0 | 1.005x | 29.265x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 22.4 | 0.0 | 0.008x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.8 | 217.5 | 222.4 | 2.2 | 0.083x | 10.030x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 829.1 | 774.7 | 1,003.1 | 99.3 | 0.310x | 37.497x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 910.3 | 823.4 | 931.5 | 40.0 | 0.340x | 41.169x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,674.4 | 2,662.5 | 2,678.2 | 5.8 | 1.000x | 120.953x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.6 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.6 | 38.0 | 39.8 | 0.7 | 0.049x | 1.088x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 180.3 | 178.0 | 194.1 | 7.1 | 0.231x | 5.087x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 183.4 | 181.0 | 198.7 | 7.3 | 0.235x | 5.173x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.9 | 773.2 | 816.6 | 15.5 | 1.000x | 22.054x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.3 | 775.2 | 790.7 | 5.7 | 1.002x | 22.094x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 29.6 | 29.4 | 29.9 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.3 | 29.8 | 0.2 | 0.011x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.1 | 228.0 | 236.0 | 2.9 | 0.087x | 7.876x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,378.1 | 1,328.7 | 1,454.5 | 43.4 | 0.516x | 46.573x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,393.8 | 1,329.8 | 1,477.1 | 53.3 | 0.522x | 47.106x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.7 | 2,661.6 | 2,683.0 | 7.4 | 1.000x | 90.325x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.3 | 32.0 | 0.3 | 0.034x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.9 | 36.3 | 38.1 | 0.7 | 0.040x | 1.170x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.8 | 244.4 | 319.0 | 26.0 | 0.326x | 9.568x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 301.9 | 287.5 | 316.4 | 9.4 | 0.326x | 9.569x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 927.1 | 922.9 | 959.8 | 13.4 | 1.000x | 29.388x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 927.2 | 916.4 | 952.0 | 12.2 | 1.000x | 29.391x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.8 | 0.2 | 0.008x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 325.4 | 310.4 | 332.1 | 8.0 | 0.100x | 12.435x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,721.8 | 1,707.1 | 1,733.0 | 10.0 | 0.527x | 65.797x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,727.5 | 1,726.3 | 1,747.3 | 8.0 | 0.529x | 66.013x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,264.4 | 3,258.9 | 3,280.4 | 8.9 | 1.000x | 124.747x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.7 | 0.2 | 0.036x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 36.6 | 38.1 | 0.6 | 0.043x | 1.207x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 273.4 | 220.9 | 322.5 | 35.2 | 0.312x | 8.750x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.8 | 216.0 | 311.5 | 34.3 | 0.324x | 9.083x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 870.6 | 864.7 | 887.7 | 10.0 | 0.994x | 27.862x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 875.9 | 871.8 | 911.6 | 14.8 | 1.000x | 28.032x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.8 | 0.4 | 0.009x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.009x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 311.9 | 306.5 | 331.6 | 10.7 | 0.103x | 11.994x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,724.5 | 1,714.5 | 1,741.8 | 10.9 | 0.568x | 66.314x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,725.9 | 1,704.1 | 1,740.4 | 12.8 | 0.569x | 66.371x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,034.0 | 3,031.1 | 3,060.1 | 10.6 | 1.000x | 116.672x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.3 | 23.3 | 23.4 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.7 | 27.2 | 29.7 | 1.0 | 0.022x | 1.189x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.3 | 146.2 | 147.3 | 0.4 | 0.115x | 6.274x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.8 | 146.6 | 150.3 | 1.2 | 0.117x | 6.382x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,255.6 | 1,243.3 | 1,276.1 | 10.8 | 0.988x | 53.856x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,271.1 | 1,249.5 | 1,310.1 | 20.4 | 1.000x | 54.520x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.9 | 19.3 | 0.2 | 0.004x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.4 | 0.1 | 0.004x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 389.2 | 387.7 | 402.0 | 5.3 | 0.084x | 20.564x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 636.1 | 599.5 | 741.2 | 49.5 | 0.137x | 33.612x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 651.3 | 625.0 | 661.0 | 13.3 | 0.141x | 34.413x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,626.5 | 4,617.6 | 4,698.0 | 29.0 | 1.000x | 244.461x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.6 | 29.9 | 30.7 | 0.3 | 0.019x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.1 | 35.3 | 0.8 | 0.021x | 1.101x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 382.7 | 381.3 | 487.7 | 49.1 | 0.242x | 12.518x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 397.8 | 384.2 | 488.1 | 47.4 | 0.252x | 13.012x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,581.3 | 1,565.2 | 1,621.2 | 21.3 | 1.000x | 51.726x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,585.0 | 1,570.1 | 1,592.3 | 7.6 | 1.002x | 51.846x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.3 | 25.4 | 0.0 | 0.004x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.004x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 488.3 | 477.1 | 499.5 | 7.4 | 0.083x | 19.269x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,759.2 | 1,757.0 | 1,764.3 | 3.0 | 0.299x | 69.421x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,769.3 | 1,764.2 | 2,014.6 | 98.1 | 0.301x | 69.818x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,880.8 | 5,866.0 | 5,946.2 | 30.2 | 1.000x | 232.065x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 33.0 | 33.4 | 0.2 | 0.052x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.6 | 37.0 | 0.8 | 0.055x | 1.059x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.7 | 144.9 | 147.5 | 0.9 | 0.231x | 4.404x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 148.4 | 150.8 | 0.9 | 0.236x | 4.513x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 631.6 | 628.7 | 652.0 | 8.6 | 1.000x | 19.096x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.0 | 629.8 | 649.4 | 7.2 | 1.009x | 19.260x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.3 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 27.8 | 0.3 | 0.013x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 196.1 | 194.3 | 198.0 | 1.3 | 0.094x | 7.288x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,512.7 | 1,428.6 | 1,546.2 | 39.6 | 0.725x | 56.233x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,567.8 | 1,535.4 | 1,665.5 | 47.1 | 0.751x | 58.280x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,086.9 | 2,058.5 | 2,094.6 | 13.1 | 1.000x | 77.578x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.7 | 27.3 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.6 | 30.3 | 33.2 | 1.1 | 0.036x | 1.136x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 210.6 | 209.8 | 221.3 | 4.4 | 0.249x | 7.828x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 214.0 | 211.9 | 214.7 | 1.0 | 0.253x | 7.954x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 845.9 | 840.7 | 854.1 | 4.5 | 1.000x | 31.445x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 846.4 | 838.7 | 851.3 | 4.4 | 1.001x | 31.465x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.7 | 21.4 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.1 | 20.9 | 21.2 | 0.1 | 0.007x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 287.6 | 286.9 | 292.4 | 2.0 | 0.099x | 13.685x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,306.0 | 1,246.3 | 1,339.8 | 34.5 | 0.448x | 62.139x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,326.9 | 1,307.9 | 1,331.9 | 10.0 | 0.455x | 63.132x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,914.4 | 2,906.2 | 2,933.6 | 9.8 | 1.000x | 138.666x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.6 | 33.2 | 0.2 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 34.7 | 36.2 | 0.5 | 0.035x | 1.071x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460.4 | 435.3 | 488.3 | 18.6 | 0.457x | 14.013x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 481.3 | 454.3 | 498.7 | 14.2 | 0.477x | 14.649x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,008.2 | 999.5 | 1,033.3 | 13.2 | 1.000x | 30.688x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,009.0 | 999.4 | 1,016.2 | 6.5 | 1.001x | 30.711x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.3 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 27.3 | 0.1 | 0.008x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.5 | 568.6 | 571.0 | 0.9 | 0.159x | 21.252x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,870.5 | 2,835.7 | 2,893.0 | 19.9 | 0.803x | 107.115x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,876.1 | 2,855.0 | 2,988.6 | 57.0 | 0.804x | 107.323x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,575.8 | 3,556.8 | 3,576.7 | 7.7 | 1.000x | 133.432x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 66.3 | 66.2 | 67.1 | 0.3 | 0.175x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 66.6 | 66.5 | 66.8 | 0.1 | 0.175x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.1 | 102.7 | 105.3 | 1.0 | 0.274x | 1.570x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 104.2 | 109.1 | 1.8 | 0.278x | 1.594x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 378.4 | 374.3 | 383.2 | 3.3 | 0.996x | 5.708x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 379.8 | 378.1 | 380.1 | 0.7 | 1.000x | 5.730x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 59.1 | 58.9 | 59.2 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 62.7 | 0.2 | 0.040x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 213.3 | 210.0 | 215.3 | 2.1 | 0.137x | 3.607x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 299.1 | 298.8 | 299.7 | 0.3 | 0.193x | 5.059x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 299.2 | 296.1 | 299.5 | 1.4 | 0.193x | 5.061x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,552.3 | 1,548.0 | 1,556.8 | 3.3 | 1.000x | 26.254x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 29.7 | 30.7 | 0.3 | 0.906x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.7 | 34.6 | 0.7 | 1.000x | 1.103x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.2 | 32.7 | 35.6 | 1.3 | 1.000x | 1.104x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.8 | 33.7 | 35.3 | 0.6 | 1.050x | 1.159x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 254.6 | 252.9 | 261.6 | 3.1 | 7.672x | 8.469x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 256.9 | 255.5 | 270.1 | 5.6 | 7.742x | 8.546x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 23.9 | 0.1 | 0.666x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 23.9 | 0.1 | 0.671x | 1.006x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.5 | 34.0 | 48.4 | 5.5 | 1.000x | 1.501x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 44.4 | 46.0 | 0.7 | 1.256x | 1.885x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,774.8 | 1,640.9 | 1,831.3 | 67.0 | 49.955x | 74.960x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,785.1 | 1,780.5 | 1,857.7 | 29.1 | 50.245x | 75.395x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.4 | 25.5 | 28.5 | 1.0 | 0.169x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.2 | 31.7 | 0.9 | 0.181x | 1.074x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.3 | 48.2 | 0.3 | 0.297x | 1.757x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.7 | 48.9 | 49.9 | 0.4 | 0.307x | 1.817x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.1 | 160.4 | 165.3 | 1.7 | 1.000x | 5.924x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 163.0 | 160.9 | 165.0 | 1.4 | 1.005x | 5.956x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.8 | 18.8 | 0.0 | 0.104x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.3 | 19.3 | 0.4 | 0.105x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 56.6 | 0.7 | 0.303x | 2.917x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 180.6 | 178.4 | 184.3 | 2.3 | 1.000x | 9.624x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 963.0 | 918.1 | 1,003.8 | 29.0 | 5.331x | 51.306x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,019.2 | 905.3 | 1,054.6 | 55.8 | 5.642x | 54.302x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.6 | 18.6 | 20.4 | 0.7 | 0.032x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.1 | 20.1 | 22.3 | 0.8 | 0.033x | 1.026x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 97.9 | 73.8 | 99.6 | 12.2 | 0.161x | 4.988x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99.4 | 97.0 | 101.5 | 1.5 | 0.163x | 5.067x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 609.7 | 607.1 | 632.2 | 9.6 | 1.000x | 31.077x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.7 | 607.7 | 624.0 | 5.7 | 1.005x | 31.230x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 11.9 | 12.2 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.4 | 12.5 | 0.0 | 0.020x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.5 | 83.3 | 90.5 | 2.6 | 0.136x | 6.977x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 173.9 | 168.7 | 177.6 | 3.5 | 0.280x | 14.352x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 174.0 | 171.0 | 176.5 | 1.9 | 0.281x | 14.363x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.1 | 616.3 | 629.1 | 4.3 | 1.000x | 51.187x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.6 | 78.3 | 78.9 | 0.2 | 0.136x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 78.7 | 78.5 | 79.1 | 0.2 | 0.137x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 144.8 | 147.8 | 1.0 | 0.253x | 1.853x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 146.8 | 150.2 | 1.2 | 0.259x | 1.900x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 575.9 | 572.5 | 588.6 | 5.7 | 1.000x | 7.331x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 576.9 | 572.5 | 583.6 | 3.9 | 1.002x | 7.345x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 71.2 | 71.2 | 71.3 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.7 | 74.3 | 0.2 | 0.026x | 1.034x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290.5 | 285.7 | 292.4 | 2.3 | 0.104x | 4.078x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 718.6 | 689.5 | 735.1 | 18.5 | 0.257x | 10.086x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 731.5 | 680.5 | 742.5 | 27.1 | 0.262x | 10.267x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,796.0 | 2,786.2 | 2,802.3 | 5.3 | 1.000x | 39.243x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.9 | 48.3 | 0.1 | 0.299x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.7 | 48.6 | 50.1 | 0.5 | 0.309x | 1.032x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67.5 | 67.3 | 67.9 | 0.3 | 0.419x | 1.401x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 68.6 | 66.9 | 68.7 | 0.7 | 0.426x | 1.424x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 160.9 | 159.6 | 163.2 | 1.4 | 1.000x | 3.344x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 163.6 | 159.7 | 164.2 | 1.8 | 1.017x | 3.399x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 61.8 | 61.8 | 62.1 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 64.2 | 64.1 | 64.7 | 0.2 | 0.063x | 1.039x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.1 | 158.7 | 163.3 | 1.8 | 0.157x | 2.590x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 162.9 | 162.6 | 163.6 | 0.3 | 0.160x | 2.636x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 163.9 | 162.9 | 164.8 | 0.7 | 0.161x | 2.651x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,019.6 | 1,007.6 | 1,024.5 | 6.0 | 1.000x | 16.493x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.6 | 32.4 | 0.3 | 0.055x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 36.6 | 39.5 | 1.0 | 0.065x | 1.181x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.8 | 148.0 | 1.2 | 0.253x | 4.574x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.0 | 147.7 | 149.4 | 0.7 | 0.257x | 4.649x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 575.8 | 568.5 | 586.0 | 5.8 | 1.000x | 18.094x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 578.0 | 573.3 | 587.6 | 4.8 | 1.004x | 18.163x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.5 | 25.5 | 26.0 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 26.2 | 0.2 | 0.013x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 198.9 | 197.5 | 206.5 | 3.3 | 0.100x | 7.784x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,403.3 | 1,279.4 | 1,534.9 | 87.2 | 0.704x | 54.925x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,416.1 | 1,330.2 | 1,550.0 | 81.3 | 0.710x | 55.427x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,993.8 | 1,982.1 | 1,998.5 | 6.2 | 1.000x | 78.039x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 24.7 | 24.7 | 24.9 | 0.1 | 0.025x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.4 | 29.6 | 0.8 | 0.028x | 1.140x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 374.3 | 364.0 | 395.7 | 12.5 | 0.378x | 15.143x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 380.9 | 350.7 | 405.1 | 18.0 | 0.384x | 15.412x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 990.7 | 989.0 | 1,022.5 | 12.7 | 1.000x | 40.086x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.0 | 989.3 | 1,000.0 | 3.9 | 1.007x | 40.379x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 18.9 | 19.6 | 0.3 | 0.006x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.9 | 20.0 | 0.0 | 0.006x | 1.030x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 539.8 | 534.4 | 549.2 | 5.0 | 0.154x | 27.913x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,724.7 | 1,707.7 | 1,784.9 | 27.0 | 0.491x | 89.189x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,740.2 | 1,713.9 | 1,786.2 | 23.7 | 0.496x | 89.990x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,511.5 | 3,499.1 | 3,520.1 | 7.6 | 1.000x | 181.584x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.2 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.0 | 28.1 | 30.7 | 0.8 | 0.018x | 1.114x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.4 | 144.4 | 148.0 | 1.2 | 0.090x | 5.629x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 147.2 | 149.4 | 0.8 | 0.092x | 5.697x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,608.6 | 1,603.6 | 1,618.3 | 5.1 | 0.993x | 61.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,619.4 | 1,612.1 | 1,654.9 | 15.3 | 1.000x | 62.253x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.7 | 0.1 | 0.003x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 20.6 | 0.1 | 0.003x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 471.5 | 465.6 | 501.8 | 13.2 | 0.078x | 23.054x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 699.9 | 697.3 | 801.1 | 47.5 | 0.116x | 34.220x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 786.6 | 700.8 | 864.0 | 61.4 | 0.130x | 38.459x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,036.2 | 6,009.3 | 6,292.1 | 107.6 | 1.000x | 295.138x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.4 | 0.0 | 0.022x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.7 | 24.3 | 0.9 | 0.028x | 1.271x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 104.0 | 107.7 | 1.4 | 0.137x | 6.149x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 109.2 | 107.3 | 109.7 | 1.0 | 0.139x | 6.268x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.6 | 775.2 | 792.5 | 6.0 | 0.999x | 44.938x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.6 | 774.8 | 813.0 | 13.7 | 1.000x | 44.996x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.6 | 12.1 | 12.7 | 0.2 | 0.006x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 12.9 | 0.1 | 0.006x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 186.2 | 179.1 | 187.7 | 3.1 | 0.092x | 14.796x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 318.5 | 305.3 | 398.1 | 35.9 | 0.157x | 25.304x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 323.3 | 311.4 | 344.6 | 11.3 | 0.160x | 25.687x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,024.6 | 2,022.1 | 2,037.7 | 5.6 | 1.000x | 160.855x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.7 | 75.6 | 76.5 | 0.3 | 0.138x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.1 | 75.8 | 76.5 | 0.3 | 0.139x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.9 | 127.5 | 166.4 | 15.2 | 0.235x | 1.702x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 131.5 | 130.4 | 132.3 | 0.7 | 0.240x | 1.736x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 548.3 | 543.4 | 556.8 | 5.0 | 1.000x | 7.239x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 550.2 | 545.3 | 555.7 | 3.6 | 1.004x | 7.265x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.4 | 0.3 | 0.027x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.9 | 72.3 | 0.1 | 0.028x | 1.044x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.3 | 272.7 | 280.6 | 3.0 | 0.107x | 3.965x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 588.2 | 558.1 | 609.6 | 16.5 | 0.230x | 8.534x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 593.6 | 588.9 | 597.8 | 3.6 | 0.232x | 8.613x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,562.2 | 2,555.9 | 2,570.6 | 4.9 | 1.000x | 37.175x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.4 | 61.0 | 0.2 | 0.079x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 61.1 | 61.4 | 0.1 | 0.080x | 1.008x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.3 | 255.1 | 299.9 | 16.5 | 0.347x | 4.373x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 275.0 | 222.2 | 318.9 | 36.3 | 0.359x | 4.532x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 765.4 | 762.3 | 785.9 | 8.6 | 1.000x | 12.616x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 770.5 | 765.1 | 776.9 | 3.8 | 1.007x | 12.700x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 54.0 | 53.8 | 54.2 | 0.2 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 57.0 | 56.7 | 57.3 | 0.2 | 0.016x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 384.7 | 375.4 | 394.7 | 7.3 | 0.109x | 7.130x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,015.3 | 995.8 | 1,023.9 | 11.7 | 0.288x | 18.817x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,021.7 | 1,005.9 | 1,037.3 | 12.2 | 0.290x | 18.935x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,520.5 | 3,506.7 | 3,524.4 | 7.2 | 1.000x | 65.249x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.6 | 76.7 | 0.4 | 0.139x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.3 | 75.7 | 76.6 | 0.3 | 0.140x | 1.006x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.9 | 127.4 | 131.8 | 1.6 | 0.236x | 1.699x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.1 | 129.1 | 131.0 | 0.7 | 0.238x | 1.715x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 545.9 | 542.6 | 550.6 | 3.1 | 0.998x | 7.195x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.8 | 538.0 | 556.9 | 6.4 | 1.000x | 7.207x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.9 | 0.1 | 0.027x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.1 | 72.6 | 0.2 | 0.028x | 1.053x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 275.5 | 272.8 | 278.8 | 2.0 | 0.107x | 4.018x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 585.0 | 563.2 | 592.0 | 10.6 | 0.228x | 8.532x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 591.1 | 534.3 | 602.8 | 24.6 | 0.230x | 8.622x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,566.5 | 2,557.1 | 2,576.5 | 6.1 | 1.000x | 37.434x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 24.8 | 26.7 | 0.7 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 30.7 | 33.1 | 0.8 | 0.040x | 1.222x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 145.6 | 147.7 | 0.8 | 0.187x | 5.666x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.3 | 147.4 | 149.7 | 0.8 | 0.190x | 5.760x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 775.7 | 775.2 | 782.1 | 3.1 | 0.993x | 30.116x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.0 | 775.5 | 812.9 | 13.7 | 1.000x | 30.324x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.6 | 19.5 | 19.8 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 19.9 | 0.1 | 0.007x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.0 | 215.4 | 219.6 | 1.6 | 0.082x | 11.160x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 623.7 | 594.9 | 734.8 | 50.2 | 0.234x | 31.779x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 667.9 | 623.4 | 726.2 | 41.6 | 0.250x | 34.028x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,670.1 | 2,662.1 | 2,691.0 | 10.8 | 1.000x | 136.043x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 20.6 | 22.9 | 0.8 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.2 | 25.9 | 27.8 | 0.6 | 0.035x | 1.235x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.8 | 144.8 | 148.3 | 1.2 | 0.187x | 6.660x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 146.2 | 149.8 | 1.2 | 0.190x | 6.754x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 777.3 | 774.6 | 781.1 | 2.3 | 0.992x | 35.258x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.5 | 775.0 | 811.7 | 12.5 | 1.000x | 35.536x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.6 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.5 | 0.3 | 0.005x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.7 | 213.4 | 225.1 | 3.8 | 0.082x | 15.152x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 582.6 | 551.7 | 644.2 | 32.1 | 0.218x | 40.360x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 619.4 | 554.2 | 659.1 | 36.2 | 0.232x | 42.915x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.4 | 2,658.1 | 2,677.7 | 6.8 | 1.000x | 184.797x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 20.8 | 22.8 | 0.7 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.2 | 25.9 | 28.1 | 0.8 | 0.035x | 1.260x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.1 | 144.7 | 177.3 | 12.6 | 0.186x | 6.778x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 148.0 | 151.6 | 1.4 | 0.190x | 6.910x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.1 | 773.1 | 789.5 | 5.3 | 0.998x | 36.293x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.5 | 776.5 | 817.2 | 14.6 | 1.000x | 36.360x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.8 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.5 | 15.5 | 0.4 | 0.006x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.8 | 213.1 | 221.6 | 3.0 | 0.082x | 15.195x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 609.2 | 552.1 | 643.4 | 30.9 | 0.229x | 42.315x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 642.0 | 567.1 | 697.9 | 42.3 | 0.241x | 44.593x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.0 | 2,653.6 | 2,675.2 | 7.7 | 1.000x | 185.178x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 20.8 | 22.3 | 0.5 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.1 | 27.9 | 0.6 | 0.035x | 1.258x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 143.9 | 146.9 | 1.0 | 0.187x | 6.758x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.9 | 147.4 | 149.0 | 0.6 | 0.190x | 6.862x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.2 | 775.8 | 817.3 | 15.5 | 1.000x | 36.203x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.2 | 773.1 | 793.1 | 6.5 | 1.003x | 36.300x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.4 | 14.6 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 15.5 | 0.4 | 0.005x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.2 | 216.4 | 231.6 | 5.8 | 0.082x | 15.019x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 591.8 | 533.3 | 649.9 | 41.6 | 0.222x | 40.930x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 618.9 | 563.1 | 681.5 | 41.1 | 0.232x | 42.808x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.8 | 2,653.3 | 2,670.6 | 6.8 | 1.000x | 184.237x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.9 | 21.6 | 23.7 | 0.8 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.2 | 29.2 | 0.7 | 0.036x | 1.285x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.0 | 144.5 | 148.8 | 1.5 | 0.187x | 6.658x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.1 | 151.1 | 1.6 | 0.190x | 6.769x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.0 | 775.8 | 787.8 | 3.9 | 0.999x | 35.573x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.8 | 777.5 | 814.8 | 13.7 | 1.000x | 35.605x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.2 | 16.6 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.5 | 16.4 | 16.6 | 0.1 | 0.006x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.4 | 218.5 | 223.5 | 1.7 | 0.083x | 13.387x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 555.7 | 534.8 | 643.5 | 40.3 | 0.209x | 33.745x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 631.0 | 549.3 | 664.6 | 40.1 | 0.237x | 38.322x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,660.3 | 2,652.2 | 2,672.9 | 7.4 | 1.000x | 161.556x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,752.2 | 7,738.9 | 7,762.6 | 10.1 | 0.760x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,757.0 | 7,741.1 | 7,768.3 | 10.3 | 0.761x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,198.4 | 10,131.2 | 10,229.3 | 37.5 | 1.000x | 1.316x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,357.2 | 10,133.0 | 10,442.1 | 131.2 | 1.016x | 1.336x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37,071.8 | 37,062.4 | 37,121.6 | 24.4 | 3.635x | 4.782x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38,209.7 | 38,203.8 | 38,350.3 | 55.9 | 3.747x | 4.929x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,531.6 | 14,526.2 | 14,545.5 | 6.4 | 0.080x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,846.1 | 14,790.1 | 14,920.7 | 44.6 | 0.082x | 1.022x | 5 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,074.4 | 29,006.7 | 29,172.2 | 58.3 | 0.160x | 2.001x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 182,106.9 | 180,332.8 | 182,450.9 | 872.2 | 1.000x | 12.532x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,380.8 | 180,674.3 | 185,666.9 | 1,790.6 | 1.002x | 12.551x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18,577.8 | 18,570.0 | 18,581.5 | 4.4 | 0.064x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,159.4 | 19,122.0 | 19,220.4 | 31.8 | 0.066x | 1.031x | 5 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,046.7 | 71,915.3 | 72,336.1 | 167.5 | 0.248x | 3.878x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 289,956.2 | 289,006.9 | 291,314.7 | 783.1 | 1.000x | 15.608x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290,540.1 | 290,252.6 | 291,483.5 | 500.6 | 1.002x | 15.639x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18,163.6 | 18,161.6 | 18,267.8 | 40.7 | 0.021x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,334.7 | 19,298.0 | 19,364.8 | 27.3 | 0.023x | 1.064x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193,955.6 | 193,774.3 | 194,597.3 | 299.7 | 0.229x | 10.678x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,444.0 | 193,977.8 | 194,831.0 | 292.3 | 0.230x | 10.705x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 845,735.2 | 839,365.8 | 884,524.6 | 17,722.5 | 1.000x | 46.562x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 870,313.9 | 843,217.7 | 871,257.4 | 13,539.5 | 1.029x | 47.915x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,294.7 | 7,282.0 | 7,298.9 | 7.0 | 0.100x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,483.1 | 7,479.0 | 7,498.5 | 7.0 | 0.103x | 1.026x | 5 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,981.0 | 10,959.6 | 11,560.9 | 230.0 | 0.151x | 1.505x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,853.0 | 72,025.0 | 73,535.7 | 564.9 | 1.000x | 9.987x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73,181.4 | 72,669.6 | 73,637.2 | 394.0 | 1.005x | 10.032x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 309.0 | 284.1 | 318.7 | 12.5 | 0.351x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 318.8 | 273.6 | 320.4 | 20.2 | 0.362x | 1.032x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.4 | 868.2 | 908.2 | 16.3 | 1.000x | 2.850x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 896.7 | 879.7 | 910.7 | 11.5 | 1.019x | 2.902x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 934.9 | 933.8 | 936.6 | 1.1 | 1.062x | 3.026x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 979.1 | 977.8 | 982.6 | 1.6 | 1.112x | 3.169x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,871.4 | 13,869.8 | 13,881.5 | 4.4 | 0.066x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,419.3 | 14,388.7 | 14,570.3 | 66.7 | 0.068x | 1.040x | 5 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 95,399.0 | 93,778.8 | 101,828.2 | 3,184.7 | 0.451x | 6.877x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211,393.0 | 210,219.3 | 212,863.7 | 1,016.1 | 1.000x | 15.240x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,631.2 | 211,204.4 | 212,893.9 | 655.7 | 1.006x | 15.329x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,883.4 | 14,875.9 | 14,911.4 | 12.9 | 0.100x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 15,329.0 | 15,307.4 | 15,359.1 | 19.1 | 0.103x | 1.030x | 5 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,733.6 | 32,663.7 | 32,793.9 | 41.3 | 0.219x | 2.199x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,567.8 | 148,067.7 | 149,746.7 | 558.6 | 0.996x | 9.982x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 149,152.9 | 147,902.5 | 149,824.6 | 647.5 | 1.000x | 10.021x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.0 | 29.7 | 1.0 | 0.171x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 33.5 | 34.7 | 0.5 | 0.210x | 1.233x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.2 | 47.8 | 48.4 | 0.2 | 0.293x | 1.719x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.1 | 49.7 | 52.7 | 1.1 | 0.305x | 1.787x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.9 | 159.9 | 165.5 | 2.0 | 0.985x | 5.770x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 164.4 | 162.7 | 167.5 | 1.7 | 1.000x | 5.858x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.1 | 21.3 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.6 | 0.2 | 0.013x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.2 | 141.6 | 146.1 | 1.9 | 0.088x | 6.724x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,195.8 | 1,129.9 | 1,239.5 | 39.1 | 0.739x | 56.536x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,230.7 | 1,137.0 | 1,258.9 | 44.1 | 0.761x | 58.183x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,617.2 | 1,614.5 | 1,642.8 | 10.5 | 1.000x | 76.457x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73.0 | 72.6 | 73.1 | 0.2 | 0.069x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.0 | 89.0 | 89.3 | 0.1 | 0.084x | 1.220x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 198.6 | 205.7 | 2.5 | 0.188x | 2.739x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.4 | 200.3 | 207.3 | 2.6 | 0.189x | 2.759x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.6 | 1,060.7 | 1,075.7 | 5.9 | 1.000x | 14.573x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,068.3 | 1,064.7 | 1,081.6 | 5.9 | 1.004x | 14.637x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.4 | 0.2 | 0.062x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.4 | 171.6 | 179.0 | 3.0 | 0.162x | 2.753x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 203.4 | 203.1 | 203.6 | 0.2 | 0.191x | 3.247x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.1 | 203.9 | 206.2 | 0.8 | 0.192x | 3.275x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.7 | 1,065.3 | 1,074.3 | 3.7 | 1.000x | 17.033x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.7 | 70.0 | 0.5 | 0.069x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.7 | 85.5 | 86.7 | 0.4 | 0.085x | 1.235x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 174.3 | 173.7 | 176.5 | 0.9 | 0.173x | 2.510x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 177.3 | 176.9 | 178.4 | 0.5 | 0.176x | 2.553x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,008.3 | 996.8 | 1,016.0 | 6.7 | 1.000x | 14.523x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,010.2 | 998.7 | 1,013.2 | 5.8 | 1.002x | 14.551x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.5 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.2 | 63.0 | 0.3 | 0.062x | 1.076x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.7 | 160.2 | 161.8 | 0.6 | 0.159x | 2.756x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 169.0 | 168.1 | 169.3 | 0.4 | 0.167x | 2.897x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 174.2 | 173.4 | 174.8 | 0.5 | 0.172x | 2.986x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,009.9 | 993.9 | 1,021.0 | 9.9 | 1.000x | 17.313x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 30.2 | 0.3 | 0.043x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.2 | 46.4 | 0.1 | 0.067x | 1.562x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 78.1 | 77.4 | 80.2 | 1.2 | 0.113x | 2.633x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 87.8 | 87.7 | 88.6 | 0.3 | 0.127x | 2.963x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 685.8 | 684.8 | 687.7 | 1.2 | 0.989x | 23.129x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 693.7 | 681.1 | 701.5 | 7.1 | 1.000x | 23.397x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.1 | 23.0 | 23.1 | 0.0 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 26.8 | 0.5 | 0.037x | 1.113x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 82.8 | 82.6 | 84.6 | 0.8 | 0.120x | 3.590x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84.3 | 84.2 | 84.4 | 0.1 | 0.122x | 3.655x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 106.2 | 1.0 | 0.151x | 4.513x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 690.3 | 683.7 | 697.2 | 5.0 | 1.000x | 29.940x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.3 | 33.8 | 0.2 | 0.053x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.2 | 37.2 | 41.6 | 1.6 | 0.062x | 1.164x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.6 | 145.3 | 147.3 | 0.8 | 0.231x | 4.355x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.9 | 147.8 | 150.6 | 1.0 | 0.236x | 4.453x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 634.3 | 630.8 | 646.9 | 7.1 | 1.000x | 18.840x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 647.2 | 639.2 | 658.3 | 6.5 | 1.020x | 19.224x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 27.0 | 27.3 | 0.1 | 0.012x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.3 | 27.1 | 27.4 | 0.1 | 0.012x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.6 | 202.8 | 206.5 | 1.3 | 0.091x | 7.470x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,414.0 | 1,329.5 | 1,555.0 | 87.8 | 0.632x | 51.875x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,436.5 | 1,317.6 | 1,464.1 | 61.3 | 0.642x | 52.698x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,238.6 | 2,227.8 | 2,266.2 | 13.4 | 1.000x | 82.125x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 58.4 | 58.4 | 59.5 | 0.4 | 0.068x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.1 | 76.2 | 0.4 | 0.089x | 1.299x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 140.1 | 138.9 | 143.7 | 1.7 | 0.164x | 2.397x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 141.4 | 139.4 | 142.0 | 1.0 | 0.166x | 2.421x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 848.8 | 845.9 | 871.6 | 10.4 | 0.994x | 14.529x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 854.1 | 846.6 | 876.1 | 10.4 | 1.000x | 14.618x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 48.6 | 48.4 | 48.8 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 52.0 | 51.8 | 52.6 | 0.3 | 0.061x | 1.071x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 145.0 | 144.7 | 145.5 | 0.3 | 0.169x | 2.985x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.0 | 147.1 | 151.2 | 1.5 | 0.173x | 3.046x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 149.3 | 148.8 | 149.6 | 0.3 | 0.174x | 3.074x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 857.6 | 851.8 | 866.0 | 4.9 | 1.000x | 17.654x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 120.5 | 120.0 | 121.2 | 0.5 | 0.136x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.7 | 135.9 | 137.0 | 0.4 | 0.155x | 1.135x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 154.9 | 154.5 | 155.4 | 0.3 | 0.175x | 1.286x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 156.3 | 155.6 | 157.5 | 0.6 | 0.177x | 1.298x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 872.4 | 868.3 | 891.8 | 8.5 | 0.988x | 7.243x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.9 | 878.2 | 884.9 | 2.4 | 1.000x | 7.330x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 110.0 | 109.6 | 121.0 | 4.5 | 0.125x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 113.6 | 112.9 | 114.3 | 0.5 | 0.129x | 1.033x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 160.4 | 160.1 | 161.2 | 0.4 | 0.182x | 1.459x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 164.4 | 164.2 | 165.8 | 0.6 | 0.186x | 1.495x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.8 | 163.8 | 168.3 | 1.5 | 0.188x | 1.508x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.7 | 876.9 | 887.4 | 4.6 | 1.000x | 8.018x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.8 | 97.2 | 0.1 | 0.043x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 99.6 | 98.2 | 100.1 | 0.6 | 0.044x | 1.027x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 738.1 | 727.7 | 742.2 | 4.9 | 0.326x | 7.614x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,074.1 | 1,048.1 | 1,100.2 | 17.7 | 0.475x | 11.081x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,263.5 | 2,228.4 | 2,276.8 | 17.5 | 1.000x | 23.351x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,273.8 | 2,227.2 | 2,287.9 | 21.4 | 1.005x | 23.457x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.2 | 89.5 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 93.2 | 93.1 | 93.5 | 0.2 | 0.030x | 1.043x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 408.5 | 401.6 | 411.5 | 3.6 | 0.131x | 4.571x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 916.9 | 908.2 | 922.4 | 4.7 | 0.295x | 10.261x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,246.0 | 1,237.9 | 1,293.7 | 20.7 | 0.401x | 13.944x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,108.0 | 3,101.9 | 3,163.7 | 26.4 | 1.000x | 34.781x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.1 | 24.7 | 25.9 | 0.4 | 0.032x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.9 | 28.0 | 30.1 | 0.8 | 0.037x | 1.150x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.2 | 143.9 | 147.7 | 1.3 | 0.187x | 5.817x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.7 | 148.2 | 150.9 | 1.0 | 0.190x | 5.916x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.3 | 781.0 | 802.0 | 7.8 | 1.000x | 31.172x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 787.2 | 781.7 | 806.5 | 10.6 | 1.005x | 31.326x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.4 | 20.6 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.0 | 0.2 | 0.008x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.5 | 218.9 | 244.7 | 9.8 | 0.082x | 10.791x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 823.3 | 779.1 | 885.7 | 39.9 | 0.308x | 40.289x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 860.0 | 716.7 | 894.7 | 62.4 | 0.322x | 42.085x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,673.4 | 2,659.4 | 2,688.6 | 9.5 | 1.000x | 130.819x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.9 | 31.7 | 32.5 | 0.3 | 0.041x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 36.8 | 41.3 | 1.8 | 0.048x | 1.169x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 188.9 | 178.3 | 191.8 | 4.8 | 0.241x | 5.913x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.5 | 178.2 | 196.2 | 6.5 | 0.247x | 6.060x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.0 | 779.2 | 792.1 | 4.6 | 1.000x | 24.580x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 786.0 | 783.9 | 802.6 | 8.1 | 1.001x | 24.610x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.6 | 26.6 | 26.9 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 26.9 | 0.1 | 0.010x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 232.7 | 229.3 | 237.7 | 3.3 | 0.087x | 8.738x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,105.9 | 1,090.1 | 1,193.9 | 40.8 | 0.414x | 41.522x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,124.1 | 1,108.4 | 1,211.3 | 42.3 | 0.421x | 42.207x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.5 | 2,661.7 | 2,712.8 | 18.6 | 1.000x | 100.231x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.8 | 70.3 | 0.5 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.4 | 85.8 | 0.2 | 0.083x | 1.231x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.2 | 175.8 | 1.0 | 0.168x | 2.497x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 176.1 | 175.8 | 188.2 | 4.8 | 0.170x | 2.537x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,034.5 | 1,029.1 | 1,054.2 | 8.8 | 1.000x | 14.902x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,054.5 | 1,025.7 | 1,063.3 | 13.3 | 1.019x | 15.190x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.6 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.7 | 0.2 | 0.060x | 1.067x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.2 | 106.3 | 112.5 | 2.3 | 0.103x | 1.837x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 175.5 | 175.4 | 177.3 | 0.7 | 0.169x | 3.007x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 176.1 | 176.0 | 176.7 | 0.3 | 0.170x | 3.017x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,038.0 | 1,025.9 | 1,073.2 | 16.0 | 1.000x | 17.783x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.9 | 70.4 | 0.5 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.0 | 85.8 | 0.3 | 0.083x | 1.237x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.3 | 173.1 | 175.6 | 0.9 | 0.168x | 2.509x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 176.4 | 175.6 | 189.2 | 5.3 | 0.171x | 2.555x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,033.7 | 1,028.4 | 1,049.6 | 8.0 | 1.000x | 14.967x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,050.7 | 1,025.4 | 1,058.6 | 12.0 | 1.017x | 15.215x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.5 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.2 | 62.9 | 0.2 | 0.061x | 1.069x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.4 | 112.2 | 2.2 | 0.104x | 1.833x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 175.5 | 175.4 | 176.9 | 0.6 | 0.170x | 3.003x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 176.0 | 176.6 | 0.2 | 0.171x | 3.016x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.0 | 1,023.7 | 1,050.0 | 8.7 | 1.000x | 17.658x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.8 | 70.2 | 0.5 | 0.061x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.6 | 85.3 | 87.1 | 0.8 | 0.075x | 1.238x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.5 | 165.2 | 177.5 | 4.7 | 0.146x | 2.394x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.1 | 169.3 | 172.7 | 1.3 | 0.151x | 2.476x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.7 | 1,130.3 | 1,168.8 | 14.3 | 1.000x | 16.416x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,151.7 | 1,131.5 | 1,177.1 | 16.4 | 1.015x | 16.662x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 59.3 | 0.3 | 0.051x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 62.5 | 0.2 | 0.055x | 1.067x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.3 | 107.6 | 111.2 | 1.5 | 0.097x | 1.887x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.9 | 170.7 | 171.2 | 0.1 | 0.150x | 2.923x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 172.0 | 171.9 | 172.5 | 0.3 | 0.151x | 2.942x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,135.6 | 1,126.4 | 1,153.6 | 10.4 | 1.000x | 19.426x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 69.0 | 70.3 | 0.5 | 0.064x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.3 | 87.9 | 1.0 | 0.079x | 1.233x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.9 | 159.7 | 173.8 | 5.5 | 0.148x | 2.310x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.3 | 160.0 | 164.7 | 1.8 | 0.148x | 2.315x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,081.0 | 1,078.2 | 1,136.1 | 22.0 | 0.997x | 15.610x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,084.1 | 1,077.4 | 1,102.9 | 8.7 | 1.000x | 15.655x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.4 | 58.7 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 62.7 | 0.2 | 0.058x | 1.065x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.5 | 107.0 | 113.6 | 2.4 | 0.102x | 1.870x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 161.3 | 161.3 | 161.8 | 0.2 | 0.150x | 2.755x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 162.9 | 162.7 | 163.2 | 0.2 | 0.152x | 2.783x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.2 | 1,069.4 | 1,090.1 | 7.5 | 1.000x | 18.329x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 76.2 | 2.7 | 0.064x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 86.8 | 85.4 | 87.8 | 0.9 | 0.080x | 1.250x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.8 | 159.8 | 173.6 | 5.5 | 0.148x | 2.302x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.4 | 159.7 | 164.6 | 1.8 | 0.148x | 2.310x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.7 | 1,072.7 | 1,102.4 | 10.0 | 1.000x | 15.596x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,086.0 | 1,070.9 | 1,109.9 | 13.6 | 1.003x | 15.644x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.9 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.1 | 62.9 | 0.3 | 0.058x | 1.069x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.9 | 106.8 | 113.0 | 2.4 | 0.100x | 1.830x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 161.4 | 161.2 | 161.8 | 0.2 | 0.150x | 2.763x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 162.8 | 162.8 | 163.3 | 0.2 | 0.152x | 2.787x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.5 | 1,065.5 | 1,084.2 | 6.8 | 1.000x | 18.361x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.2 | 48.5 | 6.8 | 0.034x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.1 | 36.6 | 37.8 | 0.5 | 0.040x | 1.176x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 289.3 | 267.5 | 319.4 | 22.2 | 0.314x | 9.172x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 290.4 | 270.8 | 320.0 | 16.9 | 0.316x | 9.208x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 920.2 | 901.9 | 935.2 | 11.4 | 1.000x | 29.178x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 923.4 | 907.2 | 969.1 | 21.5 | 1.003x | 29.279x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.3 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.2 | 26.5 | 0.1 | 0.008x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 314.1 | 305.7 | 332.3 | 11.3 | 0.098x | 12.062x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,734.0 | 1,721.5 | 1,775.4 | 19.1 | 0.544x | 66.588x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,740.2 | 1,711.1 | 1,776.5 | 21.4 | 0.546x | 66.823x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,189.3 | 3,140.0 | 3,201.6 | 26.4 | 1.000x | 122.470x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.9 | 14.9 | 1.9 | 0.327x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.5 | 12.0 | 0.2 | 0.383x | 1.173x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.6 | 0.1 | 1.000x | 3.060x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.0 | 0.7 | 1.000x | 3.060x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.6 | 63.9 | 6.7 | 1.549x | 4.739x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.6 | 48.2 | 49.7 | 0.5 | 1.604x | 4.908x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.4 | 0.0 | 0.163x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 6.0 | 0.2 | 0.171x | 1.048x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.1 | 30.5 | 52.3 | 8.2 | 1.000x | 6.145x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.6 | 40.4 | 46.2 | 2.1 | 1.318x | 8.098x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.2 | 48.3 | 78.7 | 11.8 | 1.487x | 9.138x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.9 | 49.6 | 50.5 | 0.3 | 1.509x | 9.273x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.4 | 16.6 | 1.6 | 0.419x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.4 | 13.9 | 15.5 | 0.6 | 0.476x | 1.136x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.6 | 0.1 | 1.000x | 2.386x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.7 | 30.3 | 30.8 | 0.2 | 1.012x | 2.414x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.6 | 47.4 | 50.6 | 1.2 | 1.570x | 3.746x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.8 | 48.6 | 50.8 | 0.8 | 1.611x | 3.843x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.5 | 0.2 | 0.177x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 7.4 | 0.6 | 0.178x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.3 | 30.4 | 43.8 | 4.9 | 1.000x | 5.637x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.3 | 40.3 | 46.6 | 2.1 | 1.300x | 7.327x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 66.7 | 66.4 | 69.1 | 1.0 | 2.001x | 11.281x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 68.4 | 67.2 | 69.3 | 0.7 | 2.052x | 11.564x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.0 | 33.2 | 34.5 | 0.5 | 0.970x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.1 | 33.9 | 38.5 | 1.7 | 1.000x | 1.031x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 81.3 | 80.9 | 107.3 | 10.4 | 2.319x | 2.391x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.0 | 99.5 | 107.5 | 3.3 | 3.053x | 3.146x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 110.0 | 108.6 | 111.7 | 1.1 | 3.138x | 3.234x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 113.6 | 111.7 | 114.1 | 1.0 | 3.241x | 3.341x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.1 | 34.7 | 48.6 | 5.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 46.4 | 48.3 | 0.7 | 1.293x | 1.293x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.6 | 72.4 | 72.8 | 0.1 | 2.012x | 2.012x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 73.4 | 73.3 | 73.8 | 0.2 | 2.034x | 2.034x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,858.4 | 2,844.9 | 2,876.9 | 11.9 | 79.236x | 79.236x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,932.2 | 2,884.2 | 3,166.3 | 104.0 | 81.281x | 81.281x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 22.9 | 0.5 | 0.657x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 26.0 | 0.1 | 0.778x | 1.184x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.2 | 33.0 | 35.6 | 1.0 | 1.000x | 1.523x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 34.0 | 35.6 | 0.6 | 1.045x | 1.591x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 164.2 | 162.6 | 166.5 | 1.5 | 4.946x | 7.532x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.7 | 161.9 | 167.6 | 1.9 | 4.991x | 7.601x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 16.6 | 0.1 | 0.457x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.2 | 17.1 | 0.3 | 0.462x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.7 | 33.9 | 48.2 | 5.3 | 1.000x | 2.188x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 50.4 | 2.4 | 1.245x | 2.723x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 776.6 | 768.6 | 824.2 | 23.0 | 21.761x | 47.612x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 807.4 | 783.4 | 826.5 | 16.2 | 22.624x | 49.500x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,578,231.1 | 3,576,317.9 | 3,602,224.3 | 11,669.5 | 0.069x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,591,987.4 | 3,590,797.4 | 3,601,594.9 | 4,116.6 | 0.070x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,025,693.0 | 6,998,003.0 | 7,047,193.0 | 18,029.9 | 0.136x | 1.963x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 11,005,527.0 | 10,855,866.0 | 11,201,808.0 | 126,814.2 | 0.213x | 3.076x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 11,133,526.0 | 10,950,764.0 | 13,188,808.0 | 986,462.8 | 0.216x | 3.111x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,651,471.6 | 51,519,156.4 | 52,163,729.0 | 226,578.8 | 1.000x | 14.435x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,035.0 | 18,870.4 | 19,710.6 | 297.7 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,877,191.1 | 1,876,531.7 | 1,886,882.3 | 3,884.7 | 98.618x | 98.618x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,890,786.8 | 1,887,656.8 | 1,902,865.6 | 5,443.4 | 99.332x | 99.332x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,647,411.7 | 17,584,318.0 | 17,687,825.3 | 37,942.0 | 927.103x | 927.103x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84,475,069.0 | 83,381,293.0 | 137,755,930.0 | 21,408,303.4 | 4437.881x | 4437.881x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 85,541,423.0 | 85,288,921.0 | 87,301,653.0 | 877,599.0 | 4493.902x | 4493.902x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,766.5 | 18,660.6 | 18,864.7 | 73.4 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,875,979.8 | 1,874,635.4 | 1,880,736.7 | 2,227.7 | 99.964x | 99.964x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,876,102.3 | 1,873,857.9 | 1,887,917.3 | 5,159.3 | 99.971x | 99.971x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,143,556.6 | 3,128,195.2 | 3,210,853.9 | 29,187.7 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,194,847.5 | 3,173,328.7 | 3,326,101.4 | 55,577.2 | 0.007x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42,822,086.3 | 42,753,365.7 | 43,435,853.3 | 265,893.8 | 0.095x | 13.622x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 107,359,111.0 | 102,345,462.0 | 138,607,445.0 | 13,043,775.8 | 0.239x | 34.152x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 118,280,183.0 | 115,794,518.0 | 165,329,947.0 | 19,225,323.5 | 0.263x | 37.626x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449,517,489.8 | 447,282,051.8 | 452,307,713.2 | 1,601,996.4 | 1.000x | 142.996x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,000.4 | 18,794.0 | 19,040.4 | 102.2 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,098,348.9 | 3,071,619.9 | 3,136,325.3 | 23,587.5 | 163.068x | 163.068x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,146,368.5 | 3,120,215.9 | 3,174,738.1 | 21,273.0 | 165.595x | 165.595x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,683,252.7 | 22,570,459.7 | 22,944,807.3 | 158,154.6 | 1193.831x | 1193.831x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103,654,980.0 | 97,605,454.0 | 128,461,846.0 | 11,381,593.6 | 5455.415x | 5455.415x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 110,435,166.0 | 100,536,856.0 | 173,919,428.0 | 26,454,553.1 | 5812.260x | 5812.260x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.4 | 0.3 | 0.755x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.7 | 22.3 | 0.2 | 0.766x | 2.965x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.3 | 0.2 | 0.999x | 3.870x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.000x | 3.873x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 19.1 | 0.2 | 0.185x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 19.0 | 0.2 | 0.185x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 27.0 | 30.4 | 1.5 | 0.272x | 1.469x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 32.7 | 2.0 | 0.276x | 1.491x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.8 | 44.7 | 0.3 | 0.439x | 2.375x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 100.0 | 101.9 | 0.7 | 1.000x | 5.408x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.1 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.8 | 0.1 | 0.755x | 2.939x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.995x | 3.873x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.000x | 3.891x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.182x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 30.1 | 30.4 | 0.1 | 0.300x | 1.655x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 30.4 | 29.4 | 32.4 | 1.3 | 0.303x | 1.673x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.2 | 0.2 | 0.439x | 2.420x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 99.8 | 102.2 | 0.9 | 1.000x | 5.516x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.746x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.746x | 2.923x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 28.9 | 0.1 | 0.998x | 3.907x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.3 | 0.3 | 1.000x | 3.917x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 21.6 | 1.8 | 0.176x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 19.0 | 0.4 | 0.179x | 1.019x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.7 | 0.6 | 0.180x | 1.024x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.181x | 1.028x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.2 | 0.433x | 2.462x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 100.1 | 104.9 | 1.7 | 1.000x | 5.680x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 2.925x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 3.886x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.001x | 3.889x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.184x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.8 | 0.2 | 0.185x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.2 | 0.2 | 0.444x | 2.409x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 59.1 | 1.8 | 0.555x | 3.009x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 55.4 | 54.1 | 57.7 | 1.6 | 0.562x | 3.049x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.6 | 96.8 | 100.7 | 1.2 | 1.000x | 5.423x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.4 | 23.4 | 23.9 | 0.2 | 0.812x | 3.167x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.4 | 24.3 | 0.3 | 0.819x | 3.194x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.996x | 3.884x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 3.900x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.4 | 18.2 | 18.8 | 0.2 | 0.183x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.6 | 45.0 | 0.2 | 0.443x | 2.449x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 81.8 | 81.5 | 85.1 | 1.7 | 0.811x | 4.486x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 82.2 | 82.1 | 82.3 | 0.1 | 0.815x | 4.506x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 98.2 | 102.2 | 1.3 | 1.000x | 5.529x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 2.924x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.749x | 2.929x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.1 | 0.2 | 0.994x | 3.884x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.909x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 21.6 | 1.9 | 0.177x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.022x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.023x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.182x | 1.030x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.8 | 44.3 | 0.2 | 0.437x | 2.465x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.4 | 102.2 | 1.6 | 1.000x | 5.647x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.7 | 0.0 | 0.755x | 2.930x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 3.882x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.002x | 3.890x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 21.6 | 1.9 | 0.176x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.026x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.181x | 1.027x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.9 | 0.2 | 0.182x | 1.032x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.8 | 48.4 | 1.7 | 0.438x | 2.489x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 97.1 | 102.4 | 1.8 | 1.000x | 5.686x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.921x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 0.999x | 3.882x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.000x | 3.886x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.9 | 44.6 | 0.3 | 0.441x | 2.437x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 54.3 | 54.1 | 57.7 | 1.7 | 0.540x | 2.987x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 56.4 | 0.7 | 0.545x | 3.012x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.1 | 102.5 | 1.8 | 1.000x | 5.531x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.753x | 2.923x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.9 | 0.5 | 1.000x | 3.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.002x | 3.894x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 22.9 | 1.9 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.8 | 30.8 | 1.6 | 0.270x | 1.493x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.6 | 0.1 | 0.273x | 1.509x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 44.1 | 44.6 | 0.2 | 0.440x | 2.427x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.2 | 123.9 | 9.8 | 1.000x | 5.521x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.245x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.745x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.746x | 2.927x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.993x | 3.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.4 | 0.3 | 1.000x | 3.922x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.181x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 29.6 | 1.2 | 0.269x | 1.490x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.2 | 29.9 | 1.0 | 0.272x | 1.508x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.3 | 0.5 | 0.440x | 2.442x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.8 | 97.2 | 102.5 | 1.8 | 1.000x | 5.546x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.748x | 2.925x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.926x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 0.995x | 3.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.2 | 0.2 | 1.000x | 3.913x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.0 | 1.4 | 0.270x | 1.489x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.2 | 27.5 | 0.1 | 0.273x | 1.508x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 45.0 | 0.5 | 0.441x | 2.433x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 97.2 | 102.6 | 1.7 | 1.000x | 5.517x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.751x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.752x | 2.924x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 3.890x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.001x | 3.896x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.181x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 48.5 | 1.7 | 0.444x | 2.453x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 55.1 | 1.8 | 0.513x | 2.833x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.0 | 52.0 | 52.2 | 0.1 | 0.518x | 2.858x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.5 | 102.9 | 1.8 | 1.000x | 5.520x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.319x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.751x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 2.922x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.000x | 3.892x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.001x | 3.897x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.1 | 32.0 | 35.7 | 1.7 | 0.318x | 1.765x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 33.1 | 32.8 | 33.2 | 0.1 | 0.328x | 1.817x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 50.6 | 2.8 | 0.439x | 2.436x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.9 | 97.0 | 102.3 | 1.8 | 1.000x | 5.547x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.750x | 2.921x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.000x | 3.896x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.2 | 1.003x | 3.906x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.1 | 32.0 | 35.5 | 1.7 | 0.319x | 1.762x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 32.9 | 32.8 | 33.3 | 0.2 | 0.327x | 1.809x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 48.4 | 1.7 | 0.439x | 2.430x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 97.2 | 102.8 | 1.8 | 1.000x | 5.530x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.3 | 9.2 | 10.0 | 0.3 | 0.323x | 1.253x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.753x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 2.925x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 3.883x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.004x | 3.898x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.3 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 20.7 | 20.7 | 24.5 | 1.9 | 0.206x | 1.138x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 21.0 | 21.0 | 21.0 | 0.0 | 0.209x | 1.154x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.6 | 44.7 | 0.4 | 0.441x | 2.432x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.4 | 101.8 | 1.1 | 1.000x | 5.512x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.8 | 0.2 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.920x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.5 | 0.4 | 1.000x | 3.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.001x | 3.887x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.1 | 1.2 | 0.295x | 1.619x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 30.1 | 34.4 | 1.7 | 0.301x | 1.654x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 44.8 | 0.4 | 0.446x | 2.452x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.3 | 101.9 | 1.5 | 1.000x | 5.495x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.317x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.748x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.995x | 3.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.5 | 0.3 | 1.000x | 3.912x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.1 | 1.3 | 0.294x | 1.617x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.1 | 0.1 | 0.300x | 1.649x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.0 | 0.4 | 0.443x | 2.435x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.8 | 101.9 | 1.4 | 1.000x | 5.492x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.3 | 9.2 | 10.3 | 0.4 | 0.321x | 1.255x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.918x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 2.920x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 0.997x | 3.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.1 | 0.2 | 1.000x | 3.903x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.0 | 32.0 | 35.7 | 1.7 | 0.321x | 1.764x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 33.1 | 0.2 | 0.331x | 1.817x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.4 | 0.7 | 0.445x | 2.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.1 | 102.1 | 1.3 | 1.000x | 5.491x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.2 | 0.4 | 0.317x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 2.921x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.996x | 3.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.4 | 0.3 | 1.000x | 3.911x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.183x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.6 | 29.3 | 32.0 | 1.2 | 0.297x | 1.632x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 29.9 | 30.1 | 0.1 | 0.302x | 1.657x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 44.7 | 0.4 | 0.444x | 2.440x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.8 | 102.0 | 1.4 | 1.000x | 5.492x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.3 | 0.4 | 0.318x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.921x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.2 | 1.000x | 3.899x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.1 | 0.5 | 1.000x | 3.900x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.4 | 32.0 | 35.6 | 1.6 | 0.324x | 1.779x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 32.9 | 32.7 | 33.1 | 0.2 | 0.330x | 1.811x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.0 | 52.3 | 3.2 | 0.445x | 2.439x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.3 | 102.1 | 1.5 | 1.000x | 5.485x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.748x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.748x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.995x | 3.886x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.1 | 0.1 | 1.000x | 3.905x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 19.3 | 0.4 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.3 | 0.443x | 2.442x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.1 | 48.5 | 51.2 | 1.0 | 0.489x | 2.697x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.2 | 48.5 | 54.4 | 2.2 | 0.491x | 2.707x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 97.4 | 101.7 | 1.4 | 1.000x | 5.511x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.996x | 3.886x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 3.901x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.8 | 1.4 | 0.270x | 1.486x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.5 | 28.5 | 0.4 | 0.276x | 1.514x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 44.8 | 0.4 | 0.445x | 2.446x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.6 | 101.8 | 1.4 | 1.000x | 5.492x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 2.925x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.000x | 3.902x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.0 | 0.1 | 1.004x | 3.919x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.1 | 0.4 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.6 | 1.3 | 0.270x | 1.486x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 27.8 | 0.1 | 0.276x | 1.516x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 44.5 | 0.3 | 0.442x | 2.431x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.2 | 101.8 | 1.2 | 1.000x | 5.496x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.744x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 27.4 | 2.3 | 0.748x | 2.934x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.992x | 3.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 29.1 | 0.2 | 1.000x | 3.922x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.1 | 1.0 | 0.270x | 1.483x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.4 | 27.9 | 0.2 | 0.277x | 1.520x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.2 | 44.8 | 0.2 | 0.444x | 2.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 99.3 | 102.0 | 1.0 | 1.000x | 5.494x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.750x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 2.924x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 3.895x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.001x | 3.898x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.0 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.8 | 1.3 | 0.270x | 1.484x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 32.4 | 2.0 | 0.276x | 1.517x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 44.7 | 0.3 | 0.442x | 2.430x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 98.4 | 101.8 | 1.2 | 1.000x | 5.500x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.754x | 2.929x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.8 | 0.4 | 1.000x | 3.883x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.1 | 1.006x | 3.905x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.182x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.7 | 29.7 | 1.3 | 0.271x | 1.496x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.274x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.3 | 0.6 | 0.443x | 2.444x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 98.6 | 101.7 | 1.0 | 1.000x | 5.515x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.752x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.8 | 0.1 | 0.758x | 2.944x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 3.885x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.8 | 0.0 | 1.005x | 3.903x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.9 | 1.8 | 0.269x | 1.484x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.275x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.4 | 0.6 | 0.444x | 2.446x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.6 | 101.8 | 1.4 | 1.000x | 5.507x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.9 | 0.1 | 0.752x | 2.936x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 0.996x | 3.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 3.903x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.1 | 1.5 | 0.271x | 1.484x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 30.8 | 1.3 | 0.276x | 1.516x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 50.8 | 2.7 | 0.446x | 2.446x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.8 | 102.0 | 1.1 | 1.000x | 5.486x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.317x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.747x | 2.926x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.927x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 0.995x | 3.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.6 | 0.4 | 1.000x | 3.915x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 21.2 | 1.2 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.6 | 1.6 | 0.269x | 1.481x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.4 | 27.6 | 0.1 | 0.274x | 1.508x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.8 | 50.3 | 2.4 | 0.449x | 2.472x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.4 | 102.1 | 1.5 | 1.000x | 5.502x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.254x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.744x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.744x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 0.990x | 3.892x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.6 | 30.7 | 0.7 | 1.000x | 3.932x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 22.2 | 1.6 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 31.0 | 1.8 | 0.270x | 1.488x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.6 | 0.1 | 0.275x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 50.3 | 2.5 | 0.445x | 2.447x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.1 | 101.9 | 1.3 | 1.000x | 5.502x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.747x | 2.921x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.8 | 0.1 | 0.995x | 3.893x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 3.913x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.183x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.0 | 1.5 | 0.270x | 1.486x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.277x | 1.519x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 44.8 | 0.4 | 0.442x | 2.431x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.9 | 102.0 | 1.3 | 1.000x | 5.493x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 12.6 | 1.4 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.750x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.998x | 3.888x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 3.896x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.183x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.8 | 30.8 | 1.6 | 0.272x | 1.491x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.6 | 0.0 | 0.276x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 44.8 | 0.4 | 0.447x | 2.449x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 98.7 | 102.2 | 1.2 | 1.000x | 5.481x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 2.923x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 3.892x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.000x | 3.893x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.6 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 31.0 | 1.7 | 0.272x | 1.494x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 27.7 | 0.1 | 0.276x | 1.516x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.0 | 0.5 | 0.444x | 2.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 96.9 | 102.1 | 1.8 | 1.000x | 5.499x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 2.924x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.6 | 0.4 | 1.000x | 3.887x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.000x | 3.887x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 31.1 | 1.6 | 0.272x | 1.491x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.7 | 29.9 | 0.9 | 0.278x | 1.525x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 44.9 | 0.4 | 0.444x | 2.439x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.7 | 102.1 | 1.4 | 1.000x | 5.492x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.753x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 2.927x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.2 | 1.000x | 3.881x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 28.9 | 0.2 | 1.006x | 3.903x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.7 | 1.6 | 0.269x | 1.488x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.2 | 27.7 | 0.2 | 0.274x | 1.516x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.8 | 45.1 | 0.5 | 0.442x | 2.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.6 | 102.0 | 1.4 | 1.000x | 5.525x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.749x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.993x | 3.880x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 1.000x | 3.905x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.8 | 1.4 | 0.269x | 1.483x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.4 | 27.6 | 0.1 | 0.274x | 1.509x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.4 | 0.6 | 0.442x | 2.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 98.0 | 102.0 | 1.4 | 1.000x | 5.512x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.245x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.2 | 0.748x | 2.918x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.996x | 3.886x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.000x | 3.903x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.8 | 1.3 | 0.269x | 1.485x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.8 | 27.4 | 29.4 | 0.7 | 0.278x | 1.531x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.6 | 0.7 | 0.442x | 2.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 97.2 | 102.4 | 1.7 | 1.000x | 5.513x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.745x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.746x | 2.921x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.993x | 3.890x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 29.3 | 0.2 | 1.000x | 3.916x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 30.2 | 1.5 | 0.268x | 1.483x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.6 | 0.1 | 0.272x | 1.509x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 45.0 | 0.5 | 0.440x | 2.434x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 97.1 | 101.8 | 1.7 | 1.000x | 5.537x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.239x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.746x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 2.920x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.994x | 3.889x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.3 | 0.2 | 1.000x | 3.914x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 29.4 | 1.2 | 0.268x | 1.481x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.274x | 1.519x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 44.8 | 0.5 | 0.439x | 2.433x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 97.9 | 103.2 | 1.8 | 1.000x | 5.537x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 0.998x | 3.892x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.7 | 0.8 | 1.000x | 3.900x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.3 | 1.4 | 0.294x | 1.621x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.2 | 30.0 | 31.3 | 0.5 | 0.301x | 1.661x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.6 | 44.6 | 0.4 | 0.444x | 2.448x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 99.3 | 102.4 | 1.2 | 1.000x | 5.520x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.8 | 0.0 | 0.581x | 2.273x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.0 | 0.583x | 2.280x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.993x | 3.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.5 | 0.3 | 1.000x | 3.913x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 8.9 | 0.0 | 0.273x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 8.9 | 0.0 | 0.273x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 32.7 | 0.1 | 1.000x | 3.669x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.0 | 35.6 | 44.9 | 3.4 | 1.167x | 4.282x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 59.2 | 58.9 | 60.3 | 0.6 | 1.821x | 6.683x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.1 | 59.4 | 64.4 | 2.0 | 1.970x | 7.229x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.3 | 8.3 | 8.4 | 0.0 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.104x | 1.103x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.246x | 2.599x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.246x | 2.601x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 87.9 | 86.9 | 88.5 | 0.6 | 1.000x | 10.580x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.2 | 86.7 | 88.4 | 0.6 | 1.003x | 10.615x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 16.9 | 1.3 | 0.143x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.0 | 0.166x | 1.161x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.4 | 17.2 | 17.5 | 0.1 | 0.174x | 1.224x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.4 | 22.8 | 2.0 | 0.179x | 1.254x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 47.2 | 1.3 | 0.443x | 3.110x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.4 | 101.8 | 1.2 | 1.000x | 7.016x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.2 | 0.1 | 0.696x | 2.704x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.4 | 0.2 | 0.698x | 2.711x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.9 | 0.2 | 1.000x | 3.886x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.0 | 0.1 | 1.009x | 3.922x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.5 | 18.0 | 0.2 | 0.176x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.1 | 0.176x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.8 | 27.4 | 33.1 | 2.2 | 0.279x | 1.583x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.8 | 26.9 | 37.4 | 3.9 | 0.299x | 1.695x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 47.3 | 1.3 | 0.444x | 2.522x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 102.1 | 1.4 | 1.000x | 5.677x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 2.923x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.000x | 3.894x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 1.003x | 3.906x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.6 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.3 | 19.2 | 0.3 | 0.188x | 1.033x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.6 | 47.4 | 1.4 | 0.444x | 2.435x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 51.9 | 51.5 | 55.2 | 1.7 | 0.518x | 2.841x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.1 | 52.0 | 52.1 | 0.0 | 0.520x | 2.851x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 97.7 | 102.4 | 1.5 | 1.000x | 5.484x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.926x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 0.993x | 3.881x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.000x | 3.908x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.8 | 29.3 | 32.7 | 1.5 | 0.298x | 1.638x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.2 | 0.1 | 0.300x | 1.649x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 46.6 | 1.0 | 0.443x | 2.434x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 97.4 | 102.3 | 1.6 | 1.000x | 5.495x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.239x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.9 | 0.5 | 0.755x | 2.939x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.998x | 3.885x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.000x | 3.892x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.9 | 0.3 | 0.182x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 33.3 | 1.6 | 0.293x | 1.618x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.1 | 0.1 | 0.298x | 1.648x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 47.1 | 1.3 | 0.439x | 2.428x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.3 | 102.4 | 1.7 | 1.000x | 5.527x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.924x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.4 | 0.3 | 0.753x | 2.930x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.000x | 3.890x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 3.902x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 29.3 | 1.1 | 0.266x | 1.476x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.3 | 27.8 | 0.2 | 0.275x | 1.526x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.8 | 48.6 | 1.9 | 0.442x | 2.456x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 97.5 | 102.0 | 1.6 | 1.000x | 5.557x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.752x | 2.926x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 31.0 | 0.9 | 1.000x | 3.890x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 1.002x | 3.898x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.1 | 1.3 | 0.269x | 1.483x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.4 | 30.8 | 1.3 | 0.276x | 1.526x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.8 | 48.6 | 1.8 | 0.446x | 2.461x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.4 | 102.0 | 1.5 | 1.000x | 5.522x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.5 | 19.1 | 0.2 | 0.647x | 2.522x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 18.9 | 20.2 | 0.5 | 0.662x | 2.579x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.000x | 3.895x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.3 | 0.3 | 1.000x | 3.897x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.6 | 30.7 | 1.5 | 0.269x | 1.485x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 27.8 | 0.1 | 0.275x | 1.517x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.8 | 48.8 | 1.9 | 0.445x | 2.454x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 98.0 | 101.9 | 1.3 | 1.000x | 5.519x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.318x | 1.243x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.5 | 0.4 | 0.751x | 2.934x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 0.997x | 3.897x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.000x | 3.907x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.6 | 0.2 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.8 | 0.6 | 0.181x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 47.3 | 43.6 | 49.1 | 2.0 | 0.471x | 2.600x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 48.8 | 48.7 | 52.3 | 1.7 | 0.486x | 2.682x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.1 | 48.8 | 49.3 | 0.1 | 0.489x | 2.699x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.1 | 102.3 | 1.7 | 1.000x | 5.522x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.3 | 26.3 | 0.0 | 0.911x | 3.561x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.3 | 27.2 | 0.4 | 0.914x | 3.571x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 0.996x | 3.892x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.1 | 0.1 | 1.000x | 3.908x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.8 | 30.9 | 1.8 | 0.272x | 1.496x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.275x | 1.515x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 48.2 | 1.7 | 0.443x | 2.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.0 | 101.8 | 1.6 | 1.000x | 5.506x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.754x | 2.923x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 3.874x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 1.005x | 3.894x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.6 | 48.5 | 1.8 | 0.442x | 2.424x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 48.9 | 48.7 | 52.7 | 1.8 | 0.490x | 2.686x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.0 | 48.9 | 49.4 | 0.2 | 0.491x | 2.694x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.1 | 102.1 | 1.6 | 1.000x | 5.486x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.755x | 2.924x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 3.875x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.006x | 3.897x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 30.0 | 1.4 | 0.271x | 1.492x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.8 | 0.2 | 0.275x | 1.515x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 48.1 | 1.6 | 0.443x | 2.439x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.1 | 97.4 | 102.0 | 1.5 | 1.000x | 5.511x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 2.922x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.1 | 0.2 | 1.000x | 3.874x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 28.9 | 0.2 | 1.004x | 3.889x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 29.7 | 1.4 | 0.267x | 1.481x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 30.5 | 1.2 | 0.273x | 1.510x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 47.8 | 1.5 | 0.439x | 2.432x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.7 | 97.2 | 102.1 | 1.7 | 1.000x | 5.540x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.753x | 2.925x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 3.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.002x | 3.894x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.7 | 1.7 | 0.267x | 1.489x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.8 | 0.2 | 0.272x | 1.513x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 46.6 | 1.0 | 0.438x | 2.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 97.2 | 102.0 | 1.7 | 1.000x | 5.572x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.1 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 27.2 | 2.2 | 0.748x | 2.922x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 0.995x | 3.885x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.1 | 1.000x | 3.904x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 20.2 | 0.8 | 0.181x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.7 | 0.1 | 0.273x | 1.508x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.6 | 27.0 | 29.5 | 1.1 | 0.275x | 1.518x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 45.0 | 0.5 | 0.444x | 2.448x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.1 | 102.0 | 1.6 | 1.000x | 5.520x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 2.920x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 2.921x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 1.000x | 3.890x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.001x | 3.893x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.9 | 30.3 | 1.6 | 0.273x | 1.497x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.2 | 29.6 | 0.9 | 0.276x | 1.511x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 50.5 | 2.6 | 0.445x | 2.437x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.3 | 101.9 | 1.7 | 1.000x | 5.475x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.319x | 1.243x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 3.891x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.1 | 1.002x | 3.900x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 160.0 | 159.8 | 160.8 | 0.3 | 5.567x | 21.659x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 160.1 | 159.7 | 160.6 | 0.3 | 5.571x | 21.676x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 0.999x | 3.886x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 3.889x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 70.4 | 70.2 | 70.6 | 0.1 | 2.449x | 9.524x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 70.5 | 70.3 | 70.5 | 0.1 | 2.452x | 9.536x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.259x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.7 | 0.6 | 0.321x | 1.240x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.2 | 1.000x | 3.867x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 1.007x | 3.895x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.1 | 90.8 | 92.5 | 0.7 | 3.189x | 12.331x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.0 | 91.7 | 0.3 | 3.198x | 12.368x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.241x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 0.999x | 3.884x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.000x | 3.888x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 151.3 | 151.3 | 151.4 | 0.1 | 5.269x | 20.486x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 151.6 | 151.1 | 155.5 | 1.6 | 5.279x | 20.525x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.240x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.2 | 1.000x | 3.878x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.004x | 3.892x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.0 | 42.9 | 43.1 | 0.1 | 1.502x | 5.823x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 42.9 | 44.4 | 0.6 | 1.514x | 5.871x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.903x | 3.507x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.8 | 26.1 | 0.1 | 0.905x | 3.514x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 3.885x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.002x | 3.894x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.259x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.240x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 3.868x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.006x | 3.891x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 92.6 | 92.3 | 93.3 | 0.4 | 3.239x | 12.530x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.9 | 91.7 | 93.3 | 0.6 | 3.252x | 12.580x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 1.000x | 3.892x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 1.000x | 3.893x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 70.3 | 70.2 | 71.3 | 0.4 | 2.447x | 9.523x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 70.5 | 70.3 | 70.6 | 0.1 | 2.451x | 9.538x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.9 | 21.6 | 23.5 | 0.8 | 0.765x | 2.970x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.8 | 22.6 | 23.0 | 0.2 | 0.795x | 3.089x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 3.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.003x | 3.897x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.274x | 1.512x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.6 | 26.8 | 29.5 | 1.2 | 0.275x | 1.519x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 44.8 | 0.4 | 0.443x | 2.442x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 96.9 | 101.9 | 1.8 | 1.000x | 5.516x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 23.4 | 0.8 | 0.752x | 2.928x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.9 | 22.6 | 0.2 | 0.783x | 3.047x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 0.996x | 3.876x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 3.891x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 32.8 | 1.5 | 0.296x | 1.623x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 29.9 | 29.9 | 30.0 | 0.0 | 0.300x | 1.648x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 46.0 | 0.9 | 0.448x | 2.458x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.5 | 101.8 | 1.5 | 1.000x | 5.491x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 23.0 | 0.6 | 0.752x | 2.927x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.4 | 21.6 | 22.5 | 0.4 | 0.781x | 3.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.998x | 3.883x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 3.891x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 29.6 | 1.2 | 0.273x | 1.500x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 28.1 | 0.3 | 0.277x | 1.522x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.6 | 44.8 | 0.5 | 0.444x | 2.436x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.8 | 102.2 | 1.1 | 1.000x | 5.488x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 22.5 | 0.4 | 0.756x | 2.953x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.993x | 3.879x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.3 | 0.2 | 1.000x | 3.907x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.4 | 0.0 | 0.184x | 1.009x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 18.8 | 17.7 | 22.0 | 1.8 | 0.188x | 1.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 46.5 | 1.0 | 0.447x | 2.453x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.3 | 101.8 | 1.6 | 1.000x | 5.492x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.259x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.234x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.804x | 3.103x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.1 | 0.0 | 0.804x | 3.103x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 3.860x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.005x | 3.878x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.180x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.2 | 1.5 | 0.266x | 1.478x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 27.8 | 0.1 | 0.274x | 1.523x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 44.8 | 0.4 | 0.441x | 2.450x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 97.3 | 101.9 | 1.6 | 1.000x | 5.555x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.3 | 0.3 | 0.752x | 2.926x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.6 | 22.6 | 0.4 | 0.766x | 2.979x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.8 | 0.5 | 0.999x | 3.888x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 1.000x | 3.890x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.182x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 22.8 | 1.7 | 0.183x | 1.008x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 18.6 | 17.9 | 22.1 | 1.8 | 0.186x | 1.024x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.9 | 44.7 | 0.3 | 0.444x | 2.445x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 97.5 | 101.9 | 1.5 | 1.000x | 5.512x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.748x | 2.925x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.4 | 21.6 | 22.5 | 0.4 | 0.777x | 3.037x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.4 | 0.2 | 1.000x | 3.910x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.4 | 0.3 | 1.000x | 3.910x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.182x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 44.7 | 46.5 | 0.7 | 0.450x | 2.478x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 73.6 | 73.5 | 77.3 | 1.8 | 0.734x | 4.046x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 74.1 | 74.0 | 74.3 | 0.1 | 0.739x | 4.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 97.6 | 101.7 | 1.4 | 1.000x | 5.514x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.749x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 28.2 | 2.6 | 0.757x | 2.951x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 0.999x | 3.897x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 3.901x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.5 | 0.5 | 0.183x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.9 | 44.8 | 0.3 | 0.447x | 2.448x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 60.0 | 59.7 | 63.5 | 1.7 | 0.601x | 3.293x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 60.7 | 60.3 | 60.9 | 0.2 | 0.608x | 3.334x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.1 | 101.8 | 1.2 | 1.000x | 5.479x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.3 | 0.752x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 2.923x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 3.886x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.002x | 3.892x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 28.4 | 0.4 | 0.272x | 1.510x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.1 | 26.9 | 30.1 | 1.2 | 0.288x | 1.600x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.4 | 0.439x | 2.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 98.0 | 101.9 | 1.4 | 1.000x | 5.555x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.752x | 2.923x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.4 | 0.753x | 2.926x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.2 | 1.000x | 3.887x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.002x | 3.895x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.5 | 1.6 | 0.267x | 1.486x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.273x | 1.519x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 44.7 | 0.4 | 0.440x | 2.443x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 98.1 | 101.7 | 1.3 | 1.000x | 5.558x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.4 | 0.751x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.999x | 3.887x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 3.892x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.181x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.5 | 0.1 | 0.273x | 1.513x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.0 | 26.7 | 30.6 | 1.6 | 0.288x | 1.595x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.1 | 0.6 | 0.444x | 2.458x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.6 | 97.1 | 102.3 | 1.8 | 1.000x | 5.538x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 2.924x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.751x | 2.925x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 3.884x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 3.894x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 30.2 | 1.4 | 0.273x | 1.503x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.275x | 1.512x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.8 | 45.1 | 0.5 | 0.443x | 2.436x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 98.2 | 102.3 | 1.3 | 1.000x | 5.498x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.240x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.749x | 2.923x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 0.998x | 3.893x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 3.900x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.5 | 0.5 | 0.181x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.0 | 1.5 | 0.267x | 1.477x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.8 | 0.2 | 0.273x | 1.510x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 44.9 | 0.4 | 0.442x | 2.444x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.7 | 102.3 | 1.5 | 1.000x | 5.528x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 2.921x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.754x | 2.925x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.000x | 3.882x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.1 | 0.6 | 1.006x | 3.905x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.180x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.4 | 1.7 | 0.266x | 1.483x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.8 | 0.2 | 0.273x | 1.519x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 44.9 | 0.5 | 0.440x | 2.449x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 97.3 | 101.7 | 1.6 | 1.000x | 5.569x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.244x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 2.919x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 35.4 | 2.7 | 0.995x | 3.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.1 | 1.000x | 3.909x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 30.2 | 1.6 | 0.269x | 1.481x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.275x | 1.513x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.7 | 45.2 | 0.6 | 0.448x | 2.467x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.2 | 97.2 | 102.2 | 1.6 | 1.000x | 5.509x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.242x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 2.922x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 2.924x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.000x | 3.892x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.000x | 3.893x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.181x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.6 | 0.2 | 0.182x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.6 | 1.7 | 0.268x | 1.477x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 28.0 | 0.2 | 0.275x | 1.517x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.1 | 0.5 | 0.442x | 2.439x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.2 | 102.2 | 1.6 | 1.000x | 5.518x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.280x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.0 | 8.9 | 10.1 | 0.5 | 0.315x | 1.125x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.7 | 10.8 | 0.0 | 0.375x | 1.341x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.8 | 0.1 | 0.378x | 1.350x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.6 | 0.1 | 1.000x | 3.572x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.6 | 0.0 | 1.002x | 3.578x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.3 | 6.3 | 6.5 | 0.1 | 0.197x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 6.4 | 6.3 | 6.5 | 0.1 | 0.198x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 10.2 | 10.2 | 10.9 | 0.3 | 0.317x | 1.613x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 9.2 | 14.2 | 2.3 | 0.430x | 2.186x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.3 | 32.2 | 32.6 | 0.1 | 1.000x | 5.080x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.2 | 34.3 | 38.6 | 1.5 | 1.153x | 5.855x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.8 | 10.9 | 0.0 | 0.110x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.9 | 10.9 | 0.0 | 0.111x | 1.010x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.8 | 17.6 | 17.9 | 0.1 | 0.180x | 1.640x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.5 | 19.0 | 0.5 | 0.182x | 1.659x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.1 | 95.1 | 98.8 | 1.6 | 0.996x | 9.060x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.4 | 97.1 | 99.1 | 0.7 | 1.000x | 9.094x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 16.9 | 1.3 | 0.142x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.5 | 0.0 | 0.165x | 1.166x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.0 | 17.0 | 17.0 | 0.0 | 0.170x | 1.199x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.1 | 16.9 | 17.3 | 0.1 | 0.171x | 1.205x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.8 | 0.4 | 0.444x | 3.129x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.4 | 101.8 | 1.5 | 1.000x | 7.048x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.236x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.5 | 0.0 | 0.604x | 2.348x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.5 | 0.0 | 0.604x | 2.349x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.4 | 0.3 | 0.996x | 3.872x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.3 | 0.3 | 1.000x | 3.889x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 9.9 | 9.7 | 10.1 | 0.1 | 0.295x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 10.1 | 10.0 | 10.1 | 0.0 | 0.301x | 1.020x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.5 | 33.1 | 33.8 | 0.3 | 1.000x | 3.391x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.6 | 35.5 | 40.2 | 1.6 | 1.123x | 3.807x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 134.1 | 132.9 | 135.4 | 0.8 | 4.007x | 13.589x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 139.2 | 134.7 | 154.6 | 6.9 | 4.159x | 14.104x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.241x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 17.3 | 0.2 | 0.581x | 2.281x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.9 | 17.6 | 0.3 | 0.583x | 2.291x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 30.7 | 0.8 | 0.992x | 3.894x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 30.4 | 0.7 | 1.000x | 3.927x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 9.0 | 0.1 | 0.273x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 9.2 | 8.9 | 9.2 | 0.1 | 0.281x | 1.031x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 33.7 | 0.5 | 1.000x | 3.669x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.0 | 34.8 | 42.4 | 2.7 | 1.103x | 4.048x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 45.8 | 45.8 | 46.0 | 0.1 | 1.405x | 5.156x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.9 | 45.2 | 50.5 | 2.5 | 1.532x | 5.622x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 627,186.7 | 627,062.8 | 630,211.1 | 1,203.0 | 0.175x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 628,561.1 | 627,369.0 | 629,963.1 | 844.7 | 0.175x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,707,833.8 | 1,672,779.3 | 1,798,471.9 | 45,094.7 | 0.476x | 2.723x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,590,816.7 | 3,547,529.2 | 3,622,837.1 | 27,898.4 | 1.000x | 5.725x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,908,618.9 | 3,903,859.5 | 3,957,670.5 | 20,438.8 | 1.089x | 6.232x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 4,074,182.9 | 4,050,733.8 | 4,079,345.7 | 10,216.0 | 1.135x | 6.496x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,705.1 | 17,661.1 | 17,974.2 | 113.6 | 0.997x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,720.6 | 17,691.9 | 17,756.5 | 22.8 | 0.998x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,761.8 | 17,737.7 | 17,782.5 | 17.9 | 1.000x | 1.003x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,218.5 | 39,175.2 | 39,377.1 | 72.8 | 2.208x | 2.215x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,790,208.5 | 2,789,990.7 | 2,793,229.1 | 1,208.0 | 157.090x | 157.593x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,793,280.9 | 2,790,804.1 | 2,834,053.8 | 16,716.0 | 157.263x | 157.767x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,705.9 | 17,663.6 | 17,910.7 | 89.5 | 0.996x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,715.6 | 17,690.9 | 17,733.2 | 16.3 | 0.997x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,774.7 | 17,749.1 | 18,189.7 | 165.8 | 1.000x | 1.004x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,429.5 | 39,335.9 | 40,417.2 | 469.8 | 2.218x | 2.227x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,790,569.1 | 2,789,820.2 | 2,812,500.8 | 8,845.5 | 156.997x | 157.607x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,790,950.1 | 2,790,291.5 | 2,816,695.7 | 10,419.9 | 157.019x | 157.628x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 30,813.1 | 30,673.5 | 30,904.7 | 75.0 | 0.440x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 30,873.3 | 30,758.4 | 30,996.8 | 81.5 | 0.441x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,063.3 | 68,866.1 | 71,348.8 | 948.0 | 0.986x | 2.241x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,023.5 | 69,886.2 | 70,531.7 | 235.0 | 1.000x | 2.273x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,345,865.5 | 3,336,187.4 | 3,370,228.3 | 12,544.3 | 47.782x | 108.586x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 3,371,357.6 | 3,351,732.4 | 3,382,219.3 | 10,609.7 | 48.146x | 109.413x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,686.9 | 17,632.4 | 17,694.7 | 23.5 | 0.998x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,687.2 | 17,657.9 | 17,778.4 | 44.2 | 0.998x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,730.8 | 17,678.0 | 17,774.0 | 31.2 | 1.000x | 1.002x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,876.5 | 39,670.0 | 40,040.7 | 122.1 | 2.249x | 2.255x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,793,313.5 | 2,789,369.1 | 2,821,194.2 | 11,634.5 | 157.541x | 157.931x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,823,491.0 | 2,790,294.9 | 3,213,887.3 | 163,265.3 | 159.243x | 159.637x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.4 | 44.4 | 44.8 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.0 | 46.8 | 49.9 | 1.2 | 0.085x | 1.058x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 69.2 | 69.7 | 0.2 | 0.126x | 1.560x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.8 | 69.2 | 70.3 | 0.4 | 0.126x | 1.570x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 552.4 | 546.0 | 562.4 | 6.0 | 1.000x | 12.430x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 555.7 | 548.4 | 609.7 | 22.8 | 1.006x | 12.504x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 53.2 | 52.9 | 54.1 | 0.4 | 0.097x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 55.0 | 54.1 | 55.4 | 0.5 | 0.100x | 1.034x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.5 | 58.7 | 0.1 | 0.107x | 1.100x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.4 | 58.8 | 0.2 | 0.107x | 1.102x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.9 | 76.7 | 78.1 | 0.5 | 0.142x | 1.463x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.4 | 542.3 | 569.4 | 10.2 | 1.000x | 10.288x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 84.5 | 84.4 | 84.9 | 0.2 | 0.111x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 84.3 | 85.8 | 0.6 | 0.112x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.9 | 89.7 | 90.4 | 0.3 | 0.118x | 1.065x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.3 | 89.6 | 90.6 | 0.3 | 0.118x | 1.068x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 763.0 | 754.5 | 768.3 | 4.5 | 1.000x | 9.032x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 772.4 | 756.8 | 775.1 | 7.1 | 1.012x | 9.144x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 77.7 | 77.6 | 77.7 | 0.1 | 0.103x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 77.9 | 77.7 | 78.1 | 0.1 | 0.103x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 90.7 | 90.6 | 90.9 | 0.1 | 0.120x | 1.167x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.1 | 90.4 | 95.6 | 2.2 | 0.120x | 1.173x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 92.9 | 92.7 | 93.0 | 0.1 | 0.123x | 1.195x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 758.0 | 755.4 | 779.2 | 8.8 | 1.000x | 9.753x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.1 | 30.5 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.7 | 35.4 | 1.0 | 0.068x | 1.082x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 33.1 | 33.5 | 0.1 | 0.069x | 1.092x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.1 | 35.4 | 0.9 | 0.069x | 1.094x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 483.0 | 480.8 | 490.0 | 3.3 | 1.000x | 15.883x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 485.7 | 478.2 | 492.4 | 4.7 | 1.006x | 15.973x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.6 | 0.2 | 0.054x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 37.9 | 37.9 | 38.0 | 0.1 | 0.079x | 1.459x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 38.4 | 38.4 | 38.9 | 0.2 | 0.080x | 1.479x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.0 | 63.6 | 64.8 | 0.4 | 0.133x | 2.462x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 481.6 | 478.3 | 511.8 | 12.6 | 1.000x | 18.528x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.8 | 57.5 | 59.7 | 0.8 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.2 | 61.9 | 1.1 | 0.078x | 1.036x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.6 | 99.6 | 1.1 | 0.127x | 1.684x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.0 | 98.1 | 0.4 | 0.127x | 1.685x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.8 | 760.9 | 790.6 | 10.9 | 1.000x | 13.291x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 775.2 | 767.2 | 777.4 | 4.1 | 1.010x | 13.419x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 65.9 | 63.6 | 66.8 | 1.2 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.4 | 67.3 | 70.4 | 1.2 | 0.088x | 1.023x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 86.4 | 86.2 | 87.2 | 0.4 | 0.113x | 1.311x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 86.6 | 86.2 | 87.4 | 0.5 | 0.113x | 1.313x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.5 | 91.2 | 94.7 | 1.3 | 0.122x | 1.419x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 764.9 | 760.5 | 771.8 | 3.9 | 1.000x | 11.606x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.8 | 58.2 | 0.2 | 0.102x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.2 | 62.4 | 0.7 | 0.107x | 1.056x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 131.9 | 131.1 | 132.5 | 0.5 | 0.232x | 2.278x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 132.5 | 131.7 | 132.6 | 0.3 | 0.233x | 2.289x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 564.5 | 560.5 | 572.8 | 4.9 | 0.991x | 9.750x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 569.6 | 559.7 | 590.3 | 10.5 | 1.000x | 9.838x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 66.2 | 64.4 | 66.4 | 0.8 | 0.117x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 68.8 | 67.5 | 69.4 | 0.6 | 0.122x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.9 | 90.4 | 92.0 | 0.6 | 0.161x | 1.374x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 119.8 | 120.3 | 0.2 | 0.213x | 1.814x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 119.8 | 120.8 | 0.4 | 0.214x | 1.820x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 564.3 | 560.0 | 581.2 | 7.7 | 1.000x | 8.522x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.5 | 30.3 | 31.1 | 0.4 | 0.063x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.9 | 33.3 | 0.2 | 0.068x | 1.083x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.9 | 35.1 | 0.8 | 0.069x | 1.088x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.3 | 35.3 | 0.8 | 0.069x | 1.093x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 482.0 | 479.6 | 484.5 | 1.7 | 1.000x | 15.812x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 483.6 | 478.5 | 488.2 | 3.3 | 1.004x | 15.868x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.6 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.054x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 38.1 | 37.7 | 38.9 | 0.4 | 0.079x | 1.466x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 39.1 | 0.3 | 0.080x | 1.486x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.1 | 63.4 | 65.1 | 0.6 | 0.133x | 2.462x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 483.0 | 476.0 | 497.4 | 7.8 | 1.000x | 18.568x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 65.5 | 65.0 | 66.1 | 0.4 | 0.084x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.8 | 65.4 | 67.2 | 0.6 | 0.084x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.5 | 94.6 | 98.1 | 1.2 | 0.122x | 1.458x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.6 | 112.6 | 0.7 | 0.142x | 1.693x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.4 | 777.9 | 786.9 | 3.1 | 0.998x | 11.928x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.0 | 776.8 | 797.0 | 7.6 | 1.000x | 11.952x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 55.5 | 55.2 | 55.8 | 0.2 | 0.071x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 56.0 | 0.1 | 0.072x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.8 | 84.7 | 0.3 | 0.108x | 1.514x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 133.4 | 132.2 | 134.8 | 0.8 | 0.171x | 2.403x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 138.0 | 137.0 | 141.8 | 1.8 | 0.177x | 2.486x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.8 | 769.6 | 789.6 | 7.1 | 1.000x | 14.011x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.6 | 53.7 | 0.4 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.1 | 58.1 | 1.1 | 0.090x | 1.044x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 102.4 | 101.9 | 103.2 | 0.5 | 0.166x | 1.928x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.8 | 102.6 | 103.1 | 0.2 | 0.166x | 1.936x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.2 | 612.3 | 630.6 | 6.7 | 1.000x | 11.644x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 620.4 | 616.6 | 636.2 | 7.1 | 1.003x | 11.685x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 61.8 | 61.6 | 62.4 | 0.3 | 0.100x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.3 | 63.7 | 65.5 | 0.7 | 0.105x | 1.041x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.9 | 87.2 | 95.9 | 3.2 | 0.148x | 1.471x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 91.6 | 92.4 | 0.3 | 0.149x | 1.488x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 92.1 | 91.8 | 92.1 | 0.1 | 0.150x | 1.489x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 615.6 | 607.6 | 630.7 | 7.8 | 1.000x | 9.960x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.2 | 46.6 | 0.1 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.9 | 48.7 | 51.6 | 1.1 | 0.090x | 1.054x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.3 | 80.9 | 0.2 | 0.148x | 1.733x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.3 | 80.6 | 0.1 | 0.148x | 1.734x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 541.5 | 539.2 | 554.0 | 5.4 | 0.997x | 11.655x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.1 | 542.0 | 545.7 | 1.3 | 1.000x | 11.691x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 55.6 | 54.0 | 56.4 | 0.8 | 0.102x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 56.8 | 56.4 | 57.9 | 0.5 | 0.104x | 1.022x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.3 | 70.0 | 0.2 | 0.128x | 1.251x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 69.7 | 0.1 | 0.128x | 1.251x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.2 | 78.6 | 81.3 | 1.0 | 0.147x | 1.442x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.8 | 542.7 | 562.4 | 7.5 | 1.000x | 9.780x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.5 | 42.3 | 42.9 | 0.2 | 0.079x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.3 | 45.3 | 47.5 | 0.8 | 0.084x | 1.066x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.8 | 61.6 | 61.9 | 0.1 | 0.115x | 1.453x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.0 | 61.8 | 62.2 | 0.1 | 0.115x | 1.458x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.1 | 532.2 | 543.1 | 3.6 | 0.996x | 12.628x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.2 | 536.5 | 544.7 | 3.2 | 1.000x | 12.678x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 50.9 | 49.0 | 51.3 | 0.8 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.3 | 51.3 | 51.6 | 0.1 | 0.096x | 1.009x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.9 | 0.2 | 0.096x | 1.012x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.6 | 52.3 | 53.0 | 0.2 | 0.098x | 1.034x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.3 | 74.2 | 76.4 | 0.7 | 0.140x | 1.479x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 536.6 | 531.4 | 562.1 | 11.2 | 1.000x | 10.544x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 32.2 | 0.5 | 0.071x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.5 | 34.7 | 0.8 | 0.075x | 1.063x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 62.0 | 62.2 | 0.1 | 0.142x | 2.004x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.7 | 62.9 | 0.4 | 0.142x | 2.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.3 | 432.4 | 439.1 | 2.5 | 0.999x | 14.111x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 437.6 | 432.4 | 441.2 | 3.3 | 1.000x | 14.119x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 36.3 | 35.8 | 38.6 | 1.0 | 0.082x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 37.8 | 37.6 | 38.3 | 0.3 | 0.086x | 1.041x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.117x | 1.417x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.117x | 1.417x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.4 | 67.5 | 69.0 | 0.5 | 0.155x | 1.883x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 441.7 | 428.7 | 463.3 | 11.5 | 1.000x | 12.159x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.2 | 36.0 | 1.7 | 0.092x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.8 | 0.1 | 0.097x | 1.060x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.2 | 41.5 | 0.2 | 0.120x | 1.303x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 40.9 | 43.2 | 0.8 | 0.120x | 1.303x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 344.4 | 341.7 | 349.6 | 3.0 | 0.996x | 10.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 345.7 | 341.2 | 376.5 | 13.0 | 1.000x | 10.883x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.9 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 39.9 | 2.1 | 0.020x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.4 | 135.7 | 142.6 | 2.5 | 0.081x | 4.091x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 320.0 | 315.7 | 328.4 | 4.3 | 0.182x | 9.258x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 320.9 | 317.0 | 321.6 | 1.8 | 0.183x | 9.283x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,753.7 | 1,745.4 | 1,816.2 | 26.1 | 1.000x | 50.735x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.7 | 57.7 | 63.1 | 2.0 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.1 | 62.8 | 1.0 | 0.089x | 1.027x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.7 | 76.2 | 77.3 | 0.3 | 0.113x | 1.305x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.4 | 77.8 | 0.5 | 0.113x | 1.309x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 679.2 | 676.7 | 685.6 | 3.7 | 0.997x | 11.563x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.4 | 674.5 | 694.2 | 6.4 | 1.000x | 11.600x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.9 | 62.9 | 67.2 | 1.4 | 0.096x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.6 | 65.4 | 65.9 | 0.1 | 0.097x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.1 | 65.7 | 66.2 | 0.2 | 0.097x | 1.018x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.2 | 67.2 | 67.7 | 0.2 | 0.099x | 1.036x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.8 | 80.9 | 88.0 | 2.7 | 0.120x | 1.260x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.3 | 671.1 | 683.9 | 4.6 | 1.000x | 10.463x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.6 | 58.2 | 0.2 | 0.085x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.6 | 60.4 | 62.6 | 0.9 | 0.089x | 1.045x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.2 | 75.9 | 76.7 | 0.3 | 0.112x | 1.314x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.7 | 77.1 | 0.2 | 0.112x | 1.325x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 678.2 | 676.2 | 687.1 | 3.9 | 0.993x | 11.696x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.0 | 679.5 | 687.6 | 2.8 | 1.000x | 11.779x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 65.0 | 64.2 | 65.2 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 66.2 | 0.3 | 0.096x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 65.9 | 0.1 | 0.097x | 1.013x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.4 | 67.1 | 72.9 | 2.2 | 0.099x | 1.037x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.6 | 81.3 | 85.5 | 1.6 | 0.120x | 1.255x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.4 | 677.3 | 685.4 | 3.0 | 1.000x | 10.482x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.7 | 47.6 | 50.2 | 1.0 | 0.088x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.2 | 52.6 | 0.9 | 0.093x | 1.053x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.9 | 62.7 | 0.3 | 0.114x | 1.298x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.9 | 62.3 | 0.2 | 0.115x | 1.302x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.2 | 535.7 | 543.3 | 2.8 | 1.000x | 11.363x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.8 | 534.1 | 545.0 | 4.0 | 1.001x | 11.375x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.3 | 51.3 | 51.7 | 0.1 | 0.096x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 53.2 | 0.7 | 0.096x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 56.7 | 55.9 | 57.5 | 0.6 | 0.106x | 1.105x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 56.7 | 54.8 | 58.4 | 1.4 | 0.106x | 1.105x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 76.2 | 74.9 | 78.3 | 1.2 | 0.142x | 1.485x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537.2 | 533.7 | 548.0 | 5.0 | 1.000x | 10.466x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.3 | 58.5 | 1.3 | 0.084x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.8 | 59.7 | 0.7 | 0.088x | 1.043x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.8 | 72.7 | 73.7 | 0.4 | 0.110x | 1.311x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 72.9 | 73.4 | 0.2 | 0.111x | 1.318x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.7 | 654.8 | 663.5 | 3.2 | 0.991x | 11.812x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 661.9 | 650.8 | 666.7 | 6.2 | 1.000x | 11.923x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.0 | 61.4 | 62.7 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.8 | 0.1 | 0.095x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.0 | 0.095x | 1.009x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.4 | 64.1 | 64.6 | 0.2 | 0.098x | 1.038x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.5 | 79.4 | 84.8 | 1.9 | 0.123x | 1.297x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.9 | 651.0 | 661.9 | 4.0 | 1.000x | 10.573x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.140x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.2 | 27.5 | 0.8 | 0.141x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 33.3 | 0.3 | 0.176x | 1.257x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.7 | 32.4 | 32.9 | 0.2 | 0.177x | 1.265x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 185.3 | 183.8 | 186.7 | 1.0 | 1.000x | 7.163x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.7 | 185.4 | 187.7 | 0.9 | 1.002x | 7.178x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 27.0 | 0.3 | 0.024x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 106.7 | 115.8 | 3.4 | 0.099x | 4.116x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 226.6 | 226.0 | 230.8 | 2.0 | 0.209x | 8.687x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 228.3 | 224.7 | 232.5 | 2.5 | 0.210x | 8.753x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,086.9 | 1,077.9 | 1,114.4 | 12.4 | 1.000x | 41.661x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.5 | 58.1 | 0.2 | 0.084x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.3 | 61.7 | 0.6 | 0.088x | 1.045x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.5 | 75.5 | 77.2 | 0.6 | 0.111x | 1.325x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.4 | 77.3 | 0.3 | 0.112x | 1.330x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 677.7 | 670.7 | 680.8 | 3.4 | 0.986x | 11.738x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 687.0 | 664.1 | 709.6 | 14.5 | 1.000x | 11.898x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.8 | 63.9 | 67.2 | 1.1 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 66.1 | 0.3 | 0.096x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 66.2 | 0.2 | 0.097x | 1.015x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 66.9 | 66.8 | 67.5 | 0.3 | 0.098x | 1.032x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.4 | 81.1 | 86.6 | 2.1 | 0.120x | 1.256x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 680.4 | 672.6 | 686.0 | 4.8 | 1.000x | 10.499x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.3 | 55.2 | 55.5 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.7 | 60.1 | 0.9 | 0.088x | 1.046x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.8 | 73.5 | 0.3 | 0.110x | 1.316x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.7 | 73.1 | 0.2 | 0.111x | 1.318x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 658.2 | 650.0 | 659.4 | 3.5 | 0.998x | 11.893x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 659.6 | 646.7 | 661.2 | 5.9 | 1.000x | 11.919x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.3 | 61.7 | 63.0 | 0.5 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.9 | 0.1 | 0.096x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.4 | 63.0 | 0.2 | 0.096x | 1.006x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.2 | 63.9 | 64.5 | 0.2 | 0.098x | 1.031x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.6 | 79.3 | 85.4 | 2.3 | 0.122x | 1.278x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.3 | 649.6 | 663.1 | 5.0 | 1.000x | 10.516x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 25.2 | 27.6 | 0.9 | 0.136x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.6 | 26.5 | 29.0 | 1.0 | 0.137x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 34.6 | 0.2 | 0.177x | 1.303x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 33.7 | 35.9 | 0.8 | 0.178x | 1.305x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 194.2 | 191.9 | 196.2 | 1.4 | 0.999x | 7.342x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 194.4 | 191.0 | 197.2 | 2.0 | 1.000x | 7.350x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.8 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 27.9 | 0.1 | 0.025x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.9 | 107.9 | 113.5 | 2.1 | 0.102x | 4.020x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 237.7 | 236.8 | 241.4 | 1.7 | 0.218x | 8.612x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 237.8 | 236.5 | 240.8 | 1.5 | 0.218x | 8.618x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,089.8 | 1,086.1 | 1,107.0 | 8.1 | 1.000x | 39.487x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.2 | 63.1 | 63.3 | 0.1 | 0.092x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 66.2 | 65.9 | 67.4 | 0.5 | 0.097x | 1.049x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 83.4 | 83.3 | 86.5 | 1.2 | 0.122x | 1.320x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 84.1 | 83.9 | 86.5 | 1.0 | 0.123x | 1.332x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 685.5 | 684.9 | 691.9 | 3.1 | 1.000x | 10.854x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 686.7 | 684.8 | 697.4 | 4.8 | 1.002x | 10.874x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 70.5 | 68.5 | 73.8 | 1.9 | 0.102x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 71.4 | 70.8 | 71.5 | 0.3 | 0.103x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 72.7 | 72.4 | 73.4 | 0.4 | 0.105x | 1.030x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.0 | 72.8 | 73.9 | 0.4 | 0.106x | 1.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.1 | 83.2 | 89.0 | 2.1 | 0.122x | 1.193x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 690.4 | 683.1 | 700.0 | 6.1 | 1.000x | 9.791x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.0 | 61.7 | 62.5 | 0.3 | 0.088x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.9 | 62.4 | 0.2 | 0.088x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 70.3 | 67.9 | 72.4 | 1.5 | 0.100x | 1.134x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 75.8 | 75.4 | 75.9 | 0.2 | 0.108x | 1.224x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 701.9 | 699.4 | 708.8 | 3.5 | 1.000x | 11.330x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 703.1 | 701.4 | 709.7 | 3.2 | 1.002x | 11.349x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.7 | 0.2 | 0.073x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 0.073x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.0 | 75.1 | 79.7 | 1.7 | 0.108x | 1.479x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84.7 | 84.6 | 84.8 | 0.1 | 0.120x | 1.648x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.0 | 89.9 | 92.2 | 0.9 | 0.128x | 1.752x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 703.0 | 697.8 | 726.5 | 10.3 | 1.000x | 13.677x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 38.2 | 0.9 | 0.080x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 37.8 | 40.2 | 0.9 | 0.085x | 1.058x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.3 | 91.2 | 91.5 | 0.1 | 0.204x | 2.534x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.5 | 91.4 | 92.5 | 0.4 | 0.204x | 2.539x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.2 | 446.1 | 452.4 | 2.2 | 1.000x | 12.436x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 449.5 | 446.0 | 455.8 | 3.6 | 1.003x | 12.474x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 41.0 | 39.7 | 41.3 | 0.7 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 42.0 | 41.6 | 42.2 | 0.3 | 0.093x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.1 | 70.8 | 74.6 | 1.4 | 0.160x | 1.756x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.3 | 80.0 | 80.4 | 0.2 | 0.178x | 1.958x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 80.4 | 80.6 | 0.1 | 0.179x | 1.963x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.0 | 447.0 | 470.1 | 8.3 | 1.000x | 10.971x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.3 | 57.1 | 74.4 | 7.2 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.4 | 77.0 | 0.3 | 0.114x | 1.195x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 77.0 | 76.6 | 79.3 | 1.0 | 0.114x | 1.198x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 77.1 | 76.3 | 77.9 | 0.6 | 0.114x | 1.200x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 669.6 | 661.2 | 672.5 | 3.9 | 0.994x | 10.421x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 673.9 | 665.0 | 683.9 | 7.7 | 1.000x | 10.487x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.098x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 65.8 | 0.1 | 0.098x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 77.8 | 76.3 | 87.5 | 4.1 | 0.116x | 1.184x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.0 | 82.8 | 85.7 | 1.1 | 0.124x | 1.263x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 86.0 | 85.9 | 86.1 | 0.1 | 0.129x | 1.308x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.6 | 662.0 | 689.3 | 9.8 | 1.000x | 10.160x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.5 | 62.3 | 0.3 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.6 | 62.1 | 0.2 | 0.086x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 61.4 | 74.6 | 4.9 | 0.102x | 1.183x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 78.4 | 78.2 | 87.4 | 3.5 | 0.109x | 1.267x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 707.4 | 705.1 | 715.9 | 3.7 | 0.986x | 11.429x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 717.6 | 706.9 | 721.6 | 5.1 | 1.000x | 11.594x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.8 | 0.2 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.2 | 51.7 | 0.2 | 0.072x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 86.5 | 85.2 | 88.5 | 1.1 | 0.122x | 1.684x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 87.7 | 87.6 | 89.5 | 0.7 | 0.123x | 1.706x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.1 | 88.9 | 93.2 | 1.7 | 0.125x | 1.735x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 710.8 | 707.1 | 739.3 | 11.8 | 1.000x | 13.832x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62.5 | 61.3 | 73.0 | 4.4 | 0.085x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.7 | 77.1 | 0.1 | 0.105x | 1.229x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 77.0 | 76.5 | 78.0 | 0.5 | 0.105x | 1.232x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 79.1 | 78.4 | 89.0 | 4.0 | 0.108x | 1.266x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 730.4 | 720.7 | 745.3 | 9.1 | 0.996x | 11.691x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.5 | 725.3 | 740.4 | 6.3 | 1.000x | 11.741x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 65.8 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.5 | 65.9 | 0.1 | 0.090x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.3 | 84.0 | 88.8 | 1.8 | 0.115x | 1.284x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 86.0 | 81.3 | 91.1 | 3.5 | 0.118x | 1.309x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 89.6 | 89.6 | 89.8 | 0.1 | 0.123x | 1.365x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 731.5 | 726.6 | 766.5 | 14.8 | 1.000x | 11.138x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 35.9 | 37.4 | 0.6 | 0.081x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.0 | 37.4 | 40.6 | 1.1 | 0.084x | 1.036x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 92.0 | 0.3 | 0.203x | 2.495x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.6 | 91.3 | 95.7 | 1.7 | 0.203x | 2.499x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 448.6 | 445.2 | 453.9 | 3.0 | 0.995x | 12.245x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.9 | 446.4 | 454.3 | 2.8 | 1.000x | 12.308x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 41.0 | 39.7 | 41.2 | 0.6 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 41.9 | 41.0 | 42.2 | 0.4 | 0.093x | 1.021x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.7 | 70.2 | 74.7 | 1.6 | 0.162x | 1.771x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.5 | 0.1 | 0.179x | 1.959x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 80.5 | 80.6 | 0.0 | 0.179x | 1.962x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449.3 | 446.9 | 461.5 | 5.5 | 1.000x | 10.949x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 66.9 | 57.9 | 72.1 | 6.3 | 0.106x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.7 | 72.5 | 75.4 | 1.0 | 0.117x | 1.102x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.3 | 91.2 | 91.7 | 0.2 | 0.144x | 1.366x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.5 | 91.1 | 91.7 | 0.2 | 0.145x | 1.368x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.3 | 626.7 | 634.7 | 2.6 | 1.000x | 9.456x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.4 | 632.5 | 645.4 | 4.8 | 1.003x | 9.489x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.6 | 76.3 | 77.3 | 0.4 | 0.122x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.3 | 80.3 | 80.9 | 0.3 | 0.128x | 1.049x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 80.6 | 0.1 | 0.128x | 1.052x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.3 | 94.4 | 5.2 | 0.130x | 1.065x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 86.5 | 86.4 | 86.5 | 0.0 | 0.138x | 1.130x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.3 | 627.8 | 652.7 | 9.6 | 1.000x | 8.206x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.0 | 26.9 | 28.6 | 0.7 | 0.090x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.8 | 27.2 | 0.2 | 0.091x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.6 | 35.7 | 0.8 | 0.114x | 1.260x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 0.116x | 1.287x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 295.6 | 325.1 | 11.1 | 1.000x | 11.061x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 301.0 | 299.0 | 302.1 | 1.1 | 1.008x | 11.146x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.5 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.5 | 0.2 | 0.021x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 66.3 | 69.3 | 1.2 | 0.064x | 3.096x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 256.5 | 255.4 | 259.4 | 1.4 | 0.239x | 11.569x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 256.7 | 256.0 | 259.2 | 1.2 | 0.239x | 11.580x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.4 | 1,062.5 | 1,129.6 | 23.5 | 1.000x | 48.466x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.4 | 34.9 | 0.7 | 0.113x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.2 | 0.1 | 0.118x | 1.046x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 51.2 | 50.4 | 52.1 | 0.6 | 0.173x | 1.530x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 51.3 | 51.0 | 51.7 | 0.3 | 0.174x | 1.534x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.6 | 293.6 | 357.5 | 25.1 | 1.000x | 8.838x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.0 | 297.6 | 356.0 | 22.5 | 1.015x | 8.970x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.3 | 45.8 | 0.2 | 0.043x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 45.7 | 45.4 | 46.0 | 0.2 | 0.043x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.7 | 69.4 | 72.7 | 1.1 | 0.067x | 1.576x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 528.2 | 526.6 | 534.1 | 2.6 | 0.496x | 11.614x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 531.8 | 527.3 | 541.8 | 4.8 | 0.499x | 11.694x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,065.9 | 1,061.6 | 1,128.9 | 25.4 | 1.000x | 23.438x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.5 | 27.0 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.6 | 29.5 | 1.1 | 0.090x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.1 | 33.7 | 35.0 | 0.5 | 0.115x | 1.272x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 0.117x | 1.298x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.9 | 292.9 | 380.4 | 34.0 | 1.000x | 11.085x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.5 | 294.4 | 311.9 | 5.8 | 1.019x | 11.293x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.1 | 0.0 | 0.021x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.3 | 0.1 | 0.021x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.3 | 66.5 | 69.2 | 1.0 | 0.064x | 3.095x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 258.4 | 249.9 | 264.0 | 4.9 | 0.243x | 11.714x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 265.8 | 255.9 | 272.4 | 5.5 | 0.250x | 12.051x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.2 | 1,053.9 | 1,126.1 | 26.4 | 1.000x | 48.247x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.4 | 35.3 | 0.7 | 0.114x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 34.9 | 35.1 | 0.1 | 0.119x | 1.046x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.1 | 35.6 | 0.2 | 0.120x | 1.060x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.0 | 37.2 | 0.8 | 0.120x | 1.060x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.8 | 293.7 | 295.9 | 0.7 | 1.000x | 8.800x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.3 | 294.6 | 301.2 | 2.5 | 1.008x | 8.875x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 29.6 | 29.5 | 31.3 | 0.8 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.2 | 0.2 | 0.028x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.7 | 70.4 | 72.6 | 0.8 | 0.067x | 2.422x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 329.3 | 325.5 | 338.2 | 4.4 | 0.309x | 11.126x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 330.5 | 328.2 | 332.2 | 1.4 | 0.310x | 11.169x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.7 | 1,057.9 | 1,130.7 | 27.1 | 1.000x | 36.041x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 30.9 | 31.5 | 0.2 | 0.089x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.4 | 31.3 | 33.6 | 0.9 | 0.089x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 45.0 | 44.8 | 49.4 | 1.8 | 0.127x | 1.436x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.4 | 52.8 | 55.6 | 1.2 | 0.154x | 1.739x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 352.7 | 349.0 | 359.8 | 3.7 | 1.000x | 11.269x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 361.1 | 357.8 | 363.7 | 1.9 | 1.024x | 11.535x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.4 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.3 | 0.1 | 0.020x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.4 | 69.8 | 72.3 | 0.8 | 0.055x | 2.730x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 387.4 | 381.8 | 391.7 | 4.2 | 0.298x | 14.814x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 389.4 | 383.8 | 396.8 | 4.5 | 0.299x | 14.891x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,301.2 | 1,296.6 | 1,384.8 | 33.5 | 1.000x | 49.755x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 31.4 | 0.2 | 0.100x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 30.8 | 33.2 | 0.8 | 0.101x | 1.011x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.6 | 42.7 | 0.4 | 0.134x | 1.350x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.9 | 48.9 | 52.1 | 1.3 | 0.164x | 1.643x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 311.0 | 310.0 | 315.8 | 2.0 | 1.000x | 10.049x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 317.7 | 311.2 | 321.7 | 3.5 | 1.022x | 10.265x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.6 | 0.2 | 0.023x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.023x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.7 | 69.2 | 73.2 | 1.4 | 0.062x | 2.702x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 362.4 | 358.6 | 364.8 | 2.1 | 0.319x | 13.855x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 363.1 | 353.4 | 365.7 | 4.8 | 0.320x | 13.881x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.5 | 1,130.1 | 1,191.8 | 23.3 | 1.000x | 43.376x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.6 | 0.2 | 0.040x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.4 | 23.1 | 25.0 | 0.7 | 0.040x | 1.007x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.6 | 27.2 | 0.6 | 0.045x | 1.124x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.1 | 26.4 | 0.1 | 0.045x | 1.133x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 577.4 | 575.0 | 586.8 | 4.3 | 0.995x | 24.903x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 580.4 | 571.7 | 588.4 | 6.2 | 1.000x | 25.034x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.6 | 0.3 | 0.009x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.4 | 0.1 | 0.009x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.5 | 97.4 | 101.0 | 1.4 | 0.045x | 5.128x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 178.4 | 175.9 | 178.7 | 1.0 | 0.082x | 9.390x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 183.4 | 175.1 | 188.4 | 4.9 | 0.084x | 9.652x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,184.3 | 2,162.4 | 2,287.0 | 45.3 | 1.000x | 114.944x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 29.9 | 31.9 | 0.8 | 0.038x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.3 | 0.1 | 0.038x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 115.2 | 103.4 | 119.9 | 5.8 | 0.145x | 3.831x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 126.8 | 122.5 | 127.6 | 2.0 | 0.159x | 4.215x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 794.8 | 791.1 | 805.1 | 5.0 | 1.000x | 26.424x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 795.0 | 780.6 | 809.6 | 10.4 | 1.000x | 26.431x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.8 | 0.3 | 0.008x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.1 | 133.0 | 134.0 | 0.4 | 0.044x | 5.268x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 698.8 | 691.1 | 705.4 | 5.2 | 0.231x | 27.665x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 713.3 | 703.7 | 748.8 | 17.7 | 0.236x | 28.238x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,025.5 | 3,002.9 | 3,199.6 | 72.9 | 1.000x | 119.775x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 25.1 | 26.9 | 0.7 | 0.121x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.126x | 1.039x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.7 | 34.5 | 0.6 | 0.159x | 1.313x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 33.0 | 33.2 | 0.1 | 0.160x | 1.317x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.4 | 206.3 | 208.8 | 0.9 | 1.000x | 8.241x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 208.6 | 205.0 | 209.7 | 1.6 | 1.006x | 8.286x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.1 | 0.2 | 0.037x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 26.7 | 27.2 | 0.2 | 0.037x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 66.0 | 69.5 | 1.1 | 0.093x | 2.540x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 239.4 | 239.1 | 242.6 | 1.3 | 0.326x | 8.927x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 241.4 | 237.9 | 244.8 | 2.4 | 0.329x | 9.001x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.5 | 712.4 | 748.5 | 12.1 | 1.000x | 27.352x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.8 | 28.2 | 0.6 | 0.079x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.3 | 26.7 | 27.5 | 0.3 | 0.080x | 1.014x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 39.5 | 40.7 | 0.4 | 0.118x | 1.494x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.0 | 39.6 | 41.9 | 0.8 | 0.120x | 1.526x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 338.8 | 336.6 | 342.2 | 2.1 | 0.993x | 12.600x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 341.1 | 338.6 | 404.7 | 25.7 | 1.000x | 12.686x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.7 | 21.2 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.5 | 21.4 | 21.7 | 0.1 | 0.018x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 65.8 | 70.1 | 1.5 | 0.056x | 3.237x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 296.0 | 292.9 | 300.2 | 2.4 | 0.245x | 14.063x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 310.6 | 309.0 | 316.9 | 2.8 | 0.257x | 14.757x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,209.2 | 1,204.0 | 1,254.9 | 18.7 | 1.000x | 57.447x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.6 | 34.4 | 0.6 | 0.068x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 32.7 | 33.3 | 0.2 | 0.068x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.8 | 71.4 | 71.9 | 0.2 | 0.148x | 2.172x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.1 | 74.0 | 74.2 | 0.1 | 0.153x | 2.242x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 485.5 | 480.6 | 608.0 | 49.4 | 1.000x | 14.691x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 493.0 | 484.3 | 499.0 | 5.5 | 1.016x | 14.920x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 26.9 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.2 | 0.2 | 0.015x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.5 | 94.1 | 100.7 | 2.4 | 0.052x | 3.557x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 595.7 | 576.0 | 607.9 | 10.4 | 0.325x | 22.195x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 607.5 | 597.9 | 621.3 | 9.7 | 0.332x | 22.635x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,830.8 | 1,799.0 | 1,865.1 | 21.4 | 1.000x | 68.212x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 27.1 | 0.3 | 0.127x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 26.4 | 30.1 | 1.4 | 0.137x | 1.077x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 66.8 | 66.5 | 67.6 | 0.4 | 0.323x | 2.539x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 66.9 | 66.6 | 66.9 | 0.1 | 0.324x | 2.543x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 204.8 | 204.1 | 208.3 | 1.7 | 0.991x | 7.787x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 206.7 | 201.7 | 209.1 | 2.7 | 1.000x | 7.860x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.0 | 0.0 | 0.062x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 59.2 | 58.9 | 59.4 | 0.2 | 0.062x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 101.0 | 99.8 | 101.6 | 0.6 | 0.107x | 1.714x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 101.5 | 100.9 | 102.5 | 0.6 | 0.107x | 1.721x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.1 | 105.2 | 111.5 | 2.3 | 0.112x | 1.799x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 947.7 | 932.6 | 975.4 | 14.3 | 1.000x | 16.074x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.9 | 22.8 | 23.3 | 0.2 | 0.664x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.3 | 25.4 | 0.0 | 0.736x | 1.108x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.0 | 29.9 | 30.5 | 0.2 | 0.870x | 1.310x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 29.8 | 31.1 | 0.5 | 0.876x | 1.319x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.2 | 33.7 | 35.6 | 0.7 | 0.994x | 1.496x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.4 | 34.1 | 37.5 | 1.3 | 1.000x | 1.506x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 24.0 | 23.7 | 24.0 | 0.1 | 0.669x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 24.2 | 23.8 | 24.5 | 0.3 | 0.676x | 1.010x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.8 | 35.1 | 36.6 | 0.5 | 1.000x | 1.495x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.6 | 36.2 | 39.3 | 1.2 | 1.050x | 1.569x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 197.7 | 196.7 | 200.1 | 1.4 | 5.520x | 8.251x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 198.5 | 196.4 | 200.2 | 1.4 | 5.543x | 8.285x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.2 | 14.8 | 15.3 | 0.2 | 0.513x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.5 | 0.1 | 0.552x | 1.076x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.0 | 28.0 | 0.7 | 0.890x | 1.735x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.7 | 25.6 | 27.6 | 0.7 | 0.898x | 1.751x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.3 | 29.6 | 0.1 | 0.996x | 1.941x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.7 | 29.4 | 33.6 | 1.6 | 1.000x | 1.949x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.5 | 19.3 | 0.3 | 0.507x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 18.7 | 19.9 | 0.4 | 0.508x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.5 | 35.7 | 37.6 | 0.7 | 1.000x | 1.973x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.4 | 36.9 | 42.7 | 2.0 | 1.024x | 2.020x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 143.9 | 143.6 | 146.8 | 1.3 | 3.840x | 7.574x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 144.3 | 143.2 | 144.8 | 0.5 | 3.851x | 7.597x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.7 | 17.4 | 0.3 | 0.079x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.6 | 19.6 | 0.5 | 0.088x | 1.103x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 20.2 | 0.6 | 0.088x | 1.109x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.6 | 18.8 | 0.1 | 0.088x | 1.110x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 210.7 | 208.0 | 212.3 | 1.6 | 0.992x | 12.490x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 212.4 | 204.9 | 218.4 | 4.6 | 1.000x | 12.595x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.2 | 0.3 | 0.057x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.5 | 12.8 | 0.1 | 0.057x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51.8 | 51.7 | 53.1 | 0.5 | 0.238x | 4.163x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.4 | 61.6 | 67.9 | 2.4 | 0.286x | 5.013x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 66.8 | 66.8 | 67.4 | 0.2 | 0.307x | 5.370x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.9 | 214.9 | 225.1 | 3.6 | 1.000x | 17.509x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 25.1 | 0.7 | 0.154x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.6 | 24.9 | 0.5 | 0.155x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.5 | 79.8 | 0.5 | 0.514x | 3.348x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.7 | 79.0 | 0.1 | 0.515x | 3.349x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 153.2 | 151.7 | 160.7 | 3.2 | 1.000x | 6.508x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.7 | 150.2 | 155.5 | 1.8 | 1.003x | 6.530x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 71.2 | 70.9 | 71.8 | 0.3 | 0.066x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 71.1 | 71.7 | 0.2 | 0.066x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 100.8 | 99.6 | 102.2 | 1.1 | 0.094x | 1.416x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 147.5 | 147.2 | 149.6 | 1.0 | 0.137x | 2.072x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 150.8 | 149.9 | 152.9 | 1.1 | 0.140x | 2.118x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.9 | 1,068.3 | 1,118.7 | 18.7 | 1.000x | 15.121x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.4 | 14.8 | 16.2 | 0.5 | 0.526x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.4 | 16.4 | 0.0 | 0.560x | 1.064x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.5 | 0.1 | 1.000x | 1.900x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 30.1 | 0.4 | 1.000x | 1.901x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67.6 | 67.2 | 68.2 | 0.3 | 2.310x | 4.390x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67.8 | 67.3 | 67.9 | 0.2 | 2.317x | 4.403x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.0 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 62.5 | 0.3 | 0.114x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 70.5 | 68.1 | 71.8 | 1.3 | 0.130x | 1.142x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 73.3 | 72.7 | 73.4 | 0.2 | 0.135x | 1.186x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.1 | 77.1 | 81.9 | 2.0 | 0.147x | 1.297x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.8 | 533.9 | 560.7 | 9.0 | 1.000x | 8.803x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 23.7 | 0.1 | 0.155x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.6 | 23.9 | 0.1 | 0.156x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.6 | 32.6 | 0.3 | 0.210x | 1.353x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.8 | 33.7 | 0.7 | 0.211x | 1.361x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 151.3 | 148.4 | 157.7 | 3.1 | 1.000x | 6.440x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.4 | 148.8 | 155.5 | 2.7 | 1.027x | 6.615x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 26.0 | 0.2 | 0.051x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 25.7 | 0.1 | 0.051x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.0 | 64.8 | 68.3 | 1.3 | 0.134x | 2.613x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 225.9 | 225.1 | 231.3 | 2.2 | 0.451x | 8.814x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 226.4 | 224.9 | 226.5 | 0.6 | 0.452x | 8.834x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 500.9 | 499.0 | 511.7 | 4.9 | 1.000x | 19.546x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.0 | 24.6 | 25.1 | 0.2 | 0.053x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 24.8 | 26.3 | 0.6 | 0.054x | 1.008x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.9 | 50.0 | 54.2 | 1.5 | 0.108x | 2.035x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.1 | 51.9 | 52.4 | 0.2 | 0.111x | 2.082x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 470.5 | 467.5 | 474.1 | 2.7 | 1.000x | 18.803x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 475.5 | 472.5 | 477.2 | 1.6 | 1.011x | 19.003x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 18.9 | 19.7 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 19.1 | 19.4 | 0.1 | 0.011x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.6 | 83.0 | 86.5 | 1.3 | 0.049x | 4.412x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 350.2 | 348.3 | 351.8 | 1.4 | 0.201x | 18.257x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 358.2 | 357.6 | 359.3 | 0.6 | 0.206x | 18.674x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,741.8 | 1,735.0 | 1,781.3 | 18.6 | 1.000x | 90.816x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 27.0 | 0.5 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.3 | 0.1 | 0.033x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 32.6 | 2.5 | 0.033x | 1.013x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.5 | 0.2 | 0.033x | 1.014x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 787.9 | 773.9 | 813.9 | 13.0 | 1.000x | 30.430x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 793.6 | 786.8 | 800.6 | 4.4 | 1.007x | 30.647x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.7 | 20.4 | 21.0 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.5 | 21.1 | 0.2 | 0.007x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.2 | 117.7 | 120.1 | 0.8 | 0.039x | 5.756x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 186.0 | 184.2 | 187.8 | 1.2 | 0.061x | 8.978x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 186.6 | 185.5 | 190.6 | 1.8 | 0.062x | 9.006x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,032.5 | 3,025.4 | 3,219.4 | 75.3 | 1.000x | 146.380x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.6 | 0.2 | 0.058x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.5 | 17.5 | 18.0 | 0.2 | 0.059x | 1.030x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.6 | 17.4 | 18.9 | 0.6 | 0.060x | 1.035x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.8 | 18.9 | 0.0 | 0.064x | 1.106x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.7 | 294.5 | 299.4 | 1.8 | 1.000x | 17.387x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.2 | 297.4 | 301.5 | 1.4 | 1.012x | 17.593x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.5 | 12.5 | 13.2 | 0.3 | 0.016x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 13.1 | 0.2 | 0.016x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 60.7 | 59.3 | 62.2 | 0.9 | 0.076x | 4.845x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 90.7 | 88.0 | 93.5 | 2.1 | 0.113x | 7.242x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 92.0 | 90.9 | 96.0 | 1.8 | 0.115x | 7.348x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.2 | 798.1 | 858.5 | 22.5 | 1.000x | 64.117x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.5 | 22.6 | 0.4 | 0.152x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.1 | 0.155x | 1.017x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.7 | 77.0 | 0.5 | 0.526x | 3.456x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.2 | 76.1 | 76.4 | 0.1 | 0.528x | 3.470x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 144.3 | 141.4 | 148.4 | 2.3 | 1.000x | 6.568x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.8 | 142.6 | 146.0 | 1.1 | 1.004x | 6.594x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 69.1 | 0.3 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.8 | 68.7 | 68.9 | 0.1 | 0.067x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.6 | 96.9 | 101.4 | 1.5 | 0.098x | 1.450x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 128.0 | 127.1 | 128.6 | 0.6 | 0.125x | 1.863x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 128.9 | 128.5 | 129.5 | 0.4 | 0.126x | 1.876x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,021.3 | 1,013.4 | 1,073.9 | 22.3 | 1.000x | 14.864x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.1 | 42.6 | 0.5 | 0.137x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 42.2 | 49.0 | 2.4 | 0.145x | 1.054x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.5 | 67.6 | 2.7 | 0.201x | 1.464x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.9 | 62.0 | 0.4 | 0.203x | 1.474x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.7 | 300.1 | 303.8 | 1.4 | 1.000x | 7.274x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 301.9 | 298.6 | 304.6 | 2.0 | 1.000x | 7.277x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 53.7 | 53.7 | 53.9 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 54.2 | 0.2 | 0.033x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 103.6 | 102.9 | 105.1 | 0.9 | 0.063x | 1.929x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 301.9 | 298.5 | 304.0 | 1.9 | 0.185x | 5.622x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 304.7 | 303.9 | 307.5 | 1.5 | 0.187x | 5.674x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,633.4 | 1,626.3 | 1,690.5 | 23.6 | 1.000x | 30.419x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 23.6 | 0.5 | 0.153x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.5 | 23.0 | 0.5 | 0.155x | 1.010x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.4 | 76.0 | 80.6 | 1.8 | 0.525x | 3.430x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.3 | 76.7 | 0.2 | 0.526x | 3.437x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.1 | 142.8 | 145.3 | 0.8 | 0.990x | 6.464x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 145.5 | 140.4 | 146.8 | 2.3 | 1.000x | 6.528x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.1 | 0.2 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.0 | 0.1 | 0.067x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.1 | 96.6 | 101.3 | 1.8 | 0.095x | 1.414x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 127.0 | 126.6 | 127.9 | 0.5 | 0.124x | 1.849x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 128.8 | 128.6 | 130.2 | 0.6 | 0.126x | 1.875x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,020.0 | 1,013.3 | 1,067.5 | 19.9 | 1.000x | 14.850x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.6 | 24.7 | 27.1 | 0.9 | 0.087x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.5 | 27.1 | 0.5 | 0.089x | 1.016x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.2 | 26.3 | 0.1 | 0.089x | 1.024x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 25.7 | 28.6 | 1.0 | 0.092x | 1.050x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 293.2 | 291.1 | 302.1 | 3.8 | 1.000x | 11.450x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.6 | 295.3 | 304.9 | 3.6 | 1.025x | 11.740x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.5 | 19.4 | 20.2 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 19.5 | 19.9 | 0.1 | 0.018x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.0 | 66.3 | 69.2 | 1.0 | 0.063x | 3.481x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 177.6 | 175.7 | 181.1 | 2.3 | 0.165x | 9.094x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 179.2 | 175.5 | 184.7 | 3.4 | 0.166x | 9.177x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.0 | 1,069.4 | 1,129.5 | 22.6 | 1.000x | 55.146x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.6 | 22.2 | 0.6 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 20.6 | 23.7 | 1.1 | 0.073x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.4 | 0.1 | 0.089x | 1.261x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 25.5 | 26.8 | 0.4 | 0.089x | 1.271x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.5 | 291.3 | 298.0 | 2.4 | 1.000x | 14.219x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.7 | 294.4 | 301.1 | 2.2 | 1.014x | 14.424x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.9 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.5 | 0.3 | 0.014x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.0 | 64.9 | 68.2 | 1.1 | 0.063x | 4.554x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 167.7 | 166.7 | 174.6 | 3.0 | 0.157x | 11.411x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.4 | 164.3 | 170.7 | 2.2 | 0.157x | 11.458x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.3 | 1,056.8 | 1,125.3 | 24.7 | 1.000x | 72.805x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.6 | 21.4 | 0.3 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.3 | 20.6 | 22.0 | 0.6 | 0.072x | 1.030x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.5 | 26.3 | 0.3 | 0.088x | 1.256x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.0 | 0.089x | 1.265x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.3 | 290.3 | 296.9 | 2.3 | 1.000x | 14.213x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.7 | 296.8 | 303.4 | 2.3 | 1.015x | 14.423x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 14.9 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.7 | 0.0 | 0.014x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.1 | 64.2 | 68.3 | 1.4 | 0.063x | 4.580x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.6 | 165.5 | 169.6 | 1.4 | 0.157x | 11.514x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 169.8 | 167.3 | 175.2 | 2.7 | 0.159x | 11.595x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.8 | 1,049.8 | 1,123.7 | 26.7 | 1.000x | 73.129x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.5 | 21.9 | 0.6 | 0.070x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.7 | 21.4 | 0.3 | 0.070x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.5 | 26.3 | 0.3 | 0.087x | 1.247x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.5 | 0.2 | 0.089x | 1.269x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.3 | 292.5 | 321.3 | 10.8 | 1.000x | 14.291x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.8 | 296.9 | 304.0 | 2.6 | 1.008x | 14.412x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.5 | 15.2 | 0.3 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.7 | 0.1 | 0.014x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.0 | 64.5 | 70.0 | 1.8 | 0.063x | 4.567x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 167.5 | 165.6 | 172.1 | 2.7 | 0.157x | 11.415x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.3 | 168.0 | 170.1 | 0.7 | 0.158x | 11.468x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.3 | 1,061.2 | 1,129.5 | 26.5 | 1.000x | 72.510x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.3 | 22.7 | 0.4 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.4 | 22.9 | 0.6 | 0.076x | 1.020x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.4 | 26.3 | 0.3 | 0.087x | 1.164x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.089x | 1.184x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.1 | 290.8 | 297.2 | 2.1 | 1.000x | 13.356x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.1 | 296.2 | 299.5 | 1.2 | 1.013x | 13.535x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.9 | 0.3 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.5 | 0.1 | 0.015x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.0 | 64.5 | 68.1 | 1.4 | 0.063x | 4.117x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 158.8 | 155.0 | 161.1 | 2.1 | 0.149x | 9.749x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 159.4 | 157.8 | 164.5 | 2.4 | 0.150x | 9.788x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,065.1 | 1,051.0 | 1,122.7 | 26.0 | 1.000x | 65.403x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,669.5 | 7,664.9 | 7,678.1 | 5.1 | 0.775x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,685.2 | 7,675.4 | 7,730.7 | 20.2 | 0.777x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,848.7 | 9,811.3 | 9,862.0 | 17.3 | 0.995x | 1.284x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,896.6 | 9,828.8 | 10,419.0 | 217.9 | 1.000x | 1.290x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38,207.4 | 38,199.0 | 38,218.0 | 6.3 | 3.861x | 4.982x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38,209.5 | 38,196.4 | 38,417.8 | 85.1 | 3.861x | 4.982x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,977.4 | 5,907.7 | 5,984.6 | 29.2 | 0.082x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,271.7 | 6,235.2 | 6,323.1 | 28.5 | 0.086x | 1.049x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,798.6 | 14,776.9 | 14,822.6 | 16.8 | 0.203x | 2.476x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,819.1 | 14,774.9 | 14,856.1 | 29.6 | 0.204x | 2.479x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,725.4 | 72,478.3 | 73,639.6 | 422.7 | 1.000x | 12.167x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,790.4 | 72,360.2 | 73,185.4 | 310.7 | 1.001x | 12.178x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,696.0 | 13,694.5 | 13,914.5 | 85.8 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,711.8 | 13,679.6 | 13,737.8 | 21.3 | 0.086x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,124.1 | 19,117.7 | 19,125.4 | 3.1 | 0.120x | 1.396x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,125.7 | 19,122.4 | 19,134.1 | 4.2 | 0.120x | 1.396x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158,786.1 | 157,916.1 | 160,168.4 | 777.6 | 0.997x | 11.594x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 159,198.2 | 158,381.0 | 159,531.7 | 404.0 | 1.000x | 11.624x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,644.3 | 7,634.5 | 7,652.7 | 6.4 | 0.811x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,648.7 | 7,645.9 | 7,724.8 | 29.9 | 0.811x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,411.7 | 9,405.8 | 9,423.0 | 6.1 | 0.998x | 1.231x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,426.4 | 9,419.5 | 9,579.9 | 62.3 | 1.000x | 1.233x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,303.3 | 19,298.1 | 19,315.6 | 6.0 | 2.048x | 2.525x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,309.9 | 19,299.1 | 19,317.6 | 6.7 | 2.048x | 2.526x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,134.8 | 6,132.9 | 6,174.2 | 15.8 | 0.138x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,554.1 | 6,526.1 | 6,561.2 | 12.7 | 0.147x | 1.068x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,480.2 | 7,476.1 | 7,483.8 | 2.8 | 0.168x | 1.219x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,483.2 | 7,477.2 | 7,488.3 | 3.9 | 0.168x | 1.220x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,575.2 | 44,402.1 | 44,689.4 | 93.0 | 1.000x | 7.266x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,613.9 | 44,494.9 | 44,790.6 | 102.0 | 1.001x | 7.272x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.2 | 42.4 | 45.5 | 1.1 | 0.136x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.5 | 48.9 | 52.6 | 1.5 | 0.162x | 1.190x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 317.9 | 316.6 | 329.5 | 4.8 | 0.998x | 7.353x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 318.6 | 314.2 | 321.9 | 2.5 | 1.000x | 7.368x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 977.5 | 972.5 | 978.9 | 2.3 | 3.068x | 22.607x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 979.4 | 978.4 | 986.7 | 3.1 | 3.074x | 22.651x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,850.3 | 6,848.7 | 6,860.3 | 4.2 | 0.063x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,856.5 | 6,849.4 | 6,880.9 | 11.4 | 0.063x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,399.2 | 14,390.9 | 14,462.2 | 28.1 | 0.131x | 2.102x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,401.8 | 14,394.8 | 14,429.7 | 12.3 | 0.132x | 2.102x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 109,505.1 | 109,335.1 | 110,107.1 | 324.3 | 1.000x | 15.986x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,014.0 | 109,631.4 | 110,540.5 | 295.0 | 1.005x | 16.060x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,588.5 | 10,578.9 | 10,657.6 | 28.8 | 0.111x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,636.5 | 10,577.7 | 10,765.6 | 67.1 | 0.112x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 15,312.5 | 15,307.6 | 15,336.1 | 10.1 | 0.161x | 1.446x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15,313.1 | 15,305.6 | 15,323.5 | 6.6 | 0.161x | 1.446x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95,070.2 | 94,758.3 | 95,317.2 | 217.0 | 0.998x | 8.979x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,260.0 | 95,105.0 | 95,742.2 | 225.8 | 1.000x | 8.997x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.2 | 16.4 | 0.4 | 0.533x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.5 | 16.4 | 17.9 | 0.6 | 0.563x | 1.056x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.9 | 29.3 | 0.9 | 0.925x | 1.737x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 26.6 | 29.2 | 1.0 | 0.966x | 1.813x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.0 | 29.5 | 0.1 | 1.000x | 1.878x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.9 | 0.3 | 1.007x | 1.892x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.1 | 22.0 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.8 | 21.1 | 22.1 | 0.4 | 0.039x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.7 | 60.1 | 62.9 | 1.0 | 0.109x | 2.877x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 227.5 | 227.0 | 231.4 | 1.6 | 0.403x | 10.614x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 230.4 | 227.7 | 231.4 | 1.4 | 0.408x | 10.750x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 565.1 | 562.2 | 584.0 | 8.2 | 1.000x | 26.360x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.3 | 55.2 | 55.4 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.9 | 60.2 | 0.9 | 0.087x | 1.048x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.7 | 73.1 | 0.2 | 0.109x | 1.319x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73.0 | 72.6 | 74.1 | 0.5 | 0.110x | 1.321x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 658.4 | 656.4 | 663.0 | 2.3 | 0.989x | 11.914x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 665.5 | 660.4 | 670.3 | 3.4 | 1.000x | 12.043x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.1 | 61.6 | 62.4 | 0.3 | 0.093x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.4 | 62.7 | 0.1 | 0.094x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.8 | 62.4 | 62.9 | 0.2 | 0.095x | 1.011x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.6 | 64.1 | 65.0 | 0.3 | 0.097x | 1.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.3 | 80.4 | 85.0 | 1.9 | 0.124x | 1.326x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 664.3 | 652.8 | 665.6 | 4.7 | 1.000x | 10.697x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.0 | 68.9 | 69.5 | 0.2 | 0.108x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 68.9 | 72.3 | 1.2 | 0.108x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 74.4 | 71.9 | 75.8 | 1.3 | 0.116x | 1.078x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 75.8 | 73.6 | 77.5 | 1.4 | 0.119x | 1.098x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 639.7 | 637.8 | 642.0 | 1.5 | 1.000x | 9.265x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 641.1 | 635.7 | 643.1 | 3.0 | 1.002x | 9.286x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 59.1 | 0.3 | 0.091x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.7 | 81.6 | 85.9 | 1.7 | 0.129x | 1.419x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.3 | 88.2 | 88.9 | 0.3 | 0.138x | 1.514x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 90.1 | 90.4 | 0.1 | 0.141x | 1.548x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 641.4 | 635.2 | 647.0 | 4.3 | 1.000x | 11.003x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.9 | 18.4 | 0.2 | 0.043x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.8 | 23.3 | 1.0 | 0.050x | 1.155x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 32.7 | 1.3 | 0.071x | 1.639x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.9 | 0.1 | 0.071x | 1.651x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 415.3 | 411.8 | 426.2 | 5.2 | 1.000x | 23.092x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 416.5 | 410.9 | 420.6 | 3.7 | 1.003x | 23.157x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 23.8 | 0.3 | 0.056x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 23.2 | 22.9 | 25.0 | 0.7 | 0.056x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 24.3 | 0.2 | 0.057x | 1.025x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.1 | 0.0 | 0.063x | 1.125x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 59.4 | 56.3 | 64.4 | 3.0 | 0.144x | 2.564x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 413.3 | 412.6 | 430.8 | 7.0 | 1.000x | 17.846x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.2 | 27.9 | 1.0 | 0.125x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.7 | 0.2 | 0.125x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.3 | 34.3 | 0.4 | 0.159x | 1.278x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.0 | 34.5 | 0.5 | 0.159x | 1.280x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 209.7 | 206.8 | 217.0 | 3.5 | 1.000x | 8.032x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 209.7 | 207.3 | 210.4 | 1.1 | 1.000x | 8.034x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.2 | 27.1 | 28.6 | 0.6 | 0.037x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.3 | 27.1 | 27.9 | 0.3 | 0.038x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.8 | 65.5 | 70.1 | 1.6 | 0.093x | 2.496x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 236.1 | 233.1 | 239.1 | 2.2 | 0.324x | 8.691x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 238.3 | 234.5 | 242.8 | 2.8 | 0.328x | 8.774x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.6 | 713.7 | 754.1 | 13.2 | 1.000x | 26.789x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.0 | 42.0 | 45.7 | 1.4 | 0.077x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.5 | 47.7 | 1.2 | 0.082x | 1.065x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 58.2 | 57.9 | 58.4 | 0.2 | 0.107x | 1.386x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 58.3 | 58.2 | 59.7 | 0.5 | 0.107x | 1.387x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.0 | 538.8 | 547.0 | 3.1 | 0.998x | 12.899x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.2 | 538.5 | 560.5 | 7.6 | 1.000x | 12.927x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 48.8 | 0.2 | 0.088x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 48.6 | 48.3 | 52.8 | 1.7 | 0.089x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 50.5 | 50.0 | 50.9 | 0.3 | 0.092x | 1.043x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.3 | 51.7 | 52.6 | 0.3 | 0.095x | 1.080x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 78.1 | 74.9 | 80.7 | 2.2 | 0.142x | 1.612x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 549.2 | 534.7 | 555.3 | 7.8 | 1.000x | 11.340x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.6 | 57.5 | 0.7 | 0.099x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.3 | 58.0 | 60.8 | 1.0 | 0.104x | 1.047x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 120.1 | 119.7 | 121.0 | 0.5 | 0.214x | 2.157x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 120.8 | 120.0 | 121.5 | 0.5 | 0.215x | 2.170x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 561.4 | 558.8 | 565.2 | 2.5 | 1.000x | 10.080x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 562.8 | 556.7 | 568.3 | 4.1 | 1.003x | 10.106x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.7 | 63.5 | 65.0 | 0.6 | 0.114x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 65.0 | 64.4 | 66.5 | 0.7 | 0.115x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.4 | 90.1 | 96.1 | 2.2 | 0.161x | 1.413x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 109.6 | 109.6 | 109.9 | 0.1 | 0.193x | 1.694x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.6 | 112.8 | 1.3 | 0.194x | 1.695x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.5 | 552.0 | 573.8 | 7.6 | 1.000x | 8.758x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 65.3 | 65.1 | 65.4 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.2 | 67.0 | 67.3 | 0.1 | 0.056x | 1.029x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 98.6 | 97.5 | 99.1 | 0.5 | 0.083x | 1.510x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 98.7 | 98.3 | 99.1 | 0.3 | 0.083x | 1.511x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,192.5 | 1,184.9 | 1,208.5 | 9.2 | 1.000x | 18.258x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,206.2 | 1,176.9 | 1,244.9 | 24.4 | 1.012x | 18.469x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.3 | 93.0 | 1.5 | 0.051x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 89.5 | 89.5 | 95.0 | 2.2 | 0.051x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 135.2 | 130.8 | 141.3 | 3.4 | 0.077x | 1.513x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 143.9 | 143.1 | 146.3 | 1.3 | 0.082x | 1.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.7 | 168.0 | 178.0 | 3.8 | 0.098x | 1.921x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.4 | 1,736.1 | 1,766.2 | 9.9 | 1.000x | 19.528x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.8 | 24.6 | 25.1 | 0.2 | 0.083x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 24.6 | 26.3 | 0.6 | 0.085x | 1.015x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.6 | 27.4 | 0.6 | 0.087x | 1.046x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 26.5 | 0.1 | 0.088x | 1.059x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.5 | 294.1 | 300.1 | 2.2 | 1.000x | 11.982x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.0 | 296.5 | 305.4 | 2.9 | 1.015x | 12.166x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 21.1 | 0.3 | 0.019x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.6 | 20.4 | 25.1 | 1.8 | 0.019x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.4 | 67.3 | 71.2 | 1.3 | 0.063x | 3.336x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 190.0 | 189.0 | 192.7 | 1.3 | 0.176x | 9.262x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 195.5 | 191.7 | 198.2 | 2.2 | 0.181x | 9.531x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.7 | 1,077.2 | 1,133.1 | 21.8 | 1.000x | 52.592x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.8 | 33.3 | 0.6 | 0.107x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.6 | 32.1 | 0.2 | 0.107x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.6 | 0.2 | 0.118x | 1.099x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 34.2 | 36.5 | 0.8 | 0.120x | 1.122x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.3 | 294.4 | 302.3 | 2.7 | 1.000x | 9.317x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.4 | 293.7 | 306.3 | 4.1 | 1.004x | 9.352x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.4 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 32.8 | 2.3 | 0.026x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.8 | 71.6 | 73.9 | 0.8 | 0.068x | 2.715x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 301.7 | 299.9 | 303.5 | 1.2 | 0.283x | 11.247x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 302.0 | 300.2 | 309.7 | 3.5 | 0.283x | 11.256x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,061.0 | 1,127.4 | 24.8 | 1.000x | 39.804x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 63.9 | 63.8 | 66.1 | 0.9 | 0.100x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.1 | 69.8 | 0.2 | 0.109x | 1.086x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 70.6 | 0.6 | 0.109x | 1.086x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.8 | 95.6 | 96.0 | 0.1 | 0.150x | 1.499x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 637.7 | 631.9 | 678.7 | 17.4 | 1.000x | 9.984x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 641.5 | 633.2 | 649.8 | 5.3 | 1.006x | 10.043x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 58.8 | 0.2 | 0.092x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.7 | 58.3 | 59.6 | 0.5 | 0.092x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.3 | 88.0 | 88.9 | 0.3 | 0.139x | 1.511x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.4 | 87.2 | 89.6 | 1.0 | 0.139x | 1.513x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 91.8 | 91.7 | 91.8 | 0.1 | 0.145x | 1.571x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 635.0 | 630.7 | 658.3 | 10.8 | 1.000x | 10.864x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 63.8 | 63.6 | 66.2 | 1.0 | 0.101x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 69.1 | 69.9 | 0.3 | 0.109x | 1.084x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.9 | 70.3 | 0.6 | 0.110x | 1.087x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.9 | 95.7 | 96.4 | 0.3 | 0.152x | 1.501x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.7 | 630.5 | 693.3 | 24.4 | 1.000x | 9.909x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.1 | 636.5 | 638.8 | 0.8 | 1.007x | 9.979x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.092x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.7 | 0.1 | 0.092x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.4 | 87.2 | 89.4 | 0.9 | 0.140x | 1.515x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.5 | 87.3 | 89.2 | 0.6 | 0.140x | 1.517x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 91.8 | 91.6 | 92.2 | 0.2 | 0.145x | 1.574x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.5 | 631.5 | 657.7 | 10.0 | 1.000x | 10.841x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 57.6 | 72.9 | 5.1 | 0.089x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.9 | 69.2 | 0.1 | 0.099x | 1.117x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 69.1 | 69.5 | 0.1 | 0.099x | 1.118x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 75.2 | 74.9 | 75.6 | 0.2 | 0.108x | 1.214x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 697.1 | 693.3 | 717.3 | 8.9 | 1.000x | 11.260x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 704.1 | 698.4 | 892.9 | 87.3 | 1.010x | 11.372x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.6 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.5 | 0.1 | 0.083x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.1 | 75.8 | 77.4 | 0.7 | 0.108x | 1.306x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 85.6 | 85.5 | 85.6 | 0.1 | 0.121x | 1.468x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.1 | 88.6 | 89.4 | 0.3 | 0.126x | 1.528x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 705.3 | 689.2 | 732.2 | 13.9 | 1.000x | 12.101x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 54.1 | 56.7 | 1.0 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 54.6 | 55.8 | 0.5 | 0.077x | 1.026x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 68.8 | 69.3 | 0.2 | 0.095x | 1.278x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.0 | 69.6 | 0.2 | 0.096x | 1.284x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.0 | 721.9 | 777.9 | 22.0 | 0.997x | 13.378x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 725.8 | 718.0 | 729.5 | 4.2 | 1.000x | 13.412x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.5 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 58.8 | 0.2 | 0.080x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 72.7 | 72.2 | 83.2 | 4.3 | 0.100x | 1.246x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 81.9 | 80.1 | 82.1 | 0.7 | 0.112x | 1.404x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.1 | 86.0 | 1.3 | 0.115x | 1.439x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 729.2 | 714.0 | 754.4 | 13.6 | 1.000x | 12.494x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 53.9 | 56.5 | 1.0 | 0.075x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 54.6 | 55.9 | 0.5 | 0.077x | 1.027x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 69.4 | 0.1 | 0.096x | 1.281x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.1 | 70.9 | 0.7 | 0.096x | 1.282x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.2 | 720.7 | 821.4 | 39.5 | 1.000x | 13.377x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 728.7 | 722.1 | 739.2 | 6.1 | 1.006x | 13.461x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.9 | 0.3 | 0.081x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.4 | 0.1 | 0.081x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 74.3 | 72.2 | 77.6 | 2.0 | 0.103x | 1.274x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 81.9 | 73.3 | 82.0 | 3.4 | 0.114x | 1.405x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.7 | 83.1 | 85.5 | 1.1 | 0.116x | 1.435x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 720.5 | 714.7 | 755.0 | 14.3 | 1.000x | 12.352x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.1 | 32.4 | 0.5 | 0.089x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.4 | 32.3 | 0.4 | 0.089x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 44.4 | 49.3 | 1.8 | 0.133x | 1.485x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 52.8 | 92.4 | 15.4 | 0.153x | 1.715x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 352.5 | 349.0 | 359.9 | 3.7 | 1.000x | 11.182x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.1 | 350.5 | 360.4 | 3.6 | 1.010x | 11.298x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.8 | 0.3 | 0.020x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 28.3 | 0.8 | 0.021x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.6 | 70.1 | 73.5 | 1.2 | 0.055x | 2.704x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 380.5 | 378.9 | 384.7 | 2.4 | 0.298x | 14.567x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 388.5 | 381.0 | 389.3 | 3.1 | 0.304x | 14.871x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,277.8 | 1,266.8 | 1,354.9 | 32.0 | 1.000x | 48.914x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.9 | 9.9 | 0.0 | 0.339x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.341x | 1.006x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.1 | 13.8 | 15.8 | 0.7 | 0.515x | 1.521x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.6 | 18.3 | 1.1 | 0.535x | 1.578x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 29.5 | 0.2 | 0.997x | 2.945x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.7 | 0.2 | 1.000x | 2.953x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 6.1 | 5.6 | 6.8 | 0.5 | 0.200x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.2 | 5.6 | 6.7 | 0.4 | 0.205x | 1.027x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 15.0 | 14.9 | 17.9 | 1.2 | 0.493x | 2.471x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.5 | 0.1 | 0.570x | 2.858x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 30.5 | 0.2 | 1.000x | 5.011x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.5 | 37.8 | 38.9 | 0.4 | 1.267x | 6.348x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.5 | 13.9 | 0.5 | 0.437x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.4 | 13.6 | 0.4 | 0.438x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.3 | 14.9 | 16.5 | 0.6 | 0.524x | 1.198x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.4 | 16.5 | 0.0 | 0.561x | 1.284x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.0 | 30.8 | 0.7 | 1.000x | 2.288x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.2 | 55.5 | 10.4 | 1.010x | 2.311x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.5 | 0.2 | 0.191x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.5 | 6.1 | 6.5 | 0.1 | 0.209x | 1.097x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 23.5 | 23.4 | 27.7 | 1.6 | 0.758x | 3.972x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 24.6 | 24.5 | 24.7 | 0.1 | 0.793x | 4.154x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 31.2 | 0.1 | 1.000x | 5.237x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.2 | 35.8 | 47.3 | 4.1 | 1.264x | 6.620x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.1 | 21.1 | 21.7 | 0.2 | 0.564x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.5 | 31.0 | 3.8 | 0.576x | 1.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.2 | 34.6 | 68.7 | 13.0 | 0.991x | 1.758x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.5 | 34.8 | 40.6 | 2.3 | 1.000x | 1.774x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 81.1 | 80.9 | 81.6 | 0.3 | 2.161x | 3.835x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 81.4 | 80.4 | 83.2 | 0.9 | 2.170x | 3.851x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.0 | 35.4 | 38.2 | 1.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 41.3 | 36.5 | 42.7 | 2.2 | 1.148x | 1.148x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.8 | 72.9 | 74.0 | 0.4 | 2.051x | 2.051x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 74.1 | 73.3 | 75.4 | 0.8 | 2.059x | 2.059x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 613.1 | 612.2 | 614.5 | 0.7 | 17.048x | 17.048x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 617.9 | 616.6 | 626.4 | 3.6 | 17.181x | 17.181x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.1 | 20.7 | 21.1 | 0.2 | 0.600x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 23.4 | 0.7 | 0.618x | 1.030x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.9 | 22.5 | 0.2 | 0.629x | 1.048x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.0 | 0.1 | 0.654x | 1.090x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.1 | 34.3 | 40.7 | 2.3 | 1.000x | 1.668x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.3 | 33.6 | 63.6 | 11.3 | 1.034x | 1.724x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 17.1 | 0.3 | 0.462x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.8 | 16.2 | 17.1 | 0.4 | 0.474x | 1.026x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.4 | 34.8 | 36.3 | 0.7 | 1.000x | 2.164x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.5 | 35.5 | 45.5 | 3.8 | 1.116x | 2.416x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 123.2 | 122.3 | 126.5 | 1.6 | 3.482x | 7.537x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 125.1 | 124.4 | 125.2 | 0.3 | 3.534x | 7.649x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,579,415.8 | 3,575,433.9 | 3,603,762.4 | 10,110.6 | 0.125x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,584,658.7 | 3,575,104.0 | 3,586,034.6 | 4,028.9 | 0.125x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,684,690.7 | 3,632,836.0 | 3,731,051.0 | 36,705.7 | 0.128x | 1.029x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 4,952,397.5 | 4,938,169.8 | 5,070,578.0 | 48,902.7 | 0.173x | 1.384x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 5,187,813.0 | 5,167,982.8 | 5,283,798.5 | 42,018.8 | 0.181x | 1.449x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,694,695.4 | 28,637,241.7 | 29,232,360.5 | 260,979.3 | 1.000x | 8.017x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,985.3 | 17,934.0 | 18,072.1 | 52.9 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,888,829.9 | 1,881,203.5 | 1,893,663.5 | 5,030.3 | 105.021x | 105.021x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,895,118.8 | 1,894,398.2 | 1,897,418.8 | 1,068.3 | 105.370x | 105.370x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,563,984.5 | 2,532,299.3 | 2,595,406.6 | 20,624.1 | 142.560x | 142.560x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 15,993,661.2 | 15,950,363.5 | 16,052,184.2 | 35,301.5 | 889.261x | 889.261x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,028,449.2 | 15,949,076.5 | 16,407,209.0 | 167,845.6 | 891.196x | 891.196x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,957.3 | 17,948.3 | 18,730.2 | 306.8 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,876,578.1 | 1,874,686.4 | 1,878,387.5 | 1,353.4 | 104.502x | 104.502x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,878,612.2 | 1,877,528.1 | 1,885,089.9 | 2,736.3 | 104.616x | 104.616x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,819,271.7 | 2,817,268.5 | 2,820,513.6 | 1,087.6 | 156.999x | 156.999x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,133,275.5 | 3,115,636.0 | 3,185,429.9 | 24,613.2 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,138,982.6 | 3,117,745.4 | 3,172,171.6 | 18,815.0 | 0.033x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,966,411.6 | 5,966,102.2 | 5,969,294.8 | 1,182.1 | 0.064x | 1.904x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16,858,436.8 | 16,493,784.5 | 17,140,340.8 | 217,073.2 | 0.180x | 5.380x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,947,207.0 | 16,690,895.8 | 17,749,694.2 | 397,480.3 | 0.181x | 5.409x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 93,875,420.9 | 93,800,755.8 | 99,063,161.9 | 2,030,330.6 | 1.000x | 29.961x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,076.5 | 18,019.0 | 18,087.4 | 25.3 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,106,092.4 | 3,082,235.2 | 3,130,096.1 | 15,514.6 | 171.830x | 171.830x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,113,753.6 | 3,071,198.1 | 3,125,737.8 | 22,466.6 | 172.254x | 172.254x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,157,856.9 | 3,155,408.8 | 3,164,388.8 | 3,248.9 | 174.694x | 174.694x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,600,912.8 | 16,570,925.0 | 17,639,683.8 | 411,577.1 | 918.370x | 918.370x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16,604,260.0 | 16,567,004.8 | 16,641,547.8 | 24,321.2 | 918.555x | 918.555x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_35e1ab1_auto-caps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_vm-caps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `floor` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `orig` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 141,464,363.0 | 130,784,800.0 | 181,033,514.0 | 18,383,356.4 | 5 | 38,328 | 0.130 | compiled=5 | 8,618,961.0 | 132,755,341.0 | 109,411.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 158,500,382.0 | 149,923,522.0 | 177,325,533.0 | 10,534,750.7 | 5 | 38,416 | 0.066 | compiled=5 | 11,273,977.0 | 145,619,447.0 | 97,171.0 |
| `factored` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 140,463,715.0 | 136,195,132.0 | 148,699,214.0 | 4,110,299.8 | 5 | 38,328 | 0.029 | compiled=5 | 8,726,391.0 | 130,714,848.0 | 98,790.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 155,116,653.0 | 150,699,867.0 | 173,544,091.0 | 8,260,812.8 | 5 | 38,416 | 0.053 | compiled=5 | 10,988,664.0 | 141,275,411.0 | 179,141.0 |
| `factored` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 547,577,831.0 | 546,223,373.0 | 553,227,145.0 | 2,667,457.8 | 5 | 30,288 | 0.005 | compiled=5 | 2,069,092.0 | 545,419,478.0 | 186,391.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 551,471,633.0 | 547,201,459.0 | 555,134,585.0 | 2,807,182.1 | 5 | 30,288 | 0.005 (max is trial 1) | compiled=5 | 2,077,272.0 | 549,215,960.0 | 102,721.0 |
| `factored` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 550,174,265.0 | 542,143,397.0 | 558,601,396.0 | 5,346,769.4 | 5 | 30,288 | 0.010 | compiled=5 | 2,064,322.0 | 546,000,761.0 | 108,470.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 552,115,297.0 | 548,172,073.0 | 552,589,780.0 | 1,880,987.6 | 5 | 30,288 | 0.003 (max is trial 1) | compiled=5 | 2,070,633.0 | 549,936,604.0 | 188,061.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 128,124,003.0 | 121,815,237.0 | 132,250,058.0 | 3,741,734.5 | 5 | 17,816 | 0.029 | compiled=5 | 1,563,309.0 | 126,608,855.0 | 112,481.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 136,601,994.0 | 125,250,527.0 | 138,196,622.0 | 6,006,842.3 | 5 | 17,904 | 0.044 (max is trial 1) | compiled=5 | 1,463,518.0 | 134,997,154.0 | 200,402.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 125,053,645.0 | 118,093,685.0 | 130,520,689.0 | 4,812,299.8 | 5 | 17,816 | 0.038 (max is trial 1) | compiled=5 | 1,404,458.0 | 123,415,805.0 | 99,061.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 135,198,375.0 | 124,770,805.0 | 136,922,336.0 | 4,667,899.5 | 5 | 17,904 | 0.035 | compiled=5 | 1,432,719.0 | 132,068,647.0 | 199,521.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 143,839,405.0 | 133,489,685.0 | 145,996,357.0 | 4,499,436.2 | 5 | 17,600 | 0.031 | compiled=5 | 1,470,958.0 | 142,085,106.0 | 104,780.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 131,485,234.0 | 130,493,468.0 | 152,939,310.0 | 9,269,487.4 | 5 | 17,600 | 0.070 | compiled=5 | 1,303,697.0 | 130,010,745.0 | 190,152.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 143,130,173.0 | 127,595,569.0 | 148,446,484.0 | 7,271,673.7 | 5 | 17,600 | 0.051 (max is trial 1) | compiled=5 | 1,367,788.0 | 141,680,644.0 | 107,271.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 136,645,873.0 | 127,325,307.0 | 145,517,016.0 | 6,966,108.5 | 5 | 17,600 | 0.051 | compiled=5 | 1,317,248.0 | 135,247,565.0 | 93,341.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 143,041,582.0 | 133,638,077.0 | 152,605,977.0 | 7,423,117.4 | 5 | 38,288 | 0.052 | compiled=5 | 8,399,070.0 | 133,049,073.0 | 97,811.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 161,003,156.0 | 144,668,771.0 | 174,001,693.0 | 9,821,090.4 | 5 | 38,376 | 0.061 | compiled=5 | 18,044,156.0 | 141,891,755.0 | 186,281.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,731,375.0 | 133,116,513.0 | 154,306,767.0 | 7,366,531.2 | 5 | 38,288 | 0.050 | compiled=5 | 8,303,388.0 | 134,495,101.0 | 190,511.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,766,935.0 | 141,953,955.0 | 157,360,185.0 | 5,601,770.9 | 5 | 38,376 | 0.038 (max is trial 1) | compiled=5 | 10,395,781.0 | 138,189,823.0 | 191,472.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 425,700,355.0 | 418,138,020.0 | 433,200,719.0 | 5,739,473.7 | 5 | 26,112 | 0.013 | compiled=5 | 3,573,812.0 | 423,604,592.0 | 98,321.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 418,219,710.0 | 416,284,479.0 | 424,829,349.0 | 3,247,138.2 | 5 | 26,112 | 0.008 | compiled=5 | 1,887,041.0 | 416,182,378.0 | 101,761.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 426,965,172.0 | 417,563,868.0 | 436,633,782.0 | 6,421,511.5 | 5 | 26,112 | 0.015 | compiled=5 | 3,456,131.0 | 422,794,938.0 | 94,571.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 416,505,570.0 | 410,439,183.0 | 436,855,013.0 | 9,723,201.5 | 5 | 26,112 | 0.023 (max is trial 1) | compiled=5 | 3,768,522.0 | 414,571,809.0 | 91,591.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 77,221.0 | 63,801.0 | 158,901.0 | 34,563.5 | 5 | 951 | 0.448 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,280.0 | 4,990.0 | 51,650.0 | 18,235.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 66,930.0 | 54,590.0 | 163,171.0 | 40,903.4 | 5 | 1,609 | 0.611 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,840.0 | 12,990.0 | 48,891.0 | 13,770.9 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 320.0 | 14,730.0 | 5,748.1 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,870.0 | 12,390.0 | 44,650.0 | 12,443.2 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

